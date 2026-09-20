def binarySearch(li,searchEle):
    beg=0
    end=len(li)-1
    while(beg<=end):
        #print('beg:,beg)
        #print('end:',end)
        mid=(beg+end)//2
        
        if(searchEle == li[mid]):
            return mid
        elif(searchEle<li[mid]):
            # print('less then')
            end=mid-1
            #print('end',end)
        elif(searchEle>li[mid]):
            # print('greater than')
            beg=mid+1
            #print('beg',beg)
    else:
        print -1
        
li=[10,20,30,40,50,60]
ele=int(input("enter a number:"))
res=binarySearch( li, ele)       
#print(res)
if (res!=-1):
    print(f'{ele} is present at index {res}.')
    
else:
    print(f'{ele} is not present in list.')           