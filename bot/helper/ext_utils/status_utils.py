from asyncio import gather, iscoroutinefunction
from html import escape
from pyrogram.enums import ButtonStyle
from re import findall
from time import time

from psutil import cpu_percent, disk_usage, virtual_memory

from ... import (
    DOWNLOAD_DIR,
    bot_cache,
    bot_start_time,
    status_dict,
    task_dict,
    task_dict_lock,
)
from ...core.config_manager import Config
from ..telegram_helper.button_build import ButtonMaker


SIZE_UNITS = ["B", "KB", "MB", "GB", "TB", "PB"]


class MirrorStatus:
    STATUS_UPLOAD = "Upload"
    STATUS_DOWNLOAD = "Download"
    STATUS_CLONE = "Clone"
    STATUS_QUEUEDL = "QueueDl"
    STATUS_QUEUEUP = "QueueUp"
    STATUS_PAUSED = "Pause"
    STATUS_ARCHIVE = "Archive"
    STATUS_EXTRACT = "Extract"
    STATUS_SPLIT = "Split"
    STATUS_CHECK = "CheckUp"
    STATUS_SEED = "Seed"
    STATUS_SAMVID = "SamVid"
    STATUS_CONVERT = "Convert"
    STATUS_FFMPEG = "FFmpeg"
    STATUS_YT = "YouTube"
    STATUS_METADATA = "Metadata"
    STATUS_SEEDR = "Seedr"


class EngineStatus:
    def __init__(self):
        ver = bot_cache.get("eng_versions", {})

        self.STATUS_ARIA2 = f"Aria2 v{ver.get('aria2', 'N/A')}"
        self.STATUS_AIOHTTP = f"AioHttp v{ver.get('aiohttp', 'N/A')}"
        self.STATUS_GDAPI = f"Google-API v{ver.get('gapi', 'N/A')}"
        self.STATUS_QBIT = f"qBit v{ver.get('qBittorrent', 'N/A')}"
        self.STATUS_TGRAM = f"WzPyro v{ver.get('wzgram', 'N/A')}"
        self.STATUS_MEGA = f"MegaSDK v{ver.get('mega', 'N/A')}"
        self.STATUS_YTDLP = f"yt-dlp v{ver.get('yt-dlp', 'N/A')}"
        self.STATUS_FFMPEG = f"ffmpeg v{ver.get('ffmpeg', 'N/A')}"
        self.STATUS_7Z = f"7z v{ver.get('7z', 'N/A')}"
        self.STATUS_RCLONE = f"RClone v{ver.get('rclone', 'N/A')}"
        self.STATUS_SABNZBD = f"SABnzbd+ v{ver.get('SABnzbd+', 'N/A')}"
        self.STATUS_QUEUE = "QSystem v2"
        self.STATUS_JD = "JDownloader v2"
        self.STATUS_YT = "Youtube-Api"
        self.STATUS_METADATA = "Metadata"
        self.STATUS_UPHOSTER = "Uphoster"
        self.STATUS_SEEDR = "Seedr"


STATUSES = {
    "ALL": "All",
    "DL": MirrorStatus.STATUS_DOWNLOAD,
    "UP": MirrorStatus.STATUS_UPLOAD,
    "QD": MirrorStatus.STATUS_QUEUEDL,
    "QU": MirrorStatus.STATUS_QUEUEUP,
    "AR": MirrorStatus.STATUS_ARCHIVE,
    "EX": MirrorStatus.STATUS_EXTRACT,
    "SD": MirrorStatus.STATUS_SEED,
    "CL": MirrorStatus.STATUS_CLONE,
    "CM": MirrorStatus.STATUS_CONVERT,
    "SP": MirrorStatus.STATUS_SPLIT,
    "SV": MirrorStatus.STATUS_SAMVID,
    "FF": MirrorStatus.STATUS_FFMPEG,
    "PA": MirrorStatus.STATUS_PAUSED,
    "CK": MirrorStatus.STATUS_CHECK,
}


async def get_task_by_gid(gid: str):
    async with task_dict_lock:
        for tk in task_dict.values():
            if hasattr(tk, "seeding"):
                await tk.update()

            if tk.gid() == gid or tk.gid().startswith(gid):
                return tk

        return None


