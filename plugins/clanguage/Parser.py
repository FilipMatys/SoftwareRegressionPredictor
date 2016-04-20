from models.CommitDiff import CommitDiff
from models.FileDiff import FileDiff
from models.stat.DiffState import DiffState
from plugins.clanguage.CodeAnalyzer import CodeAnalyzer
import whatthepatch

class Parser(object):
    """ Run parser """
    def run(patch):
        # Initialize changes
        changes = CommitDiff()
        
        # Parse each file
        for diff in whatthepatch.parse_patch(patch):
            # Check file extenstion for .c or .h
            filename = diff[0][3]
            if not Parser.checkFileExtension(filename):
                continue

            # Create new file diff
            file = Parser.parseFileChanges(diff)

            # Add file changes to overall diff
            changes.addFile(file)

        return changes

    """ Check file extension """
    def checkFileExtension(filename):
        lastTwoCharacters = filename[-2:]
        return (lastTwoCharacters == ".c" or lastTwoCharacters == ".h")

    """ Parse file """
    def parseFileChanges(fileDiff):
        # Analyze changes
        codeAnalyzer = CodeAnalyzer(fileDiff)
        return codeAnalyzer.analyze()
       