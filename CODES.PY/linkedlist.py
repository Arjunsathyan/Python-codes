class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
                         # print('assigning values to node')


class Linkedlist():
   
    def __intit__(self):
        self.head=None
                        #  print('Empty list')
    

    def displist(self):
                        # print('starting the list')
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next




if __name__=="__main__":

    print('is main function working')
    llist=Linkedlist()
    llist.head=Node(1)
    n2=Node(2)
    n3=Node(3)
    llist.head.next=n2
    n2.next=n3
    llist. displist()
