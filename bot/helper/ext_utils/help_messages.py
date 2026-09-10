#INDRA EDIT

mirror = """<b>📥 MIRROR</b>

<b>🔗 Start a Mirror</b>

Send the link with the command:

<code>/cmd link</code>

<b>📎 Using a Reply</b>

Reply to a link or file and use:

<code>/cmd -n New Name -e -up upload_destination</code>

<b>💡 Quick Tip</b>
You can add different options after the command to control how the file is downloaded, processed and uploaded.

<b>⚠️ Note</b>
Commands starting with <b>qb</b> are only for torrent downloads."""


yt = """<b>📺 YOUTUBE &amp; YT-DLP</b>

<b>🔗 Start a Download</b>

Send the link with the command:

<code>/cmd link</code>

<b>📎 Using a Reply</b>

Reply to a link and use:

<code>/cmd -n New Name -z password -opt x:y|x1:y1</code>

<b>🌐 Supported Websites</b>

You can use any website supported by yt-dlp.

<a href='https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md'>🔗 View Supported Sites</a>

<b>⚙️ YT-DLP Options</b>

You can use advanced yt-dlp API options with <code>-opt</code>.

<a href='https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L212'>🔗 View YT-DLP Options</a>

<a href='https://t.me/mltb_official_channel/177'>🔗 CLI to API Converter</a>"""


clone = """<b>☁️ CLONE</b>

Clone files or folders from supported cloud services.

<b>🔗 Supported Sources</b>

GDrive • Gdot • Filepress • Filebee • Appdrive • Gdflix • Rclone

You can send the link or rclone path with the command, or reply to the link/file.

<b>🔄 Rclone Sync</b>

Use <code>-sync</code> when you want to use the sync method.

<b>Example:</b>

<code>/cmd rcl/rclone_path -up rcl/rclone_path/rc -sync</code>"""


new_name = """<b>✨ NEW NAME</b> <code>-n</code>

Change the name of the downloaded file or folder.

<b>Example:</b>

<code>/cmd link -n My New File</code>

<b>💡 Tip</b>
Do not add the file extension manually.

<b>⚠️ Note</b>
This option does not work with torrents."""


multi_link = """<b>🔗 MULTI LINK</b> <code>-i</code>

Download multiple links or files in one task.

<b>📌 How to use</b>

Reply to the first link/file and tell the bot how many links/files you want to process.

<b>Example:</b>

<code>/cmd -i 10</code>

Here <code>10</code> means 10 links/files."""


same_dir = """<b>📁 SAME DIRECTORY</b> <code>-m</code>

Move multiple files or folders into one new folder.

This is useful when you want several downloads to be uploaded together as one task.

<b>1️⃣ Single Link</b>

<code>/cmd link -m My Folder</code>

<b>2️⃣ Multiple Links</b>

<code>/cmd -i 10 -m My Folder</code>

<b>3️⃣ Bulk Links</b>

<code>/cmd -b -m My Folder</code>

<b>📌 Different Folder Example</b>

<code>link1 -m folder1
link2 -m folder1
link3 -m folder2
link4 -m folder2
link5 -m folder3
link6</code>

So:

📁 link1 + link2 → <b>folder1</b>
📁 link3 + link4 → <b>folder2</b>
📁 link5 → <b>folder3</b>
📄 link6 → normal upload

<b>💡 Tip</b>
The <code>-m</code> option is especially useful when working with many links."""


thumb = """<b>🖼️ THUMBNAIL</b> <code>-t</code>

Set a thumbnail for the current task.

<b>Example:</b>

<code>/cmd link -t image-url</code>

You can also use:

• Direct image URL
• Telegram message link
• Telegram photo/document
• <code>none</code> to remove the thumbnail

<b>📌 Supported Images</b>

JPG • PNG • WEBP and other direct image formats."""


split_size = """<b>✂️ SPLIT SIZE</b> <code>-sp</code>

Set the maximum size of each output file.

<b>Examples:</b>

<code>/cmd link -sp 500mb</code>

<code>/cmd link -sp 2gb</code>

<code>/cmd link -sp 4000000000</code>

<b>💡 Tip</b>
You can use <code>mb</code> or <code>gb</code>, or enter the size directly in bytes.

<b>⚠️ Note</b>
Only MB and GB units are supported."""


