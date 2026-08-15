class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection=[]
        """
        for i in range (len(nums1)):
            for j in range(len(nums2)):
                if(nums1[i]==nums2[j]):
                    intersection.append(nums1[i])
                    break 
        return intersection  
        """

        if(len(nums1)<len(nums2)):
            for i in nums1:
                if i in nums2:
                    intersection.append(i)
                    nums2.remove(i)

        else:
             for j in nums2:
                if j in nums1:
                   intersection.append(j) 
                   nums1.remove(j)
        return intersection                    

             