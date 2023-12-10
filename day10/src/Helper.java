import java.io.*;
import java.util.ArrayList;

public class Helper {
    public static ArrayList<String> readFile(String filename) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(new File(filename)));
        ArrayList<String> contents = new ArrayList<>();

        String line = br.readLine();

        while (line != null)
        {
            contents.add(line);
            line = br.readLine();
        }

        return contents;
    }
}
