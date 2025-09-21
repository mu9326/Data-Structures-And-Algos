class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []  # keeps track of valid directory names
        cur = ""  # accumulates characters for the current directory name

        # iterate over each character in path, plus an extra "/" at the end
        for c in path + "/":
            if (
                c == "/"
            ):  # when encountering a slash, process the current directory name
                if cur == "..":  # means "go up one directory"
                    if stack:
                        stack.pop()  # remove last directory if possible
                elif cur != "" and cur != ".":
                    # add valid directory names (not "" or ".")
                    stack.append(cur)
                cur = ""  # reset current directory
            else:
                cur += c  # keep building the directory name

        # join stack with "/" to form the simplified path
        return "/" + "/".join(stack)
