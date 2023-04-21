l_no = int(input())
a = ""
for i in range(l_no):
    a+=input()+" "

l= a.split()
lnew = []
for i in l:
    if i.lower() in lnew:
        continue
    else:
        if i[0].isupper():
            b = i.lower()
            lnew.append(b)
        else:    
            lnew.append(i)
lnew.sort()

print(len(lnew))
for j in lnew:
    print(j)
