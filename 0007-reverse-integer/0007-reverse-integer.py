class Solution:
    def reverse(self, x: int) -> int:
        
        sign = 1 if x >= 0 else -1
        
        abs_x = abs(x)
        
        reversed_str = str(abs_x)[::-1]
        reversed_int = int(reversed_str) * sign
        
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
            
        return reversed_int      