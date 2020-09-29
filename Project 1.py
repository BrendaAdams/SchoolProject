##Determining if a patient has a low temp., normal temp., elevated temp., or fever and determine if the temperature is considered a fever##
low = 0             ##Katherine Darrigrand##
normal = 0
elevated = 0
fever = 0

temp1 = str(input("Please enter temp 1 in degrees F:"))
temp2 = str(input("Please enter temp 2 in degrees F:"))


avg = (float(temp1)+float(temp2))/ float(2.0)
print(avg)


##Take average of two temperatures for one patient##

##Brenda Adams##


if (avg <= float('97')):     
    print('low temp')
    
elif (avg <= float('99')):
    print('normal temp')
    
elif (avg <= float('100.3')):
    print('elevated temp')

else:
    print('fever')
    
  
if avg > float(100.4): fever = True
else: fever = False;

while( avg < 100.4):
    temp1 = str(input("Please enter temp 1 in degrees F:"))
    temp2 = str(input("Please enter temp 2 in degrees F:"))
    print(avg);
    break
while( avg < 100.4):
    avg = (float(temp1)+float(temp2))/ float(2.0)
    print(avg)

    
##Taken from homework chapter 3##


##Katherine Darrigrand##


if avg <= float('99') and avg >= float('97.1'):
    print("Normal temperature, nothing wrong")
else:
    print("Patient needs further testing")