async def get_specific_tasks(status, user_id):
    if status == "All":
        if user_id:
            return [
                tk for tk in task_dict.values()
                if tk.listener.user_id == user_id
            ]
        else:
            return list(task_dict.values())

    tasks_to_check = (
        [
            tk for tk in task_dict.values()
            if tk.listener.user_id == user_id
        ]
        if user_id
        else list(task_dict.values())
    )

    coro_tasks = []
    coro_tasks.extend(
        tk for tk in tasks_to_check
        if iscoroutinefunction(tk.status)
    )

    coro_statuses = await gather(
        *[tk.status() for tk in coro_tasks]
    )

    result = []
    coro_index = 0

    for tk in tasks_to_check:
        if tk in coro_tasks:
            st = coro_statuses[coro_index]
            coro_index += 1
        else:
            st = tk.status()

        if (st == status) or (
            status == MirrorStatus.STATUS_DOWNLOAD
            and st not in STATUSES.values()
        ):
            result.append(tk)

    return result


async def get_all_tasks(req_status: str, user_id):
    async with task_dict_lock:
        return await get_specific_tasks(req_status, user_id)


def get_raw_file_size(size):
    num, unit = size.split()
    return int(float(num) * (1024 ** SIZE_UNITS.index(unit)))


def get_readable_file_size(size_in_bytes):
    if not size_in_bytes:
        return "0B"

    if size_in_bytes < 0:
        return "Unknown"

    index = 0

    while size_in_bytes >= 1024 and index < len(SIZE_UNITS) - 1:
        size_in_bytes /= 1024
        index += 1

    return f"{size_in_bytes:.2f}{SIZE_UNITS[index]}"


def get_readable_time(seconds: int):
    periods = [
        ("d", 86400),
        ("h", 3600),
        ("m", 60),
        ("s", 1),
    ]

    result = ""

    for period_name, period_seconds in periods:
        if seconds >= period_seconds:
            period_value, seconds = divmod(
                seconds,
                period_seconds,
            )
            result += f"{int(period_value)}{period_name}"

    return result


def get_raw_time(time_str: str) -> int:
    time_units = {
        "d": 86400,
        "h": 3600,
        "m": 60,
        "s": 1,
    }

    return sum(
        int(value) * time_units[unit]
        for value, unit in findall(
            r"(\d+)([dhms])",
            time_str,
        )
    )


def time_to_seconds(time_duration):
    try:
        parts = time_duration.split(":")

        if len(parts) == 3:
            hours, minutes, seconds = map(float, parts)

        elif len(parts) == 2:
            hours = 0
            minutes, seconds = map(float, parts)

        elif len(parts) == 1:
            hours = 0
            minutes = 0
            seconds = float(parts[0])

        else:
            return 0

        return (
            hours * 3600
            + minutes * 60
            + seconds
        )

    except Exception:
        return 0


def speed_string_to_bytes(size_text: str):
    size = 0
    size_text = size_text.lower()

    if "k" in size_text:
        size += float(
            size_text.split("k")[0]
        ) * 1024

    elif "m" in size_text:
        size += float(
            size_text.split("m")[0]
        ) * 1048576

    elif "g" in size_text:
        size += float(
            size_text.split("g")[0]
        ) * 1073741824

    elif "t" in size_text:
        size += float(
            size_text.split("t")[0]
        ) * 1099511627776

    elif "b" in size_text:
        size += float(
            size_text.split("b")[0]
        )

    return size


def get_progress_bar_string(pct):
    pct = float(str(pct).strip("%"))
    pct = min(max(pct, 0), 100)

    total = 10
    filled = int(pct / 100 * total)

    return " ".join(
        "🟩" if i < filled else "⬜"
        for i in range(total)
    )


# ═══════════════════════════════════════════════
#               🎯 STATUS MESSAGE
# ═══════════════════════════════════════════════