upload = """<b>📤 UPLOAD DESTINATION</b> <code>-up</code>

Choose where the bot should upload the completed files.

<b>☁️ Rclone / Google Drive</b>

<code>/cmd link -up rcl</code>
<code>/cmd link -up gdl</code>

The buttons can be used to select the available configuration.

You can also enter a destination directly:

<code>-up remote:dir/subdir</code>

<code>-up Gdrive_ID</code>

<b>📱 Telegram</b>

<code>-up id/@username/pm</code>

<b>🤖 Upload using Bot</b>

<code>-up b:id/@username/pm</code>

<b>👤 Upload using User Account</b>

<code>-up u:id/@username</code>

This requires a user session to be configured.

<b>🔄 Hybrid Upload</b>

<code>-up h:id/@username</code>

The bot/user account is selected automatically based on file size.

<b>💬 Topic Upload</b>

<code>-up id/@username|topic_id</code>

<b>📦 Named Dump Chat</b>

Use:

<code>-ud name</code>

or:

<code>-ud id/@username</code>

If the name is configured in <code>LEECH_DUMP_CHATS</code>, the bot will use that destination.

<b>🔐 Custom Rclone / GDrive</b>

<code>-up mrcc:remote:path</code>

<code>-up mtp:gdrive_id</code>

You can also use the owner/user configuration added through User Settings.

<b>💡 Important</b>

<code>DEFAULT_UPLOAD</code> does not affect Telegram leech commands."""


user_download = """<b>⬇️ USER DOWNLOAD</b>

Use these options when you want to download using a configured user/owner account.

<b>🔐 Owner Token</b>

<code>/cmd tp:link</code>

<b>☁️ Service Account</b>

<code>/cmd sa:link</code>

<b>📁 Google Drive File ID</b>

<code>/cmd tp:gdrive_id</code>

or:

<code>/cmd sa:gdrive_id</code>

<b>👤 User Token</b>

<code>/cmd mtp:gdrive_id</code>

<code>/cmd mtp:link</code>

<b>🔄 User Rclone</b>

<code>/cmd mrcc:remote:path</code>

<b>💡 Tip</b>
You can use the owner/user configuration from User Settings without adding <code>mtp:</code> or <code>mrcc:</code> manually."""


rcf = """<b>⚙️ RCLONE FLAGS</b> <code>-rcf</code>

Use custom rclone flags for the current task.

<b>Example:</b>

<code>/cmd link -up path -rcf --buffer-size:8M|--drive-starred-only|key|key:value</code>

These flags can override other rclone settings except <code>--exclude</code>.

<a href='https://rclone.org/flags/'>🔗 View Rclone Flags</a>"""


bulk = """<b>📚 BULK DOWNLOAD</b> <code>-b</code>

Download many links from a text message or text file.

Each link should be on a separate line.

<b>Example:</b>

<code>link1 -n New Name -up remote1:path
link2 -z -n Another Name -up remote2:path
link3 -e -n File Name -up remote2:path</code>

Then reply to that message with:

<code>/cmd -b</code>

<b>🌟 Apply Options to All Links</b>

<code>/cmd -b -up remote: -z -m My Folder</code>

This applies the command options to all links.

<b>📌 Select a Range</b>

<code>-b start:end</code>

or:

<code>-b :end</code>

or:

<code>-b start</code>

The default start is <code>0</code> and the default end is the last link.

<b>⚠️ Note</b>
When <code>-m</code> is used with bulk, individual upload destinations cannot be set for each link."""


rclone_dl = """<b>🔄 RCLONE DOWNLOAD</b>

Rclone paths can be used like normal download links.

<b>Example:</b>

<code>/cmd main:dump/ubuntu.iso</code>

You can also use <code>rcl</code> to select the rclone configuration, remote and path.

<b>👤 User Rclone</b>

Users can add their own rclone configuration through User Settings.

<b>Example:</b>

<code>/cmd mrcc:main:dump/ubuntu.iso</code>

<b>💡 Tip</b>
You can use the saved owner/user configuration without manually adding <code>mrcc:</code>."""


