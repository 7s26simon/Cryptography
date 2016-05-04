# Script created by Simon McCabe
from random import *

bob = 5
alice = 1
carol = 1
soov = bob + alice + carol

def problem():
	# thanks to http://stackoverflow.com/questions/36824129/how-can-i-create-three-random-integers-which-sum-to-a-specific-value-python#36824153
	global bob1
	global bob2
	global bob3
	bob1 = randint(1,100)
	bob2 = randint(1,min(100, 100+bob-bob1))
	bob3 = 100 + bob - bob1 - bob2

	global alice1
	global alice2
	global alice3
	alice1 = randint(1,100)
	alice2 = randint(1,min(100, 100+alice-alice1))
	alice3 = 100 + alice - alice1 - alice2

	global carol1
	global carol2
	global carol3
	carol1 = randint(1,100)
	carol2 = randint(1,min(100, 100+carol-carol1))
	carol3 = 100 + carol - carol1 - carol2

	global value1
	global value2
	global value3
	# Create 3 values
	value1 = bob + alice2 + carol2 
	value2 = alice + bob2 + carol3
	value3 = carol + alice3 + bob3
	# Add values together
	sumOfValues = value1 + value2 + value3
	# print "Sum of values =",sumOfValues
	return sumOfValues

# Result of function mod 100 (should match original sum of votes)
derivedVotes = problem() % 100
while derivedVotes != soov:
	derivedVotes = problem() % 100
	if soov == derivedVotes:
		print ""
	else:
		continue

print "Original votes as follows:\nBob's vote:",bob,"\nAlice's Vote:",alice,"\nCarol's Vote:",carol
print "Create random values which give a sum of (vote + 100) for Bob, Alice and Carol"		
print "Bob 1:",bob1
print "Bob 2:",bob2
print "Bob 3:",bob3
print "Sum of bobs random integers:",bob1 + bob2 + bob3

print "alice 1:",alice1
print "alice 2:",alice2
print "alice 3:",alice3
print "Sum of alice random integers:",alice1 + alice2 + alice3

print "carol 1:",carol1
print "carol 2:",carol2
print "carol 3:",carol3
print "Sum of carol's random integers:",carol1 + carol2 + carol3

print "\nScrambled Vote 1:",value1
print "Scrambled Vote 2:",value2
print "Scrambled Vote 3:",value3

print "\nSum of original votes:", soov
print "Votes successfully derived"
print "Derived vote (sum of scrambled votes mod 100):", derivedVotes