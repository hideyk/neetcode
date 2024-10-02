import unittest
import main

class TestContainsDuplicate(unittest.TestCase):
    def test_contains_duplicate(self):
        solution = main.Solution()
        testCases = [
            [[1,2,3,4], False],
            [[1,2,3,3], True]

        ]
        for test in testCases:
            arr, res = test[0], test[1]
            self.assertEqual(solution.hasDuplicate(arr), res, msg=f"Array: {arr}, Res: {res}")

if __name__ == '__main__':
    unittest.main()