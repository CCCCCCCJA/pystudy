class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        tag = -1
        cap = capacity
        step = 0
        while tag != len(plants)-1:
            if plants[tag+1] <= cap:
                tag += 1
                cap = cap - plants[tag]
                step += 1
            else:
                step = step + (tag+1) * 2
                cap = capacity
        print(step)
        return step

plants = [1,1,1,4,2,3]
capacity = 4
ss = Solution()
ss.wateringPlants(plants, capacity)
