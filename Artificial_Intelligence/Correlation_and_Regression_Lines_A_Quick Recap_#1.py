# Enter your code here. Read input from STDIN. Print output to STDOUT
X = [15,12,8,8,7,7,7,6,5,3] 
Y = [10,25,17,11,13,17,20,13,9,15]

m1 = (sum(X)/len(X))
m2 = (sum(Y)/len(Y))

Score_1 = [x-m1 for x in X]
Score_2 = [x-m2 for x in Y]

n1 = sum([x*y for x,y in zip(Score_1,Score_2)])

X = sum([(x-m1)**2 for x in X])
Y = sum([(x-m2)**2 for x in Y])

n2 = (X**(1/2))*(Y**(1/2))

r = n1/n2

print (round(r,3))
