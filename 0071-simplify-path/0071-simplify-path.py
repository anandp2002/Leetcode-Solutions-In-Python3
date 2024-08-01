class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack = []

        for section in arr:
            # section is not empty and section is not "." which means just current directory
            if section != '' and section != ".":
                if section == "..":
                    # Pop previous section from the stack if section is ".."
                    if stack:
                        stack.pop()
                else:
                    stack.append(section)

        return "/" + "/".join(stack)