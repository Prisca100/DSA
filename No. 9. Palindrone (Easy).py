"""Math"""
def isPalindrome(self, x):
    if(x < 0) or (x != 0 and x % 10 == 0):
        return False
    reversed_str = str(x)[::-1]
    return reversed_str == str(x)