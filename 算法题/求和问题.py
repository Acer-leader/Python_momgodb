class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here
        if a == b:
            return a <<1
        if a == -b:
            return 0
        while(b != 0):
            tmpA = a^b
            b = (a&b)<<1
            a = tmpA
        return a
    aplusb(1,2)