extract_zip = """<b>📦 EXTRACT / ZIP</b> <code>-e -z</code>

<b>📂 Extract a File</b>

<code>/cmd link -e password</code>

<b>🗜️ Create a ZIP</b>

<code>/cmd link -z password</code>

<b>🔐 Extract and ZIP</b>

<code>/cmd link -z password -e</code>

If both options are used, the bot will:

1️⃣ Extract the file first
2️⃣ Then create the ZIP

<b>💡 Tip</b>
Use <code>-e</code> before <code>-z</code> when both operations are needed."""


join = """<b>🧩 JOIN FILES</b> <code>-j</code>

Join split files into one file.

<b>📌 Reply Method</b>

<code>/cmd -i 3 -j -m My Folder</code>

or:

<code>/cmd -b -j -m My Folder</code>

You can also use:

<code>/cmd link -j</code>

<b>⚠️ Important</b>
This option should be used before Extract or ZIP operations.

It is commonly used together with <code>-m</code> (Same Directory)."""


tg_links = """<b>📱 TELEGRAM LINKS</b>

Telegram links can be used like normal direct links.

Some private links require a configured user session.

<b>🌐 Public Link</b>

<code>https://t.me/channel_name/message_id</code>

<b>🔒 Private Link</b>

<code>tg://openmessage?user_id=xxxxxx&amp;message_id=xxxxx</code>

<b>📢 Supergroup / Channel Link</b>

<code>https://t.me/c/channel_id/message_id</code>

<b>📚 Message Range</b>

<code>https://t.me/channel_name/100-150</code>

or:

<code>tg://openmessage?user_id=xxxxxx&amp;message_id=555-560</code>

<b>⚠️ Note</b>
Range links work only when the command is sent as a reply to the link."""


sample_video = """<b>🎬 SAMPLE VIDEO</b> <code>-sv</code>

Create a short sample from a video or a folder of videos.

<b>Default</b>

<code>/cmd -sv</code>

Default sample duration: <b>60 seconds</b>
Default part duration: <b>4 seconds</b>

<b>⚙️ Custom Settings</b>

<code>/cmd -sv 70:5</code>

This means:

🎞️ Sample duration → 70 seconds
⏱️ Part duration → 5 seconds

You can also use:

<code>/cmd -sv :5</code>

or:

<code>/cmd -sv 70</code>"""


screenshot = """<b>📸 SCREENSHOTS</b> <code>-ss</code>

Create screenshots from a video or a folder of videos.

<b>Default:</b>

<code>/cmd -ss</code>

The default number of screenshots is <b>10</b>.

<b>Custom Number</b>

<code>/cmd -ss 6</code>

This creates 6 screenshots."""


seed = """<b>🌱 BITTORRENT SEED</b> <code>-d</code>

Continue seeding a torrent after the download finishes.

<b>Format:</b>

<code>-d ratio:time</code>

<b>Examples:</b>

<code>-d 0.7:10</code>

Ratio → 0.7
Time → 10 minutes

You can also use:

<code>-d 0.7</code>

Only ratio

or:

<code>-d :10</code>

Only time."""


zip_arg = """<b>🗜️ ZIP</b> <code>-z</code>

Create a ZIP file.

<b>Normal ZIP</b>

<code>/cmd link -z</code>

<b>🔐 Password Protected ZIP</b>

<code>/cmd link -z password</code>

<b>💡 Tip</b>
Use a strong password if the ZIP contains private files."""


qual = """<b>🎞️ QUALITY SELECTION</b> <code>-s</code>

Choose the video quality for a specific download.

This is useful when a default yt-dlp format is already configured but you want to select another quality for a particular task.

<b>Example:</b>

<code>/cmd link -s</code>

The bot will show the available quality buttons."""


yt_opt = """<b>⚙️ YT-DLP OPTIONS</b> <code>-opt</code>

Use advanced yt-dlp API options for a specific download.

<b>Example:</b>

<code>/cmd link -opt {"format": "bv*+mergeall[vcodec=none]", "nocheckcertificate": True, "playliststart": 10, "fragment_retries": float("inf"), "matchtitle": "S13", "writesubtitles": True, "live_from_start": True, "postprocessor_args": {"ffmpeg": ["-threads", "4"]}, "wait_for_video": (5, 100), "download_ranges": [{"start_time": 0, "end_time": 10}]}</code>

<a href='https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184'>🔗 View YT-DLP API Options</a>

<a href='https://t.me/mltb_official_channel/177'>🔗 CLI to API Converter</a>

<b>💡 Tip</b>
This option is mainly for advanced users."""


