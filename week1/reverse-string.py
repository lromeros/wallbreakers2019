class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s_len = len(s)
        swap_range = math.floor(s_len / 2)

        if s_len <= 3 and s_len != 0:
            swap_range = 1

        for i in range(swap_range):
            new_far = s[i]
            new_close = s[(s_len - i) - 1]
            s[i] = new_close
            s[(s_len - i) - 1] = new_far

