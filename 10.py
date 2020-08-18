def selectionSort(L):
    for i in range(len(L)):
        min = i
        for j in range(i+1,len(L)):
            if L[j] < L[min]:
                min = j
        t=L[i]
        L[i]=L[min]
        L[min]=t
    print L
    
def bubbleSort(L):
    for a in range(len(L)):
        i = 0
        while i<(len(L)-1):
            if L[i]>L[i+1]:
                t=L[i]
                L[i]=L[i+1]
                L[i+1]=t
            i+=1
    print L
    
def insertionSort(L):
    for i in range(len(L)):
        v=L[i]
        j=i
        while L[j-1]>v and j>=1:
            L[j] = L[j-1]
            j-=1
        L[j]=v   
    print L
    
def menu(List):
    a = int(raw_input('1. Selection \n2. Bubble \n3. Insertion\n--> '))
    if a == 1:
        selectionSort(List)
    elif a == 2:
        bubbleSort(List)
    elif a == 3:
        insertionSort(List)
    else:
        print "Try again"
        menu(List)
AR=[]     
while True:
    l=raw_input("Enter element to be added, press blank enter when done: ")
    if l=="":
        break
    AR.append(int(l))
print "Your entered list is: ",AR
menu(AR)
