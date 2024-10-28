def a_function():
    return "fubar"

for a in range(4):
    a_function()
    
if a_function() == "foo":
    print("they're equal!")
    
print(len(a_function()))


    
    
#     x = a_function()
#     print("variable",x)
#     
#     print("function call", a_function())
#     
#     if a_function() == "foo":
#         print("came back with foo")
#     else:
#         print("didn't come back with foo")
#         
