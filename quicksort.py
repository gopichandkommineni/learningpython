def quicksort(array):
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
        return quicksort(less)+equals+quicksort(greater)
    else:
        return array
    
def main():
    l=[]
    print("enter elements to sort separated with space")
    l=list(map(int,input().split(" ")))
    result=quicksort(l)
    print(*result,sep=" ")
    
if __name__ == '__main__':
    main()
