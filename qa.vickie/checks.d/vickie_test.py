from checks import AgentCheck
import time
import random
from hashlib import md5


class TestSupportRandomCheck(AgentCheck):
	def check(self, nistance):
		self.gauge('test.support.random', random.random())

		aggregation_key = md5('testSupportRandom').hexdigest()

		self.event({
			'timestamp': int(time.time()),
			'event_type': 'testSupportRandom_check',
			'msg_title': 'TestSupportRandom event title',
			'aggregation_key': aggregation_key 
		})
