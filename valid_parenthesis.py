class Solution:

    def match(self, top_parenthesis, parenthesis):
        if top_parenthesis == "{" and parenthesis == "}":
            return True
        if top_parenthesis == "(" and parenthesis == ")":
            return True
        if top_parenthesis == "[" and parenthesis == "]":
            return True

        return False

    def isValid(self, s: str) -> bool:

        queue = collections.deque()

        if len(s) % 2 != 0:
            return False

        for parenthesis in s:
            if parenthesis in ["{", "[", "("]:
                queue.appendleft(parenthesis)
            else:
                if len(queue) > 0:
                    top_parenthesis = queue.popleft()
                    if not self.match(top_parenthesis, parenthesis):
                        return False
                else:
                    return False

        if len(queue) == 0:
            return True
        else:
            return False