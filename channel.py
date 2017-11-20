from typing import Any, Tuple  # noqa: F401

import aioodbc.cursor  # noqa: F401

from lib.data import ChatCommandArgs
from lib.database import DatabaseMain
from lib.helper.chat import min_args, permission
from . import library


@permission('broadcaster')
async def commandSetWarpWorld(args: ChatCommandArgs) -> bool:
    db: DatabaseMain
    cursor: aioodbc.cursor.Cursor
    async with DatabaseMain.acquire() as db, await db.cursor() as cursor:
        query: str
        params: Tuple[Any, ...]
        if len(args.message) >= 2:
            if db.isSqlite:
                query = '''
REPLACE INTO warp_world (broadcaster, secretKey) VALUES (?, ?)
'''
                params = args.chat.channel, args.message[1]
            else:
                query = '''
INSERT INTO warp_world (broadcaster, secretKey) VALUES (?, ?)
    ON CONFLICT ON CONSTRAINT warp_world_pkey
    DO UPDATE SET secretKey=?
'''
                params = args.chat.channel, args.message[1], args.message[1]
            await cursor.execute(query, params)
            args.chat.send('Warp.World Secret Key is updated')
        else:
            query = '''DELETE FROM warp_world WHERE broadcaster=?'''
            await cursor.execute(query, (args.chat.channel,))
            args.chat.send('''\
Warp.World Secret Key is deleted. Warp.World support is disabled.''')
        await db.commit()
    return True


@min_args(2)
@library.warpWorldCommand
def commandAdd(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/add?\
streamer={args.chat.channel}&submitter={args.nick}&key={key}&\
levelcode={args.message.query}'''


@permission('moderator')
@min_args(2)
@library.warpWorldCommand
def commandAllow(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/allow?\
streamer={args.chat.channel}&key={key}&levelcode={args.message.query}'''


@permission('moderator')
@min_args(2)
@library.warpWorldCommand
def commandBanCreator(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/bancreator?\
streamer={args.chat.channel}&key={key}&bancreator={args.message.query}'''


@permission('moderator')
@min_args(2)
@library.warpWorldCommand
def commandUnbanCreator(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/unbancreator?\
streamer={args.chat.channel}&key={key}&bancreator={args.message.query}'''


@permission('moderator')
@min_args(2)
@library.warpWorldCommand
def commandBanUser(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/banuser?\
streamer={args.chat.channel}&key={key}&banuser={args.message.query}'''


@permission('moderator')
@min_args(2)
@library.warpWorldCommand
def commandUnbanUser(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/unbanuser?\
streamer={args.chat.channel}&key={key}&banuser={args.message.query}'''


@library.warpWorldCommand
def commandClears(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/clears?\
streamer={args.chat.channel}&key={key}'''


@permission('moderator')
@library.warpWorldCommand
def commandClose(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/close?\
streamer={args.chat.channel}&key={key}'''


@permission('moderator')
@library.warpWorldCommand
def commandCompleted(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/complete?\
streamer={args.chat.channel}&key={key}'''


@library.warpWorldCommand
def commandCurrent(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/current?\
streamer={args.chat.channel}&submitter={args.nick}'''


@permission('moderator')
@library.warpWorldCommand
def commandDelete(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/delete?\
streamer={args.chat.channel}&key={key}'''


@library.warpWorldCommand
def commandList(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/list?\
streamer={args.chat.channel}&submitter={args.nick}'''


@permission('moderator')
@library.warpWorldCommand
def commandNext(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/next?\
streamer={args.chat.channel}&key={key}'''


@permission('moderator')
@library.warpWorldCommand
def commandOpen(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/open?\
streamer={args.chat.channel}&key={key}'''


@library.warpWorldCommand
def commandQueue(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/queue?\
streamer={args.chat.channel}&submitter={args.nick}'''


@permission('moderator')
@library.warpWorldCommand
def commandRand(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/rand?\
streamer={args.chat.channel}&key={key}'''


@min_args(2)
@library.warpWorldCommand
def commandRemove(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/remove?\
streamer={args.chat.channel}&submitter={args.nick}&key={key}&\
levelcode={args.message.query}'''


@min_args(2)
@library.warpWorldCommand
def commandReplace(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/replace?\
streamer={args.chat.channel}&submitter={args.nick}&key={key}&\
levelcode={args.message.query}'''


@permission('moderator')
@min_args(2)
@library.warpWorldCommand
def commandSetCurrent(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/setcurrent?\
streamer={args.chat.channel}&submitter={args.nick}&key={key}&\
levelcode={args.message.query}'''


@permission('moderator')
@library.warpWorldCommand
def commandSkip(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/skip?\
streamer={args.chat.channel}&key={key}'''


@library.warpWorldCommand
def commandStats(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/stats?\
streamer={args.chat.channel}&submitter={args.nick}'''


@library.warpWorldCommand
def commandSubmit(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/submit?\
streamer={args.chat.channel}&submitter={args.nick}'''


@permission('broadcaster')
@library.warpWorldCommand
def commandWWSettings(args: ChatCommandArgs, key: str) -> str:
    return f'''\
http://warp.world/bot/wwsettings?\
streamer={args.chat.channel}&key={key}&q={args.message.query}'''
