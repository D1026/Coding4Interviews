class Solution:
    def ReverseSentence(self, s):
        # write code here
        stack = [n for n in s.split(' ')]
        print(stack)
        stack.reverse()
        print(stack)
        return ' '.join(stack)

print(Solution().ReverseSentence("I am a student."))