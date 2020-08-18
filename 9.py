def linearSearch(L, item):
    for i in range(len(L)):
        if L[i]==item:
            return i
    return False
            
def binarySearch(L, item):
    L.sort()

    print "Sorted List: ",L
    beg = 0
    last = len(AR)-1
    while (beg<=last):
        mid = (beg+last)/2
        if item == L[mid]:
            return mid
        elif item > AR[mid]:
            beg = mid + 1
        else:
            last = mid - 1
    else:
        return False

def menu(AR, item):
    a = int(raw_input("1. Linear Search\n2. Binary Search\n--> "))
    if a==1:
        res=linearSearch(AR, item)
        if res == False:
            print "Item not in List"
        else:
            print "Item at position {} in List".format(res)
    elif a==2:
        res=binarySearch(AR, item)
        if res == False:
            print "Item not in List"
        else:
            print "Item at position {} in Sorted List".format(res)
    else:
        print "Try again"
        menu(AR, item)
    
AR=[]
while True:
    l=raw_input("Enter element to be added, press blank enter when done: ")
    if l=="":
        break
    AR.append(int(l))
print "Your entered list is: ",AR
item = int(raw_input("Enter the element to be Searched for: "))

menu(AR, item)
