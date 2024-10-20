class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st=deque()

        for char in expression:
            if char==',' or char=='(':
                continue

            if char in ['t','f','!','&','|']:
                st.append(char)

            elif char==')':
                has_true=False
                has_false=False

                while st[-1] not in ['!','&','|']:
                    top_value=st.pop()
                    if top_value=='t':
                        has_true=True
                    elif top_value=='f':
                        has_false=True

                op=st.pop()
                if op=='!':
                    st.append('t' if not has_true else 'f')
                elif op=='&':
                    st.append('f' if has_false else 't')
                else:
                    st.append('t' if has_true else 'f')

        return st[-1]=='t'                