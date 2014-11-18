############################
#	Name: Lye Sam de Leon
############################

import os, re
from itertools import groupby


"""	
Create a program that will take as input the following files:
	1. A comma-separated data file containing an arbitrary list of fields followed by several values.
		Each line ends with a newline character.


"""

class ProcessingDataFile():
	
	def __init__(self):
		self.set_identifier = []
		self.data = []
		
	def start(self, f):
		if not os.path.isfile(f): return "File doesn't exist" 
		with open(f) as lines:
			self.set_identifier = self.validate_lines(lines,"identifier").split(',')
			for l in self.validate_lines(lines):
				self.data.append(l.split(', '))

	def validate_lines(self, lines, x = None):
		if x is not None: return re.sub(r'\s+', '', lines.readline()) 
		return (line.strip() for line in lines if line)
			
	def start_rules(self, f):
		if not os.path.isfile(f): return "File doesn't exist"
		filters = []
		groupings = ""
		with open(f) as lines:
			for linenum, line in enumerate(lines):
				# print linenum, line
				group_fields_by = self.set_rules(line,"group by ([a-z]*)")
				filter_identifier = self.set_rules(line,"filter by ([a-z]*)")
				filter_value = self.set_rules(line,"filter by .*=([a-z]*)")

				if group_fields_by is not None: groupings= group_fields_by
				if filter_identifier is not None and filter_value is not None: 
					filters.append([filter_identifier, filter_value])
				
		for k,v in filters:
			
			self.arrange_by_filter(k,v, groupings)

	def set_rules(self, line, regex):
		try:
			return re.search(regex,line.strip(), re.IGNORECASE).group(1)
		except AttributeError: pass

	def arrange_by_group(self, identifier, arr): 
		try: 
			pointer = self.set_identifier.index(identifier)
			return sorted(arr, key=lambda x:x[pointer])
		except ValueError: print "Grouping/Filtering Item not found on Data File"

	def arrange_by_filter(self, identifier, value, groupings):
		"""
			group by Company	
				filter by Company=Apple
				filter by Position=CEO

			filters = [[Company, Apple],[Position,CEO]]
		"""
		pointer = self.set_identifier.index(identifier) 
		match = []
		mismatch = []

		for each in self.data:
			try: 
				if each[pointer] == value: match.append(each)
				else: mismatch.append(each)
			except: 
				print "pointer is empty"
				pass

		match = self.arrange_by_group(identifier, match)
		mismatch = self.arrange_by_group(identifier, mismatch)


		self.writefile('%s_%s_match'%(identifier,value),match)
		self.writefile('%s_%s_mismatch'%(identifier,value),mismatch)

	def writefile(self, filename, results):
		from datetime import datetime
		now = datetime.now().strftime('%Y%m%d%H%M%S')

		print "%s_%s.txt"%(now,filename)

		data = ""
		for line in results: data += '%s\n'%(' ,'.join(line))

		with open("%s_%s.txt"%(now,filename), 'w') as txtfile: txtfile.write(data)

		
if __name__ == "__main__":
	a = ProcessingDataFile()
	a.start(r'C:\Users\Sam\SanFrancisco\datafile.txt')
	a.start_rules(r'C:\Users\Sam\SanFrancisco\sorting.txt')