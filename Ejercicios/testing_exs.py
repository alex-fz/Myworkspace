from password import validate_password
import unittest

class TestPassword(unittest.TestCase):
    def test_valid(self):
        '''Check if its equal, test passed'''
        expected = True
        password = 'asd+sd+ad+wer'
        self.assertEqual(validate_password(password), expected)
    
    def test_invalid(self):
        '''Check if we pass ain icorrect password, muste be False'''
        extpected = False
        password = 'novalidoaa'
        self.assertEqual(validate_password(password), extpected)


if __name__ == '__main__':
    unittest.main()