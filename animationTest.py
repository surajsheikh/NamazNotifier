# import turtle
#
# myTurtle = turtle.Turtle()
# myTurtle.circle(50)
# turtle.getscreen()._root.mainloop()

import time,sys
while True:
	blah="\|/-\|/-"
	for l in blah:
		sys.stdout.write(l)
		sys.stdout.flush()
		sys.stdout.write('\b')
		time.sleep(0.2)
