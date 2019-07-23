class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if '.' in IP:
            ans = self.validate_ip4(IP)
            return 'IPv4' if ans else 'Neither'
        else:
            ans = self.validate_ip6(IP)
            return 'IPv6' if ans else 'Neither'
        
    
    def validate_ip4(self, IP):
        parts = IP.split('.')
        if len(parts) != 4:
            return False
        
        for part in parts:
            if not part.isnumeric():
                return False
        
            if int(part) > 255 or str(int(part)) != part:
                return False
        
        return True
    
    
    def validate_ip6(self, IP):
        parts = IP.split(':')
        if len(parts) != 8:
            return False
        
        for part in parts:
            if not(1 <= len(part) <= 4):
                return False
            
            for i in part.lower():
                if i not in '0123456789abcdef':
                    return False
        
        return True
