class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n = len(senate)
        # Radiant 소속을 기록한 q
        qr = collections.deque([i for i, c in enumerate(senate) if c == "R"])
        # Dire 소속을 기록한 q
        qd = collections.deque([i for i, c in enumerate(senate) if c == "D"])

        # 두 큐가 남아있는 동안 반복
        while qr and qd:
            # 각 대표의 번호를 비교후, 번호가 작은 쪽(먼저 있는)이 반대쪽을 제거
            # 이후 해당 인원은 가장 맨 뒷 순서가 됨
            if qr[0] < qd[0]:
                qd.popleft()
                qr.append(qr.popleft() + n)
            else:
                qr.popleft()
                qd.append(qd.popleft() + n)

        # 어느 한쪽이라도 인원이 바닥나면 남아있는 쪽의 승리
        return "Radiant" if qr else "Dire"
