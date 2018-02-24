print("How many Kilometers did you run today")
kms = input()
miles = round(float(kms)/1.60934, 2)
print(f"Ok, you ran {kms} kilometers today \nThis is {miles} miles.")
