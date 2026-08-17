class CourseNode:
    def __init__(self, course: int):
        self.course = course
        self.next_courses = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
        m = dict()
        output = True

        for i in prerequisites:
            pre = i[1]
            post = i[0]
            if not pre in m:
                m[pre] = CourseNode(pre)
            if not post in m:
                m[post] = CourseNode(post)
            preN = m[pre]
            postN = m[post]

            preN.next_courses.append(postN)

        visited = set()
        nodes = list(m.values())
        prev = set()


        def dfs(node: CourseNode):
            nonlocal output
            if node in prev:
                output = False
                return
            elif node in visited:
                return
            elif not output == False:
                visited.add(node)
                prev.add(node)
                for n in node.next_courses:
                    dfs(n)
                    if not output:
                        return 
                prev.remove(node)
                


        for i in nodes:
            if not i in visited:
                prev.clear()
                dfs(i)
                if output == False:
                    return False
                
    
        return True

        
        


        
        
        

        

        