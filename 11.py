AR=[]
while True:
    l=raw_input("Enter element to be added, press blank enter when done: ")
    if l=="":
        break
    AR.append(int(l))
print "Your entered list is: ",AR   

while True:
    a = int(raw_input('1. Insertion\n2. Delete\n3. Display\n4. Exit\n--> '))
    if a == 1:
        AR.append(int(raw_input('Element to insert: ')))
    elif a == 2:
        s = int(raw_input('Element to delete: '))
        if s in AR:
            AR.remove(s)
        else:
            print "Element {} is not in the list".format(s)
    elif a == 3:
        print AR
    elif a == 4:
        break
    else:
        print "Try Again..."



