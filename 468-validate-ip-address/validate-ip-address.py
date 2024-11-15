class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        if all(x.isdigit() and 0 <= int(x) <= 255 and str(int(x)) == x for x in queryIP.split('.')) and len(queryIP.split('.')) == 4:
            
            return "IPv4"
        
        if all(0 < len(x) <= 4 and all(c in '0123456789abcdefABCDEF' for c in x) for x in queryIP.split(':')) and len(queryIP.split(':')) == 8:
            
            return "IPv6"
        
        return "Neither"




        