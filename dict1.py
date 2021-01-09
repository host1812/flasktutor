my_d = {"isupper": False, "islower": True}

print(my_d.get("islower"))

my_d["islower"] = False

print(my_d.get("islower"))

if any(my_d.values()):
    print("it have it!")
