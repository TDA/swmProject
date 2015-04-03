import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;


public class ParsePlayerProfile {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		  try {

			   File xmlFile = new File("PlayerProfile.xml");
			   DocumentBuilderFactory documentFactory = DocumentBuilderFactory.newInstance();
			   DocumentBuilder documentBuilder = documentFactory
			     .newDocumentBuilder();
			   Document doc = documentBuilder.parse(xmlFile);

			   doc.getDocumentElement().normalize();
			   NodeList playerdetails = doc.getElementsByTagName("player");
			   for (int temp = 0; temp < playerdetails.getLength(); temp++) {
			    Node node = playerdetails.item(temp);
			    if (node.getNodeType() == Node.ELEMENT_NODE) {
			     Element 	team = (Element) node;
			     Map<String, List<String>> map = new HashMap<String, List<String>>();
			     List<String> valSet = new ArrayList<String>();
			     valSet.add(team.getAttribute("full_name"));
			     valSet.add(team.getAttribute("nick_name"));
			     valSet.add(team.getAttribute("batting_style"));
			     valSet.add(team.getAttribute("bowling_style"));
			     valSet.add(team.getAttribute("birth_date"));
			     map.put(team.getAttribute("id"), valSet);		     
			     for (Map.Entry<String, List<String>> entry : map.entrySet()) {
			    	    System.out.println("Key = " + entry.getKey() + ", Value = " + entry.getValue());
			    	}
			    }
			   }
			   
// 			Parse Batting Statistics   
			   System.out.println("\n"+"Batting Statistics"+"\n");
			   NodeList battingodi = doc.getElementsByTagName("odi");
			   System.out.println("ODI batting statistics"+"\n");			   
			   for (int temp = 0; temp < battingodi.getLength(); temp++) {
				    Node node = battingodi.item(temp);		
				    if (node.getNodeType() == Node.ELEMENT_NODE) {
					     Element 	team = (Element) node;
// 	WIP make a generic extension like this Map<String, HashMap<String,String>> Player profile = new HashMap<String, HashMap<String,String>>() 					     
					     List<String> valSet = new ArrayList<String>();
					     if ( team.getParentNode().getNodeName().toString().trim().equalsIgnoreCase("batting")){
					     valSet.add(team.getAttribute("average"));
					     valSet.add(team.getAttribute("balls_taken"));
					     valSet.add(team.getAttribute("catches"));
					     valSet.add(team.getAttribute("ducks"));
					     valSet.add(team.getAttribute("fours"));
					     valSet.add(team.getAttribute("sixes"));
					     valSet.add(team.getAttribute("half_centuries"));
					     valSet.add(team.getAttribute("centuries"));
					     valSet.add(team.getAttribute("highest_score"));
					     valSet.add(team.getAttribute("innings"));
					     valSet.add(team.getAttribute("matches"));
					     valSet.add(team.getAttribute("not_outs"));
					     valSet.add(team.getAttribute("runs"));
					     valSet.add(team.getAttribute("stumpings"));
					     }				     
					     for (Iterator iterator = valSet.iterator(); iterator.hasNext();) {
					    	 String string = (String) iterator.next();
					    	 System.out.println(string);
	
					     }
					    }
					   }	
			   NodeList battingtest = doc.getElementsByTagName("test");
			   System.out.println("Test batting statistics"+"\n");
			   for (int temp = 0; temp < battingtest.getLength(); temp++) {
				    Node node = battingtest.item(temp);		
				    if (node.getNodeType() == Node.ELEMENT_NODE) {
					     Element 	team = (Element) node;
					     List<String> valSet = new ArrayList<String>();
					     if ( team.getParentNode().getNodeName().toString().trim().equalsIgnoreCase("batting")){
					     valSet.add(team.getAttribute("average"));
					     valSet.add(team.getAttribute("balls_taken"));
					     valSet.add(team.getAttribute("catches"));
					     valSet.add(team.getAttribute("ducks"));
					     valSet.add(team.getAttribute("fours"));
					     valSet.add(team.getAttribute("sixes"));
					     valSet.add(team.getAttribute("half_centuries"));
					     valSet.add(team.getAttribute("centuries"));
					     valSet.add(team.getAttribute("highest_score"));
					     valSet.add(team.getAttribute("innings"));
					     valSet.add(team.getAttribute("matches"));
					     valSet.add(team.getAttribute("not_outs"));
					     valSet.add(team.getAttribute("runs"));
					     valSet.add(team.getAttribute("stumpings"));					     
					     
					     }
					    
					     for (Iterator iterator = valSet.iterator(); iterator.hasNext();) {
					    	 String string = (String) iterator.next();
					    	 System.out.println(string);
	
					     }
					    }
					   }

