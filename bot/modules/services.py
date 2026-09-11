from html import escape
from pyrogram.enums import ButtonStyle
from time import monotonic, time
from uuid import uuid4
from re import match

from aiofiles import open as aiopen
from cloudscraper import create_scraper
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from .. import LOGGER, user_data
from ..core.config_manager import Config
from ..core.tg_client import TgClient
from ..helper.ext_utils.bot_utils import new_task, update_user_ldata
from ..helper.ext_utils.links_utils import decode_slink
from ..helper.ext_utils.status_utils import get_readable_time
from ..helper.ext_utils.db_handler import database
from ..helper.languages import Language
from ..helper.telegram_helper.bot_commands import BotCommands
from ..helper.telegram_helper.button_build import ButtonMaker
from ..helper.telegram_helper.filters import CustomFilters
from ..helper.telegram_helper.message_utils import (
    delete_message,
    edit_message,
    edit_reply_markup,
    send_file,
    send_message,
)


# =========================================================
#                    /START COMMAND
# =========================================================

@new_task
async def start(_, message):
    userid = message.from_user.id

    lang = Language()

    # -----------------------------------------------------
    # START BUTTONS
    # Only two buttons as requested
    # -----------------------------------------------------

    buttons = ButtonMaker()

    buttons.url_button(
        "👑 𝐎𝐖𝐍𝐄𝐑",
        "https://t.me/INDRA99999",
        style=ButtonStyle.PRIMARY,
    )

    buttons.url_button(
        "👥 𝐋𝐄𝐄𝐂𝐇 𝐂𝐇𝐀𝐍𝐍𝐄𝐋",
        "https://t.me/LEECH_HOUSE",
        style=ButtonStyle.PRIMARY,
    )

    reply_markup = buttons.build_menu(2)

    # -----------------------------------------------------
    # SPECIAL /start PARAMETERS
    # -----------------------------------------------------

    if (
        len(message.command) > 1
        and message.command[1] == "wzmlx"
    ):
        await delete_message(message)

    elif (
        len(message.command) > 1
        and message.command[1] != "start"
    ):
        decrypted_url = decode_slink(
            message.command[1]
        )

        # -------------------------------------------------
        # MEDIA STORE FILE LINK
        # -------------------------------------------------

        if (
            Config.MEDIA_STORE
            and decrypted_url.startswith("file")
        ):
            decrypted_url = decrypted_url.replace(
                "file",
                "",
            )

            chat_id, msg_id = decrypted_url.split(
                "&&"
            )

            LOGGER.info(
                f"Copying message from "
                f"{chat_id} & {msg_id} to {userid}"
            )

            return await TgClient.bot.copy_message(
                chat_id=userid,
                from_chat_id=(
                    int(chat_id)
                    if match(r"\d+", chat_id)
                    else chat_id
                ),
                message_id=int(msg_id),
                disable_notification=True,
            )

        # -------------------------------------------------
        # ACCESS TOKEN
        # -------------------------------------------------

        elif Config.VERIFY_TIMEOUT:
            input_token, pre_uid = (
                decrypted_url.split("&&")
            )

            if int(pre_uid) != userid:
                return await send_message(
                    message,
                    """
╭━━━━━━━━━━━━━━━━━━╮
┃ ⚠️ 𝐀𝐂𝐂𝐄𝐒𝐒 𝐃𝐄𝐍𝐈𝐄𝐃
┣━━━━━━━━━━━━━━━━━━┫
┃
┃ 🔐 This access token does not
┃ belong to your Telegram account.
┃
┃ 💡 Please generate your own
┃ access token and try again.
┃
╰━━━━━━━━━━━━━━━━━━╯
""",
                )

            data = user_data.get(
                userid,
                {},
            )

            if (
                "VERIFY_TOKEN" not in data
                or data["VERIFY_TOKEN"] != input_token
            ):
                return await send_message(
                    message,
                    """
╭━━━━━━━━━━━━━━━━━━━╮
┃⚠️𝐓𝐎𝐊𝐄𝐍 𝐀𝐋𝐑𝐄𝐀𝐃𝐘 𝐔𝐒𝐄𝐃
┣━━━━━━━━━━━━━━━━━━━┫
┃
┃ This access token has already
┃ been used or is no longer valid.
┃
┃ 🔄 Please generate a new token
┃ and try again.
┃
╰━━━━━━━━━━━━━━━━━━━╯
""",
                )

            elif (
                Config.LOGIN_PASS
                and data["VERIFY_TOKEN"].casefold()
                == Config.LOGIN_PASS.casefold()
            ):
                return await send_message(
                    message,
                    """
╭━━━━━━━━━━━━━━━━━━━━╮
┃ ✅ 𝐀𝐋𝐑𝐄𝐀𝐃𝐘 𝐋𝐎𝐆𝐆𝐄𝐃 𝐈𝐍
┣━━━━━━━━━━━━━━━━━━━━┫
┃
┃ Your bot access is already
┃ permanently activated.
┃
┃ 🔐 No temporary token is needed.
┃
╰━━━━━━━━━━━━━━━━━━━━╯
""",
                )

            buttons.data_button(
                "🔓 𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄 𝐀𝐂𝐂𝐄𝐒𝐒",
                f"start pass {input_token}",
                "header",
            )

            reply_markup = buttons.build_menu(2)

            msg = f"""
╭━━━━━━━━━━━━━━━━━━━━━━╮
┃ 🔐 𝐀𝐂𝐂𝐄𝐒𝐒 𝐋𝐎𝐆𝐈𝐍 𝐓𝐎𝐊𝐄𝐍
┣━━━━━━━━━━━━━━━━━━━━━━┫
┃
┃ ✅ 𝐒𝐓𝐀𝐓𝐔𝐒
┃    Generated Successfully
┃
┃ 🔑 𝐓𝐎𝐊𝐄𝐍
┃    <code>{input_token}</code>
┃
┃ ⏳ 𝐕𝐀𝐋𝐈𝐃𝐈𝐓𝐘
┃    {get_readable_time(int(Config.VERIFY_TIMEOUT))}
┃
┃
┃ 💡 Tap the button below to
┃ activate your access token.
┃
╰━━━━━━━━━━━━━━━━━━━━━━╯
"""

            return await send_message(
                message,
                msg,
                reply_markup,
            )

    # =====================================================
    #                    NORMAL /START
    # =====================================================

    if await CustomFilters.authorized(
        _,
        message,
    ):

        # -------------------------------------------------
        # AUTHORIZED USER
        # -------------------------------------------------

        start_string = f"""
╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
┃  👑 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐈𝐃 𝐋𝐄𝐄𝐂𝐇  👑
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃
┃ 👋 Hello, {escape(message.from_user.first_name)}!
┃
┃ 🚀 Your powerful file manager
┃ is ready to work for you.
┃
┃ 📥 Download files
┃ 📤 Upload & Leech
┃ ☁️ Mirror to Cloud
┃ 🔗 Generate direct links
┃ ⚡ Manage your tasks easily
┃
┃ 💡 Need help?
┃ Use <code>/{BotCommands.HelpCommand[0]}</code>
┃ to explore all available commands.
┃
┃ ❤️ Enjoy a smooth and simple
┃ downloading experience!
┃
╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯
"""

        await send_message(
            message,
            start_string,
            reply_markup,
            photo="IMAGES",
        )

    elif Config.BOT_PM:

        # -------------------------------------------------
        # BOT PM MODE
        # -------------------------------------------------

        await send_message(
            message,
            """
╭━━━━━━━━━━━━━━━━━━━━━━━╮
┃     👋 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 👋
┣━━━━━━━━━━━━━━━━━━━━━━━┫
┃
┃ 📬 This bot will send your
┃ files and links directly to
┃ your Private Message.
┃
┃ 🚀 You can start using the
┃ bot right away.
┃
┃ 💡 Send a supported link or
┃ use the available commands.
┃
┃ ❤️ Have a great experience!
┃
╰━━━━━━━━━━━━━━━━━━━━━━━╯
""",
            reply_markup,
            photo="IMAGES",
        )

    else:

        # -------------------------------------------------
        # UNAUTHORIZED USER
        # -------------------------------------------------

        await send_message(
            message,
            """
╭━━━━━━━━━━━━━━━━━━━━━━━╮
┃ 🔒 𝐀𝐂𝐂𝐄𝐒𝐒 𝐑𝐄𝐒𝐓𝐑𝐈𝐂𝐓𝐄𝐃
┣━━━━━━━━━━━━━━━━━━━━━━━┫
┃
┃ 👋 Welcome!
┃
┃ This bot is currently available
┃ only for authorized users.
┃
┃ 🚀 INDRA can handle:
┃
┃ 📥 Links & direct downloads
┃ 🧲 Torrents & magnets
┃ 📦 Telegram files
┃ ☁️ Cloud transfers
┃ 📤 Telegram Leech
┃
┃ ⚠️ You are not an authorized
┃ user of this bot.
┃
┃ 💡 You can deploy your own
┃ Leech bot for full access.
┃
┃ 👑 Contact the owner if you
┃ need more information.
┃
╰━━━━━━━━━━━━━━━━━━━━━━━╯
""",
            reply_markup,
            photo="IMAGES",
        )

    await database.set_pm_users(userid)


