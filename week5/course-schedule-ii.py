class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        
        # creating the lists
        all_prereqs = [[] for _ in range(numCourses)]
        prereq_of = [[] for _ in range(numCourses)]
        num_prereqs = {i:[] for i in range(numCourses)}
        
        # populating adjacency list
        for course, prereq in prerequisites:
            all_prereqs[course].append(prereq)
            prereq_of[prereq].append(course)
        
        # populating the dictionary of num of prereqs
        for i in range(numCourses):
            num_prq = len(all_prereqs[i]) 
            if num_prq >= 0:
                num_prereqs.get(num_prq).append(i)

        # going through the dictionary
        while len(num_prereqs.get(0)) > 0:
            course_to_add = num_prereqs.get(0).pop()

            # for all courses, for which our current course is a prereq
            for course_up_next in prereq_of[course_to_add]:
                # update the list of prereqs, and update the dictionary
                num_prq = len(all_prereqs[course_up_next])
                all_prereqs[course_up_next].remove(course_to_add)
                new_num_prq = len(all_prereqs[course_up_next])
                num_prereqs.get(new_num_prq).append(course_up_next)
                num_prereqs.get(num_prq).remove(course_up_next)

            # add course to our order
            order.append(course_to_add)
                
        return order if len(order) == numCourses else []
        
