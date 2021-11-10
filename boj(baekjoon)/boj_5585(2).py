coins = [500,100,50,10,5,1]
charges = 0


a = int(input())
m = 1000 - a 

for i in coins:
    charges += m//i
    m = m%i

print(charges)
