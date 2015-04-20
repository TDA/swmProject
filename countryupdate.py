import MySQLdb as mdb
import glob
from xml.dom import minidom
filenames = glob.glob(
    r"C:\Python27\swmProject\swmProject\xml_*\*.xml")
	
def update_table(table_name,key,key_value,field,field_value):
    query_string="UPDATE "+str(table_name)+" SET "+ str(field) +" = '"+str(field_value)+"' WHERE " +str(key)+ " = '"+str(key_value)+ "'"
    return (query_string)
def getopenconnection(host='localhost', user='root', password='jaswi!23', dbname='swmproject'):
    return mdb.connect(host=host,  # your host, usually localhost
                           user=user,  # your username
                           passwd=password,  # your password
                           db=dbname)  # name of the data base
db = getopenconnection()
cur = db.cursor()
query = "select player_id from player_attr "
for file in filenames:
    xmldoc = minidom.parse(file)
    country_value=xmldoc.getElementsByTagName("team")[0].getAttribute("name")
    print country_value
    players = xmldoc.getElementsByTagName("player")
    for player in players:
	playerid = player.getAttribute("id")
	print playerid
	country_update =update_table("player_attr","player_id",playerid,"country",country_value)
	cur.execute(country_update)
db.commit();	
	