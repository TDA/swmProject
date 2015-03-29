import requests
f = open("teamid_cricket.txt","r")
teamid= f.readlines()
count =0
for i in teamid:
	
	count+=1
	response = requests.get("http://api.sportsdatallc.org/cricket-t1/teams/"+i.strip()+"/profile.xml?api_key=ntqf89dhw2yaqdzubkw7gdt6")
	filename = str(count) + ".txt"
	f = open(filename,"w+")
	if response.status_code ==200:
		text = response.text.encode('utf-8')
		print text
		f.write(text)

