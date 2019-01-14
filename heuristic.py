import random
import greedy


class game:
    def __init__(self, n):
        self.n=n
        self.grid=[[0 for j in range(n)] for i in range(n)]
        self.score=0
        self.weight1=[[7,6,5,4],[6,5,4,3],[5,4,3,2],[4,3,2,1]]
        self.weight2=[[4096,1024,256,64],[1024,256,64,16],[256,64,16,4],[64,16,4,1]]
        self.weight3=[[1073741820,268435456,67108864,16777216],[65536,262144,1048576,4194304],[16384,4096,1024,256],[1,4,16,64]]
        
    def printgrid(self):
        for i in range(self.n):
            print(self.grid[i])
    
    def eval1(self,grid):
        score=0
        for i in range(self.n):
            for j in range(self.n):
                score+=self.weight1[i][j]*grid[i][j]
        return score
    
    def move_right(self):
        s=0
        grid_=[[0 for j in range(self.n)] for i in range(self.n)]
        grid=[[0 for j in range(self.n)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                grid_[i][j]=self.grid[i][j]
                grid[i][j]=self.grid[i][j]
        for i in range(self.n):
            num=[]
            for j in range(self.n):
                if grid[i][j]!=0:
                    num.append(grid[i][j])
            for j in range(len(num)):
                if j+1<len(num) and num[j]==num[j+1]:
                    num[j]=num[j]*2
                    s+=num[j]
                    del num[j+1]
            num.reverse()
            while len(num)<self.n:
                num.append(0)
            for j in range(len(num)):
                grid[i][self.n-j-1]=num[j]
        p=False
        for i in range(self.n):
            for j in range(self.n):
                if grid_[i][j]!=grid[i][j]:
                    p=True
                    break
            if p==True:
                break
        return p,s,grid


    def move_left(self):
        s=0
        grid_=[[0 for j in range(self.n)] for i in range(self.n)]
        grid=[[0 for j in range(self.n)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                grid_[i][j]=self.grid[i][j]
                grid[i][j]=self.grid[i][j]
        for i in range(self.n):
            num=[]
            for j in range(self.n):
                if grid[i][self.n-j-1]!=0:
                    num.append(grid[i][self.n-j-1])
            for j in range(len(num)):
                if j+1<len(num) and num[j]==num[j+1]:
                    num[j]=num[j]*2
                    s+=num[j]
                    del num[j+1]
            num.reverse()
            while len(num)<self.n:
                num.append(0)
            for j in range(len(num)):
                grid[i][j]=num[j]
        p=False
        for i in range(self.n):
            for j in range(self.n):
                if grid_[i][j]!=grid[i][j]:
                    p=True
                    break
            if p==True:
                break
        return p,s,grid

    
    def move_up(self):
        s=0
        grid_=[[0 for j in range(self.n)] for i in range(self.n)]
        grid=[[0 for j in range(self.n)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                grid_[i][j]=self.grid[i][j]
                grid[i][j]=self.grid[i][j]
        for i in range(self.n):
            num=[]
            for j in range(self.n):
                if grid[self.n-j-1][i]!=0:
                    num.append(grid[self.n-j-1][i])
            for j in range(len(num)):
                if j+1<len(num) and num[j]==num[j+1]:
                    num[j]=num[j]*2
                    s+=num[j]
                    del num[j+1]
            num.reverse()
            while len(num)<self.n:
                num.append(0)
            for j in range(len(num)):
                grid[j][i]=num[j]
        p=False
        for i in range(self.n):
            for j in range(self.n):
                if grid_[i][j]!=grid[i][j]:
                    p=True
                    break
            if p==True:
                break
        return p,s,grid
    
    def move_down(self):
        s=0
        grid_=[[0 for j in range(self.n)] for i in range(self.n)]
        grid=[[0 for j in range(self.n)] for i in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                grid_[i][j]=self.grid[i][j]
                grid[i][j]=self.grid[i][j]
        for i in range(self.n):
            num=[]
            for j in range(self.n):
                if grid[j][i]!=0:
                    num.append(grid[j][i])
            for j in range(len(num)):
                if j+1<len(num) and num[j]==num[j+1]:
                    num[j]=num[j]*2
                    s+=num[j]
                    del num[j+1]
            num.reverse()
            while len(num)<self.n:
                num.append(0)
            for j in range(len(num)):
                grid[self.n-j-1][i]=num[j]
        p=False
        for i in range(self.n):
            for j in range(self.n):
                if grid_[i][j]!=grid[i][j]:
                    p=True
                    break
            if p==True:
                break
        return p,s,grid
    
    def find_best_move(self): #down,up,left,right corresponds to 0,1,2,3
        #weight=[[4096,]]
        m=None
        score1=-1
        grid_1=[[0]*self.n for i in range(self.n)]
        for i in range(self.n):
                    for j in range(self.n):
                        grid_1[i][j]=self.grid[i][j]
        for i in range(4):
            if i==0:
                p,s,grid=self.move_down()
                if p==True:
                    score=self.eval1(grid)
                    if score>score1:
                        score1=score
                        m=i
            if i==1:
                p,s,grid=self.move_up()
                if p==True:
                    score=self.eval1(grid)
                    if score>score1:
                        score1=score
                        m=i
            if i==2:
                p,s,grid=self.move_left()
                if p==True:
                    score=self.eval1(grid)
                    if score>score1:
                        score1=score
                        m=i
            if i==3:
                p,s,grid=self.move_right()
                if p==True:
                    score=self.eval1(grid)
                    if score>score1:
                        score1=score
                        m=i
        return m
    def play(self):
        can_move=True
        i=random.randint(0,self.n-1)
        j=random.randint(0,self.n-1)
        self.grid[i][j]=2
        i=random.randint(0,self.n-1)
        j=random.randint(0,self.n-1)
        while self.grid[i][j]!=0:
            i=random.randint(0,self.n-1)
            j=random.randint(0,self.n-1)
        self.grid[i][j]=2
        while can_move:
            self.printgrid()
            if not (self.move_down()[0] or self.move_up()[0] or self.move_left()[0] or self.move_right()[0]):
                can_move=False
            if can_move:
                move=self.find_best_move()
                if move==0:
                    print('move down')
                    temp1=self.move_down()[2]
                    self.score+=self.move_down()[1]
                    for i in range(self.n):
                        for j in range(self.n):
                            self.grid[i][j]=temp1[i][j]
                if move==1:
                    print('move up')
                    temp2=self.move_up()[2]
                    self.score+=self.move_up()[1]
                    for i in range(self.n):
                        for j in range(self.n):
                            self.grid[i][j]=temp2[i][j]
                if move==2:
                    print('move left')
                    temp3=self.move_left()[2]
                    self.score+=self.move_left()[1]
                    for i in range(self.n):
                        for j in range(self.n):
                            self.grid[i][j]=temp3[i][j]
                if move==3:
                    print('move right')
                    temp4=self.move_right()[2]
                    self.score+=self.move_right()[1]
                    for i in range(self.n):
                        for j in range(self.n):
                            self.grid[i][j]=temp4[i][j]
                empty={}
                empty_i=0
                for i in range(self.n):
                    for j in range(self.n):
                        if self.grid[i][j]==0:
                            empty[empty_i]=[i,j]
                            empty_i+=1
                k=random.randint(0,len(empty)-1)
                #i=empty[k][0]
                #j=empty[k][1]
                t=random.randint(0,9)
                grid_1=[[0]*self.n for i in range(self.n)]
                for i in range(self.n):
                    for j in range(self.n):
                        grid_1[i][j]=self.grid[i][j]
                score1=float('inf')
                m=None
                print(type(empty))
                print(empty)
                for ele1 in empty:
                    ele=empty[ele1]
                    if t<9:
                        grid_1[ele[0]][ele[1]]=2
                        score=self.eval1(grid_1)
                        grid_1[ele[0]][ele[1]]=0
                        if score<score1:
                            score1=score
                            m=(ele[0],ele[1])
                    else:
                        grid_1[ele[0]][ele[1]]=4
                        score=self.eval1(grid_1)
                        grid_1[ele[0]][ele[1]]=0
                        if score<score1:
                            score1=score
                            m=(ele[0],ele[1])
                if t<9:
                     self.grid[m[0]][m[1]]=2
                else:
                      self.grid[m[0]][m[1]]=4
        print(self.score)
        self.printgrid()
        return self.score

score=[]
for i in range(100):
    g=game(4)
    score.append(g.play())
print('Max: ',max(score))
print('avg: ',sum(score)/100)
print('min: ',min(score))
