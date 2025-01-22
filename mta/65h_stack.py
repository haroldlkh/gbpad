class Solution:
    def isNumber(self, s: str) -> bool:
        # Trim spaces
        s = s.strip()
        if not s:
            return False

        stack = []
        has_digit = False
        has_decimal = False
        has_exponent = False

        for i, char in enumerate(s):
            if '0' <= char <= '9':  # Digit
                has_digit = True
                stack.append(char)
            elif char in '+-':  # Sign
                # Sign is valid only at the start or immediately after 'e/E'
                if i > 0 and s[i-1] not in 'eE':
                    return False
                stack.append(char)
            elif char == '.':  # Decimal point
                # Decimal is invalid if there's already a decimal or exponent
                if has_decimal or has_exponent:
                    return False
                has_decimal = True
                stack.append(char)
            elif char in 'eE':  # Exponent
                # Exponent is invalid if there's already one or no digit before it
                if has_exponent or not has_digit:
                    return False
                has_exponent = True
                has_digit = False  # Reset digit check for exponent part
                stack.append(char)
            else:  # Invalid character
                return False

        # Valid input must have at least one digit, and stack should contain a valid combination
        return has_digit


# class Solution:
#     def isNumber(self, s: str) -> bool:
#         def is_integer(s):
#             if not s:  # Empty string is not a valid integer
#                 return False
#             if s[0] in '+-':  # Handle optional sign
#                 s = s[1:]
#             # Ensure the remaining string contains only digits
#             return all('0' <= char <= '9' for char in s) if s else False
        
#         def is_decimal(s):
#             if not s:
#                 return False
#             if s[0] in '+-':  # Handle optional sign
#                 s = s[1:]
#             if s.count('.') != 1:  # Must contain exactly one decimal point
#                 return False
#             integer_part, _, fractional_part = s.partition('.')
#             # At least one part must contain digits
#             integer_valid = all('0' <= char <= '9' for char in integer_part) if integer_part else False
#             fractional_valid = all('0' <= char <= '9' for char in fractional_part) if fractional_part else False
#             if integer_part and not fractional_part or not integer_part and fractional_part:
#                 return integer_valid or fractional_valid
#             else: return integer_valid and fractional_valid
        
#         # Step 1: Strip spaces
#         s = s.strip()
#         if not s:
#             return False
        
#         # Step 2: Check for invalid characters
#         valid_chars = set("0123456789+-eE.")
#         if any(char not in valid_chars for char in s):
#             return False
        
#         # Step 3: Handle 'e' or 'E'
#         if 'e' in s or 'E' in s:
#             base, _, exponent = s.partition('e') if 'e' in s else s.partition('E')
#             return (is_decimal(base) or is_integer(base)) and is_integer(exponent)
#         else:
#             # Step 4: Validate as either a decimal or integer
#             return is_decimal(s) or is_integer(s)


# class Solution:
#     def isNumber(self, s: str) -> bool:
#         def is_integer(s):
#             if not s:  # Empty string is not a valid integer
#                 return False
#             if s[0] in '+-':  # Handle optional sign
#                 s = s[1:]
#             # Ensure the remaining string contains only digits
#             return all('0' <= char <= '9' for char in s) if s else False
        
#         def is_decimal(s):
#             if not s:
#                 return False
#             if s[0] in '+-':  # Handle optional sign
#                 s = s[1:]
#             if s.count('.') != 1:  # Must contain exactly one decimal point
#                 return False
#             integer_part, _, fractional_part = s.partition('.')
#             # At least one part must contain digits
#             integer_valid = all('0' <= char <= '9' for char in integer_part) if integer_part else False
#             fractional_valid = all('0' <= char <= '9' for char in fractional_part) if fractional_part else False
#             if integer_part and not fractional_part or not integer_part and fractional_part:
#                 return integer_valid or fractional_valid
#             else: return integer_valid and fractional_valid
        
#         # Step 1: Strip spaces
#         s = s.strip()
#         if not s:
#             return False
        
#         # Step 2: Check for invalid characters
#         valid_chars = set("0123456789+-eE.")
#         if any(char not in valid_chars for char in s):
#             return False
        
#         # Step 3: Handle 'e' or 'E'
#         if 'e' in s or 'E' in s:
#             base, _, exponent = s.partition('e') if 'e' in s else s.partition('E')
#             return (is_decimal(base) or is_integer(base)) and is_integer(exponent)
#         else:
#             # Step 4: Validate as either a decimal or integer
#             return is_decimal(s) or is_integer(s)
