def swap(inputlist):
    #inputlist=[1,2,3,4,5]
    for i in range(0,len(inputlist)):
        if i%2==1:
            temp=inputlist[i]
            inputlist[i]=inputlist[i-1]
            inputlist[i-1]=temp            

        else:
            continue
    print(inputlist)
swap([1,2,3,4,5])
'''lengthoflist=input("enter the number of list items you are entering")
for i in range(0,lengthoflist):
    listtoswap=[int(input("enter the list items to be swapped"))]
print(type(listtoswap))
swap(listtoswap)'''
