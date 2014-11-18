
from itertools import groupby
import collections

class CountWords():
	
	def start(self, str):
		arrStr = str.split(' ')
		a = [len(list(group)) for key, group in groupby(arrStr)]
		counter=collections.Counter(arrStr)
		print(counter.most_common(3))
		# for key, group in groupby(arrStr):
		# 	print len(list(group)) 
	# def count(self, arr):
	# 	for 

if __name__ == "__main__" :
	a = CountWords()
	a.start("the quick brown fox the")