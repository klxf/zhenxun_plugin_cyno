from configs.path_config import DATA_PATH
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent
from nonebot.rule import to_me
from random import choice
from utils.message_builder import image
import json

__zx_plugin_name__ = "来点赛诺笑话"
__plugin_usage__ = """
usage：
    来点赛诺笑话
    指令：
        来点赛诺笑话
""".strip()
__plugin_des__ = "来点赛诺笑话"
__plugin_cmd__ = ["来点赛诺笑话"]
__plugin_version__ = 0.1
__plugin_author__ = "Mr_Fang"
__plugin_setting__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["来点赛诺笑话"],
}

getjoke = on_command("来点赛诺笑话", rule=to_me(), priority=5, block=True)

@getjoke.handle()
async def _(event: GroupMessageEvent):
    jokes_json_file = DATA_PATH / "cyno" / "jokes.json"
    jokes = json.loads(open(jokes_json_file, "r").read())
    img = image(DATA_PATH / "cyno" / "cyno.jpg")
    msg = choice(jokes["jokes"]) + img
    await getjoke.send(msg)