# =========================================================
#                 START ACCESS CALLBACK
# =========================================================

@new_task
async def start_cb(_, query):
    user_id = query.from_user.id
    input_token = query.data.split()[2]
    data = user_data.get(
        user_id,
        {},
    )

    if input_token == "activated":
        return await query.answer(
            "✅ Already Activated!",
            show_alert=True,
        )

    elif (
        "VERIFY_TOKEN" not in data
        or data["VERIFY_TOKEN"] != input_token
    ):
        return await query.answer(
            "⚠️ Token already used. Please generate a new one.",
            show_alert=True,
        )

    update_user_ldata(
        user_id,
        "VERIFY_TOKEN",
        str(uuid4()),
    )

    update_user_ldata(
        user_id,
        "VERIFY_TIME",
        time(),
    )

    if Config.DATABASE_URL:
        await database.update_user_data(
            user_id
        )

    await query.answer(
        "✅ Access Token Activated!",
        show_alert=True,
    )

    kb = query.message.reply_markup.inline_keyboard[1:]

    kb.insert(
        0,
        [
            InlineKeyboardButton(
                "✅️ 𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐃",
                callback_data="start pass activated",
            )
        ],
    )

    await edit_reply_markup(
        query.message,
        InlineKeyboardMarkup(kb),
    )