convert_media = """<b>🔄 CONVERT MEDIA</b> <code>-ca -cv</code>

Convert audio or video files into another format.

<b>🎵 Convert Audio</b>

<code>/cmd link -ca mp3</code>

Convert all audio files to MP3.

<b>🎬 Convert Video</b>

<code>/cmd link -cv mp4</code>

Convert all video files to MP4.

<b>🎵 + 🎬 Convert Both</b>

<code>/cmd link -ca mp3 -cv mp4</code>

<b>🎯 Convert Selected Audio Types</b>

<code>/cmd link -ca mp3 + flac ogg</code>

<b>🎯 Convert Selected Video Types</b>

<code>/cmd link -cv mkv - webm flv</code>

This lets you include or exclude specific formats."""


force_start = """<b>🚀 FORCE START</b> <code>-f -fd -fu</code>

Force a queued task to start.

<b>📥 Force Download + Upload</b>

<code>/cmd link -f</code>

<b>📥 Force Download Only</b>

<code>/cmd link -fd</code>

<b>📤 Force Upload After Download</b>

<code>/cmd link -fu</code>

<b>💡 Tip</b>
These options are useful when you want to control the normal task queue."""


gdrive = """<b>☁️ GOOGLE DRIVE</b>

Download or upload using Google Drive.

<b>🔗 Direct GDrive Link</b>

<code>/cmd gdriveLink</code>

<b>📤 Upload to GDrive</b>

<code>/cmd gdriveLink -up gdl</code>

You can also use a Google Drive ID.

<b>🔐 Token / Service Account</b>

<code>/cmd tp:gdriveLink</code>

<code>/cmd sa:gdriveLink</code>

<b>👤 User Token</b>

<code>/cmd mtp:gdriveLink</code>

This uses the user token added through User Settings.

<b>💡 Tip</b>
You can use the saved owner/user configuration without manually adding the prefix when supported."""


rclone_cl = """<b>🔄 RCLONE</b>

Use an rclone remote or path as the source or destination.

<b>📥 Download</b>

<code>/cmd rcl/rclone_path</code>

<b>📤 Upload</b>

<code>/cmd rcl/rclone_path -up rclone_path</code>

<b>⚙️ Rclone Flags</b>

<code>/cmd rcl/rclone_path -rcf flagkey:flagvalue|flagkey|flagkey:flagvalue</code>

<b>👤 User Rclone</b>

<code>/cmd mrcc:rclone_path</code>

This uses the user rclone configuration added through User Settings."""


name_swap = r"""<b>🔄 NAME SUBSTITUTION</b> <code>-ns</code>

Replace words or patterns inside file names.

<b>Format:</b>

<code>wordToReplace/wordToReplaceWith/sensitiveCase</code>

<b>Examples:</b>

<code>/cmd link -ns script/code/s</code>

Replace <code>script</code> with <code>code</code>.

<code>/cmd link -ns mirror/leech</code>

Replace <code>mirror</code> with <code>leech</code>.

<code>/cmd link -ns clone/</code>

Remove <code>clone</code>.

<b>📌 Special Characters</b>

You must escape special characters with <code>\</code> when required.

Special characters include:

<code>^ $ . | ? * + ( ) [ ] { } -</code>

<b>⏱️ Timeout</b>

60 seconds.

<b>💡 Tip</b>
The substitution affects all files processed by the task."""


transmission = """<b>📤 TELEGRAM TRANSMISSION</b>

Choose which Telegram account should upload the file.

<b>🔄 Hybrid</b>

<code>/cmd link -hl</code>

Uses the user account for files larger than 2 GB and the bot for files up to 2 GB.

<b>🤖 Bot Only</b>

<code>/cmd link -bt</code>

Uses the bot account only.

<b>👤 User Only</b>

<code>/cmd link -ut</code>

Uses the user account only."""


thumbnail_layout = """<b>🖼️ THUMBNAIL LAYOUT</b> <code>-tl</code>

Choose how thumbnails are arranged.

<b>Example:</b>

<code>/cmd link -tl 3x3</code>

This creates a layout with:

3️⃣ images in each row
3️⃣ rows in each column

<b>💡 Tip</b>
Change the numbers to create a different layout."""


