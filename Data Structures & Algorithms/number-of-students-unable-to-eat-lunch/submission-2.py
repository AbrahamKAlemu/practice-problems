class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        countStudents = Counter(students)
        for sandwich in sandwiches:
            if countStudents[sandwich] > 0:
                countStudents[sandwich] -= 1
            else:
                break

        return countStudents[1] + countStudents[0]