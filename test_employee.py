import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        print("setup")
        self.emp_1 = Employee('azharul', 'mulla', 50000)
        self.emp_2 = Employee('suvro', 'mulla', 60000)

    def tearDown(self):
        print("tearDown\n")    

    def test_email(self):
        print("test_email")
        emp_1 = Employee('azharul', 'mulla', 50000)
        emp_2 = Employee('suvro', 'mulla', 60000)

        self.assertEqual(emp_1.email, 'azharul.mulla@email.com')
        self.assertEqual(emp_2.email, 'suvro.mulla@email.com')

        emp_1.first = 'Programmer'
        emp_2.first = 'Odoo'

        self.assertEqual(emp_1.email, 'Programmer.mulla@email.com')
        self.assertEqual(emp_2.email, 'Odoo.mulla@email.com')

    def test_fullname(self):
        print("test_fullname")
        emp_1 = Employee('azharul', 'mulla', 50000)
        emp_2 = Employee('suvro', 'mulla', 60000)

        self.assertEqual(emp_1.fullname, 'azharul mulla')
        self.assertEqual(emp_2.fullname, 'suvro mulla')
        emp_1.first = 'Programmer'
        emp_2.first = 'Odoo'
        self.assertEqual(emp_1.fullname, 'Programmer mulla')
        self.assertEqual(emp_2.fullname, 'Odoo mulla')                           

    def test_apply_raise(self):
        print("test_pay")
        emp_1 = Employee('azharul', 'mulla', 50000)
        emp_2 = Employee('suvro', 'mulla', 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)                
                                    

if __name__ == '__main__':
    unittest.main()                


            