leech_as = """<b>📤 LEECH TYPE</b> <code>-doc -med</code>

Choose how Telegram should send the file.

<b>📄 As Document</b>

<code>/cmd link -doc</code>

Send the file as a Telegram document.

<b>🎬 As Media</b>

<code>/cmd link -med</code>

Send the file as Telegram media."""


ffmpeg_cmds = """<b>🎬 FFMPEG COMMANDS</b> <code>-ff</code>

Run custom FFmpeg commands before uploading files.

Do not write <code>ffmpeg</code> at the beginning. Start directly with the arguments.

<b>🗑️ Delete Original</b>

Add <code>-del</code> to a command when you want the original file deleted after processing.

<b>📌 Pre-Saved Command</b>

If a command is saved with a key such as <code>subtitle</code>, use:

<code>/cmd -ff subtitle</code>

<b>Example Commands</b>

<code>-i mltb.mkv -c copy -c:s srt mltb.mkv</code>

<code>-i mltb.video -c copy -c:s srt mltb</code>

<code>-i mltb.m4a -c:a libmp3lame -q:a 2 mltb.mp3</code>

<code>-i mltb.audio -c:a libmp3lame -q:a 2 mltb.mp3</code>

<b>📚 What does mltb.* mean?</b>

<code>mltb.mkv</code>
→ Works only with MKV files.

<code>mltb.video</code>
→ Works with all video files.

<code>mltb.m4a</code>
→ Works only with M4A audio.

<code>mltb.audio</code>
→ Works with all audio files.

<b>💡 Tip</b>
FFmpeg commands are powerful. Use them carefully."""


alldebrid_arg = """<b>🔓 ALLDEBRID</b> <code>-ad</code>

Use AllDebrid to unlock supported file-host links.

<b>Example:</b>

<code>/cmd link -ad</code>

It can resolve supported hosts such as 1fichier, Rapidgator, Mega and others supported by AllDebrid.

<b>🧲 Torrents</b>

Magnet links and torrent files can also be processed through AllDebrid when <code>-ad</code> is enabled.

<b>⚡ Why use it?</b>

AllDebrid can be useful when normal downloading is slow or a torrent has poor availability.

<b>🔑 Required</b>

You need to configure:

<code>ALLDEBRID_API_KEY</code>"""


seedr_arg = """<b>☁️ SEEDR CLOUD</b> <code>-seedr</code>

Send a magnet link to your Seedr cloud account.

<b>Example:</b>

<code>/cmd magnet -seedr</code>

The bot waits for Seedr to finish the download and then downloads the finished files over HTTP.

<b>📌 Supported Input</b>

• Magnet links
• .torrent URLs

<b>🔐 Required Settings</b>

Configure:

<code>SEEDR_EMAIL</code>

and:

<code>SEEDR_PASSWORD</code>

You can add them through User Settings or the bot configuration."""


metadata = """<b>🏷️ METADATA</b> <code>-meta</code>

Add custom metadata to media files.

<b>📌 Format</b>

<code>key=value|key2=value2|key3=value3</code>

<b>🔤 Dynamic Variables</b>

<code>{filename}</code>
Original filename

<code>{basename}</code>
Filename without extension

<code>{extension}</code>
File extension

<code>{audiolang}</code>
Detected audio language

<code>{sublang}</code>
Detected subtitle language

<code>{year}</code>
Year found in the filename

<b>🎵 Audio Metadata</b>

Set metadata for audio streams.

<b>🎬 Video Metadata</b>

Set metadata for video streams.

<b>💬 Subtitle Metadata</b>

Set metadata for subtitle streams.

<b>Example:</b>

<code>/mirror link -meta title=My Movie|artist={audiolang} Version</code>

<code>/yt link -meta album={basename}|year={year}|genre=Action</code>

<b>🔐 Escape Pipe Character</b>

Use <code>\|</code> when you want to write a literal <code>|</code> inside a value.

<b>Example:</b>

<code>title=Movie \| Director's Cut</code>"""


