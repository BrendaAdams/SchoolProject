##Determining if a patient has a low temp., normal temp., elevated temp., or fever and determine if the temperature is considered a fever##
low = 0             ##Katherine Darrigrand##
normal = 0
elevated = 0
fever = 0
temperature1 = input()
temperature2 = input()
if temperature <= "97":     ##Brenda Adams##
    print(low)
elif temperature == (range(97.1, 99, [0.1])):
    print(normal)
elif temperature == (range(99.1, 100.3, [0.1])):
    print(elevated)
else:
    print (fever)
if temperature > "100.4": fever = True
else: fever = False
##Taken from homework chapter 3##       ##Katherine Darrigrand##
avg = (temperature1 + temperature2)/2
##Take average of two temperatures for one patient##
for temperature in range(97.1, 99):
    print("Normal temperature, nothing wrong")
