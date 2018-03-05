from random import randint
num = randint(1,300)
print(input)
passward = False
while passward == False:
	daan = int(input())
	if daan > num:
		print("no,no,no,too big")
	if daan < num:
		print("no,no,no,too small")
	if daan == num:
		print("yes,you are right")
		passward = True