'''
Russell Schlup
DPW
1/6/13
'''

info = dict()

#info['name'] = input('Your Name.')
#info['school'] = input('What school have you previously gone to?')
#info['dur'] = input('How many year have you attended this school?')
#info['school'] = input('What school do you go to?')
info['grades'] = []

# The asking of what your grades are
for i in range(0,1000000):
    if i == 0:
        grade = input("""Write you grades you have and enter '#' with the quoets when you are finished,
please use only numbers and have them be between 0 and 4.
    """)
    else:
        grade = input('''   ''')
    if grade == '#':
        break
    else:
        info['grades'].append(grade)

# What your highest grade in classes are
info['best'] = 0

for num in info['grades']:
    if num > info['best']:
        info['best'] = num

# Grading system
if info['best']==4:
    info['let']='A'
elif info['best']==3:
    info['let']='B'
elif info['best']==2:
    info['let']='C'
elif info['best']==1:
    info['let']='D'
else:
    info['let']='F'
    
#Adding up The GPA
info['gpa'] = 0

amt = 0
ttl = 0

for a in info['grades']:
    ttl = ttl + a
    amt = amt + 1

info['gpa'] = ttl/amt

print info['gpa']

# The Story
#Hi my name is {info['name']}+ and I have gone through {info['dur']} year(s) at {info['school']}. I have tried to get mostly {info['let']}'s and my GPA is a {info['gpa']}. I have tried my hardest in my classes and my grades clearly show it.