from functools import wraps
from typing import Callable, Optional, Tuple  # noqa: F401

import aiohttp
import aioodbc.cursor  # noqa: F401

import bot
from lib.data import ChatCommandArgs, ChatCommand


async def getSecretKey(args: ChatCommandArgs) -> Optional[str]:
    query: str = '''SELECT secretKey FROM warp_world WHERE broadcaster=?'''
    cursor: aioodbc.cursor.Cursor
    async with await args.database.cursor() as cursor:
        await cursor.execute(query, (args.chat.channel,))
        row: Optional[Tuple[str]] = await cursor.fetchone()
        if row is not None:
            return row[0]
    return None


async def api_call(url: str) -> Optional[str]:
    session: aiohttp.ClientSession
    response: aiohttp.ClientResponse
    try:
        async with aiohttp.ClientSession(raise_for_status=True) as session, \
                session.get(url, timeout=bot.config.httpTimeout) as response:
            if response.status == 200:
                message = await response.text()
                message = message.replace('\r\n', ' ')
                message = message.replace('\n', ' ')
                message = message.replace('\r', ' ')
                message = message.replace('\0', '')
                return message
    except aiohttp.ClientResponseError as e:
        if e.code == 404:
            return None
    return 'Warp.World API error'


def warpWorldCommand(func: Callable[[ChatCommandArgs, str], str]
                     ) -> ChatCommand:
    @wraps(func)
    async def chatCommand(args: ChatCommandArgs) -> bool:
        key: Optional[str] = await getSecretKey(args)
        if key is None:
            return False
        url: str = func(args, key)
        args.chat.send(await api_call(url))
        return True
    return chatCommand
