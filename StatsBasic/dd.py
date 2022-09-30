print("Can I form a Triangle?")
def is_traingle(sd1,sd2,sd3):
    if((sd1+sd2>sd3)and(sd1+sd3>sd2)and(sd2+sd3>sd1)):
        print(f"You can form the triangle with sides : {sd1},{sd2},{sd3}")
    else:
        print(f"You cannont form the triangle with sides : {sd1},{sd2},{sd3}")

def input_sides():
    sides=[]
    for i in range(0,3):
        sides.append(int(input(f"Enter {i+1} side of triangle : ")))
        
    #function_call
    is_traingle(sides[0],sides[1],sides[2])    

input_sides()