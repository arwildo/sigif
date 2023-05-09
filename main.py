import json


# followers
f = open('./data/followers.json')

data = json.load(f)

follower = []

for i in data:
    for j in i["string_list_data"]:
        follower.append(j["value"])
        

# following
f = open('./data/following.json')

data = json.load(f)

following = []

for i in data["relationships_following"]:
    for j in i["string_list_data"]:
        following.append(j["value"])

# main
goodpeople = []

for i in following:
    if i in follower:
        goodpeople.append(i)

for i in following:
    if i not in goodpeople:
        print("https://www.instagram.com/" + i)
