# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 23:12:12 2018

@author: ashis
"""
import random
import greedy

class game:
    def __init__(self, n):
        self.n=n
        self.grid=[[0 for j in range(n)] for i in range(n)]
        self.score=0

    def printgrid(self):
        for i in range(self.n):
            print(self.grid[i])
    
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
        return greedy.get_move(self)
        
        
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
                i=empty[k][0]
                j=empty[k][1]
                t=random.randint(0,9)
                if t<9:
                    self.grid[i][j]=2
                else:
                    self.grid[i][j]=4
        print(self.score)
        self.printgrid()
g=game(4)
g.play()
