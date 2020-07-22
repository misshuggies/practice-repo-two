import unittest
from name_function import formatted_name

class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        result = formatted_name("harry", "potter")
        self.assertEqual(result, "Harry Potter")

    def test_first_middle_last_name(self):
        result = formatted_name("albus", "potter", "severus")
        self.assertEqual(result, "Albus Severus Potter")

    
    def test_other_first_last_name(self):
        result = formatted_name("hermione", "granger")
        self.assertEqual(result, "Hermione Granger")
 
if __name__ == '__main__':
   unittest.main()