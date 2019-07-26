class Node:
    """
    Instance of node, implelements a singly linked list.
    """
    def __init__(self,element):
        self.element= element
        self.next= None
    """
    Contains value & points to the next node of linked list
    
    Args:
        self, element: self is the instance of the class, element is 
    
    Returns:
        Next Node
    """

    class Stack:
        """
        Implements stack using linked lists
        """
      
        def __init__(self):
            self.head = None

        
        def is_empty(self, size):
            """
            Checks if  a stack is empty
            
            Args:
                size: items in stack if it is not empty
            
            Returns:
                [Boolean]: True if stack is empty else False

            Runtime:
                 Time complexity: O(1) 
                 Name : Constant
            """
            return self.size == 0


        def push(self,element):
            """
            Adds a new value to the stack
            
            Args:
                element: to be added to the stack

            Runtime:
                 Time complexity: O(1) 
                 Name : Constant
            """

            if self.head = None :
                self.head = Node(element)
            else:
                new_node = Node(element)
                new_node.next = self.head
                self.head = new_node

         def peek(self, element):
             """
            [Retrieves but does not remove values from the stack]
             
            Args:
                 element ([int/str]): element is viewed 
                
            Raise:
            Exception : 'Stack is empty' , if the stack is empty.

            Runtime:
                 Time complexity: O(1) 
                 Name : Constant
             """
        if self.is_empty:
            raise Exception("Empty stack")
        else:
            return self.head.element

        def pop(self):
            """
            [Retrieves and removes values from stack]

            Args:
                 element ([int/str]): element is removed
            
            Runtime:
                 Time complexity: O(1) 
                 Name : Constant
            """

            if self.head = None:
                return None
            else:
                popped = self.head.element
                self.head = self.head.next
                return popped

lstack = Stack()
while True:
    """
    [Prompt for operation to be done]
    """
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    """
    [Conditional statement that determines type of operation to be carried out]
    """
    if operation == 'push':
        lstack.push(int(do[1]))
    elif operation == 'pop':
        popped = lstack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
        break


