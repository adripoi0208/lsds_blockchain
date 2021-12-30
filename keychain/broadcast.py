import requests
import pickle

# BASE = "http://127.0.0.1:5001/"
#
# print("Send a get request to helloworld by pressing any key.")
# input()
# response = requests.get(BASE + "helloworld")
# print(response.json())
#
# print("Send the post request to helloworld by pressing any key.")
# input()
# response = requests.post(BASE + "helloworld")
# print(response.json())
#
# print("Send a get request to paramexemple with tim as a parameter by pressing any key.")
# input()
# response = requests.get(BASE + "/paramexemple/tim")
# print(response.json())
#
# print("Send a put request to video by pressing any key.")
# input()
# response = requests.put(BASE + "video/1", {"likes":10})
# print(response.json())
#
# print("Send a get request to video by pressing any key.")
# input()
# response = requests.get(BASE + "video/1")
# print(response.json())
class Peer:
    def __init__(self, address):
        """Address of the peer.
        Can be extended if desired.
        """
        self._address = address

    def send(self, message):
        """Sends message to another process
        """
        raise NotImplementedError


class Broadcast:
	def __init__(self):
		# Will contain all the peers
		self.list = []


	def join(self, Peer):
		""" Add a new Peer object to the list
		"""
		raise NotImplementedError


	def broadcast_transaction(self, transaction):
		""" Broadcasts a transaction to add to the 'mempool'
		will maybe require to add some consensuce.
		"""
		message = {"transaction": pickle.dumps(transaction)}
		for peer in self.list:
			response = requests.put("http://" + peer.address + "/node/transaction",
									message)
