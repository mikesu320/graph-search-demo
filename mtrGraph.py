MINVAL, MAXVAL = 0, 255
graphSearchs = ["dfs", "bfs","dfsPriHigh", "dfsPriLow", "greedy", "a*search"]
numMap = {'empty': MINVAL, 'wall': MAXVAL, 'endpoint' : MAXVAL -1, 'startpoint':MINVAL+1 , 'path':MAXVAL+1}




class MtrGraph :
    def __init__(self, dims, src=None, dest=None) :
        self.dims = dims
        self.stack = []
        self.closedSet = set()
        self.colorcode = MINVAL+1
        self.incr = 1
        self.mtr = [[0 for x in range(dims[1])] for y in range(dims[0])]
        self.start = src
        self.fringe = []
        self.dest = dest
        self.block = []
        for n in range(1, dims[1] - 1, 4) :
            [self.block.append((x, n)) for x in range(dims[0]//3, dims[0] - dims[0]//3)]

        for x in self.block:
            self.mtr[x[0]][x[1]] = numMap.get('wall')
        if dest is not None:
            self.setDest(dest)
        if src is not None:
            self.setStart(src)
        self.max = self.min = self.colorcode

    def isWall(self,node):
        return self.block.count(node)

    def setStart(self,node):
        self.start = node
        self.mtr[self.start[0]][self.start[1]] = numMap.get('startpoint')
        self.fringe = [(self.start, 0, 0)]

    def setDest(self,node):
        self.dest = node
        self.mtr[self.dest[0]][self.dest[1]] = numMap.get('endpoint')

    def markNode(self, node) :
        self.mtr[node[0]][node[1]] = self.colorcode
        self.colorcode += self.incr
        self.max = max(self.colorcode, self.max)



    def insertIntoFringe(self, next, sType) :
        if sType == "dfs" :
            [self.fringe.insert(0, (nd, next[1] + 1, 0)) for nd in self.findChildren(next[0]) if
             not nd in self.closedSet]
            self.fringe = sorted(self.fringe, key=lambda x : (-x[1], x[0]))
        elif sType == "bfs" :
            [self.fringe.insert(0, (nd, next[1] + 1, 0)) for nd in self.findChildren(next[0]) if
             not nd in self.closedSet]
            self.fringe = sorted(self.fringe, key=lambda x : (x[1], x[0]))
        elif sType == "dfsPriHigh" :
            [self.fringe.insert(0, (nd, next[1] + 1, 0)) for nd in self.findChildren(next[0]) if
             not nd in self.closedSet]
            self.fringe = sorted(self.fringe, key=lambda x : -x[1])
        elif sType == "dfsPriLow" :
            [self.fringe.insert(0, (nd, next[1] + 1, 0)) for nd in self.findChildren(next[0]) if
             not nd in self.closedSet]
            self.fringe = sorted(self.fringe, key=lambda x : x[1])
        elif sType == "greedy" :
            [self.fringe.insert(0, (nd, 0, costFun(nd, self.dest))) for nd in self.findChildren(next[0]) if
             not nd in self.closedSet]
            self.fringe = sorted(self.fringe, key=lambda x : x[2])
        elif sType == "a*search" :
            [self.fringe.insert(0, (nd, next[1] + 1, costFun(nd, self.dest))) for nd in self.findChildren(next[0]) if
             not nd in self.closedSet]
            self.fringe = sorted(self.fringe, key=lambda x : (x[2] + x[1], x[2]))
        return

    def outOfBounds(self, node) :
        if node[0] < 0 or node[1] < 0 :
            return 1
        elif node[0] >= self.dims[0] or node[1] >= self.dims[1] :
            return 1
        elif self.block.count(node) :
            return 1
        else :
            return 0

    def findChildren(self, node) :
        north = (node[0] - 1, node[1])
        west = (node[0], node[1] - 1)
        south = (node[0] + 1, node[1])
        east = (node[0], node[1] + 1)

        order = [north, west, south, east]
        lst = [i for i in order if not self.outOfBounds(i)]
        return lst

#Cost Fun is manhattan path cost for the Matrix Type Graph
def costFun(x1, x2) :
    return abs(x1[0] - x2[0]) + abs(x1[1] - x2[1])


# Generic Graph Search Recursive Algorithm uses Algorithm Type to change
# fringe. Child nodes are added to the  priority list structure
# according to the search used.
# mtr = nxn matrix array
# sType = algorithm type , dfs,bfs,greedy,etc
def graphSearchRec(mtr, sType) :
    if not len(mtr.fringe) :
        return False
    next = mtr.fringe.pop(0)
    if next[0] == mtr.dest :
        mtr.stack.append(next[0])
        return True

    # add node to the Closed list
    if not next[0] in mtr.closedSet :
        mtr.closedSet.add(next[0])
        mtr.markNode(next[0])
        mtr.insertIntoFringe(next, sType)

    while len(mtr.fringe) :
        if graphSearchRec(mtr, sType) :
            mtr.stack.append(next[0])
            return True
    return False

    # Generic Graph Search Algorithm uses Algorithm Type to change
    # fringe. Child nodes are added to the  priority list structure
    # according to the search used.
    # mtr = nxn matrix array
    # sType = algorithm type , dfs,bfs,greedy,etc

def graphSearch(mtr, sType) :
    if not len(mtr.fringe):
        mtr.fringe.append((mtr.start,0,0))
    while len(mtr.fringe):
        next = mtr.fringe.pop(0)
        if next[0] == mtr.dest :
            mtr.stack.append(next[0])
            return True
        else:
        # add node to the Closed list
            if not next[0] in mtr.closedSet :
                mtr.closedSet.add(next[0])
                mtr.markNode(next[0])
                mtr.insertIntoFringe(next, sType)
    return False
