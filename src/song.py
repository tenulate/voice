'''
make a song
'''

import subprocess, os

ford = "a ford ess cort"
ford_notes = [60, 40, 20, 20]

mini = 'a mini mini mini and a ford ess cort'
mini_notes = [50, 70, 70, 70, 50, 50, 40, 20, 20, 20]

ford_words = ford.split()
mini_words = mini.split()

i = 0
for word in ford_words:
    os.system('espeak -a 700 -p %s "%s"'%(str(ford_notes[i]), word))
    i+=1   

i = 0
for word in ford_words:
    os.system('espeak -a 500 -p %s "%s"'%(str(ford_notes[i]), word))
    i+=1 

i = 0
for word in mini_words:
    os.system('espeak -v en-us -a 600 -p %s "%s"'%(str(mini_notes[i]), word))
    i+=1 