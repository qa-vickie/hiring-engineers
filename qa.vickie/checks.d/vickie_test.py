from checks import AgentCheck
import time
import random
from hashlib import md5


class TestSupportRandomCheck(AgentCheck):
	def check(self, nistance):
		self.gauge('test.support.random', random.random())

