import time

global currentSection
global file
global exitcode

def interpreter(fille, split):
	if(split!=""):
		if(split.upper()=="WAY0" or split.upper()=="WAY 0")
			file=open("/Resources/"+fille+"-0.txt",r)
		elif(split.upper()=="WAY1" or split.upper()=="WAY 1")
			file=open("/Resources/"+fille+"-1.txt",r)
		else:
			input("ERROR")
			exit()
	else:
		file=open(fille, 'r')
	temp=open("temp.txt", 'wb')
	story=file.readlines()
	int=0
	line=story[int]
	while(True)
		if("INPUT" in line)
			foo=line.upper().replace("INPUT ", "")
			lsts=foo.split(',', 1)
			while(var==""):
				var=input(lsts.get[0])
			temp.seek(0, 2)
			temp.write(lsts.get[1]+"="+var)
		elif("SECTION:" in line):
			cu=line.replace("SECTION: ", "")
			cus=cu.replace(".", " ")
			currS=cus.split(' ', 1)
			chapter=currS.get[0]
			scene=currS.get[1]
			option=currS.get[2]
			finncS=str("CHAPTER "+chapter+", SCENE "+scene+", OPTION "+option)
			print(finncS)
			currentSection=finncS
			time.wait(3)
		elif("+ " and " +" in line):
			j=line.split(' + ', 1)
			j.pop(0)
			j.pop(1)
			jkl=j.get[0]
			jklm=temp.readline()
			while(jkl not in jklm)
				jklm=temp.readline()
				if(jklm="")
					input("ERROR! FILE COULD NOT BE READ!")
					exitcode=1
			lolls=jklm.replace(jkl+"=", "")
			loolls=line.replace("+ "+jkl+" +", lolls)
			input(loolls)
		elif("SPLIT " in line):
			jklomp=line.replace("SPLIT ", "")
			jollo=jklomp.split(',' ,1)
			jol=jollo.get[0].upper()
			llo=jollo.get[1].upper()
			interpreter(jol, llo)
		elif("SKIP" in line):
			lomlom=str(line.replace("SKIP ", ""))
			ple= int(lomlom)
			file.seek(ple, 0)
		elif("python" in line.lower()):
			kmslol=line.lower().replace("python(","")
			lolsmk=kmslol.replace(")","")
			filelele=open("run.py", "wb")
			k="""
def run():
	"""+lolsmk+"""
#THIS IS ONLY TEMPORARY..."""
			filelele.write(k)
			if(args):
				import run
				run.run()
		elif("RNDS" in line):
			argggggggggghhhs=line.replace("RNDS ", "").replace(" ","").split(',', 1)
			random.randint(argggggggggghhhs.get[0], argggggggggghhhs.get[1])
		elif():
		elif():
		elif(line=="FINAL"):
			exitcode=0
		elif(line=="*START*"):
		elif(line=="*END*"):
		else:
			input(line)
	temp.close()
	file.close()
	return exitcode
def run():
	print("21 DAYS")
	time.sleep(4)
	print("A GAME MADE BY EN, WJ, JZ")
	interpreter()
	input("THANKS FOR PLAYING")

class main():
	interpreter("storyline.txt")
