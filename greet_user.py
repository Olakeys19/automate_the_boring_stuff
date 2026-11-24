import json

filename = 'username.json'
with open(filename) as u_obj:
    username = json.load(u_obj)
    print('Welcome back, ' + username + '!')
