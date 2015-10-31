import random

depth = 4
n=26
mass =[[0] for i in range(depth)]
key = [random.randint(0, n-1) for x in range(depth)]
result=[]

def CreateTable(key = [random.randint(0, n-1) for x in range(depth)]):
	table = [[0]*n for i in range(depth)]
	for i in range(depth):
		for j in range(n):
			table[i][j]=(j+key[i])%n
	print("Key = " + str(key))
	return table

def Circle(depth):
	for i in range(n):
		mass[len(mass)-depth] = table[depth-1][i]
		if depth > 1:
			Circle(depth-1)
		else:
			result.append([mass[x] for x in range(len(mass))])

def CreateLine():
	for i in range(10):
		print(result[i])


def Crypt(message):
	message = message.lower()
	m = list(message)
	ab = "abcdefghijklmnopqrstuvwxyz"
	for i in range(len(m)):
		if m[i] != ' ':
			print(m[i])
			ind = ab.find(m[i])
			print(ind)
			for j in range(depth):
				ind = (ind + result[i][j])%n
			m[i] = ab[ind]
	print("".join(m))

table = CreateTable([0,0,0,0])
Circle(depth)
CreateLine()
Crypt("Hi Vlad")


	


