import vk
import json
import sys
import codecs
session = session = vk.AuthSession('vkapp_id', 'mail', 'pass')
vk_api = vk.API(session)
id = input("User ID : ")

def write_json(data):
    with open('friends_ids1.json', 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def write_json1(data, id_name):
    with open('%d.json' % id_name, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def main():
    r = vk_api.friends.get(user_id=id, fields='city, domain', order='name')
    write_json(r)

def get_friends_ids():
    with codecs.open('friends_ids1.json', 'r', 'utf-8') as json_data:            //# To make this recursive, just change friends_ids1.json to '%d.json' % id_name
        d = json.load(json_data)
        for q in d:
            get_friends_friends(q['uid'])

def get_friends_friends(uids):
    r1 = vk_api.friends.get(user_id=uids, fields='city, domain', order='name')
    write_json1(r1, uids)

__name__ == '__main__'
main()
get_friends_ids()
