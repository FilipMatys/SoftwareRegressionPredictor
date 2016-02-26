from plugins.dejagnu.stat.ChangeToken import ChangeToken
from models.CommitDiff import CommitDiff
from models.FileDiff import FileDiff
from models.stat.DiffState import DiffState
import whatthepatch

class Parser(object):
    def __init__(self, repo, hash):
        self.repo = repo
        self.hash = hash

    def run(self):
        # Initialize changes
        changes = CommitDiff()

        # Parse each file
        for diff in whatthepatch.parse_patch(self.repo.get_commit_diff(self.hash)):
            # Check file extenstion for .c or .h
            filename = diff[0][3]
            if not self.checkFileExtension(filename):
                continue

            # Create new file diff
            file = self.parseFile(diff)

            # Add file changes to overall diff
            changes.addFile(file.getVars())

        return changes

    """ Check file extension """
    def checkFileExtension(self, filename):
        lastTwoCharacters = filename[-2:]
        return (lastTwoCharacters == ".c" or lastTwoCharacters == ".h")

    """ Parse file """
    def parseFile(self, fileDiff):
        file = FileDiff(fileDiff[0][3])

        newFileContent = self.repo.get_file_content(self.hash, file.name)

        # Get content of previous file
        try:
            prevFileContent = self.repo.get_file_content(self.hash + "^", file.name)
        except:
            prevFileContent = ""
            print("Previous file did not exist")

        return file   
       