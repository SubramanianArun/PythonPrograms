import unittest
import ShortestPalindromicBase

class TestShortestPalindome(unittest.TestCase):

    def test_base(self):
        self.assertEqual(ShortestPalindromicBase.base(26,5),{0:1,1:0,2:1})
        self.assertEqual(ShortestPalindromicBase.base(19,18),{0:1,1:1})
        self.assertEqual(ShortestPalindromicBase.base(49,7),{0:0,1:0,2:1})
        self.assertEqual(ShortestPalindromicBase.base(42,33),{0:9,1:1})
        self.assertEqual(ShortestPalindromicBase.base(26,0), None)
        self.assertEqual(ShortestPalindromicBase.base(31,1), None)
        self.assertEqual(ShortestPalindromicBase.base(-45,1), None)
        self.assertEqual(ShortestPalindromicBase.base(-2, -11), None)
        self.assertEqual(ShortestPalindromicBase.base(4.5, 3), None)
        self.assertEqual(ShortestPalindromicBase.base(5, 3.4), None)

    def test_palindrome(self):
        self.assertEqual(ShortestPalindromicBase.palindrome({0:'1',1:'0',2:'1'}), None)
        self.assertEqual(ShortestPalindromicBase.palindrome('101'), None)
        self.assertEqual(ShortestPalindromicBase.palindrome('abba'), None)
        self.assertEqual(ShortestPalindromicBase.palindrome(1221), True)
        self.assertEqual(ShortestPalindromicBase.palindrome(None), None)
        self.assertEqual(ShortestPalindromicBase.palindrome(False), None)
        self.assertEqual(ShortestPalindromicBase.palindrome(14.41), None)
        
    def test_validate_input(self):
        self.assertEqual(ShortestPalindromicBase.validate_input(None), None)
        self.assertEqual(ShortestPalindromicBase.validate_input('None'), None)
        self.assertEqual(ShortestPalindromicBase.validate_input('adsde'), None)
        self.assertEqual(ShortestPalindromicBase.validate_input({0:'1',1:'0',2:'1'}), None)
        self.assertEqual(ShortestPalindromicBase.validate_input({0:1,1:1}),{0:1,1:1})
        self.assertEqual(ShortestPalindromicBase.validate_input(121), [1,2,1])
        self.assertEqual(ShortestPalindromicBase.validate_input(True), None)
        self.assertEqual(ShortestPalindromicBase.validate_input(124.324), None)

if __name__ == '__main__' :
    unittest.main()
