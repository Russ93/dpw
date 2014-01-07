'''Russell Schlup
DPW
1/6/13'''

info = dict()

#info['name'] = input('Your Name.')
#info['school'] = input('What school have you previously gone to?')
#info['dur'] = input('How many year have you attended this school?')
#info['school'] = input('What school do you go to?')
info['grades'] = []
for i in range(0,1000000):
    if i == 0:
        grade = input("""Write you grades you have and enter '#' with the quoets when you are finished,
please use only numbers and have them be between 0 and 4.
    """)
    else:
        grade = input('')
    if grade == '#':
        break
    else:
        info['grades'].append(grade)
info['best'] = 0
for num in info['grades']:
    if num > info['best']:
        info['best'] = num
print info['best']
"""'Hi my name is '+info['name']+' and I have gone through '+info['dur']+' year(s) at '+info['school']+'. I have tried to get mostly '+info['grades']+"'s and my GPA is a "info['grades']'. I have tried my hardest in my classes and my grades clearly show it.'"""