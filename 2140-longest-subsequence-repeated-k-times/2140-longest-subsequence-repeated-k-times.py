class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        result=""
        candidates=sorted([char for char,count in Counter(s).items() if count>=k],reverse=True)

        dq=deque(candidates)
        while dq:
            curr=dq.popleft()

            if len(curr)>len(result):
                result=curr

            for ch in candidates:
                nxt=curr+ch
                it=iter(s)

                if all(ch in it for ch in nxt*k):
                    dq.append(nxt)

        return result