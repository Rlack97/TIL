# 240209
class Solution:

    # 이진트리용 클래스
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BFS 함수
        def validate(node, low=-float('inf'), high=float('inf')):

            # 값이 비어있으면 노드가 없으므로 상관 없음
            if not node:
                return True

            # 범위를 벗어난 값일 경우 False
            if node.val <= low or node.val >= high:
                return False

            # 범위 조건에 문제가 없을 경우 재귀탐색
            # 왼쪽 노드는 현재 노드값이 최댓값이 되어야 할 것이고
            # 오른쪽 노드는 현재 노드값이 최솟값이 되어야 할 것이다.
            return (validate(node.left, low, node.val)
                    and validate(node.right, node.val, high))

        return validate(root)


# input은 리스트 형태로 받는데, root 값이 뭐길래?
