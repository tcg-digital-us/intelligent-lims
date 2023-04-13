
from actions.ActionHandler import ActionHandlerABC
from microservices.ReleaseScore import ReleaseScore

"""
_args here should be the entire content block
"""

class GetScoreHandler(ActionHandlerABC):
    @staticmethod
    def exec(_args):
        return ReleaseScore.get(_args)