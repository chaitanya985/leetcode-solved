class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:

            return False

        count=Counter(hand)

        for card in sorted(count):

            while count[card] > 0:

                for i in range(groupSize):

                    if count[card+i] <= 0:

                        return False

                    count[card+i]-=1

        return True
        