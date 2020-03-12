'''
March 10, 2020, Japan.
Author: hawkeyeAlice.
Topic: A program to teach yourself basic python.
'''
#!/usr/bin/python
import os
import re
from subprocess import PIPE, run

class basicPython:
    def __init__(self):
        self.printhello= "print(\"Hello, World.\")\n"
        self.ifelifelse= "n=1\nif(n==0):\n print(\"hi\")\nelse:\n print(\"bye\")\n"
        self.forloop= "for i in range(3):\n print(i)\n"
        self.whileloop="n=3\nwhile n>=0:\n print(n)\n n-=1\n"

    def learningPrint(self):
        print(self.printhello)
        print("\nThe output of the above code is: ")
        print("Hello, World.\n")
    def learningCondition(self):
        print(self.ifelifelse)
        n=1
        if n==0:
            print("\nThe output of the above code is: ")
            print("hi")
            print("\n\n")
        else:
            print("\nThe output of the above code is: ")
            print("bye")
            print("\n\n")
    def learningForloop(self):
        print(self.forloop)
        for i in range(3):
            print(i)
    def learningWhileloop(self):
        print(self.whileloop)
        n=3
        while(n>=0):
            print(n)
            n-=1



Object=basicPython()
print("\n\nAre you excited to teach yourself python?\nHere are some explanation and guidelines that will help you while learning python.\n")
input("Press Enter to continue...")
print("\n\nEvery program begins with printing hello world message.\nI will teach you how to print hello world using python.\n\n")
input("Press Enter to continue...")
print("\n\nThe print function prints the specific message on the screen.\nThe message can be a string or any other object.\nHowever, the object will be converted into string before showing the output on the screen.\n\nBelow is an example on how we can write print statement in python.\n\n")
input("Press Enter to continue...\n")
Object.learningPrint()
print("Do you want to give it a try now?\n")
cmdHello=input("Please enter the print statement code that you have learned now:")
print("\nYou have entered: ",cmdHello)
outPrint=re.search("\(([^)]+)", cmdHello).group(1)
outPrint = outPrint.replace('"', '')
print("\nThe output of the above code is: ",outPrint)
input("\n\nPress Enter to continue...")
print("\n----------------------------------------------------------------------------------------------------------")
print("\n\nLet's move on to the next section. Shall we?\nWe will now learn about conditional statement in Python.\n")
input("\nPress Enter to continue...")
print("\n\nDecision structures evaluate multiple expressions which produce TRUE or FALSE as outcome.\nAn if statement can be followed by an optional else statement, which executes when the boolean expression is FALSE.\nBelow is an example on how we can write if-else statement in python.\n\n")
input("Press Enter to continue...\n")
Object.learningCondition()
input("Press Enter to continue...\n")
print("P.S. Please use one whitespace for newline & two whitespace for newline+tab\n")
cmdCon=input("It is time to test what you have learned. Are you ready? You can enter a python conditional statement now.")
cmdCon1 = cmdCon.replace('  ','\n\t')
cmdCon2= cmdCon1.replace(' ','\n')
print("\nYou have entered the following code:\n")
print(cmdCon2)
myConFile='/home/rhui/babycodes/learningCondition.py'
with open(myConFile, "w") as fd:
    fd.write("#!/usr/bin/python \n")
    #fd.write("def cmdConFunc():\n\t")
    fd.write(cmdCon2)
    fd.close()

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

my_output = out("python learningCondition.py")
print("\nThe output of the above code is: ",my_output)

input("\n\nPress Enter to continue...")
print("\n----------------------------------------------------------------------------------------------------------")
print("Let's move forward to for loop in Python.\nA for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).\n ")
input("\nPress Enter to continue...")
print("\n\nfor loop we can execute a set of statements, once for each item in a list, tuple, set etc.\nHere is an example:\n\n")
Object.learningForloop()
input("\nPress Enter to continue...")
print("P.S. Please use two whitespace for newline+tab\n")
cmdFor=input("It is time to test what you have learned. Are you ready? You can enter a python for loop now.\n")
cmdFor1 = cmdFor.replace('  ','\n\t')
print("\nYou have entered the following code:\n")
print(cmdFor1)
myForFile='/home/rhui/babycodes/learningFor.py'
with open(myForFile, "w") as fd:
    fd.write("#!/usr/bin/python \n")
    fd.write(cmdFor1)
    fd.close()

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

my_output = out("python learningFor.py")
print("\nThe output of the above code is: ",my_output)

input("\n\nPress Enter to continue...")
print("\n----------------------------------------------------------------------------------------------------------")
print("Let's move forward to while loop in Python.\nWith the while loop we can execute a set of statements as long as a condition is true.\n ")
input("\nPress Enter to continue...")
print("\n\nHere is an example:\n\n")
Object.learningWhileloop()
input("\nPress Enter to continue...")
print("\nP.S. Please use one whitespace for newline & two whitespace for newline+tab\n\n")
cmdWhile=input("It is time to test what you have learned. Are you ready? You can enter a python for loop now.\n\n")
cmdWhile1 = cmdWhile.replace('  ','\n\t')
cmdWhile2= cmdWhile1.replace(' ','\n')
print("\nYou have entered the following code:\n\n")
print(cmdWhile2)
myWhileFile='/home/rhui/babycodes/learningWhile.py'
with open(myWhileFile, "w") as fd:
    fd.write("#!/usr/bin/python \n")
    fd.write(cmdWhile2)
    fd.close()

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

my_output = out("python learningWhile.py")
print("\n\nThe output of the above code is: ",my_output)

print("\n\nThat's all for now. I hope you learned basic Python through this tutorial.\n\nHAVE A NICE DAY and THANK YOU!!!\n")
#output = subprocess.check_output("cat /home/rhui/babycodes/learningCondition.py", shell=True)
#learningCondition.cmdConFunc()
#os.system('python learningCondition.py')
#call(['python', '/home/rhui/babycodes/learningCondition.py'])
