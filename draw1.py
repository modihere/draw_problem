from random import shuffle
import sys
from guuplot import plotter
f=open("best_alloc.txt","w")
while (1):
	g=0
	rooms = list()
	first_pref=list()

	def zerofunc(t,r):
		global rooms
		for i in range(t):
			for j in range(t):
				if (r==rooms[i][j]):
					rooms[i][j]=0

	def draw():
		global g
		h=0
		global rooms
		rand=list()
		# pref1=[]
		t=int(input("enter the number of students "))
		pref1=[0 for _ in range(t)]
		for i in range (t):
			rooms.append([])
			for j in range (t):
				rooms[i].append(j+1)
				shuffle(rooms[i])
			first_pref.append(rooms[i][0])
		
		for i in rooms:
			print("the preference for student number",h+1," ")
			print (i)
		print(" ")
		for i in first_pref:
			print(i)

		for i in range(t):
			rand.append(i+1)
		shuffle(rand)
		print(" ")
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
			#f.write("preference of student"+str(i+1)+"is"+str(pref1[i])+"\n")
		for i in range(0,t):
			if(pref1[i]==first_pref[i]):
				g+=1
		print("out of ",t," students ",g," student got their first preference.")
		f.write(str(t)+" "+str(g)+"\n")
	draw()
	inp1=int(input("want to continue: 1 for yes,0 for no "))
	if (inp1==0):
		f.close()
		print("\n Do you want a graph of best allocation?")
		inp2=int(input(" -> 1 for yes,0 for no "))
		if (inp2==1):
			f=open("best_alloc.txt","r")
			plotter(f)
			break
		else:
			break	

	
