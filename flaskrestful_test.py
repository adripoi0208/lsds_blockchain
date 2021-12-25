from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)


#############################################################
######Returning a simple json upon a get/post request########
class HelloWorld(Resource):
    def get(self): #The name of the method is important
        ret = {} #we need to return a dictionnary -> auto json
        ret["data"] = "Hello world"
        return ret

    def post(self):
        ret = {}
        ret["data"] = "Hello world but with a post"
        return ret

###Once the class is finished, we have to add it to the app.
api.add_resource(HelloWorld, "/helloworld")
#############################################################



#############################################################
###########Passing parameter through the request#############
#################+ a global data structure###################
#A global dictionnary
names = {"tim": {"age": 19, "gender": "male"},
        "bill": {"age": 70, "gender": "male"}}

class ParamExemple(Resource):
    def get(self, name): #The name of the method is important
        ret = names[name]
        return ret

###Once the class is finished, we have to add it to the app.
api.add_resource(ParamExemple, "/paramexemple/<string:name>")
#############################################################



#############################################################
#############Parsing an incoming json file###################
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str,
                            help="Name of the video")
video_put_args.add_argument("views", type=int,
                            help="views of the video")
video_put_args.add_argument("likes", type=int,
                            help="likes of the video")
#We can add the argument required=True. It will erturn the
#help message if the argu=mment is omitted.

videos = {}

class Video(Resource):
    def get(self, video_id):
        if video_id not in videos:
            abort(404, message="Could not find the video...")
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

api.add_resource(Video, "/video/<int:video_id>")
#############################################################

if __name__ == "__main__":
    app.run(debug=True) # Remove debug=true when deploying
