import requests

BASE = "http://127.0.0.1:5000/"

# data = [
#     {"likes": 78, "name": "Joe", "views": 10000},
#     {"likes": 1000, "name": "How to make REST API", "views": 8000},
#     {"likes": 10, "name": "Tim", "views": 1000}
# ]
#
# for i in range(len(data)):
#     response = requests.put(BASE + 'video/' + str(i), data[i])
#     print(response.json())

# response = requests.delete(BASE + 'video/1')
# print(response)

# input()
# response = requests.patch(BASE + 'video/2', {"views": 99, "likes": 101})
# print(response.json())

input()
response = requests.get(BASE + 'video/1')
print(response.json())
