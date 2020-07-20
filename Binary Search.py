pos=-1
def search(list,n):
    l=0
    u=len(list)-1

    while l<=u: 
        
        mid= (u+l) // 2
  
        if list[mid]==n:
           globals()['pos']=mid
           return True
        else:
           if list[mid]<n:
               l=mid+1
           else:
               u=mid-1

    return False   


list = [1,2,3,4,5,6,9]    #for binary search list must have sorted

n=9

if search(list,n):
    print(n,"Found at index",pos+1)
    
else:
    print(n,"Not Found")