async def get_readable_message(
    sid,
    is_user,
    page_no=1,
    status="All",
    page_step=1,
):
    msg = ""
    button = None

    tasks = await get_specific_tasks(
        status,
        sid if is_user else None,
    )

    STATUS_LIMIT = Config.STATUS_LIMIT
    tasks_no = len(tasks)

    pages = (
        (max(tasks_no, 1) + STATUS_LIMIT - 1)
        // STATUS_LIMIT
    )

    if page_no > pages:
        page_no = (page_no - 1) % pages + 1
        status_dict[sid]["page_no"] = page_no

    elif page_no < 1:
        page_no = pages - (abs(page_no) % pages)
        status_dict[sid]["page_no"] = page_no

    start_position = (
        (page_no - 1) * STATUS_LIMIT
    )

    for index, task in enumerate(
        tasks[
            start_position:
            STATUS_LIMIT + start_position
        ],
        start=1,
    ):

        if status != "All":
            tstatus = status

        elif iscoroutinefunction(task.status):
            tstatus = await task.status()

        else:
            tstatus = task.status()

        task_titles = {
            MirrorStatus.STATUS_DOWNLOAD: "𝐋𝐄𝐄𝐂𝐇",
            MirrorStatus.STATUS_UPLOAD: "𝐔𝐏𝐋𝐎𝐀𝐃",
            MirrorStatus.STATUS_CLONE: "𝐂𝐋𝐎𝐍𝐄",
            MirrorStatus.STATUS_QUEUEDL: "𝐐𝐔𝐄𝐔𝐄",
            MirrorStatus.STATUS_QUEUEUP: "𝐐𝐔𝐄𝐔𝐄",
            MirrorStatus.STATUS_PAUSED: "𝐏𝐀𝐔𝐒𝐄𝐃",
            MirrorStatus.STATUS_ARCHIVE: "𝐀𝐑𝐂𝐇𝐈𝐕𝐄",
            MirrorStatus.STATUS_EXTRACT: "𝐄𝐗𝐓𝐑𝐀𝐂𝐓",
            MirrorStatus.STATUS_SPLIT: "𝐒𝐏𝐋𝐈𝐓",
            MirrorStatus.STATUS_CHECK: "𝐂𝐇𝐄𝐂𝐊",
            MirrorStatus.STATUS_SEED: "𝐒𝐄𝐄𝐃",
            MirrorStatus.STATUS_SAMVID: "𝐒𝐀𝐌𝐕𝐈𝐃",
            MirrorStatus.STATUS_CONVERT: "𝐂𝐎𝐍𝐕𝐄𝐑𝐓",
            MirrorStatus.STATUS_FFMPEG: "𝐅𝐅𝐌𝐏𝐄𝐆",
            MirrorStatus.STATUS_YT: "𝐘𝐎𝐔𝐓𝐔𝐁𝐄",
            MirrorStatus.STATUS_METADATA: "𝐌𝐄𝐓𝐀𝐃𝐀𝐓𝐀",
            MirrorStatus.STATUS_SEEDR: "𝐒𝐄𝐄𝐃𝐑",
        }

        task_title = task_titles.get(
            tstatus,
            "𝐓𝐀𝐒𝐊",
        )

        # Header
        msg += (
            f"📥 <b>{task_title} 𝐓𝐀𝐒𝐊 "
            f"𝟎{index + start_position}</b>\n\n"
        )

        # File
        msg += (
            f"📁 <b>𝐅𝐈𝐋𝐄</b> → "
            f"<i>{escape(str(task.name()))}</i>\n"
        )

        # Sub Name
        if task.listener.subname:
            msg += (
                f"🏷️ <b>𝐒𝐔𝐁 𝐍𝐀𝐌𝐄</b> → "
                f"<i>{escape(str(task.listener.subname))}</i>\n"
            )

        # Task By
        elapsed = (
            time()
            - task.listener.message.date.timestamp()
        )

        msg += (
            f"👤 <b>𝐓𝐀𝐒𝐊 𝐁𝐘</b> → "
            f"{task.listener.message.from_user.mention(style='html')}"
            f" <i>(#ID"
            f"{task.listener.message.from_user.id})</i>\n"
        )

        # Super Group Link
        if task.listener.is_super_chat:
            msg += (
                f"🔗 <a href='{task.listener.message.link}'>"
                f"<b>𝐎𝐩𝐞𝐧 𝐓𝐚𝐬𝐤 𝐌𝐞𝐬𝐬𝐚𝐠𝐞</b></a>\n"
            )

        # Progress
        if (
            tstatus not in [
                MirrorStatus.STATUS_SEED,
                MirrorStatus.STATUS_QUEUEUP,
            ]
            and task.listener.progress
        ):

            progress = task.progress()

            msg += "\n"
            msg += "🎯 <b>𝐏𝐑𝐎𝐆𝐑𝐄𝐒𝐒</b> →\n"

            msg += (
                f"{get_progress_bar_string(progress)} "
                f"<b>《{progress}%》</b>\n"
            )

            # Processed / Count
            if task.listener.subname:
                subsize = (
                    f" / "
                    f"{get_readable_file_size(task.listener.subsize)}"
                )

                ac = len(
                    task.listener.files_to_proceed
                )

                count = (
                    f"{task.listener.proceed_count}"
                    f" / {ac or '?'}"
                )

            else:
                subsize = ""
                count = ""

            msg += (
                f"📦 <b>𝐏𝐑𝐎𝐂𝐄𝐒𝐒𝐄𝐃</b> → "
                f"<i>{task.processed_bytes()}"
                f"{subsize} / {task.size()}</i>\n"
            )

            if count:
                msg += (
                    f"🔢 <b>𝐂𝐎𝐔𝐍𝐓</b> → "
                    f"<b>{count}</b>\n"
                )

            # Status / Speed
            msg += (
                f"🟢 <b>𝐒𝐓𝐀𝐓𝐔𝐒</b> → "
                f"<b>{tstatus}</b>\n"
            )

            msg += (
                f"🚀 <b>𝐒𝐏𝐄𝐄𝐃</b> → "
                f"<i>{task.speed()}</i>\n"
            )

            # Time
            msg += (
                f"⏱️ <b>𝐓𝐈𝐌𝐄</b> → "
                f"ETA <i>{task.eta()}</i> | "
                f"Elapsed <i>{get_readable_time(elapsed)}</i>\n"
            )

            # Torrent information
            if tstatus == MirrorStatus.STATUS_DOWNLOAD and (
                task.listener.is_torrent
                or task.listener.is_qbit
            ):
                try:
                    msg += (
                        f"👥 <b>𝐒𝐄𝐄𝐃𝐄𝐑𝐒</b> → "
                        f"{task.seeders_num()} | "
                        f"👤 <b>𝐋𝐄𝐄𝐂𝐇𝐄𝐑𝐒</b> → "
                        f"{task.leechers_num()}\n"
                    )

                except Exception:
                    pass

        # Seeding
        elif tstatus == MirrorStatus.STATUS_SEED:

            msg += (
                f"📦 <b>𝐒𝐈𝐙𝐄</b> → "
                f"<i>{task.size()}</i>\n"
            )

            msg += (
                f"📤 <b>𝐔𝐏𝐋𝐎𝐀𝐃𝐄𝐃</b> → "
                f"<i>{task.uploaded_bytes()}</i>\n"
            )

            msg += (
                f"🟢 <b>𝐒𝐓𝐀𝐓𝐔𝐒</b> → "
                f"<b>{tstatus}</b>\n"
            )

            msg += (
                f"🚀 <b>𝐒𝐏𝐄𝐄𝐃</b> → "
                f"<i>{task.seed_speed()}</i>\n"
            )

            msg += (
                f"📊 <b>𝐑𝐀𝐓𝐈𝐎</b> → "
                f"<i>{task.ratio()}</i>\n"
            )

            msg += (
                f"⏱️ <b>𝐓𝐈𝐌𝐄</b> → "
                f"<i>{task.seeding_time()}</i>\n"
            )

            msg += (
                f"⌛ <b>𝐄𝐋𝐀𝐏𝐒𝐄𝐃</b> → "
                f"<i>{get_readable_time(elapsed)}</i>\n"
            )

        # Other status
        else:

            msg += (
                f"📦 <b>𝐒𝐈𝐙𝐄</b> → "
                f"<i>{task.size()}</i>\n"
            )

        # Engine
        msg += (
            f"⚙️ <b>𝐄𝐍𝐆𝐈𝐍𝐄</b> → "
            f"<i>{task.engine}</i>\n"
        )

        # Modes
        msg += (
            f"📥 <b>𝐈𝐍</b> → "
            f"<i>{task.listener.mode[0]}</i> | "
            f"📤 <b>𝐎𝐔𝐓</b> → "
            f"<i>{task.listener.mode[1]}</i>\n"
        )

        # Select
        from ..telegram_helper.bot_commands import BotCommands

        if tstatus in [
            MirrorStatus.STATUS_DOWNLOAD,
            MirrorStatus.STATUS_PAUSED,
            MirrorStatus.STATUS_QUEUEDL,
        ]:

            if (
                task.listener.is_torrent
                or task.listener.is_qbit
                or task.listener.is_nzb
            ):
                msg += (
                    f"🎛️ <b>𝐒𝐄𝐋𝐄𝐂𝐓</b> → "
                    f"/{BotCommands.SelectCommand[1]}_"
                    f"{task.gid()[:8]}\n"
                )

        # Stop
        msg += (
            f"🛑 <b>𝐒𝐓𝐎𝐏</b> → "
            f"/{BotCommands.CancelTaskCommand[1]}_"
            f"{task.gid()[:8]}\n"
        )

        msg += "\n"

    # No active tasks
    if len(msg) == 0:

        if status == "All":
            return None, None

        else:
            msg = (
                f"❌ <b>No Active {status} Tasks!</b>\n\n"
            )

    # Bot Stats
    msg += (
        "⌬ 👑 <b><u>𝐁𝐎𝐓 𝐒𝐓𝐀𝐓𝐒</u></b>\n"
    )

    buttons = ButtonMaker()

    # Telegram group TStats
    if not is_user:
        buttons.data_button(
            "📊 𝗧𝗦𝘁𝗮𝘁𝘀",
            f"status {sid} ov",
            position="header",
            style=ButtonStyle.PRIMARY,
        )

    # Pages
    if len(tasks) > STATUS_LIMIT:

        msg += (
            f"📄 <b>𝐏𝐀𝐆𝐄</b> → "
            f"{page_no}/{pages}  |  "
            f"📊 <b>𝐓𝐀𝐒𝐊𝐒</b> → {tasks_no}  |  "
            f"🔢 <b>𝐒𝐓𝐄𝐏</b> → {page_step}\n"
        )

        buttons.data_button(
            "‹‹",
            f"status {sid} pre",
            position="header",
        )

        buttons.data_button(
            "››",
            f"status {sid} nex",
            position="header",
        )

        if tasks_no > 30:
            for i in [1, 2, 4, 6, 8, 10, 15]:
                buttons.data_button(
                    i,
                    f"status {sid} ps {i}",
                    position="footer",
                )

    # Status buttons
    if status != "All" or tasks_no > 20:

        for label, status_value in list(
            STATUSES.items()
        ):

            if status_value != status:
                buttons.data_button(
                    label,
                    f"status {sid} st {status_value}",
                )

    # Refresh
    buttons.data_button(
        "♻️ 𝗥𝗲𝗳𝗿𝗲𝘀𝗵",
        f"status {sid} ref",
        position="header",
        style=ButtonStyle.PRIMARY,
    )

    button = buttons.build_menu(8)

    # Server information
    free_disk = disk_usage(DOWNLOAD_DIR).free
    disk_free_percent = round(
        100 - disk_usage(DOWNLOAD_DIR).percent,
        1,
    )

    ram_percent = virtual_memory().percent
    cpu = cpu_percent()

    uptime = get_readable_time(
        time() - bot_start_time
    )

    msg += (
        f"\n🖥️ <b>𝐂𝐏𝐔</b> → "
        f"{cpu}%  |  "
        f"💾 <b>𝐅𝐑𝐄𝐄</b> → "
        f"{get_readable_file_size(free_disk)} "
        f"[{disk_free_percent}%]\n"
    )

    msg += (
        f"🧠 <b>𝐑𝐀𝐌</b> → "
        f"{ram_percent}%  |  "
        f"⏱️ <b>𝐔𝐏</b> → "
        f"{uptime}"
    )

    return msg, button
