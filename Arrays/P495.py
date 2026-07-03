class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        # seconds = []
        # for i in range (len(timeSeries)):
        #     for j in range(timeSeries[i] , (timeSeries[i]+duration)):
        #         seconds.append(j)
        # return len(set(seconds))
        
        total = 0
        for i in range(len(timeSeries)-1):
            gap = timeSeries[i+1] - timeSeries[i]
            if gap>=duration:
                total+=duration
            else:
                total+=gap

        return total+duration