
from Release import ReleaseHandler

import random

class SampleHandler(ReleaseHandler):
	def handle(self, data):
		score = random.random()
		return score