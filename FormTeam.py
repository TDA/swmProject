#!C:\Python27\python2.7.exe
import cgi, cgitb
import MySQLdb as mdb
import glob
import adjacency
from selection_process import *
from xml.dom import minidom
import dbquery
form = cgi.FieldStorage()
# Get data from fields



print "Content-type:text/html\r\n\r\n"
#print "<html></html>"
inputFromHtml = form.getvalue('swm')
inputList=list()
inputList.append(inputFromHtml)

list=list()
with open("output.txt",'r') as file:
	for line in file:
		list.append(line)
rank=list[len(list)-1]


string="""<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title>Team Formation</title>

    <script type="text/javascript" src="Scripts/jquery-2.1.3.min.js"></script>
    <script type="text/javascript" src="Scripts/myjs.js"></script>
    <script type="text/javascript" src="Scripts/bootstrap.min.js"></script>
    <link rel="stylesheet" type="text/css" href="Scripts/bootstrap.min.css" />
    <link rel="stylesheet" href="Scripts/mystyles.css">

</head>
<body>
    <nav class="navbar navbar-default">
        <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#"><b>Team Formation</b></a>
            </div>
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li class="active"><a href="home.html">Home <span class="sr-only">(current)</span></a></li>

                </ul>
            </div><!-- /.navbar-collapse -->
        </div><!-- /.container-fluid -->
    </nav>
    <div>
        <div class=" ">
            <h3 class="text-success">List of Selected Players</h3>
			<h3 class="text-success">Team Strength : """+str(rank)+""" </h3>
        </div>

        <div class="panel panel-default">

            <!-- Table -->
            <table class="table">

                <thead>
                    <tr>
                        <th>#</th>
                        <th>Type</th>
                        <th>Player Name</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
 """
print string
#print inputList

for x in range(2,13):
	string="""<tr><th scope="row">"""+str(x-1)+"""</th>"""
	if(x==8):
		string+="""<td class="wicketkeeper"></td>"""
	if(x>8):
		string+="""<td class="bowler"></td>"""
	elif(x<8):
		string+="""<td class="batsman"></td>"""

	string+="""<td class="name">"""+list[x]+"""</td>
                        <td><input type="button" id="btnReset" value="Replace Player" class="btn btn-danger" /></td>
    </tr>"""
	print string

#Team_Formation()
print "</body>"
print "</html>"
 