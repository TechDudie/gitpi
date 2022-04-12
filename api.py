import requests
import html
import json

class UserAPI:
  def __init__(self, user):
    self.user = user
    self.url = html.escape(f"https://api.github.com/users/{user}")
    request = requests.get(self.url)
    request.raise_for_status()
    self.resp = json.loads(request.text)
  def getRepo(self, repoName):
    return RepoAPI(self.user, repoName)

class RepoAPI:
  def __init__(self, user, repo):
    self.user = user
    self.repo = repo
    self.url = html.escape(f"https://api.github.com/repos/{user}/{repo}")
    request = requests.get(self.url)
    request.raise_for_status()
    self.resp = json.loads(request.text)
  def getUser(self):
    return UserAPI(self.user)
