"""
Simplify Path
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.



Example 1:

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
Example 4:

Input: path = "/a/./b/../../c/"
Output: "/c"


Constraints:

1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.
"""
from collections import deque


class Solution:
    def simplifyPath(self, path: str) -> str:
        # Solution 1 - 32 ms
        """
        s = []
        for x in path.split('/'):
            if not x:
                continue
            elif x == '.':
                continue
            elif x == '..':
                if s:
                    s.pop()
            else:
                s.append(x)
        return '/' + '/'.join(s)
        """

        # Solution 2 - 12 ms
        s = deque()
        for node in path.split('/'):
            if node == '..':
                if s:
                    s.pop()
            elif node and node != '.':
                s.append(node)
        return "/" + "/".join(s)


# Main Call
path = "/home//foo/"
solution = Solution()
print(solution.simplifyPath(path))