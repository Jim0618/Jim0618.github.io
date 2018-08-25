from git import Repo
import os

git_path = os.path.abspath('./')
repo = Repo(git_path)

commit_words = ''

index = repo.index
index.add('*')
index.commit(commit_words)
repo.remote().push()