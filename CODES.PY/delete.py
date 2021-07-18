from typing import Any


class Node:
    def __init__(self, item: Any, next: Any) -> None:
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def add(self, item: Any) -> None:
        self.head = Node(item, self.head)
        self.size += 1

    def remove(self) -> Any:
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            self.size -= 1
            return item

    def is_empty(self) -> bool:
        return self.head is None

    def __str__(self) -> str:
        
         linked_list = LinkedList()
         linked_list.add(23)
         linked_list.add(14)
         linked_list.add(9)
         print(linked_list)
        
    
         if not self.is_empty:
            return ""
         else:
            iterate = self.head
            item_str = ""
            item_list = []
            while iterate:
                item_list.append(str(iterate.item))
                iterate = iterate.next

            item_str = " --> ".join(item_list)

            return item_str

    def __len__(self) -> int:
    
         linked_list = LinkedList()
         len(linked_list)
        
         linked_list.add("a")
         len(linked_list)
        
         linked_list.add("b")
         len(linked_list)
        
         return self.size
