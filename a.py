import random
import openpyxl
s = [i for i in range(1000)]
random.shuffle(s)



def qucksort(l):
	if len(l) <= 1:
		return l
	base = l.pop()
	smaller,bigger = [],[]
	for i in l:
		if i > base:
			bigger.append(i)
		else:
			smaller.append(i)
	return qucksort(smaller) + [base] + qucksort(bigger)


print(qucksort(s))