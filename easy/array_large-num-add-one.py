class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lastDigit = digits[-1] + 1
        carry = lastDigit // 10
        digits[-1] = lastDigit % 10
        for i in range(len(digits) - 2, -1, -1):
            if carry:
                newSum = digits[i] + carry
                digits[i] = newSum % 10
                carry = newSum // 10
            else:
                break

        if carry:
            return [1] + digits
        return digits
