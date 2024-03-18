class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        res,i,j = 0,0,0
        players.sort()
        trainers.sort()
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                res += 1
                i += 1
            j += 1
        return res
