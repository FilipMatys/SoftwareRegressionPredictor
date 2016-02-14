import git
import os

class GitWrap:
    def __init__(self, url, path):
        self.url = url
        self.repo_name = self.url.split('/')[-1]
        self.path = os.path.join(path, self.repo_name)

    """ Initialize repository object """
    def init(self, repository):
        self.repo = Repo(repository)

    """ Clone new repository and init repository object """
    def clone(self):
        # Try to clone repo
        self.repo = git.Repo.clone_from(self.url, self.path, bare=True)

    def checkout(self):
        self.repo.heads.past_branch.checkout()

    def commit_diff(self, commit):
        g = git.cmd.Git(self.repo.working_dir)
        return g.execute("git show %s" % commit)

    def log(self):
        return self.repo.git.log()