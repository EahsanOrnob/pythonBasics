
def sort(list):
    
    
    for i in range(len(list)-1,0,-1):
        
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j+1]
                list[j+1]=list[j]
                list[j]=temp  
        print(list)  
        print("----------------------------------------------------->")  
    return list
    return list

list=[10,5,3,62,9,6,2,1,56]

print(list," first")

sort(list)
print(list," end")