YT_HELP_DICT = {
    "main": yt,
    "New-Name": f"{new_name}\n\n<b>📌 Note:</b> Don't add the file extension.",
    "Zip": zip_arg,
    "Quality": qual,
    "Options": yt_opt,
    "Multi-Link": multi_link,
    "Same-Directory": same_dir,
    "Thumb": thumb,
    "Split-Size": split_size,
    "Upload-Destination": upload,
    "Rclone-Flags": rcf,
    "Bulk": bulk,
    "Sample-Video": sample_video,
    "Screenshot": screenshot,
    "Convert-Media": convert_media,
    "Force-Start": force_start,
    "Name-Swap": name_swap,
    "TG-Transmission": transmission,
    "Thumb-Layout": thumbnail_layout,
    "Leech-Type": leech_as,
    "FFmpeg-Cmds": ffmpeg_cmds,
    "Metadata": metadata,
}


MIRROR_HELP_DICT = {
    "main": mirror,
    "New-Name": new_name,
    "DL-Auth": """<b>🔐 DIRECT LINK AUTHORIZATION</b> <code>-au -ap</code>

Some direct links require a username and password.

<b>Example:</b>

<code>/cmd link -au username -ap password</code>""",
    "Headers": """<b>📨 CUSTOM HEADERS</b> <code>-h</code>

Add custom headers for a direct download.

<b>Example:</b>

<code>/cmd link -h key: value key1: value1</code>""",
    "Extract/Zip": extract_zip,
    "Select-Files": """<b>📂 SELECT FILES</b> <code>-s</code>

Select specific files from Bittorrent, JDownloader or Sabnzbd tasks.

<b>Example:</b>

<code>/cmd link -s</code>

You can also reply to a file or link.""",
    "Torrent-Seed": seed,
    "Multi-Link": multi_link,
    "Same-Directory": same_dir,
    "Thumb": thumb,
    "Split-Size": split_size,
    "Upload-Destination": upload,
    "Rclone-Flags": rcf,
    "Bulk": bulk,
    "Join": join,
    "Rclone-DL": rclone_dl,
    "Tg-Links": tg_links,
    "Sample-Video": sample_video,
    "Screenshot": screenshot,
    "Convert-Media": convert_media,
    "Force-Start": force_start,
    "User-Download": user_download,
    "Name-Swap": name_swap,
    "TG-Transmission": transmission,
    "Thumb-Layout": thumbnail_layout,
    "Leech-Type": leech_as,
    "FFmpeg-Cmds": ffmpeg_cmds,
    "Metadata": metadata,
    "AllDebrid": alldebrid_arg,
    "Seedr": seedr_arg,
}


CLONE_HELP_DICT = {
    "main": clone,
    "Multi-Link": multi_link,
    "Bulk": bulk,
    "Gdrive": gdrive,
    "Rclone": rclone_cl,
}


RSS_HELP_MESSAGE = """
<b>📡 RSS FEED SETUP</b>

Add your RSS feed using this format:

<code>Title1 link</code>

<code>Title2 link -c cmd -inf xx -exf xx</code>

<code>Title3 link -c cmd -d ratio:time -z password</code>

<b>⚙️ Available Options</b>

<code>-c</code> → Command

<code>-up</code> → Upload destination

<code>-rcf</code> → Rclone flags

<code>-inf</code> → Include words

<code>-exf</code> → Exclude words

<code>-stv</code> → Sensitive filter (true/false)

<b>📌 Example</b>

<code>Title https://www.rss-url.com -inf 1080 or 720 or 144p|mkv or mp4|hevc -exf flv or web|xxx</code>

<b>Filter Rules</b>

<code>|</code> means AND.

Use <code>or</code> between similar choices.

<b>Example:</b>

<code>1080 or 720p|mkv or mp4|hevc</code>

This means:

1080 OR 720p
AND
mkv OR mp4
AND
hevc

<b>💡 Tip</b>

Look at the exact title format of the content and use special characters when needed to avoid incorrect matches.

<b>⏱️ Timeout:</b> 60 seconds.
"""


PASSWORD_ERROR_MESSAGE = """
<b>🔐 PASSWORD REQUIRED</b>

This link is password protected.

Add <code>::</code> after the link and enter the password.

<b>Example:</b>

<code>link::my password</code>
"""


