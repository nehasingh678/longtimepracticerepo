import json
def read_data():

    with open("/Users/neha/PycharmProjects/nehalearningvenev/playwright/newfile.json",'r') as f:

        data=f.read()
        jsondata=json.loads(data)
    return jsondata


chk=read_data()
val=chk['name']
print(val)














