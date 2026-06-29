"""
Problem Name: Hand of Straights
Difficulty: Medium
Tags: Array, Hash Table, Greedy, Sorting
"""

"""
Submission 1
Language: python3
Runtime: 119 ms
Memory: 21 MB
"""
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()
        hmap = {}
        for i in range(len(hand)):
            num = hand[i]
            if num not in hmap:
                hmap[num] = []
            hmap[num].append(i)
        print(hmap)
        print(hand)
        for i in range(len(hand)):
            num = hand[i]

            if num == -1: # If index has already been used
                continue
            print(f"Num = {num}")
            for j in range(num, num + groupSize):
                print(f"{j} found in hmap")
                if j not in hmap: # if consecutive num not in hmap
                    return False
                temp = hmap[j].pop(0) # Get index of number from hmap
                print(f"{temp} popped from hmap")
                hand[temp] = -1 # Setting index as used
                
                if len(hmap[j]) == 0: # If no more occurences, delete from hmap
                    del hmap[j]
            print("--")
        return True

"""
Submission 2
Language: python3
Runtime: 29 ms
Memory: 21.2 MB
"""
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        card_count = Counter(hand)

        for card in hand:
            start_card = card
            # Find start of potential straight
            while card_count[start_card - 1]:
                start_card -= 1
            
            # Process sequence starting from start_card
            while start_card <= card:
                while card_count[start_card]:
                    for next_card in range(start_card, start_card + groupSize):
                        if not card_count[next_card]:
                            return False
                        card_count[next_card] -= 1
                start_card += 1
        
        return True

