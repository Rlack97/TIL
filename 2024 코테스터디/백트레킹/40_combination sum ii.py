# candidtes 안의 숫자를 조합하여
# 합이 target이 되는 숫자의 조합을 리턴해라
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        # 오름차순 정렬
        candidates.sort()
        length = len(candidates)

        def DFS(start, path, remain):
            # 목표값 도달, 기록해둔 경로를 정답에 추가한다
            if remain == 0:
                answer.append(path)
            # 합이 목표값보다 커졌으므로 되돌아간다
            elif remain < 0:
                return

            # 현재 위치에서 뒤에 있는 숫자들에 대해서
            for i in range(start, length):
                # 이전값과 같은 중복값일 경우 ?
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                # 현재 보는 값이 남은 값보다 크면 이후 숫자들과의 조합은 버려도 됨(오름차순이므로)
                if candidates[i] > remain:
                    break

                DFS(i+1, path + [candidates[i]], remain - candidates[i])

        DFS(0, [], target)

        return answer
