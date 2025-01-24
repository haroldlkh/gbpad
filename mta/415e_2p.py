class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1  # Start from the end of both strings
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0  # Get digit from num1 or 0 if out of bounds
            digit2 = int(num2[j]) if j >= 0 else 0  # Get digit from num2 or 0 if out of bounds

            # Compute the sum of digits and the carry
            total = digit1 + digit2 + carry
            carry = total // 10  # Carry for the next step
            result.append(str(total % 10))  # Append the current digit to result

            # Move to the next digits
            i -= 1
            j -= 1

        # Join and reverse the result to get the final string
        return ''.join(result[::-1])
