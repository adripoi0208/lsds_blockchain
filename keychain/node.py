from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from blockchain import *
import argparse
import requests
import pickle

app = Flask(__name__)
api = Api(app)

def parse_arguments():
    parser = argparse.ArgumentParser(
        "KeyChain - An overengineered key-value store "
        "with version control, powered by fancy linked-lists.")

    parser.add_argument("--miner", type=bool, default=False, nargs='?',
                        const=True, help="Starts the mining procedure.")
    parser.add_argument("--bootstrap", type=str, default=None,
                        help="Sets the address of the bootstrap node.")
    parser.add_argument("--difficulty", type=int, default=5,
                        help="Sets the difficulty of Proof of Work, only has "
                             "an effect with the `--miner` flag has been set.")
    arguments, _ = parser.parse_known_args()

    return arguments

arguments = parse_arguments()
blk_chain = blockchain.Blockchain(arguments.bootstrap, arguments.difficulty)
mempool = []
node_put_args = reqparse.RequestParser()
node_put_args.add_argument("transaction", type=str,
                            help="string defining a transaction")
node_put_args.add_argument("block", type=str,
                            help="string defining a block")

class Node_Blockchain(Resource):
    def get(self, action):
        if action == "bootstrap":
            ret["list_of_block"] = pickle.dumps(blk_chain._blocks)
            ret["list_of_peer"] = pickle.dumps(blk_chain._broadcast.list)
            ret["current_transactions"] = pickle.dumps(blk_chain._current_transactions)
            return ret

        else:
            abort(501, message="Method not implemented...")

    def put(self, action):
        if action == "transaction":
            args = node_put_args.parse_args()
            #Deserializes the transaction
            transaction = pickle.loads(args["transaction"])
            mempool.append()
            abort(501, message="Method not implemented...")

        elif action == "block":
            args = node_put_args.parse_args()
            #Deserializes the block
            transaction = pickle.loads(args["block"])
            abort(501, message="Method not implemented...")

        else:
            abort(501, message="Method not implemented...")

api.add_resource(ParamExemple, "/node/<string:action>")

if __name__ == "__main__":
    app.run(debug=True, port=5001) # Remove debug=true when deploying
