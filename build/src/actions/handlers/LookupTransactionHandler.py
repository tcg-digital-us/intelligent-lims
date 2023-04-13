from actions.ActionHandler import ActionHandlerABC
from storage.RecordStore import RecordStore

"""
The _args here should just be something like:

{
    "transaction_id": "vaf849jhaf4jaw"
}
"""

class LookupTransactionHandler(ActionHandlerABC):
    @staticmethod
    def exec(_args):
        return RecordStore.get_record(_args.get('transaction_id', None))
