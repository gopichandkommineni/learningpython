import random
l=[]
for i in range(0,100000000):
    l.append(random.randint(1,1000000000))
def sort(array):
    for i in range(0,len(array)):
        for j in range(0,len(array)):
            if(array[i]<array[j]):
                array[i],array[j]=array[j],array[i]
    
