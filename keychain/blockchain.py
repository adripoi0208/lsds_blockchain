"""
Blockchain (stub).

NB: Feel free to extend or modify.
"""


class Block:
    def __init__(self):
        """Describe the properties of a block."""
        self.hashpointer = None
        #Holds the list of transactions a.k.a. the key-value pairs.
        self.data = []

        #Holds the proof of the block. Since we haven't decided how it will be
        #done, we currently stre it as an unknown object.
        self.proof = None

    def proof(self):
        """Return the proof of the current block."""
        return self.proof

    def transactions(self):
        """Returns the list of transactions associated with this block."""
        return self.data

    def contains(self, transaction):
        """Returns a boolean expressing wether or not the transaction is contained in the block."""
        out = False
        for tran in self.data:
            out = out or transaction == tran

        return out

class Transaction:
    def __init__(self, key, value, origin):
        """A transaction, in our KV setting. A transaction typically involves
        some key, value and an origin (the one who put it onto the storage).
        """
        self.key = key
        self.value = value
        self.origin = origin

    def __eq__(self, other):
        """Defines how to compare two transactions using the operator ==.
        """
        if isinstance(other, Transaction):
            return self.key == other.key and self.value == other.value and
                   self.origin == ther.origin

        return False

class Peer:
    def __init__(self, address):
        """Address of the peer.

        Can be extended if desired.
        """
        self._address = address


class Blockchain:
    def __init__(self, bootstrap, difficulty):
        """The bootstrap address serves as the initial entry point of
        the bootstrapping procedure. In principle it will contact the specified
        address, download the peerlist, and start the bootstrapping procedure.
        """
        raise NotImplementedError

        # Initialize the properties.
        self._blocks = []
        self._peers = []
        self._difficulty = difficulty

        # Initialize the chain with the Genesis block.
        self._add_genesis_block()

        # Bootstrap the chain with the specified bootstrap address.
        self._bootstrap(bootstrap)

    def _add_genesis_block(self):
        """Adds the genesis block to your blockchain."""
        raise NotImplementedError
        pass

    def _bootstrap(self, address):
        """Implements the bootstrapping procedure."""
        peer = Peer(address)
        raise NotImplementedError

    def difficulty(self):
        """Returns the difficulty level."""
        return self._difficulty

    def add_transaction(self, transaction):
        """Adds a transaction to your current list of transactions,
        and broadcasts it to your Blockchain network.

        If the `mine` method is called, it will collect the current list
        of transactions, and attempt to mine a block with those.
        """
        raise NotImplementedError

    def mine(self):
        """Implements the mining procedure."""
        raise NotImplementedError

    def is_valid(self):
        """Checks if the current state of the blockchain is valid.

        Meaning, are the sequence of hashes, and the proofs of the
        blocks correct?
        """
        raise NotImplementedError
