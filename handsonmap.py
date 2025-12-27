#add to lists using map and lambda
num1=[3,6,9]
num2=[8,4,1]
result=map(lambda x, y: x+y, num1,num2) #lambda is the syntax for adding numbers in map
print("Addition of two lists")
print(list(result))

#using map 
nums=[1,2,3,4,5]
def sq(n):
    return n*n
square=list(map(sq, nums))
print("Square of numbers in list")
print(square)