import git

class GitWrap:
    def __init__(self, url):
        self.url = url

    """ Initialize repository object """
    def init(self, path):
        self.repo = Repo(path)

    """ Clone new repository and init repository object """
    def clone(self, path):
        # Try to clone repo
        self.repo = git.Repo.clone_from(self.url, os.path.join(rw_dir, path), bare=True)

    def checkout(self):
        self.repo.heads.past_branch.checkout()

    def commit_diff(self, commit):
        g = git.cmd.Git(self.repo.working_dir)
        return g.execute("git show %s" % commit)