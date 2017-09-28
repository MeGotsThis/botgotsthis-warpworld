from typing import Iterable, Mapping, Optional

from lib.data import ChatCommand

from .. import channel


def filterMessage() -> Iterable[ChatCommand]:
    return []


def commands() -> Mapping[str, Optional[ChatCommand]]:
    if not hasattr(commands, 'commands'):
        setattr(commands, 'commands', {
            '!setwarpworld': channel.commandSetWarpWorld,
            '!add': channel.commandAdd,
            '!allow': channel.commandAllow,
            '!bancreator': channel.commandBanCreator,
            '!unbancreator': channel.commandUnbanCreator,
            '!banuser': channel.commandBanUser,
            '!unbanuser': channel.commandUnbanUser,
            '!clears': channel.commandClears,
            '!close': channel.commandClose,
            '!completed': channel.commandCompleted,
            '!current': channel.commandCurrent,
            '!delete': channel.commandAdd,
            '!list': channel.commandList,
            '!next': channel.commandNext,
            '!open': channel.commandOpen,
            '!queue': channel.commandQueue,
            '!rand': channel.commandRand,
            '!remove': channel.commandRemove,
            '!replace': channel.commandReplace,
            '!setcurrent': channel.commandSetCurrent,
            '!skip': channel.commandSkip,
            '!stats': channel.commandStats,
            '!submit': channel.commandSubmit,
            '!wwsettings': channel.commandWWSettings,
            }
        )
    return getattr(commands, 'commands')


def commandsStartWith() -> Mapping[str, Optional[ChatCommand]]:
    return {}


def processNoCommand() -> Iterable[ChatCommand]:
    return []
