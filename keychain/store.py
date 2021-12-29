"""
KeyChain key-value store (stub).

NB: Feel free to extend or modify.
"""

from keychain import Blockchain
from keychain import Transaction


class Callback:
    def __init__(self, transaction, chain):
        self._transaction = transaction
        self._chain = chain

    def wait(self):
        """Wait until the transaction appears in the blockchain."""
        while True:
            iterator = self._chain.descendingIterator()
            for block in iterator:
                if block.contains(self._transaction):
                    return
        # Use a timeout to avoid infinite loops ????

    def completed(self):
        """Polls the blockchain to check if the data is available."""
        raise NotImplementedError


class Storage:
    def __init__(self, bootstrap, miner, difficulty):
        """Allocate the backend storage of the high level API, i.e.,
        your blockchain. Depending whether or not the miner flag has
        been specified, you should allocate the mining process.
        """
        self._blockchain = Blockchain(bootstrap, difficulty)

    def put(self, key, value, block=True):
        """Puts the specified key and value on the Blockchain.

        The block flag indicates whether the call should block until the value
        has been put onto the blockchain, or if an error occurred.
        """
        transaction = Transaction(key, value, ??ORIGIN??)
        self._blockchain.add_transaction(self, transaction)
        callback = Callback(transaction, self._blockchain)
        if block:
            callback.wait()

        return callback

    def retrieve(self, key):
        """Searches the most recent value of the specified key.

        -> Search the list of blocks in reverse order for the specified key,
        or implement some indexing schemes if you would like to do something
        more efficient.
        """
        iterator = self._blockchain.descendingIterator()
        for block in iterator:
            value = block.retrieve(key)
            if value != None:
                return value

        return "Key not found"



    def retrieve_all(self, key):
        """Retrieves all values associated with the specified key on the
        complete blockchain.
        """
        values = []
        iterator = self._blockchain.descendingIterator()
        for block in iterator:
            val = block.retrieve(key)
            if val != None:
                values.append(val)

        if values == []:
            return "Key not found"
        else:
            return values