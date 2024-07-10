from BFSDemo import BFS
from aStarDemo import aStar
from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit

myMaze=maze(12,10)
myMaze.CreateMaze(loopPercent=100)
# myMaze.CreateMaze()
searchCale,aCale,fwdCale=aStar(myMaze)
bSearch,bfsCale,fwdBFSCale=BFS(myMaze)

l=textLabel(myMaze,'Lungimea caii A-Star',len(fwdCale)+1)
l=textLabel(myMaze,'Lungimea caii BFS',len(fwdBFSCale)+1)
l=textLabel(myMaze,'Lungimea cautarii A-Star',len(searchCale)+1)
l=textLabel(myMaze,'Lungimea cautarii BFS',len(bSearch)+1)

a=agent(myMaze,footprints=True,color=COLOR.cyan,filled=True)
b=agent(myMaze,footprints=True,color=COLOR.yellow)
myMaze.tracePath({a:fwdBFSCale},delay=50)
myMaze.tracePath({b:fwdCale},delay=50)

t1=timeit(stmt='aStar(myMaze)',number=10,globals=globals())
t2=timeit(stmt='BFS(myMaze)',number=10,globals=globals())

textLabel(myMaze,'A-Star Time',t1)
textLabel(myMaze,'BFS Time',t2)


myMaze.run()