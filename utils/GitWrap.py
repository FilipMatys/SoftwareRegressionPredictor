import git
import os
import time
import chardet
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

    def get_commit_diff(self, previous_revision, revision):
        return self.repo.git.diff(previous_revision, revision)

    """ Clone new repository and init repository object """
    def clone(self):
        # Try to clone repo
        self.repo = git.Repo.clone_from(self.url, self.path, bare=True)

    def checkout(self):
        self.repo.heads.past_branch.checkout()

    def get_file_content(self, commit, file):
        content = self.repo.git.execute(['git', 'show', '%s:%s' % (commit, file)], stdout_as_string=False)

        result = chardet.detect(content)
        return content.decode(encoding=result['encoding'])

    def get_file_path(self, commit, filename):
        files = self.repo.git.execute(['git', 'ls-tree', '-r', '--name-only', '%s' % (commit)])
        for line in files.split('\n'):
            if filename in line:
                return line

    def log(self, number):
        return list(self.repo.iter_commits(self.repo.active_branch, max_count=number))

class CommitWrap(object):
    diff = list()

    def __init__(self, commit):
        self.message = commit.message
        self.author = commit.author.name
        self.hash = commit.hexsha
        self.test = False
        self.commited_time = time.asctime(time.gmtime(commit.committed_date))

    def getVars(self):
        return vars(self)
