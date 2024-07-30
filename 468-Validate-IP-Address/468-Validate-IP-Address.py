class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        # Check if the IP address contains a dot (IPv4)
        if "." in queryIP:
            list_IP = queryIP.split(".")
            
            # IPv4 must have exactly 4 parts
            if len(list_IP) != 4:
                return "Neither"
            
            for address in list_IP:
                # Check if the part is numeric and has no leading zeros
                if not (address.isdigit() and 0 <= int(address) <= 255):
                    return "Neither"
                # Check if there are leading zeros (except for "0")
                if len(address) > 1 and address[0] == '0':
                    return "Neither"
            
            return "IPv4"
        
        # Check if the IP address contains a colon (IPv6)
        elif ":" in queryIP:
            list_IP = queryIP.split(":")
            hex_pattern = re.compile(r'^[0-9a-fA-F]{1,4}$')
            
            # IPv6 must have exactly 8 parts
            if len(list_IP) != 8:
                return "Neither"
            
            for address in list_IP:
                # Each part must be a valid hexadecimal number between 1 and 4 characters long
                if not hex_pattern.match(address):
                    return "Neither"
            
            return "IPv6"
        
        # If it is neither IPv4 nor IPv6
        return "Neither"