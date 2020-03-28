import pyrogram
import re

async def sec(time):
    a = time
    d = re.compile(r'\d+').findall(a)
    if "d" in time:
        timev = str(int(d[0]) * 24 * 3600)
    elif "h" in time:
        timev = str(int(d[0]) * 3600)
    elif "m" in time:
        timev = str(int(d[0]) * 60)
    elif "s" in time:
        timev = str(int(d[0]))
    else:
        timev = "no format"
    return timev
