from git import Repo
import os

git_path = os.path.abspath('./')
repo = Repo(git_path)

index = repo.index

commit_words = ''
index.add('*') # git add --all
index.commit(commit_words)

repo.remote().push()
