import json
import random

import requests

from userbot import CMD_HELP, bot
from userbot.events import register
from userbot.utils import edit_delete, edit_or_reply

category = ["classic", "kids", "party", "hot", "mixed"]


async def get_task(mode, choice):
    url = "https://psycatgames.com/api/tod-v2/"
    data = {
        "id": "truth-or-dare",
        "language": "id",
        "category": category[choice],
        "type": mode,
    }
    headers = {
        "referer": "https://psycatgames.com/app/truth-or-dare/?utm_campaign=tod_website&utm_source=tod_id&utm_medium=website"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    result = response.json()["results"]
    return random.choice(result)


@register(outgoing=True, pattern=r"^\.(task|truth|dare)$")
async def tod(event):
    tod=event.pattern_match.group(1)
    if tod == "task":
        xxnx=await edit_or_reply(event, "`Processing...`")
        tod=random.choice(["truth", "dare"])
    else:
        xxnx=await edit_or_reply(event, f"`Tugas {tod} acak untuk Anda...`")
    category=event.pattern_match.group(2)
    category=int(random.choice(category)
                 ) if category else random.choice([1, 2])
    try:
        task=await get_task(tod, category)
        if tod == "truth":
            await xxnx.edit(f"**Tugas Truth untuk Anda adalah**\n`{task}`")
        else:
            await xxnx.edit(f"**Tugas Dare untuk Anda adalah**\n`{task}`")
    except Exception as e:
        await edit_delete(xxnx, f"**ERROR: `{e}`")


CMD_HELP.update(
    {
        "truth_dare": f"**Plugin : **`truth_dare`\
        \n\n  •  **Syntax :** `.truth`\
        \n  •  **Function : **Memberikan anda tantangan kejujuran secara random.\
        \n\n  •  **Syntax :** `.dare`\
        \n  •  **Function : **Memberikan anda tantangan Keberanian secara random.\
        \n\n  •  **Syntax :** `.task`\
        \n  •  **Function : **Untuk Memberikan anda tantangan secara random.\
    "
    }
)
