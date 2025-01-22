# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
import re

# get number of students
n_students = int(input())

# collect the column names
column_names = input()
column_names = re.split("\s+", column_names)

# iterate through the column names to check for the column named mark
for column_name_idx in range(len(column_names)):
    if column_names[column_name_idx] == "MARKS":
        # store the column name index whose name is "id" or "ID"
        mark_index = column_name_idx
        break
#print(mark_index)
#
# list of namedtuple
list_namedtuple = list()

# total marks
marks = 0

# enter students records
for student_id in range(n_students):
    record = input()
    record = re.split("\s+", record)
    
    #print(int(record[10]))
    marks += int(record[mark_index])
        
# # store the mark scores in a named tuple
# stu_marks = namedtuple('Marks', marks)

# # total
#print(sum(stu_marks))

print(marks/n_students)
