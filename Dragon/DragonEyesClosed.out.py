"""
Mario Garcia Palacio
12/04/2023
CloseDragonEyes
"""

openEyes = open('Dragon.in', 'r')
eyes = openEyes.read()
openEyes.close()

eyes = eyes.replace('0', 'X')

closeEyes = open('DragonEyesClosed.out', 'w')
closeEyes.write(eyes)
closeEyes.close()













