import json

jsonString = '''
{
  "name": "John Doe",
  "age": 30,
  "occupation": "Software Engineer",
  "address": {
    "street": "123 Main Street",
    "city": "Anytown",
    "state": "CA",
    "zip": "98765"
  },
  "interests": ["programming", "reading", "traveling"]
}
'''
data = json.loads(jsonString)
print(data['interests'][1])

