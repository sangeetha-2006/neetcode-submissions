class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time=0
        total=0
        for arrival, prep in customers:
            start=max(time,arrival)
            time=start+prep
            wait =time-arrival
            total+=wait
            avg=total/len(customers)
        return avg
        