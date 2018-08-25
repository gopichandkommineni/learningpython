def quicksort1(arr, min, max):
    if min  < max:
        sep = partition1(arr, min, max)
        quicksort1(arr, min, sep-1)
        quicksort1(arr, sep+1, max)
def partition1(arr1, min1, max1):
    piv = arr1[min1]
    l = min1 
    r = max1
    while l < r:
        while l <= r and arr1[l] <= piv: 
            l = l+1
        while l <= r and arr1[r] > piv:
            r = r-1
        if l < r:
            arr1[l],arr1[r]=arr1[r],arr1[l]
    arr1[min1] = arr1[r]
    arr1[r] = piv
    return r
def main():
    l=[]
    print("enter elements to sort separated with space")
    l=list(map(int,input().split(" ")))
    quicksort1(l,0,len(l)-1)
    print(*l,sep=" ")
    
if __name__ == '__main__':
    main()
