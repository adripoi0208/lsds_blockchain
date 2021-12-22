class Broadcast:
	def __init__(self):
	# Will contain all the peers
	self.list = []


	def join(self, Peer):
	""" Add a new Peer object to the list 
	"""
	raise NotImplementedError


	def broadcast(self, message):
	""" Broadcast message to all the peers in list 
	"""
	raise NotImplementedError