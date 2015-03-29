from xml.dom import minidom

f = open('teamid_cricket.txt','w+')
teamid = minidom.parse('teams.xml')
ids = teamid.getElementsByTagName('team')
for id in ids:
	f.write(id.getAttribute('id') + "\n")
