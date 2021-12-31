import requests
import pickle


class Peer:
    def __init__(self, address):
        """Address of the peer.
        Can be extended if desired.
        """
        self._address = address

    def send_transaction(self, transaction):
        """sends a transaction to the peer in order to add it to the mempool.
        """
		message = {"transaction": pickle.dumps(transaction)}
		response = requests.put("http://" + self._address + "/node/transaction",
								message)

	def send_block(self, block):
		"""Sends a block to the peer in order to add it to the
		blockchain (if valid).
        """
		message = {"block": pickle.dumps(block)}
        response = requests.put("http://" + self._address + "/node/block",
								message)

	def request_bootstrap(self):
		"""Sends a bootstrap message to the peer that returns the list of
		every node's address and the entire blockchain.
		"""
		response = requests.get("http://" + self._address + "/node/bootstrap")

		list_of_block = pickle.loads(response.json()["list_of_block"])
		current_transactions = pickle.loads(response.json()["current_transactions"])
		list_of_peer = pickle.loads(response.json()["list_of_peer"])

		return list_of_peer, list_of_block, current_transactions


class Broadcast:
	def __init__(self):
		# Will contain all the peers
		self.list = []

	def join(self, peer):
		""" Add a new Peer object to the list
		"""
		self.list.append(peer)

	def broadcast_block(self, block):
		"""Broadcasts a block in order to add it to the blockchain (if valid).
		"""
		for peer in self.list:
			peer.send_block(block)

	def broadcast_transaction(self, transaction):
		""" Broadcasts a transaction to add to the 'mempool'
		will maybe require to add some consensuce.
		"""
		for peer in self.list:
			peer.send_transaction(transaction)
