import git
import os
import time
from enum import Enum

class GitWrap:
    def __init__(self, url, path):
        self.url = url
        self.repo_name = self.url.split('/')[-1]
        self.path = os.path.join(path, self.repo_name)

    """ Initialize repository object """
    def init(self):
        try:
            self.repo = git.Repo(self.path)
        except git.exc.InvalidGitRepositoryError:
            return False

        return True

    def get_commit(self, hash):
        return self.repo.commit(hash)

    def get_commit_diff(self, hash):
        return self.repo.git.diff(hash + '^', hash)

    """ Clone new repository and init repository object """
    def clone(self):
        # Try to clone repo
        self.repo = git.Repo.clone_from(self.url, self.path, bare=True)

    def checkout(self):
        self.repo.heads.past_branch.checkout()

    def log(self, number):
        return list(self.repo.iter_commits(self.repo.active_branch, max_count=number))

class CommitWrap(object):
    diff = list()

    def __init__(self, commit):
        self.message = commit.message
        self.author = commit.author.name
        self.hash = commit.hexsha
        self.commited_time = time.asctime(time.gmtime(commit.committed_date))

    def getVars(self):
        return vars(self)

class DiffState(Enum):
    REMOVED = 0
    INSERTED = 1

class DiffWrap(object):
    def __init__(self, diff):
        self.old_path = diff[0][1]
        self.new_path = diff[0][3]
        self.changes = list()

        changes = diff[1]
        # Iterate through changes
        for change in changes:
            if change[0] is None:
                self.changes.append({ "state": DiffState.REMOVED.value, "text": change[2]})
            elif change[1] is None:
                self.changes.append({ "state": DiffState.INSERTED.value, "text": change[2]})

    def getVars(self):
        return vars(self)

