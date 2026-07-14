class Solution:
    def isHappy(self, n: int) -> bool:
            j=0
            while j<100 :
                    j+=1
                    s=0
                    for i in str(n):
                        s+=(int(i))**2
                    n=s
                    if n == 1:
                        return True
            return False
