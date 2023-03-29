
from abc import ABC, abstractmethod

class ReleaseHandler(ABC):

	@abstractmethod
	def calculateReleaseScore(self, request):
		pass
		
