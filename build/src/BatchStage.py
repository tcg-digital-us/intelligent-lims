
from Release import ReleaseHandler

import random

class BatchStageHandler(ReleaseHandler):
	def handle(self, data):
		score = random.random()
		return score