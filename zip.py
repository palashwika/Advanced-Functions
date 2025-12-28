#zip elements of two lists
s1={4,3,2}
s2={'a','c','d'}
s3=list(zip(s1,s2))
print(s3,"\n")

#Zip elements of two lists
#Print elements 1 by 1 , but elements of 2nd list will be in reverse order
list1=[1,2,3,4,5]
list2=[3,4,5,6]

for x, y in zip(list1,list2[::-1]):
    print(x,y)

#Zip into dictionary
stocks=['reliance','infosys','tcs']
prices=[2175,2334,2982]

newdict={stocks:prices for stocks,prices in zip(stocks, prices)}
print('\n{}'.format(newdict))