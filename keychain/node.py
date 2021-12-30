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
# video_put_args.add_argument("views", type=int,
#                             help="views of the video")
# video_put_args.add_argument("likes", type=int,
#                             help="likes of the video")

class Node_Blockchain(Resource):
    def get(self, action):
        pass

    def put(self, action):
        tran = node_put_args.parse_args()
        transaction = blockchain.Transaction()
        mempool.append()

api.add_resource(ParamExemple, "/node/<string:action>")

if __name__ == "__main__":
    app.run(debug=True, port=5001) # Remove debug=true when deploying
