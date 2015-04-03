import java.io.*;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.Scanner;
public class DownloadXMLContent {

	/**
	 * @param args
	 * @throws FileNotFoundException 
	 */
	public static void main(String[] args) throws FileNotFoundException {
		File saveFile = new File("TeamHierarchy.xml");
		String location;
		String APIKEY = "ptd42agcacsw87pbcgvfzss5";
		location = "http://api.sportsdatallc.org/soccer-t2/wc/teams/hierarchy.xml?api_key="+APIKEY;
        URL url;
        try {
            url = new URL(location);
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(url.openStream()));
            BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(saveFile));
            String s = "";
            while ((s = bufferedReader.readLine()) != null) {
                bufferedWriter.write(s);
                bufferedWriter.newLine();
                bufferedWriter.flush();
            }
        }
         catch (MalformedURLException e) {
                    e.printStackTrace();
                }
        catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
		File file = new File("TeamIds.txt");
		FileOutputStream fos;
		try {
			fos = new FileOutputStream(file);
			PrintStream ps = new PrintStream(fos);
			System.setOut(ps);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
        Scanner scanner = new Scanner(new File("TeamHierarchy.xml"));
                String line;
                while (scanner.hasNextLine()) {
                    line = scanner.nextLine();
                    if (line.contains("<team id=")) {
                        System.out.println(line.trim().substring(10, 46));
                    }
                }

	}

}

