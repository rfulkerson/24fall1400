def greet(name, msg = "good morning!"):
    print(f"Hello, {name}, {msg}")
    
greet(msg = "how are you?", name = "Siobhán")
greet(name = "Siobhán", msg = "how are you?")
greet("Siobhán", "how are you?")
greet("Siobhán")

