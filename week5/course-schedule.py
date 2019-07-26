class Solution:
    def find_next_course(self, all_prereqs: List[List[int]], visited: List[bool]) -> List[int]:
        for i in range(len(all_prereqs)):
            if not visited[i] and len(all_prereqs[i]) > 0:
                return [i]
        return []
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # creating the adjacency lists
        all_prereqs = [[] for _ in range(numCourses)]
        
        # populating adjacency lists
        for course, prereq in prerequisites:
            all_prereqs[course].append(prereq)
        
        overall_visited = [False for _ in range(numCourses)]
        visited_this_time = overall_visited
        next_courses = self.find_next_course(all_prereqs, overall_visited)

        while len(next_courses) > 0:
            course = next_courses.pop()
            if visited_this_time[course]:
                print(f"course {course} already visited this time")
                return False
            elif len(all_prereqs[course]) > 0:
                print(f"course {course} not visited this time and has children")
                visited_this_time[course] = True
                overall_visited[course] = True
                for p in all_prereqs[course]:
                    if p not in next_courses:
                        next_courses.append(p)
                        
            if len(next_courses) == 0:
                print(f"the stack is empty, lets try to fix that")
                next_courses = self.find_next_course(all_prereqs, overall_visited)
                visited_this_time = [False for _ in range(numCourses)]
            print(f"stack = {next_courses}")

        return True