"""
Blockchain (stub).
NB: Feel free to extend or modify.
"""
from collections import OrderedDict
import hashlib as hl
import time

class Block:
    def __init__(self, hashpointer, data, proof = None):
        """Describe the properties of a block."""
        self.hashpointer = hashpointer
        #Holds the list of transactions a.k.a. the key-value pairs.
        self.data = data

        #Holds the proof of the block. Since we haven't decided how it will be
        #done, we currently stre it as an unknown object.
        self.proof = proof

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

    def retrieve(self, key):
        """Returns most recent value of the specified key or None."""
        for tran in self.data:
            if key == tran.get_key():
                return tran.get_value()

        return None


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
                   self.origin == other.origin

        return False

    def get_string(self):
        return str(self.key) + "," + str(self.value) + "," + str(self.origin)

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def load_from_string(t_string):
        # Creates a Transaction object from a transaction string.
        split = t_string.split(',')
        key = split[0]
        value = split[1]
        origin = split[2]

        transaction = Transaction(key, value, origin)
        return transaction


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


class Blockchain:

    #Variables used to tune difficulty. Will have to be modified when testing.
    N_NONCE_CMP = 10
    MIN_TIME = 600

    def __init__(self, bootstrap, difficulty):
        """The bootstrap address serves as the initial entry point of
        the bootstrapping procedure. In principle it will contact the specified
        addres, download the peerlist, and start the bootstrapping procedure.
        """
        raise NotImplementedError

        # Initialize the properties.
        self._blocks = []
        self._peers = []
        self._difficulty = difficulty

        # Storing times at which we found nonces to be able to tune difficulty.
        self._found_times = []

        # Initialize the chain with the Genesis block.
        self._add_genesis_block()

        # Bootstrap the chain with the specified bootstrap address.
        self._bootstrap(bootstrap)

    def _add_genesis_block(self):
        """Adds the genesis block to your blockchain."""
        #Need to add proof (+hashpointer ?)
        genesis_block = Block('',[])
        self._blocks.append(genesis_block)

        return

    def _bootstrap(self, address):
        """Implements the bootstrapping procedure."""
        peer = Peer(address)
        raise NotImplementedError

    def difficulty(self):
        """Returns the difficulty level."""
        return self._difficulty

    def tune_difficulty(self):
        """Tunes difficulty if blocks are found too fast"""
        times = self._found_times

        if len(times) >= N_NONCE_CMP:
            total = 0
            for i in range(len(times)):
                total += times[i]
            mean_time = total / len(times)
            if mean_time < MIN_TIME:
                self._difficulty += 1
                self._found_times.clear()
            else:
                return
        else:
            return

    def add_transaction(self, transaction):
        """Adds a transaction to your current list of transactions,
        and broadcasts it to your Blockchain network.
        If the `mine` method is called, it will collect the current list
        of transactions, and attempt to mine a block with those.
        """
        raise NotImplementedError

    def mine(self, transactions, hashpointer):
        """Implements the mining procedure."""

        nonce = self.proof_of_work(transactions, hashpointer)
        self.tune_difficulty()

        block = Block(hashpointer, transactions, nonce)
        self._blocks.append(block)

        #Je pense qu'il manque des trucs ici ça me parait trop simple.

        return block

    def proof_of_work(self, transactions, hashpointer):
        # Finds a nonce such that the hash function of this nonce combined with 
        # the hashpointer and the transactions fills the condition that depends on the difficulty.

        nonce = 0
        start_time = time.time()
        while not self.is_valid_guess(transactions, hashpointer, nonce):
            nonce += 1
        end_time = time.time()
        elapsed_time = end_time - start_time
        self._found_times.append(elapsed_time)

        print("Found a nonce after ", elapsed_time," seconds, value of nonce : ", nonce)

        return nonce

    def is_valid_guess(self, transactions, hashpointer, nonce):
        guess = (";".join([tran.get_string() for tran in transactions]) + str(hashpointer) + str(nonce)).encode()
        guess_hash = hl.sha256(guess).hexdigest()
        difficulty = self._difficulty
        return guess_hash[0:difficulty] == '0' * difficulty

    def is_valid(self):
        """Checks if the current state of the blockchain is valid.
        Meaning, are the sequence of hashes, and the proofs of the
        blocks correct?
        """
        raise NotImplementedError