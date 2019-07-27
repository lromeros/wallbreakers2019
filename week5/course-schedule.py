class Solution:
        
    def has_cycle_dfs(self, all_prereqs: List[List[int]], course: int, visited: List[int]) -> bool:  
        print(f"calling recursive with {course}")
        print(f"visited looks like: {visited}")
        if course in visited:
            print(f"already visited that course :O")
            return True
        else:
            visited.append(course)
        
        og_visited = copy.copy(visited)

        if len(all_prereqs) > 0:
            for prereq in all_prereqs[course]:
                if self.has_cycle_dfs(all_prereqs, prereq, visited):
                    print(f"found a cycle")
                    return True
                else:
                    visited = og_visited
        
        return False

    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        print("================================================================")
        # creating the adjacency lists
        all_prereqs = [[] for _ in range(numCourses)]
        
        # populating adjacency lists
        for course, prereq in prerequisites:
            all_prereqs[course].append(prereq)
        
        for i in range(numCourses):
            if len(all_prereqs[i]) > 0:
                print(f"from the top, calling on {i}")
                if self.has_cycle_dfs(all_prereqs, i, []):
                    return False
        
        return True
