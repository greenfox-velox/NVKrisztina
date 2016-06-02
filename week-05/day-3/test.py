import unittest
from gyak5 import use
from gyak5 import text_open
from gyak5 import list_print
from gyak5 import list_append
from gyak5 import list_remove
from gyak5 import list_ignore

class Test(unittest.TestCase):
    def list_print(self):
        self.assertEqual(list_print('todo.py -a', 'Unable to add: No task is provided'))

    def list_remove(self):
        self.assertEqual(list_remove('todo.py -r', 'Unable to remove: No index is provided'))

if __name__ == '__main__':
    unittest.main()
