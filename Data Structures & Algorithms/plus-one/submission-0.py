class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = 1
        for i in range(len(digits)):
            val = digits[i] + carry
            digit = val % 10
            carry = val // 10
            digits[i] = digit
        if carry:
            digits.append(carry)
        
        digits.reverse()
        return digits
        