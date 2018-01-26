import random
l=[]
for i in range(0,100000000):
    l.append(random.randint(1,1000000000))
def sort(array):
    less = []
    greater = []
    equals=[]
    if len(array) > 1:
        pivot = array[len(array)-1]
        for x in array:
            if x < pivot:
                less.append(x)
            if x==pivot:
                equals.append(x)
            if x > pivot:
                greater.append(x)
        return sort(less)+equals+sort(greater)
    else:
        return array

