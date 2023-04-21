l1 = [1,2,3,4,5,6,7,8,9]
print("original list:" + str(l1))
rot = input("TYPE 'R' TO ROTATE RIGHT AND 'L' TO ROTATE LEFT: ")
if rot =='L':
     n = int(input("ENTER THE NUMBER OF ROTATIONS:"))
     l1 = l1[n:] + l1[:n]
     print(l1)
else:
     n = int(input("ENTER THE NUMBER OF ROTATIONS: "))
     l1 = l1[-n:] + l1[:-n]
     print(l1)
