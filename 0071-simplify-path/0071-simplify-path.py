class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack = []

        for sec in arr:
            # Section is not empty and section is not "." which means just current directory
            if sec != '' and sec != ".":
                if sec == "..":
                    # Pop previous val in stack if sec is ".."
                    if stack:
                        stack.pop()
                else:
                    stack.append(sec)

        return "/" + "/".join(stack)