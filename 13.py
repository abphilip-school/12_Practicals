def isempty(stk):
    if stk == []:
        return True
    else:
        return False

def push(stk,item):
    stk.append(item)
def pop(stk):
    if isempty(stk):
        return "Underflow"
    else:
        top = len(stk)-1
        item = stk[top]
        del stk[top]
        return item
    
def peek(stk):
    if isempty(stk):
        return "Underflow"
    else:
        top = len(stk)-1
        return stk[top]

def display(stk):
    if isempty(stk):
        print "Stack empty"
    else:
        top = len(stk)-1
        print stk[top], "<-- Top"
        for a in range(top-1,0,-1):
            print stk[a]
        print stk[0], "<-- Bottom"
    pause = raw_input("Press Enter to Continue: ")

stk = []
top = None
while True:
    print '''Stack Operations
1. Push
2. Pop
3. Peek
4. Display
5. Exit '''
    ch = int(raw_input("Enter your choice: "))
    if ch==1:
        item = int(raw_input("Enter Item: "))
        push(stk,item)
    elif ch==2:
        item = pop(stk)
        if item == 'UnderFlow':
            print "UnderFlow"
        else:
            print "Item: ",item
        pause = raw_input("Press Enter to Continue:\n")

    elif ch==3:
        item = peek(stk)
        if item == "Underflow":
            print "Underflow"
        else:
            print "Top most item is: ",item
        pause = raw_input("Press Enter to Continue:\n")
    elif ch==4:
        display(stk)
    elif ch==5:
        break
    else:
        print "Invalid Choice"
