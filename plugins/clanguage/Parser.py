from models.CommitDiff import CommitDiff
from models.FileDiff import FileDiff
from models.stat.DiffState import DiffState
from plugins.clanguage.CodeAnalyzer import CodeAnalyzer
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
            file = self.parseFileChanges(diff)

            # Add file changes to overall diff
            changes.addFile(file)

        return changes

    """ Check file extension """
    def checkFileExtension(self, filename):
        lastTwoCharacters = filename[-2:]
        return (lastTwoCharacters == ".c" or lastTwoCharacters == ".h")

    """ Parse file """
    def parseFileChanges(self, fileDiff):
        # Analyze changes
        codeAnalyzer = CodeAnalyzer(fileDiff)
        return codeAnalyzer.analyze()
       