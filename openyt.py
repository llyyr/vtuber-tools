# opens an url in streamlink, along with the chat if the stream is on youtube

import sys
import subprocess
from urllib import parse

DEFAULT_QUALITY = 'best'
BROWSER_PATH = r'C:\Program Files\Mozilla Firefox\firefox.exe'
BROWSER_ARGS = '-new-window'
CHAT_URL = 'https://www.youtube.com/live_chat?is_popout=1&v='

if 2 <= len(sys.argv) <= 3:
    url = sys.argv[1]
    quality = DEFAULT_QUALITY if len(sys.argv)==2 else sys.argv[2]

    if 'youtu' in url:
        v = parse.parse_qs(parse.urlparse(url).query)['v'][0]
        subprocess.run([BROWSER_PATH, BROWSER_ARGS, CHAT_URL+v])
    try:
        subprocess.run(['streamlink', url, quality], shell=True)
    except KeyboardInterrupt:
        exit()
else:
    print('invalid args')
