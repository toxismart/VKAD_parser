import vk
import json
import time
import sys
session = session = vk.AuthSession('6037750', 'leninanton@gmail.com', 'Jmpwl4pl5123')
api = vk.API(session, v='3.0', lang='ru', timeout=10)
id1 = input("ID to parse: ")
values = int(id1)
profile = api.users.get(user_ids=values, fields=('uid','deactivated'))
friends = api.friends.get(user_id=values, fields=('user_id', 'city','domain'))
lvl = input('Depth: ')
max_depth = int(lvl)

def profile_json(data, id_name):
    with open('%d.json' % id_name, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

temp = []

def parse(level, values, friends):
    try:
        if level<max_depth:
            friends = api.friends.get(user_id=values, fields=('user_id', 'city','domain'))
            time.sleep(5)
            for value in friends:
                values = value['uid']
                temp.append(values)
                profile_json(value, value['uid'])
                temp.pop()
                parse(level+1, values, friends)
                continue
    except:
        value['deactivated']




def main():
    parse(0, values, friends)

if __name__ == '__main__':
    main()
