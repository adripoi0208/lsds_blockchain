from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from blockchain import *
import argparse
import requests
import pickle

def parse_arguments():
    parser = argparse.ArgumentParser(
        "KeyChain - An overengineered key-value store "
        "with version control, powered by fancy linked-lists.")

    parser.add_argument("--bootstrap", type=str, default=None,
                        help="Sets the address of the bootstrap node.")
    parser.add_argument("--difficulty", type=int, default=5,
                        help="Sets the difficulty of Proof of Work, only has "
                             "an effect with the `--miner` flag has been set.")
    arguments, _ = parser.parse_known_args()

    return arguments

class Node_Blockchain(Resource):
    def __init__(self, **kwargs):
        self.blk_chain = kwargs["blockchain"]

    def get(self, action):
        if action == "bootstrap":
            ret["list_of_block"] = pickle.dumps(self.blk_chain._blocks)
            ret["list_of_peer"] = pickle.dumps(self.blk_chain._broadcast.list)
            ret["current_transactions"] = pickle.dumps(self.blk_chain._current_transactions)
            return ret

        else:
            abort(501, message="Method not implemented...")

    def put(self, action):
        if action == "transaction":
            args = node_put_args.parse_args()
            #Deserializes the transaction
            transaction = pickle.loads(args["transaction"])
            self.blk_chain.receive_block(transaction)

        elif action == "block":
            args = node_put_args.parse_args()
            #Deserializes the block
            block = pickle.loads(args["block"])
            self.blk_chain.receive_block(block)

        else:
            abort(501, message="Method not implemented...")

def run_node(blockchain, port):
    app = Flask(__name__)
    api = Api(app)

    node_put_args = reqparse.RequestParser()
    node_put_args.add_argument("transaction", type=str,
                                help="string defining a transaction")
    node_put_args.add_argument("block", type=str,
                                help="string defining a block")
    api.add_resource(Node_Blockchain, "/node/<string:action>",
                     resource_class_kwargs={"blockchain":blockchain})

    app.run(debug=False, port=port) # Remove debug=true when deploying

if __name__ == "__main__":
    arguments = parse_arguments()

    app = Flask(__name__)
    api = Api(app)

    node_put_args = reqparse.RequestParser()
    node_put_args.add_argument("transaction", type=str,
                                help="string defining a transaction")
    node_put_args.add_argument("block", type=str,
                                help="string defining a block")
    #For the
    blockchain = Blockchain(arguments.bootstrap, arguments.difficulty)
    api.add_resource(Node_Blockchain, "/node/<string:action>",
                     resource_class_kwargs={"blockchain":blockchain})

    app.run(debug=True, port=5001) # Remove debug=true when deploying
