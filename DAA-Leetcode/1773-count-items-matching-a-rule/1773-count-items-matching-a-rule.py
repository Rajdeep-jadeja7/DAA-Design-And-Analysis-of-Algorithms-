class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        
        itemscount=0
        temp=0
        
        for i in items:
            temp=i
        
            if ruleKey=="type":
                type1=i[0]
                if type1==ruleValue:
                    itemscount+=1

            elif ruleKey=="color":
                color1=i[1]
                if color1==ruleValue:
                    itemscount+=1
            else:
                name1=i[2]
                if name1==ruleValue:
                    itemscount+=1
        return itemscount            

