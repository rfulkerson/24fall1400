names = []
n = input("Enter name: ")
while n != "done":
    names.append(n)
    n = input("Enter name: ")
names.sort(reverse=True)
#names.sort(reverse=False, key=str.upper)
print(names)

# monica
# Chandler
# ross
# Phoebe
# done