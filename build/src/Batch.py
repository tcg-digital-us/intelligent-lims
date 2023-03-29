
from Release import ReleaseHandler

import random

class BatchHandler(ReleaseHandler):
	def calculateReleaseScore(self, data):
		score = random.random()
		return score
