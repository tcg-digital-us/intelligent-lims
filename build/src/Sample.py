
from Release import ReleaseHandler

import random

class SampleHandler(ReleaseHandler):
	def caculateReleaseScore(self, data):
		score = random.random()
		return score
