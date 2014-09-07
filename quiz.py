import sys
from random import randint

count = 0
 


Q = ["What is a non metal that remains liquid at room temperature? ",
     "Chlorophyll is a naturally occurring compound. Which central metal is it? ",
     "What is used in pencils in order to write? ",
     "Which metal forms an amalgam/mixture with other metals? ",
     "The gas usually filled in the electric light bulb is: ",
     "What is used as a moderator in a nuclear reactor? ",
     "Isotopes are separated by: ",
     "What radioactive pollutant has drawn public attention, due to its occurrence in the building material? ",
     "Who suggested that most of the mass in the atom is located in the nucleus ?",
     "According to Avogadro's Hypothesis, the smallest particle of an element or a compound, that can exist independently, is called a(n) ",
     "Nuclear fission is caused by the impact of: ",
     "How many colors are in the sunlight spectrum? ",
     "What color is bromine? ",
     "The hardest substance available on earth is: ",
     "The variety of coal in which the deposit contains recognizable traces of the original plant material is ",
     "What is the only substance that expands as it freezes? ",
     "What is the only letter that does appear on the periodic table? "]
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
     "seven",
     "red",
     "diamond",
     "peat",
     "water",
     "j"]
     
moreinfo = ["http://www.softschools.com/facts/periodic_table/bromine_facts/213/",
            "http://scifun.chem.wisc.edu/chemweek/chlrphyl/chlrphyl.html",
            "http://www.sciencekids.co.nz/sciencefacts/chemistry/carbon.html",
            "http://www.ducksters.com/science/chemistry/mercury.php",
            "http://www.ducksters.com/science/chemistry/nitrogen.php",
            "http://www.chemicool.com/elements/radium.html",
            "http://stilltutorial.com/2013/08/distilling-10-interesting-things-you-didnt-know/",
            "http://www.chemicool.com/elements/thorium.html",
            "http://ernestrutherfordpd7.weebly.com/interesting-facts.html",
            "http://www.ducksters.com/science/molecules.php",
            "http://scienceforkids.kidipede.com/chemistry/atoms/neutron.htm",
            "http://www.sciencekids.co.nz/sciencefacts/light.html",
            "http://www.softschools.com/facts/periodic_table/bromine_facts/213/",
            "http://www.softschools.com/facts/periodic_table/carbon_facts/183/",
            "http://www.snsk.no/facts-about-coal.145744.en.html",
            "http://www.sciencekids.co.nz/sciencefacts/water.html",
            "http://www.ptable.com/"]
            

i = randint(0, 14)
answer = raw_input("Question 1:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong \nCorrect Answer : " + A[i]
    print "To learn more visit this site" + moreinfo[i]


i = randint(0, 14) 
answer = raw_input("\nQuestion 2:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong \nCorrect Answer : " + A[i]
    print "To learn more visit this site" + moreinfo[i]

i = randint(0, 14)
answer = raw_input("\nQuestion 3:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong \nCorrect Answer : " + A[i]
    print "To learn more visit this site" + moreinfo[i]

i = randint(0, 14) 
answer = raw_input("\nQuestion 4:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong \nCorrect Answer : " + A[i]
    print "To learn more visit this site" + moreinfo[i]

i = randint(0, 14)
answer = raw_input("\nQuestion 5:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong \nCorrect Answer : " + A[i]
    print "To learn more visit this site" + moreinfo[i]

i = randint(0, 14) 
answer = raw_input("\nQuestion 6:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong \nCorrect Answer : " + A[i]
    print "To learn more visit this site" + moreinfo[i]

i = randint(0, 14)
answer = raw_input("\nQuestion 7:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong \nCorrect Answer : " + A[i]
    print "To learn more visit this site" + moreinfo[i]

i = randint(0, 14) 
answer = raw_input("\nQuestion 8:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong \nCorrect Answer : " + A[i]
    print "To learn more visit this site" + moreinfo[i]

i = randint(0, 14)
answer = raw_input("\nQuestion 9:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong \nCorrect Answer : " + A[i]
    print "To learn more visit this site" + moreinfo[i]

i = randint(0, 14) 
answer = raw_input("\nQuestion 10:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong \nCorrect Answer : " + A[i]
    print "To learn more visit this site" + moreinfo[i]

i = randint(0, 14)
answer = raw_input("\nQuestion 11:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong \nCorrect Answer : " + A[i]
    print "To learn more visit this site" + moreinfo[i]

i = randint(0, 14) 
answer = raw_input("\nQuestion 12:" + Q[i])
if answer.lower() == A[i]:
    print "Correct"
    count = count + 1
else:
    print "Wrong \nCorrect Answer : " + A[i]
    print "To learn more visit this site" + moreinfo[i]


print "\nOut of 14 questions asked, you got %d of them right." % (count)
print "\nYou got %d percent." % (count / float(14) * 100)
