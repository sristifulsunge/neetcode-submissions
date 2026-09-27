class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        for num in nums:
            elements[num] = 1 + elements.get(num,0)

        arr = []
        for num,count in elements.items():
            arr.append([count,num])
        arr.sort()
        arr.reverse()

        res = []
        for i in range(k):
            res.append(arr[i][1])
        
        return res
    

                
        
        