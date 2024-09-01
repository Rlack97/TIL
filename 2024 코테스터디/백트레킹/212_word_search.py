class Solution:
    def findWords(self,board, words):
        # Trie를 구성하는 함수
        def build_trie(words):
            trie = {}
            for word in words:
                node = trie
                for char in word:
                    if char not in node:
                        node[char] = {}
                    node = node[char]
                node['$'] = word  # 단어의 끝을 표시하고, 단어를 저장
            return trie
        """
          trie = {} 일 때
          처음에는 trie에 값을 추가하지만
          'abc' 단어를 넣는다고 하면
          trie:{a:{}} 로 노드를 추가한 뒤 
          node 영역이 trie 가 아닌 a: {} 로 들어간다.
          그래서 하위 노드에 새로운 글자 'b' 노드가 생기는 것이고.
          a:{b:{}} 형태가 됨.
          이후는 반복. '$', 즉 단어가 끝나는 시점에서는 전체 단어를 기록해준다.
        """

        # DFS를 사용하여 단어를 찾는 함수
        def search(node, i, j):
            char = board[i][j]
            if char not in node:
                return
            node = node[char]
            if '$' in node:  # 단어의 끝을 찾은 경우
                result.add(node['$'])
                del node['$']  # 중복 결과를 피하기 위해 단어를 제거
            
            # 방문 표시
            board[i][j] = '#'
            for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + x, j + y
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] != '#':
                    search(node, ni, nj)
            board[i][j] = char  # 방문 표시 복원

        # Trie 구축
        trie = build_trie(words)
        result = set()

        # 보드의 각 위치에서 DFS 시작
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    search(trie, i, j)

        return list(result)