# https://gitlab.com/agupta628
# This script will find determine the char frequency in your projects

from subprocess import call
import requests
import glob

thread_count = 8
username = "agupta628"
api_url_gitlab = "https://gitlab.com/api/v4/users/" + username + "/projects"

char_freq_dict = {}

def get_char_count(url):
    # call(["git", "clone", url])
    
    dir_name = url.split("/")[-1][:-4]
    print(dir_name)



repos = requests.get(api_url_gitlab)

for repo in repos.json():
    get_char_count(repo['http_url_to_repo'])

