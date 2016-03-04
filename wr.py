import random
f = open('inputrandom.txt','w')
for x in xrange(0, 10):
	f.write(str(random.random())[2:10]+'\n')


