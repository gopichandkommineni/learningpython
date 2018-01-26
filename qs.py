
>>> def quicks(list,low,high):
	i=low,j=high-1
	pivot=high
	if(i<j):
		while(list[i]<pivot):
			i=i+1
		while(list[j]>pivot):
			j=j-1
		if(i<j):
			(list[i],list[j])=(list[j],list[i])
		(list[j],list[pivot])=(list[pivot],list[j])
		quicks(list,0,j)
		quicks(list,j+1,len(list))

		
>>> 
