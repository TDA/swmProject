from xml.dom import minidom
import requests
import time

f =open("E:\\spring\'15\\semantic_web mining\\project_git_files\\swmProject\\playerid.txt")
playerList = set(list(f))

#playerid = minidom.parse("E:\\spring\'15\\semantic_web mining\\project_git_files\\swmProject\\playerid.txt")
#ids = playerid.getElementsByTagName('player')

#[ i.getAttribute('id') for i in ids]
count = 0

for i in playerList:
    count+=1
    response = requests.get("http://api.sportsdatallc.org/cricket-t1/players/"+i+"/profile.xml?api_key=6jesh8duf5nu62r7edar2rk9")
    filename = str(count) + ".xml"
    f = open(filename,"w+")
    if response.status_code ==200:
	text = response.text.encode('utf-8')
	#print text
	f.write(text)   
    
    #http://api.sportsdatallc.org/cricket-t1/players/0f5aab08-51e6-4d61-a26f-d9ca0c2d29b6/profile.xml?api_key=zdym978y7776u4s8zn2c98wn