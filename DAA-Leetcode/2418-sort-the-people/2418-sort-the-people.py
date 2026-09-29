class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:

        fusedarray=sorted(zip(names,heights),key=lambda x:x[1],reverse=True)
        sortedpeople=[]
        for i in fusedarray:
            sortedpeople.append(i[0])

        return sortedpeople

        