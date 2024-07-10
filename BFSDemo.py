from pyamaze import maze,agent,textLabel,COLOR
from collections import deque

def BFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    frontiera = deque()
    frontiera.append(start)
    bfsCale = {}
    explorat = [start]
    bCale=[]

    while len(frontiera)>0:
        currCell=frontiera.popleft()
        if currCell==m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explorat:
                    continue
                frontiera.append(childCell)
                explorat.append(childCell)
                bfsCale[childCell] = currCell
                bCale.append(childCell)
    # print(f'{bfsPath}')
    fwdCale={}
    cell=m._goal
    while cell!=(m.rows,m.cols):
        fwdCale[bfsCale[cell]]=cell
        cell=bfsCale[cell]
    return bCale,bfsCale,fwdCale

if __name__=='__main__':

    m=maze(12,10)
    m.CreateMaze(loopPercent=10,theme='dark')
    bCale,bfsCale,fwdCale=BFS(m)
    a=agent(m,footprints=True,color=COLOR.yellow,shape='square',filled=True)
    b=agent(m,footprints=True,color=COLOR.red,shape='square',filled=False)
    # c=agent(m,5,4,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(m.rows,m.cols))
    c=agent(m,1,1,footprints=True,color=COLOR.cyan,shape='square',filled=True,goal=(m.rows,m.cols))
    m.tracePath({a:bCale},delay=100)
    m.tracePath({c:bfsCale},delay=100)
    m.tracePath({b:fwdCale},delay=100)
    l=textLabel(m,'Lungimea celui mai scurt drum',len(bfsCale)+1)
    l=textLabel(m,'Lungimea cautarii BFS',len(bCale))
    m.run()