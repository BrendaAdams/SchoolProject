##Determining if a patient has a low temp., normal temp., elevated temp., or fever and determine if the temperature is considered a fever##
##Worked together on all lines##
low = 0
normal = 0
elevated = 0
fever = 0

temp1 = (input("Please enter temp 1 in degrees F:"))
temp2 = (input("Please enter temp 2 in degrees F:"))


avg = (float(temp1)+float(temp2))/ float(2.0)

##Take average of two temperatures for one patient##


if (avg <= float('97')):     
    print('low temp')
    
elif (avg <= float('99')):
    print('normal temp')
    
elif (avg <= float('100.3')):
    print('elevated temp')
    
else:
    print('fever')
    

if avg <= float('99') and avg >= float('97.1'):
    print("Normal temperature, nothing wrong")
else:
    print("Patient needs further testing")

  
if avg > float(100.4): fever = True
else: fever = False

while (fever):
    print ("Patient has fever")
    break
