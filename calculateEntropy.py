import math

a = int(raw_input("Enter phases (integer): "))
print "Key entropy =", math.log(a) / math.log(2),"bits"