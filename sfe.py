# Script created by Simon McCabe
from random import *

def problem():
	bob = 5
	alice = 4
	carol = 2
	global soov # sum of original votes
	soov = bob + alice + carol
	# print "sum of original votes:",soov
	# create random values which give a sum of (vote + 100) for Bob
	# bobs vote is a variable, so random ints need to have a sum of 100 + bob's int
	# http://stackoverflow.com/questions/36824129/how-can-i-create-three-random-integers-which-sum-to-a-specific-value-python#36824153
	bob1 = randint(1,100)
	bob2 = randint(1,min(100, 100+bob-bob1))
	bob3 = 100 + bob - bob1 - bob2
	# print "Bob 1:",bob1
	# print "Bob 2:",bob2
	# print "Bob 3:",bob3
	# print "Sum of bobs random ints",bob1 + bob2 + bob3

	# create random values which give a sum of (vote + 100) for Alice
	alice1 = randint(1,100)
	alice2 = randint(1,min(100, 100+alice-alice1))
	alice3 = 100 + alice - alice1 - alice2

	# create random values which give a sum of (vote + 100) for Carol
	carol1 = randint(1,100)
	carol2 = randint(1,min(100, 100+carol-carol1))
	carol3 = 100 + carol - carol1 - carol2

	# Create 3 values
	value1 = bob + alice2 + carol2 
	value2 = alice + bob2 + carol3
	value3 = carol + alice3 + bob3

	sumOfValues = value1 + value2 + value3
	# print "Sum of values =",sumOfValues
	return sumOfValues

decryptedVotes = problem() % 100
while decryptedVotes != soov:
	decryptedVotes = problem() % 100
	if soov == decryptedVotes:
		print "Decrypted:", decryptedVotes
	else:
		continue