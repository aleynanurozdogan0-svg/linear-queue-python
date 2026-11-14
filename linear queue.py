def create():
    Q=[]
    front=0
    rear=-1
    size=int(input("enter the size of the queue: "))
    print("empty queue is created.")
    return Q,rear,front,size
 
def isFull(rear,front,size):
    if(rear>=size-1):
        return True
    else:
        return False
   
def isEmpty(front,rear):
    if(front>rear or rear==-1):
        front=0
        rear>=-1
        return True
    else:
        return False
   
def enqueue(Q,rear,front,size):
    if(isFull(rear,front,size)==True):
        print("Overflow queue is full!!!")
        return Q,rear
    item=int(input("enterr the number to push onto the Queue: "))
    rear+=1
    Q.insert(rear,item)
    return Q,rear
 
def dequeue(Q,rear,front,size):
    if(isEmpty(front,rear)==True):
        front=0
        rear=-1
        print("underflow: there is no element in the Queue")
        return Q,front+1,rear
    else:
        print("the element to pop is ", Q[0])
        return Q,front+1,rear
   
def display(Q,front,rear,size):
    print("front is at index ->",front)
    print("rear is at index ->",rear)
    if(isEmpty(front,rear)==True):
        print("\n Queue is empty...")
    elif(isFull(rear,front,size)==True):
        print("The elements in the queue is:")
        for i in range(front,rear+1):
            print(i,"->",Q[i])
        print("Queue is full...")
    else:
        print("The elements in the queue is:")
        for i in range(front,rear+1):
            print(i,"->",Q[i])
 
 
def menu():
    print("\n----menu----")
    print("1.insert to queue")
    print("2.delete from queue")
    print("3.display the queue")
    print("4.exit")
    opt=int(input("enter a valid menu item: "))
    return opt
 
Q,rear,front,size=create()
i=1
while(i>0 and i<=3):
    i=menu()
    if i==1:
        Q,rear=enqueue(Q,rear,front,size)
        display(Q,front,rear,size)
    if i==2:
        Q,front,rear=dequeue(Q,rear,front,size)
        display(Q,front,rear,size)
    if i==3:
        display(Q,front,rear,size)
    else:
        print("...exit...")