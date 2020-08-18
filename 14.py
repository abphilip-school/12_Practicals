def isempty(qu):
    if qu == []:
        return True
    else:
        return False

def enqueue(qu,item):
    qu.append(item)
def dequeue(qu):
    if isempty(qu):
        return "Underflow"
    else:
        item = qu[0]
        del qu[0]
        return item
    
def peek(qu):
    if isempty(qu):
        return "Underflow"
    else:
        return qu[0]

def display(qu):
    if isempty(qu):
        print "Queue empty"
    else:
        top = len(qu)-1
        print qu[0], "<-- First"
        for a in range(1,top):
            print qu[a]
        print qu[top], "<-- Last"
    pause = raw_input("Press Enter to Continue: ")

qu = []
top = None
while True:
    print '''Queue Operations:
1. Enqueue
2. Dequeue
3. Peek
4. Display
5. Exit '''
    ch = int(raw_input("Enter your choice: "))
    if ch==1:
        item = int(raw_input("Enter Item: "))
        enqueue(qu,item)
    elif ch==2:
        item = dequeue(qu)
        if item == 'UnderFlow':
            print "UnderFlow"
        else:
            print "Item: ",item
        pause = raw_input("Press Enter to Continue: \n")

    elif ch==3:
        item = peek(qu)
        if item == "Underflow":
            print "Underflow"
        else:
            print "Top most item is: ",item
        pause = raw_input("Press Enter to Continue: \n")
    elif ch==4:
        display(qu)
    elif ch==5:
        break
    else:
        print "Invalid Choice..."
