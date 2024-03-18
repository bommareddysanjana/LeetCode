from collections import defaultdict
class Solution(object):
    def findRelativeRanks(self, score):
        d = defaultdict(int)
        n = len(score)
        a = [" "] * n
        place = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        for i in range(n):
            d[score[i]] = i

        score.sort(reverse = True)

        for i in range(n):
            if i < 3:
                a[d[score[i]]] = place[i]
            else:
                a[d[score[i]]] = str(i+1)
        return a
