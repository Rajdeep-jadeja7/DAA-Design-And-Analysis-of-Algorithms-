class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        separateddigits=[]
        temp=0
        for i in nums:
            temp=i
            if temp<10:
                separateddigits.append(temp)
            else:
                temp=str(temp)
                for i in temp:
                    separateddigits.append(int(i))
        return separateddigits                



        