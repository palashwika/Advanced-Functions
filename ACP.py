num=int(input('Enter a number: '))
limit=range(0,num+1)
odd_list1=[x for x in limit if x%2!=0]
print(odd_list1)
oddlist2=[x for x in odd_list1 if num%x!=0]
print(oddlist2)


fruits=['apple','banana','strawberry','watermelon']
capital=[x.capitalize() for x in fruits]
print(capital)
