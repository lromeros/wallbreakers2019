class Solution:
    def find_next_course(self, all_prereqs: List[List[int]], visited: List[bool]) -> List[int]:
        # finds the next course that hasn't been visited and has prerequisites
        for i in range(len(all_prereqs)):
            if not visited[i] and len(all_prereqs[i]) > 0:
                return [i]
        return []
    
    def has_cycle_dfs(self, all_prereqs: List[List[int]], course: int, visited: dict, overall_visited: List[int]) -> bool:  
        if course in visited:
            return True
        else:
            overall_visited[course] = True
            visited[course] = 1

        if len(all_prereqs) > 0:
            for prereq in all_prereqs[course]:
                if self.has_cycle_dfs(all_prereqs, prereq, visited, overall_visited):
                    return True
            visited.pop(course)
        
        return False

    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # creating the adjacency lists
        all_prereqs = [[] for _ in range(numCourses)]
        
        # populating adjacency lists
        for course, prereq in prerequisites:
            all_prereqs[course].append(prereq)
        
        # global list of all courses visited
        overall_visited = [False for _ in range(numCourses)]
        
        # next valid course to visit
        next_course = self.find_next_course(all_prereqs, overall_visited)
        
        while len(next_course) > 0:
            course = next_course.pop()
            
            if self.has_cycle_dfs(all_prereqs, course, {}, overall_visited):
                return False
            
            next_course = self.find_next_course(all_prereqs, overall_visited)
        
        return True
