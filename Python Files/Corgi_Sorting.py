


weight = int(input("How much does your dog weigh?:"))

if weight <= 0:
	print("ERROR: Reweigh") 
	exit()


high_energy = int(input("Is your dog high energy?, 1 for yes, 0 for no:"))




if weight < 20 and high_energy == 1:
	print("Go to the Zoomies Yard")
elif weight < 20 and high_energy == 0:
	print("Go to the Puppy Lounge")
elif weight > 20 and high_energy == 1:
	print("Go to the Big Dog Run")
elif weight > 20 and high_energy == 0:
	print("Go to the Nap Porch")




