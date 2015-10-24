"awdwad"
class NQueens:
	def __init__(self, n):
		try:
			import time
			import itertools
		except:
			pass
		else:
			self.time = time
			self.itertools = itertools
		self.n = n
		self.results = []

	def Check(self, a):
		for i in range(len(a)):
			for j in range(i + 1, len(a)):
				if abs(a[i][0] - a[j][0]) == abs(a[i][1] - a[j][1]):
					return False
		return True

	def Find(self, n):
		queens = [0 for x in range(n)]
		startT = self.time.time()
		for iters in self.itertools.permutations([x for x in range(n)]):
			field = [[0]*n for i in range(n)]
			for j in range(n):
				queens[j]=[j, iters[j]]
			if self.Check(queens):
				for j in range(n):
					field[j][iters[j]] = 1
				self.results.append(field)
		self.finishT = self.time.time()-startT

	def Count(self): 
		return len(self.results)

	def Time(self): 
		return self.finishT

	def GetPositions(self):    
		self.Find(self.n)
		return self.results

	def Print(self):     
		result = self.GetPositions()
		for i in range(len(self.results)):
			print(i+1,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
			for j in range(self.n):
				print(self.results[i][j])
		

q = NQueens(7)
q.Print()
print("Count: ",q.Count())
print("Time: {:0.3} s".format(q.Time()))