def get_bot_commands():
    from ...core.plugin_manager import get_plugin_manager

    static_commands = {
        "Mirror": "[link/file] Mirror to Upload Destination",
        "QbMirror": "[magnet/torrent] Mirror using qBittorrent",
        "Ytdl": "[link] Download YouTube and other yt-dlp supported links",
        "UpHoster": "[link/file] Upload to supported DDL servers",
        "Leech": "[link/file] Download and send files to Telegram",
        "QbLeech": "[magnet/torrent] Leech using qBittorrent",
        "YtdlLeech": "[link] Leech yt-dlp supported links",
        "Clone": "[link] Clone files/folders to Google Drive",
        "UserSet": "Manage your personal bot settings",
        "ForceStart": "[gid/reply] Force start a queued task",
        "Count": "[link] Count files/folders in Google Drive",
        "List": "[query] Search text in Google Drive",
        "Search": "[query] Search torrents using Qbit plugins",
        "Select": "[gid/reply] Select files from a task",
        "Ping": "Check bot response speed",
        "Status": "[id/me] View current bot tasks",
        "Stats": "View bot and server statistics",
        "Rss": "Manage RSS feeds",
        "CancelAll": "Cancel all active tasks",
        "Help": "Open detailed bot help",
        "BotSet": "[SUDO] Manage bot settings",
        "Log": "[SUDO] View bot logs",
        "Memory": "[SUDO] View memory and cache usage",
        "Restart": "[SUDO] Restart the bot",
        "RestartSessions": "[SUDO] Restart user sessions",
    }

    commands = static_commands.copy()

    plugin_manager = get_plugin_manager()

    if plugin_manager:
        for plugin_info in plugin_manager.list_plugins():
            if plugin_info.enabled and plugin_info.commands:
                for cmd in plugin_info.commands:
                    key = cmd.capitalize()

                    if key not in commands:
                        commands[key] = (
                            plugin_info.description
                            or f"Plugin command: {cmd}"
                        )

    return commands


BOT_COMMANDS = get_bot_commands()


