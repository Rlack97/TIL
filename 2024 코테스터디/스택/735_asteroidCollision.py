class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        copy_list = asteroids.copy()
        after_copy_list = copy_list.copy()
        while True:
            plus_stack = []
            minus_stack = []
            crash_cnt = 0

            for a in range(len(copy_list)):
                if  copy_list[a] > 0:
                    # 오른쪽으로 가는 값이 추가될 때 왼쪽으로 가는 값들이 추가되있으면
                    # 어차피 만나지 않는다.
                    plus_stack.append((copy_list[a],a))

                else:
                    minus_stack.append((copy_list[a],a))
                    if plus_stack:
                      crash_cnt += 1
                      crash = plus_stack.pop()
                      if abs(copy_list[a]) > abs(crash[0]):
                          after_copy_list[crash[1]] = 0
                          continue
                      elif abs(copy_list[a]) < abs(crash[0]):
                          minus_stack.pop()
                          after_copy_list[a] = 0
                          plus_stack.append(crash)
                      elif abs(copy_list[a]) == abs(crash[0]):
                          minus_stack.pop()
                          after_copy_list[a] = 0
                          after_copy_list[crash[1]] = 0
            
            if plus_stack == [] or minus_stack == []:
                if plus_stack:
                  answer = [s[0] for s in plus_stack]
                  return answer
                else:
                  answer = [s[0] for s in minus_stack]
                  return answer
                
            if crash_cnt == 0:
                return copy_list
            
            copy_list = [x for x in after_copy_list if x != 0]

        
            