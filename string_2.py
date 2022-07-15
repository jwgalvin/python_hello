     #     01234567890123
     #    -432109876543210            
parrot = "Norwegian Blue"
# print(parrot)
# print(parrot[3])
# print(parrot[4]) # print(parrot[13])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])
# print(parrot[9])
# print(parrot[-11]) #print(3 -14)
# print(parrot[-1])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])

# print(parrot[0:6])  # slice out up to locations six up to but not including index 6

# print(parrot[3:5])
# print(parrot[:8])#start defaults to index 0 and isn't needed.
# print(parrot[10:14])
# print(parrot[10:])#starts at designated location and carries to end of string
# print(parrot[:]) #runs entire thing

# print(parrot[-4:-2])
# print(parrot[-4:12])# these are the same ^

print(parrot[0:6:2]) #Nre  moves in steps of 2
print(parrot[0:6:3]) #Nw   moves in steps of 3

# python has 5 sequence tyoes built in. String, list, tuple, range and bytes & bytearray
#ranges cannot be concantenated
