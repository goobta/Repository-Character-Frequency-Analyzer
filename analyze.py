# https://gitlab.com/agupta628
# This script will find determine the char frequency in your projects

from multiprocessing.dummy import Pool as ThreadPool
from subprocess import call
import operator
import requests
import glob

thread_count = 8
username = "agupta628"
api_url_gitlab = "https://gitlab.com/api/v4/users/" + username + "/projects"

char_freq_dict = {}

excluded_files = [".git",
                  ".log",
                  ".pyc"]

def get_char_count(url):
    call(["git", "clone", url])
    dir_name = url.split("/")[-1][:-4]
    
    for f in glob.iglob(dir_name + "/**/*.*", recursive=True):
        cont = True
        for e in excluded_files:
            if e in f:
                cont = False

        if not cont:
            continue

        buff = open(f,"rb").read()
        
        for char in buff:
            if char == " ":
                char = "space"
            elif char == "\n":
                char = "enter"
            elif char == "\t":
                char = "tab"

            try:
                char_freq_dict[char] += 1
            except:
                char_freq_dict[char] = 1

    call(["rm", "-rf", dir_name])

res = requests.get(api_url_gitlab).json()
repos = [r['http_url_to_repo'] for r in res]

pool = ThreadPool(thread_count)
pool.map(get_char_count, repos)

for key, value in sorted(char_freq_dict.items(), key=operator.itemgetter(1), reverse=True):
    if key == 11:
        s = "tab"
    elif key == 32:
        s = "space"
    elif key < 32 or key > 126:
        continue
    else:
        s = chr(key)

    print("Character {} had {} hits".format(s, value))
