import random

def generate():
    values = []
    for a in range(5):
        v = random.randint(1,3)
        values.append(v)

generate()
x = generate()
print(x)
print(generate())
# 