			   NodeList battingt20 = doc.getElementsByTagName("t20");
			   System.out.println("T20 batting statistics"+"\n");
			   for (int temp = 0; temp < battingt20.getLength(); temp++) {
				    Node node = battingt20.item(temp);		
				    if (node.getNodeType() == Node.ELEMENT_NODE) {
					     Element 	team = (Element) node;
					     List<String> valSet = new ArrayList<String>();
					     if ( team.getParentNode().getNodeName().toString().trim().equalsIgnoreCase("batting")){
					     valSet.add(team.getAttribute("average"));
					     valSet.add(team.getAttribute("balls_taken"));
					     valSet.add(team.getAttribute("catches"));
					     valSet.add(team.getAttribute("ducks"));
					     valSet.add(team.getAttribute("fours"));
					     valSet.add(team.getAttribute("sixes"));
					     valSet.add(team.getAttribute("half_centuries"));
					     valSet.add(team.getAttribute("centuries"));
					     valSet.add(team.getAttribute("highest_score"));
					     valSet.add(team.getAttribute("innings"));
					     valSet.add(team.getAttribute("matches"));
					     valSet.add(team.getAttribute("not_outs"));
					     valSet.add(team.getAttribute("runs"));
					     valSet.add(team.getAttribute("stumpings"));					     
					     }
					     for (Iterator iterator = valSet.iterator(); iterator.hasNext();) {
					    	 String string = (String) iterator.next();
					    	 System.out.println(string);
	
					     }
					    }
					   }
//      Parse Bowling Statistics
			   System.out.println("\n"+"Bowling Statistics"+"\n");
			   NodeList Bowlingodi = doc.getElementsByTagName("odi");
			   System.out.println("ODI Bowling statistics"+"\n");			   
			   for (int temp = 0; temp < Bowlingodi.getLength(); temp++) {
				    Node node = Bowlingodi.item(temp);		
				    if (node.getNodeType() == Node.ELEMENT_NODE) {
					     Element 	team = (Element) node;
					     List<String> valSet = new ArrayList<String>();
					     if ( team.getParentNode().getNodeName().toString().trim().equalsIgnoreCase("bowling")){
					     valSet.add(team.getAttribute("average"));
					     valSet.add(team.getAttribute("balls_bowled"));
					     valSet.add(team.getAttribute("four_wicket"));
					     valSet.add(team.getAttribute("ten_wicket"));
					     valSet.add(team.getAttribute("five_wicket"));
					     valSet.add(team.getAttribute("innings"));
					     valSet.add(team.getAttribute("matches"));
					     valSet.add(team.getAttribute("runs"));
					     valSet.add(team.getAttribute("strike_rate"));
					     valSet.add(team.getAttribute("wickets"));
					     valSet.add(team.getAttribute("economy"));
					     }				     
					     for (Iterator iterator = valSet.iterator(); iterator.hasNext();) {
					    	 String string = (String) iterator.next();
					    	 System.out.println(string);
	
					     }
					    }
					   }
			   
			   NodeList Bowlingtest = doc.getElementsByTagName("test");
			   System.out.println("Test Bowling statistics"+"\n");			   
			   for (int temp = 0; temp < Bowlingtest.getLength(); temp++) {
				    Node node = Bowlingtest.item(temp);		
				    if (node.getNodeType() == Node.ELEMENT_NODE) {
					     Element 	team = (Element) node;
					     List<String> valSet = new ArrayList<String>();
					     if ( team.getParentNode().getNodeName().toString().trim().equalsIgnoreCase("bowling")){
					     valSet.add(team.getAttribute("average"));
					     valSet.add(team.getAttribute("balls_bowled"));
					     valSet.add(team.getAttribute("four_wicket"));
					     valSet.add(team.getAttribute("ten_wicket"));
					     valSet.add(team.getAttribute("five_wicket"));
					     valSet.add(team.getAttribute("innings"));
					     valSet.add(team.getAttribute("matches"));
					     valSet.add(team.getAttribute("runs"));
					     valSet.add(team.getAttribute("strike_rate"));
					     valSet.add(team.getAttribute("wickets"));
					     valSet.add(team.getAttribute("economy"));
					     }				     
					     for (Iterator iterator = valSet.iterator(); iterator.hasNext();) {
					    	 String string = (String) iterator.next();
					    	 System.out.println(string);
	
					     }
					    }
					   }
			   NodeList Bowlingt20 = doc.getElementsByTagName("t20");
			   System.out.println("T20 Bowling statistics"+"\n");			   
			   for (int temp = 0; temp < Bowlingt20.getLength(); temp++) {
				    Node node = Bowlingt20.item(temp);		
				    if (node.getNodeType() == Node.ELEMENT_NODE) {
					     Element 	team = (Element) node;
					     List<String> valSet = new ArrayList<String>();
					     if ( team.getParentNode().getNodeName().toString().trim().equalsIgnoreCase("bowling")){
					     valSet.add(team.getAttribute("average"));
					     valSet.add(team.getAttribute("balls_bowled"));
					     valSet.add(team.getAttribute("four_wicket"));
					     valSet.add(team.getAttribute("ten_wicket"));
					     valSet.add(team.getAttribute("five_wicket"));
					     valSet.add(team.getAttribute("innings"));
					     valSet.add(team.getAttribute("matches"));
					     valSet.add(team.getAttribute("runs"));
					     valSet.add(team.getAttribute("strike_rate"));
					     valSet.add(team.getAttribute("wickets"));
					     valSet.add(team.getAttribute("economy"));
					     }				     
					     for (Iterator iterator = valSet.iterator(); iterator.hasNext();) {
					    	 String string = (String) iterator.next();
					    	 System.out.println(string);
	
					     }
					    }
					   }			   
			   
			  } catch (Exception e) {
			   e.printStackTrace();
			  }
		}

	}

