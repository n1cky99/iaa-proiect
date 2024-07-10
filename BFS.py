from pyamaze import maze,agent,COLOR,textLabel
def BFS(m):
    start=(m.rows,m.cols)
    frontiera=[start]
    explorat=[start]
    bfsPath={}
    while len(frontiera)>0:
        currCell=frontiera.pop(0)
        if currCell==(1,1):
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
                if childCell in explorat:
                    continue
                frontiera.append(childCell)
                explorat.append(childCell)
                bfsPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return fwdPath

if __name__=='__main__':
    m=maze(5,7)
    m.CreateMaze(loopPercent=40)
    path=BFS(m)

    a=agent(m,footprints=True,filled=True)
    m.tracePath({a:path})
    l=textLabel(m,'Lungimea celui mai scurt drum',len(path)+1)
    
    m.run()