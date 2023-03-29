
from Batch import BatchHandler
from BatchStage import BatchStageHandler
from MonitorGroup import MonitorGroupHandler
from Sample import SampleHandler

class HandlerFactory:
	def __init__(self):
		self.handlers = {
			"Batch": BatchHandler,
			"BatchStage": BatchStageHandler,
			"MonitorGroup": MonitorGroupHandler,
			"Sample": SampleHandler
		}

	def get_handler(self, type):
		HandlerClass = self.handlers.get(type)
		if not HandlerClass:
			raise ValueError(f"No handler found for type {type}")
		return HandlerClass()