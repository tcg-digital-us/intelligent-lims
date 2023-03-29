
from Release import ReleaseHandler

import random

class MonitorGroupHandler(ReleaseHandler):
	def calculateReleaseScore(self, data):
		score = random.random()
		return score
