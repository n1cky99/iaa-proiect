from pyamaze import maze,agent,COLOR,textLabel
from queue import PriorityQueue
def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return (abs(x1 - x2) + abs(y1 - y2))
    
def aStar(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    open = PriorityQueue()
    open.put((h(start, m._goal), h(start, m._goal), start))
    aCale = {}
    g_scor = {row: float("inf") for row in m.grid}
    g_scor[start] = 0
    f_scor = {row: float("inf") for row in m.grid}
    f_scor[start] = h(start, m._goal)
    searchCale=[start]
    while not open.empty():
        currCell = open.get()[2]
        searchCale.append(currCell)
        if currCell == m._goal:
            break        
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_scor = g_scor[currCell] + 1
                temp_f_scor = temp_g_scor + h(childCell, m._goal)

                if temp_f_scor < f_scor[childCell]:   
                    aCale[childCell] = currCell
                    g_scor[childCell] = temp_g_scor
                    f_scor[childCell] = temp_g_scor + h(childCell, m._goal)
                    open.put((f_scor[childCell], h(childCell, m._goal), childCell))


    fwdCale={}
    cell=m._goal
    while cell!=start:
        fwdCale[aCale[cell]]=cell
        cell=aCale[cell]
    return searchCale,aCale,fwdCale

if __name__=='__main__':
    m=maze(12,10)
    m.CreateMaze(loopPercent=10,theme='dark')

    searchCale,aCale,fwdCale=aStar(m)
    a=agent(m,footprints=True,color=COLOR.blue,filled=True)
    b=agent(m,1,1,footprints=True,color=COLOR.yellow,filled=True,goal=(m.rows,m.cols))
    c=agent(m,footprints=True,color=COLOR.red)

    m.tracePath({a:searchCale},delay=100)
    m.tracePath({b:aCale},delay=100)
    m.tracePath({c:fwdCale},delay=100)

    l=textLabel(m,'Lungimea caii A-Star',len(fwdCale)+1)
    l=textLabel(m,'Lungimea cautarii A-Star',len(searchCale))
    m.run()
