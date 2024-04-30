def swaplist(inputlist):
    
    for i in range(0,len(inputlist)):
        if i%2==1:
            temp=inputlist[i]
            inputlist[i]=inputlist[i-1]
            inputlist[i-1]=temp            

        else:
            continue
    return inputlist
lengthoflist=int(input("enter the number of list items you are entering"))
listtoswap=[int(input(f"Enter list item {i}")) for i in range(0,lengthoflist)]
print(swaplist(listtoswap))
