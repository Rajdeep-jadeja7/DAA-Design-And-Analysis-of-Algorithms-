class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest=strs[0]
        common=""
        for i in strs:
            if len(i) < len(shortest):
                shortest=i

        for j in range(len(shortest)):
            count=0
            for k in range(len(strs)):
                temp=strs[k]

                if shortest[j]==temp[j]:
                    count+=1
                else:
                    return common
            if count==len(strs):
                common+=shortest[j]
        return common                            
        