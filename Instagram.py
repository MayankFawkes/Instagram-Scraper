import requests
import re
import json
import os
from download import *
import time
import sys
import random
import ctypes
import platform

if platform.system() == 'Windows':
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
print_mode = False
COMMANDS = {
    # Lables
    'info': (33, '[!] '),
    'que': (34, '[?] '),
    'bad': (31, '[-] '),
    'good': (32, '[+] '),
    'run': (97, '[~] '),

    # Colors
    'green': 32,
    'lgreen': 92,
    'lightgreen': 92,
    'grey': 37,
    'black': 30,
    'red': 31,
    'lred': 91,
    'lightred': 91,
    'cyan': 36,
    'lcyan': 96,
    'lightcyan': 96,
    'blue': 34,
    'lblue': 94,
    'lightblue': 94,
    'purple': 35,
    'yellow': 93,
    'white': 97,
    'lpurple': 95,
    'lightpurple': 95,
    'orange': 33,

    # Styles
    'bg': ';7',
    'bold': ';1',
    'italic': '3',
    'under': '4',
    'strike': '09',
}
def _gen(string, prefix, key):
    colored = prefix if prefix else string
    not_colored = string if prefix else ''
    result = '\033[{}m{}\033[0m{}'.format(key, colored, not_colored)
    if print_mode:
        print(result)
    else:
        return result
for key, val in COMMANDS.items():
    value = val[0] if isinstance(val, tuple) else val
    prefix = val[1] if isinstance(val, tuple) else ''
    locals()[key] = lambda s, prefix=prefix, key=value: _gen(s, prefix, key)
co=[green,lgreen,lightgreen,grey,red,lred,lightred,cyan,lcyan,lightcyan,blue,lblue,lightblue,purple,yellow,white,lpurple,lightpurple,orange]
def print_logo():
    x = b"\n\n\n        \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n        \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n        \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n        \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n        \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n        \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d   \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d   \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\n                        Mayank Gupta  @ gitHub.com/MayankFawkes\n            Note! : We don't Accept any responsibility for any illegal usage.      \n"
    for n in x.decode().split("\n"):
        print(random.choice(co)(n))
        time.sleep(0.1)
class InvalidUsernameException(Exception):
    def __init__(self, msg=None):
        if msg:
            print(msg)
        else:
            print("Instagram username provided in not valid")
def create_user_dir(username):
    foldername = "instagram_downloads/instagram_" + username
    if not os.path.exists(foldername):
        os.makedirs(foldername)
    return foldername
def get_response_from_hash(username):
    response = requests.get("https://www.instagram.com/explore/tags/" + username + "/")
    if response.status_code == 404:
        raise InvalidUsernameException()
    return response
def get_response(username):
    response = requests.get("https://www.instagram.com/" + username + "/")
    if response.status_code == 404:
        raise InvalidUsernameException()
    return response
def instavideo(code=""):
	url="https://www.instagram.com/p/{}/".format(code)
	text=requests.get(url).text
	url=re.findall(' <meta property="og:video" content="(.*?)" />',text)
	# print(url[0])
	return url[0]
def get_user_data_json(script_tags):
	data=re.findall('<script type="text/javascript">window._sharedData = {.*?};</script>',script_tags)
	return json.loads(data[0][52:-10])
def Get_Data(usernamee,limit):
	dir=create_user_dir(usernamee)
	pictures=[]
	html=get_response(usernamee).text
	json_obj=get_user_data_json(html)
	user_id = json_obj["entry_data"]["ProfilePage"][0]["graphql"]["user"]["id"]
	is_next = json_obj["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["page_info"]["has_next_page"]
	end_cursor = json_obj["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["page_info"]["end_cursor"]
	for n in json_obj["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]:
		if n['node']['is_video']:
			pictures.append(instavideo(n["node"]["shortcode"]))
		else:
			pictures.append(n["node"]["thumbnail_resources"][4]["src"])
	while is_next:
		if len(pictures) > limit:
			break
		url='https://www.instagram.com/graphql/query/?query_id=17888483320059182&variables={"id":"' + user_id + '","first":12,"after":"' + end_cursor + '"}'
		ss=json.loads(requests.get(url).text)
		for n in ss["data"]["user"]["edge_owner_to_timeline_media"]["edges"]:
			if n['node']['is_video']:
				pictures.append(instavideo(n["node"]["shortcode"]))
			else:
				pictures.append(n["node"]["thumbnail_resources"][4]["src"])
		page_info=ss["data"]["user"]["edge_owner_to_timeline_media"]["page_info"]
		is_next = page_info["has_next_page"]
		if is_next:
			end_cursor = page_info["end_cursor"]
	return pictures[:limit],dir
def Get_Data_from_Hash(usernamee,limit):
	dir=create_user_dir(usernamee)
	pictures=[]
	html=get_response_from_hash(usernamee).text
	json_obj=get_user_data_json(html)
	# print(json_obj)
	user_id = json_obj['entry_data']['TagPage'][0]['graphql']['hashtag']['name']
	is_next = json_obj['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['has_next_page']
	end_cursor = json_obj['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
	for n in json_obj['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_top_posts']['edges']:
		if n['node']['is_video']:
			pictures.append(instavideo(n["node"]["shortcode"]))
		else:
			pictures.append(n["node"]["thumbnail_resources"][4]["src"])
	for n in json_obj['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges']:
		if n['node']['is_video']:
			pictures.append(instavideo(n["node"]["shortcode"]))
		else:
			pictures.append(n["node"]["thumbnail_resources"][4]["src"])
	while is_next:
		if len(pictures) > limit:
			break
		url='https://www.instagram.com/graphql/query/?query_hash=bd33792e9f52a56ae8fa0985521d141d&variables={"tag_name":"'+user_id+'","first":12,"after":"'+end_cursor+'"}'
		ss=json.loads(requests.get(url).text)
		for n in ss["data"]["hashtag"]["edge_hashtag_to_media"]["edges"]:
			if n['node']['is_video']:
				pictures.append(instavideo(n["node"]["shortcode"]))
			else:
				pictures.append(n["node"]["thumbnail_resources"][4]["src"])
		page_info=ss["data"]["hashtag"]["edge_hashtag_to_media"]['page_info']
		is_next = page_info["has_next_page"]
		if is_next:
			end_cursor = page_info["end_cursor"]
	return pictures[:limit],dir
if __name__ == "__main__":
	print_logo()
	username=str(input("Enter Username -->"))
	howmany=int(input("How Many Images or Videos -->"))
	fun={"tag":Get_Data_from_Hash,'user':Get_Data}
	if '#' in username:
		print("Collecting Images and Videos From Hashtag")
		username=username.split("#")[1]
		da,path=Get_Data(username,howmany)
	else:
		print("Collecting Images and Videos From Username")
		da,path=Get_Data(username,howmany)

	print("Downloading Started")
	c=1
	for n in da:
		print("Process: [{}/{}] {}".format(c,len(da),n.split("?")[0].split("/")[-1]),end="\r")
		Download(urlinit=n,location=path)
		c+=1
	print("Downloading Completed {}".format(len(da)))
	input("Press Enter To Exit")
