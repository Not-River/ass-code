import sys

class Classes:
    #class variable
    times = ['8:30', '9:27', '10:24', '11:21', '12:47', '1:43', '2:40']

    def __init__(self):
        #where I store all my information
        self.classDict = {
        1 : {
        'period' : '1',
        'class' : 'Chemistry',
        'time' : '8:30',
        'teacher' : 'Mr.Philips'
        },
        2:{
        'period' : '2',
        'class' : 'Online',
        'time' : '9:27',
        'teacher' : 'Ms.Bradshaw'
        },
        3:{
        'period' : '3',
        'class' : 'AP CSP',
        'time' : '10:24',
        'teacher' : 'Ms.Duncan'
        },
        4:{
        'period' : '4',
        'class' : 'English',
        'time' : '11:21',
        'teacher' : 'Ms.Spindler'
        },
        5:{
        'period' : '5',
        'class' : 'Spanish',
        'time' : '12:47',
        'teacher' : 'Ms.Gherman'
        },
        6:{
        'period' : '6',
        'class' : 'Engineering',
        'time' : '1:43',
        'teacher' : 'Mr.Lupton'
        },
        7:{
        'period' : '7',
        'class' : 'Game Design',
        'time' : '2:40',
        'teacher' : 'Ms.Duncan'
        }

        }
    #where I run all my calculations
    def getInfo(self, userinfo):
        if userinfo == 'time':
            count = 0
            while count < 7:
                count += 1
                print('    Period %d is at %s ' %( count,  self.classDict[count]['time']))

        elif userinfo == 'teacher':
            count = 0
            while count < 7:
                count += 1
                print('    Period %d is taught by %s ' %( count,  self.classDict[count]['teacher']))

        elif userinfo == 'name':
            count = 0
            while count < 7:
                count += 1
                print('    Period %d is %s ' %( count,  self.classDict[count]['class']))

        elif userinfo == 'full':
            count = 0
            while count < 7:
                count += 1
                print('    Period %d is %s with %s at %s ' %( count, self.classDict[count]['class'], self.classDict[count]['teacher'], self.classDict[count]['time']))
        elif userinfo != '':
            print('Not valid')
        print('_________________________________')
#where I set up my menu and ask for user input
if __name__ == '__main__':
    info = Classes()
    cond = ''
    #I want the user to be able to use the program multiple times in a row without a rerun so I use a while loop with a condition
    while cond != 'b':
        print('\n  Ask the machine \n')
        print("  Enter 'time' to recive class times \n  Enter 'name' to recive class names \n  Enter 'teacher' to recieve teacher names\n  Enter'full' for full list \n  Enter to break")
        g = input("\n  Enter here: ")
        if g != '':
            info.getInfo(g)
        else:
            print('\n  Closing...')
            cond = 'b'
        """ What the menu looks like

          Ask the machine

          Enter 'time' to recive class times
          Enter 'name' to recive class names
          Enter 'Teachers' to recieve teacher names
          Enter'full' for full list
          Enter to break

          Enter here:
        """

#print(class1.__dict__, '\n')
#print('Times of all classes',Classes.times, '\n')
#print(Classes.amount)
