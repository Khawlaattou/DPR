import time
import matplotlib.pyplot as plt
from naive7 import naive
from DPR7 import DPR
from moy import moy
fx = [10, 100, 1000, 10000,100000]

#initialize variables
T=[]
tps,tps2=[],[]
ploot,ploot2=[],[]
lst=[]
n1=n2=0
#open the file
file=open("data-file path",'r')
tab=file.read()
x=int(input("donnez element a chercher: "))
#split the lists according to their length
listes=tab.split("##")
file.close()
for i in listes:
    #split every collection into 20 lists
    lst.extend(i.split("\n"))
    #converting the lists data from string to int
    res = [eval(k) for k in lst]
    for j in res:
        start=time.time()
        dpr=DPR(j,x) #ysing dpr func
        end=time.time()
        start2=time.time()
        nv=naive(j,x) #using naive func
        end2=time.time()
        if dpr>0:
            n1=n1+dpr #calculating the number of accurance according to dpr func
        if nv>0:
            n2=n2+nv  #calculating the number of accurance according to naive func
        print("le nombre d'occurence de", x ,"dans cette liste est: ",dpr)
        tps.append(end-start)
        tps2.append(end2-start2)
    #calculating the average of time wasted on 20 lists of the same size
    p = moy(tps) 
    p2=moy(tps2)
    ploot.append(p)
    ploot2.append(p2)
    tps.clear()
print("le nombre total d'occurence de", x ," on utilisant la methode DPR","est: ",n1)
print("le nombre total d'occurence de", x ," on utilisant la methode naif","est: ",n2)

plt.plot(fx, ploot, label='DPR', linestyle='-', color='purple')
plt.plot(fx, ploot2, label='naive', linestyle='-', color='green')
print("moyen de temps pour parcourir les listes obtenu en:\n","dpr: ",ploot,"\n naive: ",ploot2)
plt.xlabel('taille')
plt.ylabel('temps')
plt.title("difference entre l'application du algorithme deviser pour regner et un algorithme naive")
plt.legend()
plt.grid(True)
plt.show()