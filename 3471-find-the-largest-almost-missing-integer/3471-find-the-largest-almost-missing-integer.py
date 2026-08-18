class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        maximum=0
        digits={}
        once=[]  #numbers which occur only once 
        
        if k==1:
            for i in nums:
                if i in digits:
                    digits[i]+=1
                else:
                    digits[i]=1
            if (len(digits)==1):
                return -1
            else:    
                for k,v in digits.items():
                    if v==1:
                        once.append(k)   
                return (max(once)) 
        elif (nums[0]==nums[-1] and k!=len(nums)):
                return -1         
        elif k==len(nums):
            return max(nums)  
        else:
            first_digit=0
            last_digit = 0
            for i in nums:
                if  (i == nums[0]):
                    first_digit+=1

                elif(i == nums[-1]):
                    last_digit+=1
                   
            if (last_digit ==1 and first_digit==1):
                return max(nums[0],nums[-1])  
            elif (last_digit>1 and first_digit>1):
                return -1
            else:
                if (first_digit==1):
                    return nums[0]
                else:
                    return nums[-1]                  





                
                
