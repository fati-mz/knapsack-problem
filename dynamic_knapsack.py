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

def dynamic_knapsack(W, wt, val):
	#number of items 
	n = len(val)

	#Building empty 2D array P[][] 
	P = [[0 for w in range(W + 1)]
			for i in range(n + 1)]
			
	#solving dynamic knapsack
	for i in range(n + 1):
		for w in range(W + 1):
			if i == 0 or w == 0:
				P[i][w] = 0
			elif wt[i - 1] <= w:
				P[i][w] = max(val[i - 1]
				+ P[i - 1][w - wt[i - 1]],
							P[i - 1][w])
			else:
				P[i][w] = P[i - 1][w]

	#print the max profit
	res = P[n][W]
	print(res)
	
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
	
dynamic_knapsack(W, wt, val)
print("--- %s seconds ---" % (time.time() - start_time))