# =========================================================
#                       /LOGIN
# =========================================================

@new_task
async def login(_, message):

    if Config.LOGIN_PASS is None:
        return await send_message(
            message,
            """
╭━━━━━━━━━━━━━━━━━━━━━━╮
┃ 🔒 𝐋𝐎𝐆𝐈𝐍 𝐃𝐈𝐒𝐀𝐁𝐋𝐄𝐃
┣━━━━━━━━━━━━━━━━━━━━━━┫
┃
┃ Bot login is currently
┃ not enabled.
┃
╰━━━━━━━━━━━━━━━━━━━━━━╯
""",
        )

    elif len(message.command) > 1:

        user_id = message.from_user.id
        input_pass = message.command[1]

        if (
            user_data.get(
                user_id,
                {},
            ).get(
                "VERIFY_TOKEN",
                "",
            )
            == Config.LOGIN_PASS
        ):
            return await send_message(
                message,
                """
╭━━━━━━━━━━━━━━━━━━━━━━╮
┃ ✅ 𝐀𝐋𝐑𝐄𝐀𝐃𝐘 𝐋𝐎𝐆𝐆𝐄𝐃 𝐈𝐍
┣━━━━━━━━━━━━━━━━━━━━━━┫
┃
┃ You are already logged in.
┃
┃ 💡 No need to login again.
┃
╰━━━━━━━━━━━━━━━━━━━━━━╯
""",
            )

        if (
            input_pass.casefold()
            != Config.LOGIN_PASS.casefold()
        ):
            return await send_message(
                message,
                """
╭━━━━━━━━━━━━━━━━━━━━━━╮
┃ ❌ 𝐖𝐑𝐎𝐍𝐆 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃
┣━━━━━━━━━━━━━━━━━━━━━━┫
┃
┃ The password you entered
┃ is incorrect.
┃
┃ 🔄 Please check it and try again.
┃
╰━━━━━━━━━━━━━━━━━━━━━━╯
""",
            )

        update_user_ldata(
            user_id,
            "VERIFY_TOKEN",
            Config.LOGIN_PASS,
        )

        if Config.DATABASE_URL:
            await database.update_user_data(
                user_id
            )

        return await send_message(
            message,
            """
╭━━━━━━━━━━━━━━━━━━━━━━╮
┃ 🎉 𝐋𝐎𝐆𝐈𝐍 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋
┣━━━━━━━━━━━━━━━━━━━━━━┫
┃
┃ ✅ Your bot access has been
┃ permanently activated.
┃
┃ 🚀 You can now use the bot.
┃
╰━━━━━━━━━━━━━━━━━━━━━━╯
""",
        )

    else:

        await send_message(
            message,
            """
╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
┃ 🔐 𝐁𝐎𝐓 𝐋𝐎𝐆𝐈𝐍
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃
┃ Use the command below:
┃
┃ <code>/login [password]</code>
┃
┃ 💡 Replace [password] with
┃ your login password.
┃
╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯
""",
        )


# =========================================================
#                        /PING
# =========================================================

@new_task
async def ping(_, message):

    start_time = monotonic()

    reply = await send_message(
        message,
        """
╭━━━━━━━━━━━━━━━━━━━━━━╮
┃ 📡 𝐂𝐇𝐄𝐂𝐊𝐈𝐍𝐆 𝐏𝐈𝐍𝐆
┣━━━━━━━━━━━━━━━━━━━━━━┫
┃
┃ ⏳ Please wait...
┃
╰━━━━━━━━━━━━━━━━━━━━━━╯
""",
    )

    end_time = monotonic()

    await edit_message(
        reply,
        f"""
╭━━━━━━━━━━━━━━━━━━━━━━╮
┃ 🏓 𝐏𝐎𝐍𝐆!
┣━━━━━━━━━━━━━━━━━━━━━━┫
┃
┃ ⚡ Response Time
┃    <code>{int((end_time - start_time) * 1000)} ms</code>
┃
┃ 🟢 Bot is online and working.
┃
╰━━━━━━━━━━━━━━━━━━━━━━╯
""",
    )


