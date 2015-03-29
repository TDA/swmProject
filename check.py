import glob
from xml.dom import minidom
filenames=[]
f = open('retrievedteams2.txt','w+')
filenames=glob.glob(r"C:\Python27\xml_cric1\*.xml")
print filenames
for file in filenames:
	teamid = minidom.parse(file)
	ids = teamid.getElementsByTagName('team')
	for id in ids:
		f.write(id.getAttribute('id') + "\n")


