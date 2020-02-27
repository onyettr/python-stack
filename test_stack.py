import unittest
from pystack import pystack

class TestStack(unittest.TestCase):
    """
        unit test harness for the stack 
    """
    def test_push_pop(self):
        """
            Test basic push and pop operations
        """
        Stack1 = pystack()

        Stack1.push(10)
        self.assertTrue(Stack1.pop() == 10)

    def test_overflow(self):
        """
            Test overvlow of stack by pushing too many items
        """
        Stack2 = pystack(1)

        try:
            Stack2.push(10)
            Stack2.push(11)
        except ValueError:
            pass
        else:
            self.fail('test_overflow - didnt see exception error')

    def test_underflow(self):
        """
            Pop from stack that is empty
        """

        Stack3 = pystack(1)
        try:
            Stack3.pop()
        except:
            pass
        else:
            self.fail('test_underflow - didnt see exception error')

    def test_size(self):
        """
            Add items and test the size of the stack
        """
        Stack = pystack(5)
        Stack.push(100)
        Stack.push(101)
        Stack.push(102)

        self.assertTrue(Stack.size() == 3)

    def test_peek(self):
        """
            test the stack peek operation
        """
        Stack = pystack(5)

        try:
            Stack.peek()
        except:
            pass
        else:
            self.fail('test_peek - didnt seen an expcetion')
        
        Stack.push(200)
        Stack.push(201)
        Stack.push(202)

        self.assertTrue(Stack.peek() == 202)
        self.assertTrue(Stack.size() == 3)

    def test_isFull(self):
        """
            test ths isFull API 
        """
        Stack = pystack(2)
        Stack.push(300)

        self.assertFalse(Stack.isFull())

    def test_isEmpty(self):
        """
            test ths isEmpty API
        """
        Stack = pystack(2)

        self.assertTrue(Stack.isEmpty())
        
        
if __name__ == '__main__':
    unittest.main()
        
