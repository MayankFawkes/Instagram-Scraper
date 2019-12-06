import requests
import re
import json
import os
from download import *

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
def Get_Data(usernamee):
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
	return pictures,dir
if __name__ == "__main__":
	# username="coderburn"
	username=str(input("Enter Username -->"))
	print("Collecting Images and Videos")
	da,path=Get_Data(username)
	print("Downloading Started")
	c=1
	for n in da:
		print("Process: [{}/{}] {}".format(c,len(da),n.split("?")[0].split("/")[-1]),end="\r")
		Download(urlinit=n,location=path)
		c+=1