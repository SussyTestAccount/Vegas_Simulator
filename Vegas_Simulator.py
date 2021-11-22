import time
import serial
import numpy as np
import matplotlib.pyplot as plt
from drawnow import *
plt.ion()
n=1
x=[]
y=[]
z=0
e=0

def simBegin():
    global n
    global e
    print ("Welcome to the Vegas Simulator!")
    print ("Enter the simulator by pressing 1")
    e=input()
    print(e)
    if(e==1):
        for a in range(1,150):
            t=np.pi*4/200*n
            p1=np.sin(t)
            p2=np.cos(t)
            x.append(p1)
            y.append(p2)
            n=n+1
            drawnow(start)
            plt.pause(.000001)  
            if(n>100):
                y.pop(0)
                x.pop(0)
    print ("")
    print ("Thank you for experiencing the Vegas Simulator")
    print ("")

def start():
    #x=np.linspace(0,np.pi*4+n,109)
    #x=np.linspace(0,2*(np.pi/109*n))
    plt.title("Sin city ha")
    plt.plot(y,'r-',label='amogus')
    plt.plot(x,'b--',label="amogus_2")
    plt.show()

while (1):
    simBegin()
    print ("Relive the Experience? Press 1 to do so")
    z=input()
    if(z==1):
        simBegin()



