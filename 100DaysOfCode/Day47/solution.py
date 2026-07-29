"""
Day 47 - Course Schedule

Problem:
There are numCourses courses labeled from 0 to numCourses-1.

Some courses have prerequisites.

Return True if you can finish all courses,
otherwise return False.

Example:

numCourses = 2

prerequisites = [[1,0]]

Output:
True

Course 0 → Course 1
"""


from collections import deque


def can_finish(num_courses, prerequisites):

    # Create adjacency list
    graph = {i: [] for i in range(num_courses)}

    # Store indegree of every course
    indegree = [0] * num_courses

    # Build graph
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        indegree[course] += 1

    # Queue for courses with no prerequisites
    queue = deque()

    for i in range(num_courses):
        if indegree[i] == 0:
            queue.append(i)

    completed = 0

    while queue:

        current = queue.popleft()
        completed += 1

        for neighbor in graph[current]:

            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return completed == num_courses

Test Case 1
# -------------------------

num_courses1 = 2
prerequisites1 = [[1, 0]]

print("Courses:", num_courses1)
print("Prerequisites:", prerequisites1)
print("Can Finish:", can_finish(num_courses1, prerequisites1))

print()

 Test Case 2
# -------------------------

num_courses2 = 2
prerequisites2 = [[1, 0], [0, 1]]

print("Courses:", num_courses2)
print("Prerequisites:", prerequisites2)
print("Can Finish:", can_finish(num_courses2, prerequisites2))

print()

 Test Case 3
# -------------------------

num_courses3 = 4
prerequisites3 = [[1, 0], [2, 0], [3, 1], [3, 2]]

print("Courses:", num_courses3)
print("Prerequisites:", prerequisites3)
print("Can Finish:", can_finish(num_courses3, prerequisites3))