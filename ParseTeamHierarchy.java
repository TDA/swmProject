import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.ParserConfigurationException;

import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.w3c.dom.Node;
import org.w3c.dom.Element;
import java.io.File;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ParseTeamHierarchy {
	

		public static void main(String args[])
		{
	  try {

		   File xmlFile = new File("TeamHierarchy.xml");
		   DocumentBuilderFactory documentFactory = DocumentBuilderFactory.newInstance();
		   DocumentBuilder documentBuilder = documentFactory
		     .newDocumentBuilder();
		   Document doc = documentBuilder.parse(xmlFile);
		   doc.getDocumentElement().normalize();
		   NodeList nodeList = doc.getElementsByTagName("team");
		   for (int temp = 0; temp < nodeList.getLength(); temp++) {
		    Node node = nodeList.item(temp);
		    if (node.getNodeType() == Node.ELEMENT_NODE) {
		     Element 	team = (Element) node;
		     Map<String, List<String>> map = new HashMap<String, List<String>>();
		     List<String> valSet = new ArrayList<String>();
		     valSet.add(team.getAttribute("name"));
		     valSet.add(team.getAttribute("alias"));
		     valSet.add(team.getAttribute("country_code"));
		     valSet.add(team.getAttribute("country"));
		     map.put(team.getAttribute("id"), valSet);		     
		     for (Map.Entry<String, List<String>> entry : map.entrySet()) {
		    	    System.out.println("Key = " + entry.getKey() + ", Value = " + entry.getValue());
		    	}
		    }
		   }
		  } catch (Exception e) {
		   e.printStackTrace();
		  }
	}
}
