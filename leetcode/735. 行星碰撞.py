class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        while 1:
            for i in range(len(asteroids)-1):
                if asteroids[i] > 0 and asteroids[i+1] < 0:
                    a1 = asteroids[i]
                    a2 = abs(asteroids[i+1])
                    if a1 == a2:
                        asteroids.pop(i)
                        asteroids.pop(i)
                    elif a1 > a2:
                        asteroids.pop(i+1)
                    else:
                        asteroids.pop(i)
                    break
            else:
                break
        print(asteroids)
        return asteroids



asteroids = [10,2,-5]
ss = Solution()
ss.asteroidCollision(asteroids)