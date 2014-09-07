from random import randint 
 
count = 0
 
Q = ["What is a non metal that remains liquid at room temperature? ",
     "Chlorophyll is a naturally occurring chelate compound in which central metal is: ",
     "Which of the following is used in pencils? ",
     "Which of the following metals forms an amalgam with other metals? ",
     "The gas usually filled in the electric bulb is: ",
     "Which of the following is used as a moderator in a nuclear reactor? ",
     "Isotopes are separated by: ",
     "Which radioactive pollutant has recently drawn to public, due to its occurrence in the building material? ",
     "Who suggested that most of the mass of the atom is located in the nucleus? ",
     "According to Avogadro's Hypothesis, the smallest particle of an element or a compound, that can exist independently, is called a(n): ",
     "Nuclear fission is caused by the impact of: ",
     "How many colours the sunlight spectrum has? "]
A = ["bromine",
     "magnesium",
     "graphite",
     "mercury",
     "nitrogen",
     "radium",
     "distillation",
     "thorium",
     "rutherford",
     "molecule",
     "neutron",
     "seven"]
 
i = randint(0, 11)
answer = raw_input("\nQuestion 1:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong"

i = randint(0, 11) 
answer = raw_input("\nQuestion 2:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong"

i = randint(0, 11)
answer = raw_input("\nQuestion 3:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong"

i = randint(0, 11) 
answer = raw_input("\nQuestion 4:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong"

i = randint(0, 11)
answer = raw_input("\nQuestion 5:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong"

i = randint(0, 11) 
answer = raw_input("\nQuestion 6:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong"

i = randint(0, 11)
answer = raw_input("\nQuestion 7:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong"

i = randint(0, 11) 
answer = raw_input("\nQuestion 8:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong"

i = randint(0, 11)
answer = raw_input("\nQuestion 9:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong"

i = randint(0, 11) 
answer = raw_input("\nQuestion 10:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong"

i = randint(0, 11)
answer = raw_input("\nQuestion 11:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong"

i = randint(0, 11) 
answer = raw_input("\nQuestion 12:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong"


print "\nYou got %d out of 12 correct." % (count)
if count <=6:
	print "Better luck next time!"
else: print "Good job!"
