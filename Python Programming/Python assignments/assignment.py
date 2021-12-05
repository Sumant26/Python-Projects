age = 20
comorbidities = True

if age > 45:
    print("Vaccine allowed")
elif age > 30 and comorbidities:
    print("Vaccine allowed")
else:
    print("Vaccine not allowed")