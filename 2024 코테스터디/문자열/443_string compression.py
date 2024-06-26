class Solution:
    def compress(self, chars: List[str]) -> int:
        stack = []
        nums = 1
        idx = 0
        
        if len(chars) > 0:
            stack.append(chars[0])
        
        for i in range(1, len(chars)):
            if chars[i] == stack[idx]:
                nums = nums + 1
                
                if i == len(chars) - 1:
                    num_list = list(str(nums))
                    idx = idx + 1 + len(num_list)
                
                    stack = stack + num_list
                    
                
            elif chars[i] != stack[idx]:

                if nums == 1:    
                    idx = idx + 1

                num_list = list(str(nums))
                
                if num_list != ['1']:
                    idx = idx + 1 + len(num_list)
                    stack = stack + num_list
                
                stack.append(chars[i])
                nums = 1

        for i in range(len(stack)):
            chars[i] = stack[i]
        
        chars = chars[0:len(stack)]
        
        return len(chars)