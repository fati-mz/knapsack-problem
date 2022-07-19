import time
start_time = time.time()

#number of items 
n = int(input("Enter number of items : ")) 

#item's values
val=list(map(int,input("\nEnter the values : ").strip().split()))[:n]

#item's weights
wt=list(map(int,input("\nEnter the weights : ").strip().split()))[:n]

#max capacity
W = int(input("Enter the max capasity : "))

def improved(W,wt,val): 

    #Building empty 2D array P[][] 
    P = [[0 for w in range(W + 1)]
			for i in range(n + 1)]
    i=n
    w=W
    P[i][w]=1

    #marking needed items
    #from P[n][w] to P[1][1]
    while i!=1:
        for w in range(W,0,-1):
         if P[i][w]==1: 
            P[i-1][w]=1
            if w-wt[i - 1]!=0:
                P[i-1][w-wt[i - 1]]=1
        i-=1
    
    #solving improved dynamic knapsack
    for i in range(1,n + 1):
        for w in range(1,W + 1):
            if P[i][w]==1 and wt[i - 1] <= w:
                P[i][w] = max(val[i - 1]+ P[i - 1][w - wt[i - 1]],P[i - 1][w])  
            if P[i][w]==1 and wt[i - 1] >w :
                P[i][w] = P[i - 1][w]    
    
    #print the max profit
    res = P[n][W]
    print('max profit:' ,res)
    
    #print selected items
    print('Selected items : ')
    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == P[i - 1][w]:
            continue
        else:
			#This item is included.
            print(i ,"'th item, ",end=' ' )
            res = res - val[i - 1]
            w = w - wt[i - 1]
    print()
    print('-------------------')

improved(W,wt,val)
print("--- %s seconds ---" % (time.time() - start_time))