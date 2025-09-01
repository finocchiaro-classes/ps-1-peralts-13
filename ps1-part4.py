prior_arrests = int(input("Prior arrests: "))

local_ordinance = input("Prior arrests for local ordinance (Y/N): ")

release_age = int(input("Age at release: "))

i = 0


if prior_arrests >= 2:
    i += 1
#Additional point to recividism score if user has more than 5 priors
    if prior_arrests >= 5:
        i += 1
if local_ordinance == 'Y':
    i += 1

if release_age >= 18 and release_age <= 24:
    i += 1
elif release_age >= 40:
    i -= 1

print(f"The recidivism risk score is {i}")
