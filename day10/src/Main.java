import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) throws IOException {
        ArrayList<String> fileContents = Helper.readFile("input");
        System.out.println("fileContents = " + fileContents);
        Integer[] startingPointLocation = Day10Helper.findStartingPoint(fileContents);
        System.out.println("Arrays.toString(startingPointLocation) = " + Arrays.toString(startingPointLocation));
        Day10Helper.MfindLoop(fileContents, startingPointLocation);

    }
}