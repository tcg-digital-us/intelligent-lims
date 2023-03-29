
from Release import ReleaseHandler

import random

class SampleHandler(ReleaseHandler):
	def calculateReleaseScore(self, data):
		score = random.random()
		return score
