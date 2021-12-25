import requests

BASE = "http://127.0.0.1:5001/"

print("Send a get request to helloworld by pressing any key.")
input()
response = requests.get(BASE + "helloworld")
print(response.json())

print("Send the post request to helloworld by pressing any key.")
input()
response = requests.post(BASE + "helloworld")
print(response.json())

print("Send a get request to paramexemple with tim as a parameter by pressing any key.")
input()
response = requests.get(BASE + "/paramexemple/tim")
print(response.json())

print("Send a put request to video by pressing any key.")
input()
response = requests.put(BASE + "video/1", {"likes":10})
print(response.json())

print("Send a get request to video by pressing any key.")
input()
response = requests.get(BASE + "video/1")
print(response.json())
