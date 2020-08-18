AR = []
def shift(AR, pos):
    AR.append(None)
    i = len(AR)-1
    while i >= pos:
        AR[i] = AR[i-1]
        i=i-1
    return AR

def insert(AR, item):
    for i in range(0,len(AR)-1):
        if AR[i] <= item and item < AR[i+1]:
            pos = i+1
    A = shift(AR,pos)
    A[pos] = ITEM
    print A

def delete(AR, item):
    pos = AR.index(item)
    del AR[pos]
    print AR

def menu(AR, ITEM):
    a = int(raw_input('1. Insertion in a sorted list \n2. Deletion of an element from a list\n--> '))
    if a == 1:
        insert(AR, ITEM)
    elif a == 2:
        if ITEM in AR:
            delete(AR, ITEM)
        else:
            print "Item not found!!!"
    else:
        print "Try again"
        menu(AR, ITEM)
        
while True:
    l=raw_input("Enter element to be added, press blank enter when done: ")
    if l=="":
        break
    AR.append(int(l))
print "Your entered list is: ",AR
AR.sort()
print "Sorted List: ",AR
ITEM = int(raw_input("Enter element to be inserted or deleted: "))

menu(AR, ITEM)
