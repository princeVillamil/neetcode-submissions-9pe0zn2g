class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        fed = 0
        print(s,g)
        for i in range(len(s)):
            if len(g)<=fed: return fed
            print(s[i], g[fed],"----")
            if s[i] >= g[fed]:
                # print("run", s[i], g[fed])
                fed+=1
            i+=1




        return fed