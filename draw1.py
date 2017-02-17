from random import shuffle
import sys 

f=open("best_alloc.txt","w")
f.write("this is the file for seeing the number of best allocations : \n")
while (1):

	rooms = list()

	def zerofunc(t,r):
		global rooms
		for i in range(t):
			for j in range(t):
				if (r==rooms[i][j]):
					rooms[i][j]=0

	def draw():
		global rooms
		rand=list()
		# pref1=[]
		t=int(input("enter the number of students "))
		pref1=[0 for _ in range(t)]
		for i in range (t):
			rooms.append([])
			print("enter the preference for student number",i+1," ")
			for j in range (t):
				pref=int(input(''))
				rooms[i].append(pref)
		for i in rooms:
			print (i)

		for i in range(t):
			rand.append(i+1)
		shuffle(rand)
		for i in rand:
			print(i)

		for i in range (1,t+1):
			for j in range(t):
				if (i == rand[j]):
					for k in range(t):
						if (rooms[j][k] > 0):
							pref1[j]=rooms[j][k]
							#print(pref1)
							r=pref1[j]
							zerofunc(t,r)
							# print(rooms)
							break
		for i in range(0,t):
			print ("preference of student",i+1,"is",pref1[i])
			f.write("preference of student"+str(i+1)+"is"+str(pref1[i])+"\n")
	draw()
	inp1=int(input("want to continue: 1 for yes,0 for no "))
	if (inp1==0):
		break	
f.close()
	
