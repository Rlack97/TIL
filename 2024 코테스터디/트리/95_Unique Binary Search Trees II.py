# 0308

class Solution:

    # 이진트리용 클래스
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    # 구조적으로 유일한 구조의 이진 탐색 트리를 반환
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generate_trees_helper(1, n)

    def generate_trees_helper(self, start, end):
        if start > end:
            return [None]

        all_trees = []
        for i in range(start, end + 1):
            left_trees = self.generate_trees_helper(start, i - 1)
            right_trees = self.generate_trees_helper(i + 1, end)
            # 좌측과 우측의 BST를 재귀해서 생성

            for left_tree in left_trees:
                for right_tree in right_trees:

                    # 가능한 모든 루트 값 i에 대해
                    # 해당 루트 값에서 가능한 모든 왼쪽 하위트리 조합과
                    # 오른쪽 하위트리 조합을 생성

                    root = TreeNode(i)
                    root.left = left_tree
                    root.right = right_tree

                    # 생성된 트리를 리스트에 담아서 반환
                    all_trees.append(root)

        return all_trees
