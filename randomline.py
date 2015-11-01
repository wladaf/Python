import random


depth = 8
n=6
N=26
done = 0

mass =[[0] for i in range(depth)]
key = [random.randint(0, n-1) for x in range(depth)]
result=[]
message = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

def CreateTable(key = [random.randint(0, n-1) for x in range(depth)]):
	table = [[0]*n for i in range(depth)]
	for i in range(depth):
		for j in range(n):
			table[i][j]=(j+key[i])%N
	print("Key = " + str(key))
	return table

def Circle(depth):
	for i in range(n):
		mass[len(mass)-depth] = table[depth-1][i]
		if depth > 1:
			Circle(depth-1)
		else:
			result.append([mass[x] for x in range(len(mass))])
			print(mass)
		if len(result) > len(message):
			return 0

def CreateLine():
	for i in range(len(message)):
		print(result[i])


def Crypt(message):
	print(message)
	message = message.lower()
	m = list(message)
	ab = "abcdefghijklmnopqrstuvwxyz"
	for i in range(len(m)):
		if m[i] != ' ':
			ind = ab.find(m[i])
			for j in range(depth):
				ind = (ind + result[i][j])%N
			m[i] = ab[ind]
	print("".join(m))

table = CreateTable([0,0,0,0,0,0,0,1])
Circle(depth)
#CreateLine()
Crypt(message)


	


