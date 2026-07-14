class Solution:
    def reverseVowels(self, s: str) -> str:
        v={"a","o","i","e","u","A","O","E","U","I"}
        s=list(s)
        b=[]
        for i in range(len(s)):
            if s[i] in v:
                b.append(s[i])
                s[i] = '_'
        #return s
        for i in range(len(s)):
            if s[i]=="_":
                s[i]=b[-1]
                b=b[:-1]
        s="".join(s)
        return s
