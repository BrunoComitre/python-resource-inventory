import requests


req = requests.get('https://github.com/timeline.json')
print(req)

req = requests.post("http://httpbin.org/post")
print(req)

req = requests.put("http://httpbin.org/put")
print(req)

req = requests.delete("http://httpbin.org/delete")
print(req)

req = requests.head("http://httpbin.org/get")
print(req)

req = requests.options("http://httpbin.org/get")
print(req)

###

payload = {'key1'}