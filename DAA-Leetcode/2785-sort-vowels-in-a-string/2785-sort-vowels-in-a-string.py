class Solution:
    def sortVowels(self, s: str) -> str:
        vowels=[]
        j=0
        for i in s:
            if i in "aeiouAEIOU":
                vowels.append(i)
        vowels.sort()
        t=list(s)
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                t[i]=vowels[j]
                j+=1
        return ("".join(t))        

        """
        index=[]
        t=""
        freq={}
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                if s[i] in freq:
                    freq[s[i]]+=1
                else:
                    freq[s[i]]=1
                index.append(i)


        sorted_freq=dict(sorted(freq.items(),key=lambda x:x[0]))
        for i in range(len(s)):
            if i not in index:
                t+=s[i]
            else:
                for k,v in sorted_freq.items():
                    if  v>0:
                        t+=k
                        sorted_freq[k]-=1
                        break

        return t
        """
        """
        vowels=[]
        index=[]
        t=""
        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                #if s[i] not in vowels:
                vowels.append(s[i])
                index.append(i)
        vowels.sort() 
        """
        """
        j=0
        for i in range(len(s)):
            if i not in index:
                t+=s[i]
            else:
                t+=vowels[j]   
                j+=1 

        return t    
        """
        freq={}
        for i in vowels:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in range(len(s)):
            if i not in index:
                t+=s[i]
            else:
                for k,v in freq.items():
                    if  v>0:
                        t+=k
                        freq[k]-=1
                        break
        return t                


        