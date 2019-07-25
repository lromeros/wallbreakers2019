class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        
        for num1 in nums1:
            found = False
            appended = False
            
            for num2 in nums2:
                if num2 == num1:
                    found = True
                if found and num2 > num1:
                    answer.append(num2)
                    appended = True
                    break
            if not appended:
                answer.append(-1)
                
        return answer
