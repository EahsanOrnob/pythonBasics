a=1
b=0


try:
    k=int(input("Input a integer number:"))
    print(k)
    print("Resource open")
    print(a/b)
    
    
except ZeroDivisionError as error:   
    print("You can't devide a number by zero.")
    print("Exception:",error)
    
except ValueError as error:
    print("You haven't gave an integer number")
    print("Exception:",error)
    
except Exception as error:
    print("Something want wrong...")
    print("Exception:",error)
finally:
    print("Resource close")
    
    
print("Bye")

