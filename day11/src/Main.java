import java.io.IOException;
import java.util.*;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) throws IOException {
        ArrayList<String> contents = Helper.readFile("input");

        System.out.println(Helper.part_1(contents));
        System.out.println(Helper.part_2(contents));
    }
}