import MySQLdb
import glob
from xml.dom import minidom
import utilities

def getopenconnection(host='localhost', user='root', password='', dbname='swmProject1'):
    return MySQLdb.connect(host=host,  # your host, usually localhost
                           user=user,  # your username
                           passwd=password,  # your password
                           db=dbname)  # name of the data base


def list_populate(dest_list, source_list, source):
    source_list_copy = source_list[:]
    # make a copy of the lists and pop those
    length = len(source_list)
    for x in xrange(0, length):
        temp = source.getAttribute(source_list_copy.pop(0))
        dest_list.append(temp)


def generate_query(table_name, list_values):
    query_string = "INSERT IGNORE INTO " + str(table_name) + " VALUES(null,"
    for x in range(0, len(list_values) - 1):
        query_string += "'" + \
            MySQLdb.escape_string(str(list_values.pop(0))) + "'" + ","
    query_string += "'" + MySQLdb.escape_string(str(list_values.pop(0))) + "'"
    query_string += ")"
    return query_string
# try:
db = getopenconnection()
cur = db.cursor()
query = "DESCRIBE batsmen_attr"
cur.execute(query)
rows = cur.fetchall()
# for row in rows:
# print row
filenames = glob.glob(
    r"C:\Python27\swmProject\playerprofiles\player*\*.xml")
# print filenames
for file in filenames:
    xmldoc = minidom.parse(file)
    # retrieve the nodes from the dom.
    # print xmldoc.getElementsByTagName("player").length
    # print xmldoc.getElementsByTagName("odi").length
    player = None
    batting_odi = None
    bowling_odi = None
    if xmldoc.getElementsByTagName("player").length > 0:
        player = xmldoc.getElementsByTagName("player")[0]
    if xmldoc.getElementsByTagName("odi").length > 1:
        batting_odi = xmldoc.getElementsByTagName("odi")[0]
        bowling_odi = xmldoc.getElementsByTagName("odi")[1]
    # lists to store the final values extracted from the xml file
    values = []
    batting_values = []
    bowling_values = []

    # attributes we want to extract from the xml doc
    player_attrs = [
        "id", "full_name", "batting_style", "bowling_style", "birth_date"]

    batting_attrs = ["average", "balls_taken", "catches", "ducks", "fours", "sixes", "half_centuries",
                     "centuries", "highest_score", "innings", "matches", "not_outs", "runs", "stumpings"]
    bowling_attrs = ["average", "balls_bowled", "four_wicket", "ten_wicket",
                     "five_wicket", "innings", "runs", "strike_rate", "wickets", "economy"]
    # print "I am here"

    player_exists = player.nodeName != None
    batting_odi_exists = batting_odi != None
    bowling_odi_exists = bowling_odi != None

    # print "here tooooo",player_exists,batting_odi_exists,bowling_odi_exists
    if(player_exists and batting_odi_exists and bowling_odi_exists):
        player_id = player.getAttribute("id")
        player_name = MySQLdb.escape_string(player.getAttribute("full_name"))

        # populate the lists with the required values
        list_populate(values, player_attrs, player)
        list_populate(batting_values, batting_attrs, batting_odi)
        list_populate(bowling_values, bowling_attrs, bowling_odi)

        # print values, batting_values, bowling_values
        # print player_attrs,bowling_attrs,bowling_attrs

        query_string = generate_query("player_attr", values)
        # print query_string+"\n"
        #cur.execute(query_string)
        query_string_batting = generate_query(
            "batsmen_attr", [player_id] + (batting_values))
        # print query_string_batting+"\n"
        #cur.execute(query_string_batting)

        query_string_bowling = generate_query(
            "bowlers_attr", [player_id] + (bowling_values))

        # print query_string_bowling+"\n"
        #cur.execute(query_string_bowling)

db.commit()
db.close()
# except:
#   print "Unable to connect to MySQLDB"
