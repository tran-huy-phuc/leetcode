class Solution:
    def isHappy(self, n: int) -> bool:
        seen_numbers = set()
        current_number = n
    
        while current_number != 1:
            current_number = self.sum_of_digits_squares(current_number) 
            if current_number in seen_numbers:
                return False
        
            seen_numbers.add(current_number)
        
        
        return True

    def sum_of_digits_squares(self, n: int) -> int:
        s = 0
        while n > 0:
            remaining = n % 10
            s += remaining ** 2
            n = n // 10
        return s