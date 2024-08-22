
from PiBot import MoveInstruction

while 1:
    
    dir, dist = input("Which direciton? "), input("How far? ")
    coord = MoveInstruction(dir, dist)
    
    print("Direction: ",dir)
    print("Distance: ", dist)
