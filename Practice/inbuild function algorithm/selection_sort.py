def selectionsort(li):
    size=len(li)
    for i in range(0,size):
        min_ind=i
        for j in range(i+1,size):
            if(li[j]<li[min_ind]):
                min_ind= j
        li[i],li[min_ind]= li[min_ind] ,li[i]
        # print(li)
        
li=[60,50,10,20,40,30]
print('before sorting:',li)
selectionsort(li)
print('after sorting:',li)                