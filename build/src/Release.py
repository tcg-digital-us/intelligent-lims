
from abc import ABC, abstractmethod

class ReleaseHandler(ABC):

	@abstractmethod
	def handle(self, request):
		pass
		