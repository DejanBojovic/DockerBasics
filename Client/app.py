import http.client
import json

conn = http.client.HTTPConnection("localhost:5000")
payload = json.dumps({'ime': 'Milutin', 'prezime': 'Milankovic', 'username': 'Mimi', 'smer': 'IT', 'predmeti': [{'ime': 'JS', 'espb': 8}, {'ime': 'Python', 'espb': 8}]})
headers = {
  'Content-Type': 'application/json'
}

conn.request("POST", "/users", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))