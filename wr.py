import random
f = open('inputrandom.txt','w')
for x in xrange(0, 100000):
	f.write(str(random.random())[2:10]+'\n')


