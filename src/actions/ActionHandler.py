
from abc import ABC, abstractmethod

class ActionError(Exception):
    pass

class ActionHandlerABC(ABC):
    @abstractmethod
    def exec(_args):
        pass

# These imports must stay here as them being below the ABC allows for getting around a 'circular import' situation.

from actions.handlers.GetScoreHandler import GetScoreHandler
from actions.handlers.LookupTransactionHandler import LookupTransactionHandler

# |---------- To add a new action, import the handler and add an entry here.
# V
action_handlers = {
    "getScore": GetScoreHandler,
    "lookupTransaction": LookupTransactionHandler
}

def handle_action(action: str, args: dict) -> None:
    if action not in action_handlers: raise ActionError("Unsupported action")

    try:
        return action_handlers[action].exec(_args=args)
    except Exception as e:
        raise ActionError(str(e))