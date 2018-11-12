class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0
    def show(self, level=0):
        print("%s%s val=%d:" % (level*"  ", self.name, self.val))
        for c in self.children: 
            c.show(level + 1)

def increment(graph):#call this method in the server
    graph.val += 1;
    for c in graph.children:
        increment(c)
        
def TreeToListDict(graph, list=[]): #tree to list of dictionaries #each dictionary is an object
    #creates dictionary of current node
    list.append({"name":  graph.name, "children": [str(child.name)for child in graph.children], "value": graph.val})
    for c in graph.children: #creates 
        list = TreeToListDict(c,list)
    return list

def ListDictToTree(curr = "root",listDict=[]):#converts List of dictionaries into a tree recursively
    start = findNodeDict(curr, listDict)#dictionary for current node
    if start == None:
        return None
    children = []
    for element in start["children"]: #creates the list of children recursively
        repetition = False
        for child in children:  #checks for repition of an object
            if element in child.name:
                children.append(child)
                print("repetition")
                repetition = True
                break
        if not repetition:      #if not a repetition adds it to a list
            children.append(ListDictToTree(element,listDict))
    currentNode = node(curr,children)
    currentNode.val = start["value"]
    return currentNode


    x
def findNodeDict(search = "blerh", listDict = []): #finds node's dictionary in list of dictionaries
    for element in listDict:
        if search in element["name"]:
            return element
    return None
    