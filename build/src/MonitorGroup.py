
from Release import ReleaseHandler

import random

class MonitorGroupHandler(ReleaseHandler):
	def handle(self, data):
		score = random.random()
		return score