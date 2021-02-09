
import matplotlib.pyplot as plt
import random

from mtrGraph import MtrGraph, graphSearchRec, graphSearch


def searchAlgsRun() :
    size = (10, 12)
    # Use Random start and finish cells
    x1 = (random.randint(0, size[0] - 1), random.randint(0, size[1] - 1))
    x2 = (random.randint(0, size[0] - 1), random.randint(0, size[1] - 1))
    x2=(9,9)
    x1=(1,1)
    mtr0 = MtrGraph(size, x1, x2)
    mtr1 = MtrGraph(size, x1, x2)
    mtr2 = MtrGraph(size, x1, x2)
    mtr3 = MtrGraph(size, x1, x2)
    mtr4 = MtrGraph(size, x1, x2)
    mtr5 = MtrGraph(size, x1, x2)
    print(mtr0.start)
    print(mtr0.dest)
    graphSearch(mtr0, "dfs")
    graphSearch(mtr1, "dfsPriHigh")
    graphSearch(mtr2, "bfs")
    graphSearch(mtr3, "bfs")
    graphSearch(mtr4, "greedy")
    graphSearch(mtr5, "a*search")
    '''
    Use ColorMesh to demonstrate the search algorithms cost and invasiveness.
    Cost of each search algorithm is measured by the number of vertices visited.
    '''

    fig, axarr = plt.subplots(2, 3)
    axarr[0, 0].pcolormesh(mtr0.mtr, cmap='coolwarm', edgecolors='k', linewidths=1, vmin=mtr0.min, vmax=mtr0.max,
                           hatch='o')
    axarr[0, 0].set_title('DFS')
    axarr[0, 0].invert_yaxis()
    axarr[0, 1].pcolormesh(mtr1.mtr, cmap='coolwarm', edgecolors='k', linewidths=1, vmin=mtr1.min, vmax=mtr1.max)
    axarr[0, 1].set_title('DFS DEPTH')
    axarr[0, 1].invert_yaxis()
    axarr[0, 2].pcolormesh(mtr2.mtr, cmap='coolwarm', edgecolors='k', linewidths=1, vmin=mtr2.min, vmax=mtr2.max)
    axarr[0, 2].set_title('DFS DEPTH0')
    axarr[0, 2].invert_yaxis()
    axarr[1, 0].pcolormesh(mtr3.mtr, cmap='coolwarm', edgecolors='k', linewidths=1, vmin=mtr3.min, vmax=mtr3.max)
    axarr[1, 0].set_title('BFS')
    axarr[1, 0].invert_yaxis()
    axarr[1, 1].pcolormesh(mtr4.mtr, cmap='coolwarm', edgecolors='k', linewidths=1, vmin=mtr4.min, vmax=mtr4.max)
    axarr[1, 1].set_title('GREEDY')
    axarr[1, 1].invert_yaxis()
    axarr[1, 2].pcolormesh(mtr5.mtr, cmap='coolwarm', edgecolors='k', linewidths=1, vmin=mtr5.min, vmax=mtr5.max)
    axarr[1, 2].set_title('A* SEARCH')
    axarr[1, 2].invert_yaxis()
    print("DFS cost - path ", len(mtr0.closedSet), mtr0.max)
    print("DFS1 cost - path ", len(mtr1.closedSet), mtr1.max)
    print("DFS0 cost - path ", len(mtr2.closedSet), mtr2.max)
    print("BFS cost - path ", len(mtr3.closedSet), mtr3.max)
    print("GREEDY cost - path ", len(mtr4.closedSet), mtr4.max)
    print("A* cost - path ", len(mtr5.closedSet), mtr5.max)
    print(mtr0.start)
    print(mtr0.dest)
    print(mtr0.stack)
    fig.set_size_inches(9, 6.5)
    plt.tight_layout()
    plt.show()


searchAlgsRun()
