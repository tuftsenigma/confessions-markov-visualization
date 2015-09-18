import sys
import io
import csv
import time
import json


with open("topic_markov.csv", "r") as f:
	rd = csv.reader(f, delimiter=",")
	orig = []
	ln = []
	sums = {}

	order = [
		"Loneliness",
		"Social dynamic",
		"Time",
		"Social issues",
		"Party",
		"Desire",
		"Someone hot",
		"Domestic",
		"Bathroom",
		"Body",
		"Sexual Assault",
		"Academic",
	]

	for i,row in enumerate(rd):
		if i != 0:
			orig.append(row)

	for to_ in order:
		for from_ in order:
			for triple in orig:
				if triple[0] == from_ and triple[1] == to_:
					ln.append(triple)		


	for i,row in enumerate(orig):
		if i%13 == 0 and i != 0:
			sums[orig[i-12][0]] = (sum([int(r[2]) for r in orig[i-12:i]]))


	for i,row in enumerate(ln):
		if row[1] == "Loneliness":
			print float(row[2])/float(sums[row[0]])
			print row
