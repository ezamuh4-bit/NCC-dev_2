class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in digits:  
            s = s + str(i)
        
        s = int(s) + 1  
        s = str(s) 
        f = []
        
        for i in s:
            f.append(int(i))  
        return f
