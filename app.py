import requests

repo = "torvalds/linux"

r = requests.get("https://api.github.com/repos/{0}/commits?per_page=1".format(repo))

commit = r.json()[0]["commit"]

print(commit)
