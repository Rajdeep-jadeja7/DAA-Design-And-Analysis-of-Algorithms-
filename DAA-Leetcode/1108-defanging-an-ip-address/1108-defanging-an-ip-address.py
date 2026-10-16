class Solution:
    def defangIPaddr(self, address: str) -> str:

        defanged=""
        for i in address:
            if i !=".":
                defanged+=i
            else:
                defanged+="[.]"
        return defanged            
        