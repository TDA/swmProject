import requests
f = open("teamid_cricket.txt","r")
f1 = open("retrievedteams.txt","r")
f2 = open("retrievedteams1.txt","r")
f3= open("retrievedteams2.txt","r")
teamid= f.readlines()
team_present = f1.readlines()
team_present1 = f2.readlines()
team_present2 = f3.readlines()
count =0
for i in teamid:
	if i not in team_present:
		if i not in team_present1:
			if i not in team_present2:
				count+=1
				response = requests.get("http://api.sportsdatallc.org/cricket-t1/teams/"+i.strip()+"/profile.xml?api_key=7w5tnhxcrxvtewj3eqv6u3td")
				filename = str(count) + ".xml"
				f = open(filename,"w+")
				if response.status_code ==200:
					text = response.text.encode('utf-8')
					print text
					f.write(text)


		
		
		
		
		
		

