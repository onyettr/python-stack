#!/usr/bin/python
#pylint; ignore invalid-name
"""
   Stack implementation

   - create (includes initial size)
   - pop
   - push
   - delete
   - peek
   - size
   - swap
   - stackPrint
"""

class pystack(object):
    """
        simple class type for a stack
    """
    def __init__(self, max_stack_size=1):
        self.stack = []
        self.stackcount = 0
        self.stacktop = -1
        self.stackmax = max_stack_size

    def size(self):
        """
            Current size of the stack (active elements)
        """
        return self.stackcount

    def isEmpty(self):
        """
            Test if anything is on the stack
        """
        if self.stacktop == -1:
            return True

        return False

    def isFull(self):
        """
            Test if any room left on the stack
        """
        if self.stacktop >= self.stackmax:
            return True

        return False

    def push(self, item):
        """
            push item to stack
        """
        if self.stacktop+1 == self.stackmax:
            print("ERROR - Full stack!")
            return

        self.stacktop = self.stacktop + 1
        self.stackcount = self.stackcount + 1
        self.stack.append(item)

    def pop(self):
        """
            pop top of the stack
        """
        if self.isEmpty():
            print("ERROR- Empty stack!")
            return

        item = self.stack.pop()

        self.stackcount = self.stackcount - 1

        return item

    def peek(self):
        """
            peek the top of the stack
        """
        if self.isEmpty():
            print("ERROR = Stack is empty")
            return

        return self.stack[self.stacktop]

        
    def show(self):
        """
            Show contents of the stack
        """
        if self.isEmpty():
            print("ERROR - stack is empty")
            return

        for item in range(self.stackcount):
            print(str(item) + " " + str(self.stack[item]))

if __name__ == "__main__":
    print("Test01 - create <int> stack")
    stack1 = pystack()

    print("Test01 - size = ", stack1.size())
    print("Test01  pop   = ", stack1.pop())
    stack1.push(10)
    print("Test01 - size = ", stack1.size())
    stack1.show()

    print("Test02 - create <int> stack, size 4")
    stack2 = pystack(4)
    print("Test02 - size = ", stack2.size())
    stack2.push(11)
    stack2.push(12)
    stack2.push(13)
    print("Test02 - size = ", stack2.size())
    print("Test02 - push too many")
    stack2.push(14)
    print("Test02 - size = ", stack2.size())
    stack2.show()

    # <char>  Stack
    print("Test03 - create <char> stack")
    stack3 = pystack(4)
    print("Test03 - size = ", stack1.size())          
    stack3.push('A')
    stack3.push('B')
    stack3.push('C')
    stack3.show()

    # String Stack
    print("Test04 - create <string> stack")
    stack4 = pystack(4)

    stack4.push("Hello")
    stack4.push("there")
    stack4.push("stack4")
    stack4.show()

    print("stack4 peek = ", stack4.peek())
    stack4.show()
    print("stack4 pop  = ", stack4.pop())
    stack4.show()
    print("stack4 pop  = ", stack4.pop())
    stack4.show()

    
