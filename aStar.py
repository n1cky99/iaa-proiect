from pyamaze import maze,agent,textLabel
from queue import PriorityQueue
def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2

    return abs(x1-x2) + abs(y1-y2)
def aStar(m):
    start=(m.rows,m.cols)
    g_scor={cell:float('inf') for cell in m.grid}
    g_scor[start]=0
    f_scor={cell:float('inf') for cell in m.grid}
    f_scor[start]=h(start,(1,1))

    open=PriorityQueue()
    open.put((h(start,(1,1)),h(start,(1,1)),start))
    aCale={}
    while not open.empty():
        currCell=open.get()[2]
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_scor=g_scor[currCell]+1
                temp_f_scor=temp_g_scor+h(childCell,(1,1))

                if temp_f_scor < f_scor[childCell]:
                    g_scor[childCell]= temp_g_scor
                    f_scor[childCell]= temp_f_scor
                    open.put((temp_f_scor,h(childCell,(1,1)),childCell))
                    aCale[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[aCale[cell]]=cell
        cell=aCale[cell]
    return fwdPath

if __name__=='__main__':
    m=maze(5,5)
    m.CreateMaze()
    path=aStar(m)

    a=agent(m,footprints=True)
    m.tracePath({a:path})
    l=textLabel(m,'Lungimea caii A Star',len(path)+1)

    m.run()