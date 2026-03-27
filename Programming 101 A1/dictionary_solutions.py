def find_grades(grades, students):
    """ grades is a dict mapping student names (str) to grades (str)
        students is a list of student names
    Returns a list containing the grades for students (in same order) """
    unique = []
    for i in students:
        for k, v in list(grades.items()):
            if i == k:
                unique.append(v)
    return unique

# for example
d = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}
print(find_grades(d, ['Matt', 'Katy'])) # returns ['C', 'A']

# -----------------------------------------------------------------------------

def find_in_L(Ld, k):
    """Ld is a list of dicts
    k is an int
    Returns True if k is a key in any dict of Ld, and False otherwise."""
    for o in Ld:
        if k in o:     # simpler and more Pythonic
            return True
    return False
# for example
d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}

print(find_in_L([d1, d2, d3], 2))   # returns True
print(find_in_L([d1, d2, d3], 25))  # returns False

# ----------------------------------------------------------------------------

def count_matches(d):
    count = 0
    """ d is a dictionary
    Returns how many entries in d have the key equal to its value """
    for k, v in d.items():
        if k == v:
            count += 1
    return count

# for example
d = {1:2, 3:4, 5:6}
print(count_matches(d)) # prints 0
d = {1:2, 'a':'a', 5:5}
print(count_matches(d)) # prints 2
# ---------------------------------------------------------------------------

my_d = {  # q = quiz, a = assignments
    'ali':{'q':[10], 'a':[10,10]},
    'bilal':{'a':[7,8], 'q':[8]},
    'zaid':{'q':[3], 'a':[0]}
}

def get_average(data, what):
    all_data = []
    for stud in data.keys():
        all_data = all_data + data[stud][what]
        
    return sum(all_data)/len(all_data)

print(get_average(my_d, 'a'))