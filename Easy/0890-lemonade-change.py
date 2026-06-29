"""
Problem Name: Lemonade Change
Difficulty: Easy
Tags: Array, Greedy
"""

"""
Submission 1
Language: python3
Runtime: 9 ms
Memory: 23.4 MB
"""
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_collection = {}  # {Bill : frequency}
        cost = 5

        def changeAvailable(rem) -> bool:
            if rem == 5:
                if 5 in bill_collection and bill_collection[5] != 0:
                    bill_collection[5] -= 1
                    return True
            if rem == 15:
                if 10 in bill_collection and bill_collection[10] >= 1 and 5 in bill_collection and bill_collection[5] >= 1:
                    bill_collection[10] -= 1
                    bill_collection[5] -= 1
                    return True
                elif 5 in bill_collection and bill_collection[5] >= 3:
                    bill_collection[5] -= 3
                    return True
            
            return False

        for bill in bills:
            bill_collection[bill] = bill_collection.get(bill, 0) + 1 
            rem = bill - cost
            if not rem:
                continue
            
            if not changeAvailable(rem):
                return False

        return True

