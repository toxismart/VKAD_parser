import vk
import json
import time
session = session = vk.AuthSession('vkapp', 'email', 'pass')
vk_api = vk.API(session)
id = input("User ID : ")
lvl = input("Depth level : ")
def write_json(data, id_name):
    with open('%d.json' % id_name, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
def main():
    profile = vk_api.friends.get(user_id=id, fields='city, domain', order='name')
    write_json(profile, int(id))
def depth_level(level=0, root_id=id):
    max_depth = int(lvl)
    friends_list = vk_api.friends.get(user_id=root_id, fields='city, domain', order='name')
    if level < max_depth:
        for bean in friends_list:
            try:
                r = vk_api.friends.get(user_id=bean['uid'], fields='city, domain', order='name')
                time.sleep(2)
                write_json(r, bean['uid'])
                level+=1
                bean_friend = depth_level(level, bean['uid'])
            except:
                bean['deactivated']
                continue
if __name__ == '__main__':
    main()
    depth_level(level=0)
