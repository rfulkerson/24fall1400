stuff = input()
stuff = stuff.split(",")
coll = []

for a in stuff:
  if a.strip().isdecimal():
    coll.append(int(a.strip()))

print(coll)
print(sum(coll))