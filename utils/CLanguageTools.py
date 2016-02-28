from pycparser import c_parser, c_ast

class CLanguageTools(object):
    # Initialize object with parser
    def __init__(self):
        self.parser = c_parser.CParser()

    """ Remove comments from source """
    def stripCommments(source):
        p = r'/\*[^*]*\*+([^/*][^*]*\*+)*/|("(\\.|[^"\\])*"|\'(\\.|[^\'\\])*\'|.[^/"\'\\]*)'
        return ''.join(m.group(2) for m in re.finditer(p, source, re.M|re.S) if m.group(2))

    """ Compare two source and return arrays of added and removed nodes """
    def compareSources(self, sourceX, sourceY):
        # Remove comments
        sourceX = stripCommments(sourceX)
        sourceY = stripCommments(sourceY)

        # Create syntactic tree for each source
        astX = self.parser.parse(sourceX, filename='<none>')
        astY = self.parser.parse(sourceY, filename='<none>')

        # Do the comparison
        return compare(astX, astY)   

    """ Check if nodes are the same """
    def checkNodes(nodeX, nodeY):
        # Get type of first node. 
        # There is no need for the other cause it would not be used
        typeOfX = type(nodeX)
    
        # Compare node type
        if not typeOfX == type(nodeY):
            return False

        # Check attributes based on type

        # Assignment operator
        if typeOfX == c_ast.Assignment:
            if not nodeX.op == nodeY.op:
                return False
        # Binary operator
        elif typeOfX == c_ast.BinaryOp:
            if not nodeX.op == nodeY.op:
                return False
        # Constant
        elif typeOfX == c_ast.Constant:
            if not nodeX.type == nodeY.type or not nodeX.value == nodeY.value:
                return False
        # Declaration
        elif typeOfX == c_ast.Decl:
            if not nodeX.name == nodeY.name:
                return False
        # Enum
        elif typeOfX == c_ast.Enum:
            if not nodeX.name == nodeY.name:
                return False
        # Enumerator
        elif typeOfX == c_ast.Enumerator:
            if not nodeX.name == nodeY.name:
                return False
        # Go to
        elif typeOfX == c_ast.Goto:
            if not nodeX.name == nodeY.name:
                return False
        # ID
        elif typeOfX == c_ast.ID:
            if not nodeX.name == nodeY.name:
                return False
        # Identifier type
        elif typeOfX == c_ast.IdentifierType:
            if not nodeX.names == nodeY.names:
                return False
        # Label
        elif typeOfX == c_ast.Label:
            if not nodeX.name == nodeY.name:
                return False
        # Named initializer
        elif typeOfX == c_ast.NamedInitializer:
            if not nodeX.name == nodeY.name:
                return False
        # Pointer declaration
        elif typeOfX == c_ast.PtrDecl:
            if not nodeX.quals == nodeY.quals:
                return False
        # Structure
        elif typeOfX == c_ast.Struct:
            if not nodeX.name == nodeY.name:
                return False
        # Structure reference
        elif typeOfX == c_ast.StructRef:
            if not nodeX.type == nodeY.type:
                return False 
        # Type declaration
        elif typeOfX == c_ast.TypeDecl:
            if not nodeX.declname == nodeY.declname:
                return False
        # Typedef
        elif typeOfX == c_ast.Typedef:
            if not nodeX.name == nodeY.name:
                return False
        # Typename
        elif typeOfX == c_ast.Typename:
            if not nodeX.name == nodeY.name:
                return False
        # Unary operator
        elif typeOfX == c_ast.UnaryOp:
            if not nodeX.op == nodeY.op:
                return False
        # Union
        elif typeOfX == c_ast.Union:
            if not nodeX.name == nodeY.name:
                return False

        # Check was successful
        return True

    """ Check if two nodes are equal """
    def areEqual(astX, astY):
        # Compare roots
        if not checkNodes(astX, astY):
            return (False, 0)

        # Nodes are equal
        equal = True
        score = 1

        # Check number of children
        if not len(astX.children()) == len(astY.children()):
            return (False, score)

        # Check each node
        index = 0
        for (_, child) in astX.children():
            # Compare nodes
            (isEqual, subScore) = areEqual(child, astY.children()[index][1])
        
            # Assign result
            equal = isEqual and equal
            score = subScore + score

            index = index + 1

        return (equal, score)

    """ Get children of given node """
    def getChildren(node):
        children = list()

        for (_, child) in node.children():
            children.append(child)

        return children

    """ Merge nodes """
    def mergeNodes(node, children):
        maximum_score = 0
        child_to_merge = {}
        for child in children:
            (equal, score) = areEqual(node, child)

            # Found exact match
            if equal:
                children.remove(child)
                return (True, children, None, None)

            # Found partial match
            if score > maximum_score:
                maximum_score = score
                child_to_merge = child

        # Check maximum score
        if maximum_score > 0:
            # Partial merge
            children.remove(child_to_merge)
            return (True, children, node, child_to_merge)
        else:
            # Unable to merge
            return (False, children, None, None)

    """ Compare two nodes """
    def compare(astX, astY):
        # Compare node type
        if not type(astX) == type(astY):
            return ([], [])

        added = list()
        removed = list()

        # Get children of both nodes
        childrenOfX = getChildren(astX)
        childrenOfY = getChildren(astY)

        # Merge each node
        for child in childrenOfX:
            (merged, children, xNode, yNode) = mergeNodes(child, childrenOfY)
            childrenOfY = children

            # If could not find match, add node to removed ones
            if not merged:
                removed.append(child)

            # If the match is only partial, go deeper
            if xNode is not None:
                (yAdded, xRemoved) = compare(xNode, yNode)
                added = added + yAdded
                removed = removed + xRemoved
       
        # Children that are not merged are new
        added = added + childrenOfY

        return (added, removed)