# =========================================================
#                         /LOG
# =========================================================

@new_task
async def log(_, message):

    uid = message.from_user.id

    buttons = ButtonMaker()

    buttons.data_button(
        "📋 𝐃𝐈𝐒𝐏𝐋𝐀𝐘 𝐋𝐎𝐆",
        f"log {uid} disp",
    )

    buttons.data_button(
        "🌐 𝐖𝐄𝐁 𝐋𝐎𝐆",
        f"log {uid} web",
    )

    buttons.data_button(
        "❌ 𝐂𝐋𝐎𝐒𝐄",
        f"log {uid} close",
        style=ButtonStyle.DANGER,
    )

    await send_file(
        message,
        "log.txt",
        buttons=buttons.build_menu(2),
    )


# =========================================================
#                    LOG CALLBACK
# =========================================================

@new_task
async def log_cb(_, query):

    data = query.data.split()

    message = query.message
    user_id = query.from_user.id

    if user_id != int(data[1]):

        await query.answer(
            "⚠️ This log panel does not belong to you!",
            show_alert=True,
        )

    elif data[2] == "close":

        await query.answer()

        await delete_message(
            message,
            message.reply_to_message,
        )

    elif data[2] == "disp":

        await query.answer(
            "📋 Loading log...",
        )

        async with aiopen(
            "log.txt",
            "r",
        ) as f:
            content = await f.read()

        def parse(line):
            parts = line.split(
                "] [",
                1,
            )

            return (
                f"[{parts[1]}"
                if len(parts) > 1
                else line
            )

        try:

            res, total = [], 0

            for line in reversed(
                content.splitlines()
            ):

                line = parse(line)

                res.append(line)

                total += len(line) + 1

                if total > 3500:
                    break

            text = (
                f"""
╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
┃ 📋 𝐋𝐎𝐆 𝐏𝐑𝐄𝐕𝐈𝐄𝐖
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃
┃ Showing the latest
┃ {len(res)} log lines.
┃
╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯

<b>━━━━━━━━ 𝐒𝐓𝐀𝐑𝐓 𝐋𝐎𝐆 ━━━━━━━━</b>

<blockquote expandable>{escape('\n'.join(reversed(res)))}</blockquote>

<b>━━━━━━━━ 𝐄𝐍𝐃 𝐋𝐎𝐆 ━━━━━━━━</b>
"""
            )

            btn = ButtonMaker()

            btn.data_button(
                "❌ 𝐂𝐋𝐎𝐒𝐄",
                f"log {user_id} close",
                style=ButtonStyle.DANGER,
            )

            await send_message(
                message,
                text,
                btn.build_menu(1),
            )

            await edit_reply_markup(
                message,
                None,
            )

        except Exception as err:

            LOGGER.error(
                f"TG Log Display : {str(err)}"
            )

    elif data[2] == "web":

        boundary = "R1eFDeaC554BUkLF"

        headers = {
            "Content-Type": (
                "multipart/form-data; "
                f"boundary=----WebKitFormBoundary{boundary}"
            ),
            "Origin": "https://spaceb.in",
            "Referer": "https://spaceb.in/",
            "sec-ch-ua": (
                '"Not-A.Brand";v="99", '
                '"Chromium";v="124"'
            ),
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": (
                "Mozilla/5.0 "
                "(Linux; Android 10; K) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/124.0.0.0 "
                "Mobile Safari/537.36"
            ),
        }

        async with aiopen(
            "log.txt",
            "r",
        ) as f:
            content = await f.read()

        data = (
            f"------WebKitFormBoundary{boundary}\r\n"
            'Content-Disposition: form-data; name="content"\r\n\r\n'
            f"{content}\r\n"
            f"------WebKitFormBoundary{boundary}--\r\n"
        )

        cget = create_scraper().request

        resp = cget(
            "POST",
            "https://spaceb.in/",
            headers=headers,
            data=data,
        )

        if resp.status_code == 200:

            await query.answer(
                "🌐 Generating web log...",
            )

            btn = ButtonMaker()

            btn.url_button(
                "📨 𝐖𝐄𝐁 𝐏𝐀𝐒𝐓𝐄",
                resp.url,
                style=ButtonStyle.PRIMARY,
            )

            await edit_reply_markup(
                message,
                btn.build_menu(1),
            )

        else:

            await query.answer(
                "❌ Web paste failed. Please check the logs.",
                show_alert=True,
            )
