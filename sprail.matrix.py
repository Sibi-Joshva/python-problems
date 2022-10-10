import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class SPMatrix:
    
    def __init__(self,n):
        self.sv = 1
        self.mc = 0
        self.n = n
        self.M = []
        self.get_mid()
        self.cr = self.mid
        self.cc = self.mid
        self.get_M()
        self.M[self.cr][self.cc] = self.sv
        self.SMF = False
        self.n2 = n*n

    def get_M(self):
        for i in range(self.n):
            self.M.append([])
            for j in range(self.n):
                self.M[i].append(0)

    def get_mid(self):
        if (self.n%2)==0:
            self.mid = int(self.n/2)-1
        else:
            self.mid = int(self.n/2)

    def move_right(self):
        self.cc+=1
    
    def move_down(self):
        self.cr+=1
    
    def move_up(self):
        self.cr-=1
    
    def move_left(self):
        self.cc-=1
    
    def set_MV(self):
        if self.sv<=self.n2 or (self.cr<self.n and self.cc<self.n and self.cr>=0 and self.cc>=0):
            self.M[self.cr][self.cc] = self.sv
        else:
            self.SMF = True

    def process(self):
        
        while not self.SMF:
            self.mc += 1
            for i in range(self.mc):
                self.move_right()
                self.sv+=1
                self.set_MV()

            for i in range(self.mc):
                self.move_down()
                self.sv+=1
                self.set_MV()

            self.mc+=1

            for i in range(self.mc):
                self.move_left()
                self.sv+=1
                self.set_MV()

            for i in range(self.mc):
                self.move_up()
                self.sv+=1
                self.set_MV()
    
    def display(self):

        for r in self.M:
            for c in r:
                print("%4d"%c,end="")
            print()
    def display_heat(self):
        plt.imshow(self.M, cmap='hot', interpolation='nearest')
        plt.show()

    def display_cool(self):
        plt.imshow(self.M, cmap='hot', interpolation='nearest')
        plt.show()


sp = SPMatrix(10)
sp.process()
sp.display()
sp.display_heat()