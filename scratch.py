#Dictionary 
char=['fiona','lip','carl','ian','liam']
dict={x: x*2 for x in char }
print(dict)

def square(n):
    return n*2
num=(1,2,3,4)
result=(square,num)
print(list(result))

list=["food","cake","cupcakes","pizza"]
newlist=[]
for i in list:
    if i=="food":
        #print(newlist.append(i)) #using print with append always returns None, has to be done separately
        newlist.append(i)
print(newlist)


list2=["beets","cake","cupcakes","pizza"]
nlist=[i for i in list2 if i=="beets"]

list3=[9,7,5,3,2]
my_dict={x**2: x**2 for x in list3} #key:value for (key,value) in variable or a list [1,2,3,4]
print(my_dict)



a=list(input("Enter a series of 5 numbers with no spaces or characters in between: "))
print(a)
odd_list=[x for x in a if x%2==0]
print(odd_list)