def get_help_string():
    from ..telegram_helper.bot_commands import BotCommands

    help_lines = [
        "╔══════════════════════════╗",
        "      🤖 <b>HELP CENTER</b>",
        "╚══════════════════════════╝",
        "",
        "👋 <b>Welcome!</b>",
        "Use the commands below to control the bot.",
        "",
        "💡 <b>Tip:</b> Try a command without arguments to see its detailed usage.",
        "",
        "━━━━━━━━━━━━━━━━━━━━",
    ]

    commands = BotCommands.get_commands()

    for key, cmds in commands.items():
        cmd_attr = getattr(BotCommands, f"{key}Command", None)

        if not cmd_attr:
            continue

        if isinstance(cmd_attr, list):
            cmd_str = f"/{' or /'.join(cmd_attr)}"
        else:
            cmd_str = f"/{cmd_attr}"

        if key == "Mirror":
            help_lines.append(f"📥 <b>{cmd_str}</b> — Mirror to cloud.")
        elif key == "QbMirror":
            help_lines.append(f"🧲 <b>{cmd_str}</b> — Mirror using qBittorrent.")
        elif key == "JdMirror":
            help_lines.append(f"📦 <b>{cmd_str}</b> — Mirror using JDownloader.")
        elif key == "NzbMirror":
            help_lines.append(f"📰 <b>{cmd_str}</b> — Mirror using Sabnzbd.")
        elif key == "Ytdl":
            help_lines.append(f"📺 <b>{cmd_str}</b> — Download yt-dlp supported links.")
        elif key == "UpHoster":
            help_lines.append(f"📤 <b>{cmd_str}</b> — Upload to DDL servers.")
        elif key == "Leech":
            help_lines.append(f"📱 <b>{cmd_str}</b> — Send files to Telegram.")
        elif key == "QbLeech":
            help_lines.append(f"🧲 <b>{cmd_str}</b> — Leech using qBittorrent.")
        elif key == "JdLeech":
            help_lines.append(f"📦 <b>{cmd_str}</b> — Leech using JDownloader.")
        elif key == "NzbLeech":
            help_lines.append(f"📰 <b>{cmd_str}</b> — Leech using Sabnzbd.")
        elif key == "SeedrLink":
            help_lines.append(f"☁️ <b>{cmd_str}</b> — Get Seedr download links.")
        elif key == "YtdlLeech":
            help_lines.append(f"📺 <b>{cmd_str}</b> — Leech yt-dlp supported links.")
        elif key == "Clone":
            help_lines.append(f"☁️ <b>{cmd_str}</b> [drive_url] — Clone to Google Drive.")
        elif key == "Count":
            help_lines.append(f"🔢 <b>{cmd_str}</b> [drive_url] — Count Drive files.")
        elif key == "Delete":
            help_lines.append(
                f"🗑️ <b>{cmd_str}</b> [drive_url] — Delete Drive files."
            )
        elif key == "UserSet":
            help_lines.append(f"⚙️ <b>{cmd_str}</b> — Personal settings.")
        elif key == "BotSet":
            help_lines.append(f"🛠️ <b>{cmd_str}</b> — Bot settings.")
        elif key == "Select":
            help_lines.append(f"📂 <b>{cmd_str}</b> — Select files from a task.")
        elif key == "CancelTask":
            help_lines.append(f"❌ <b>{cmd_str}</b> [gid] — Cancel a task.")
        elif key == "ForceStart":
            help_lines.append(f"🚀 <b>{cmd_str}</b> [gid] — Force start a task.")
        elif key == "CancelAll":
            help_lines.append(f"🛑 <b>{cmd_str}</b> — Cancel all tasks.")
        elif key == "List":
            help_lines.append(f"🔎 <b>{cmd_str}</b> [query] — Search Google Drive.")
        elif key == "Search":
            help_lines.append(f"🔍 <b>{cmd_str}</b> [query] — Search torrents.")
        elif key == "Status":
            help_lines.append(f"📊 <b>{cmd_str}</b> — View active tasks.")
        elif key == "Stats":
            help_lines.append(f"🖥️ <b>{cmd_str}</b> — View server statistics.")
        elif key == "Ping":
            help_lines.append(f"🏓 <b>{cmd_str}</b> — Check bot response time.")
        elif key == "Authorize":
            help_lines.append(f"🔐 <b>{cmd_str}</b> — Authorize a user or chat.")
        elif key == "UnAuthorize":
            help_lines.append(f"🔓 <b>{cmd_str}</b> — Remove authorization.")
        elif key == "Users":
            help_lines.append(f"👥 <b>{cmd_str}</b> — View user settings.")
        elif key == "AddSudo":
            help_lines.append(f"👑 <b>{cmd_str}</b> — Add a sudo user.")
        elif key == "RmSudo":
            help_lines.append(f"➖ <b>{cmd_str}</b> — Remove a sudo user.")
        elif key == "BlackList":
            help_lines.append(f"🚫 <b>{cmd_str}</b> — Block a user.")
        elif key == "RmBlackList":
            help_lines.append(f"✅ <b>{cmd_str}</b> — Remove a user from blacklist.")
        elif key == "AddImage":
            help_lines.append(f"🖼️ <b>{cmd_str}</b> — Add an image to the gallery.")
        elif key == "Images":
            help_lines.append(f"🎨 <b>{cmd_str}</b> — Manage the image gallery.")
        elif key == "Restart":
            help_lines.append(f"🔄 <b>{cmd_str}</b> — Restart and update the bot.")
        elif key == "Log":
            help_lines.append(f"📜 <b>{cmd_str}</b> — Get bot logs.")
        elif key == "Shell":
            help_lines.append(f"💻 <b>{cmd_str}</b> — Run a shell command.")
        elif key == "AExec":
            help_lines.append(f"⚡ <b>{cmd_str}</b> — Run an async function.")
        elif key == "Exec":
            help_lines.append(f"⚡ <b>{cmd_str}</b> — Run a sync function.")
        elif key == "ClearLocals":
            help_lines.append(
                f"🧹 <b>/{BotCommands.ClearLocalsCommand}</b> — Clear execution locals."
            )
        elif key == "Rss":
            help_lines.append(
                f"📡 <b>/{BotCommands.RssCommand}</b> — RSS management."
            )
        elif key in BOT_COMMANDS:
            help_lines.append(
                f"🔹 <b>{cmd_str}</b> — {BOT_COMMANDS[key]}"
            )

    help_lines.extend(
        [
            "",
            "━━━━━━━━━━━━━━━━━━━━",
            "✨ <b>WZML-X • Simple • Powerful • Fast</b>",
        ]
    )

    return "\n".join(help_lines)


help_string = get_help_string()
