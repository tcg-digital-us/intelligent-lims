
from Release import ReleaseHandler

import random

class BatchHandler(ReleaseHandler):
	def handle(self, data):
		score = random.random()
		return score