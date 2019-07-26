class Solution:
    def find_next_course(self, all_prereqs: List[List[int]], visited: List[bool]) -> int:
        for i in range(len(all_prereqs)):
            if visited[i] is False and len(all_prereqs[i]) > 0:
                return [i]
        return []
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # creating the adjacency lists
        all_prereqs = [[] for _ in range(numCourses)]
        
        # populating adjacency lists
        for course, prereq in prerequisites:
            all_prereqs[course] += [prereq]
        
        overall_visited = [False] * numCourses
        visited_this_time = overall_visited
        next_courses = self.find_next_course(all_prereqs, overall_visited)
        
        while len(next_courses) > 0:
            course = next_courses.pop()
            if visited_this_time[course]:
                return False
            elif len(all_prereqs[course]) > 0:
                visited_this_time[course] = True
                overall_visited[course] = True
                for p in all_prereqs[course]:
                    if p not in next_courses:
                        next_courses.append(p)
                        
            if len(next_courses) == 0:
                next_courses = self.find_next_course(all_prereqs, overall_visited)
                visited_this_time = [False] * numCourses
                

        return True
