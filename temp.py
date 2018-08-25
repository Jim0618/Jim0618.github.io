from git import Repo
import os

git_path = os.path.abspath('./')
repo = Repo(git_path)

commit_words = 'a'

index = repo.index
index.add(['.gitignore'])
index.commit('commit .gitignore')
index.add('*')
index.commit(commit_words)
repo.remote().push()
# repo.delete_head()