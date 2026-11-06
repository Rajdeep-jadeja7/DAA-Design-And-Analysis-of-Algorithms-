class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        newfirsthalf=[]
        newlasthalf=[]
        updated=[]
        newfirsthalf=nums[:n]
        newlasthalf=nums[n:]
        i=0
        for i in range(n):
            updated.append(newfirsthalf[i])
            updated.append(newlasthalf[i])
        return updated 
       
          

         

        