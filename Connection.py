import requests

# And done.
i = 0
while i<10:
    r = requests.post("http://192.168.43.133/", data={'foo': 'i'})
    print(r.text) # displays the result body.
    i=i+1
