import requests
import html
import json

class RepoAPI:
  def __init__(self, user, repo):
    self.user = user
    self.repo = repo
    self.url = html.escape(f"https://api.github.com/repos/{user}/{repo}")
    self.data = requests.get(self.url).text
  def getUser(self):
    return UserAPI(self.user)

class UserAPI:
  def __init__(self, user):
    self.user = user
    self.url = html.escape(f"https://api.github.com/users/{user}")
    self.data = requests.get(self.url).text
  def getRepo(self, repoName):
    return RepoAPI(self.user, repoName)
