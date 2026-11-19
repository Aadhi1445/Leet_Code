class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def calculate_days(capacity):
            total = 0
            count = 1
            for weight in weights:
                if total + weight <= capacity:
                    total += weight
                else:
                    count += 1
                    total = weight
            return count
        start = max(weights)
        end = sum(weights)
        while start <= end:
            mid = (start + end) // 2
            required_days = calculate_days(mid)
            if required_days <= days:
                end = mid - 1
            else:
                start = mid + 1
        return start
        
        # count=0
        # total=0
        # maxium=max(weights)
        # for i in weights:
        #     if total+i<= maxium:
        #         total+=i
        #     else:
        #         count+=1
        #         total=i
        # return count
        