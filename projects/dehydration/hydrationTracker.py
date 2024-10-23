import math

print("water tracker")
weight = int(input("Your weight: "))
bodyWater = 0.03 *weight

if bodyWater - int(bodyWater) < 0.5:
	bodyWater = int(bodyWater) + 0.5
else:
	math.ceil(bodyWater)


print(f"Your daily water intake is {bodyWater} litres")

print(f"You're .'. to drink 8 glasses {1000* bodyWater/8}ml of water every 2 hours btwn 05:00 t0 19:00")
