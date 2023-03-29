
from Release import ReleaseHandler

import random

class BatchStageHandler(ReleaseHandler):
	def calculateReleaseScore(self, data):
		score = random.random()
		return score
