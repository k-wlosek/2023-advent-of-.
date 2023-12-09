import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

public class Helper {
    public static ArrayList<ArrayList<ArrayList<Integer>>> createHistories(ArrayList<String> input) {
        ArrayList<ArrayList<ArrayList<Integer>>> allHistories = new ArrayList<>();
        for (String history:
                input) {
            ArrayList<ArrayList<Integer>> histories = new ArrayList<>();
            ArrayList<String> beginningHistoryStr = new ArrayList<>(Arrays.asList(history.split(" ")));

            ArrayList<Integer> beginningHistory = new ArrayList<>();
            for (String datapoint:
                    beginningHistoryStr) {
                beginningHistory.add(Integer.parseInt(datapoint));
            }
            histories.add(beginningHistory);

            // Parse first history
            ArrayList<Integer> secondHistory = new ArrayList<>();
            for (int i = 0; i < beginningHistory.size()-1; i++) {
                secondHistory.add(beginningHistory.get(i+1)-beginningHistory.get(i));
            }
            histories.add(secondHistory);

            // Parse next histories
            ArrayList<Integer> lastElement = histories.get(histories.size() - 1);
            Integer zeroCount = 0;
            for (int i = 0; i < lastElement.size(); i++) {
                if (lastElement.get(i) == 0)
                    zeroCount++;
            }
            while (zeroCount != lastElement.size())
            {
                ArrayList<Integer> nextHistory = new ArrayList<>();
                for (int i = 0; i < lastElement.size()-1; i++) {
                    nextHistory.add(lastElement.get(i+1)-lastElement.get(i));
                }
                histories.add(nextHistory);

                // Check if we're done
                lastElement = histories.get(histories.size() - 1);
                zeroCount = 0;
                for (int i = 0; i < lastElement.size(); i++) {
                    if (lastElement.get(i) == 0)
                        zeroCount++;
                }
            }
            allHistories.add(histories);
        }
        return allHistories;
    }

    public static ArrayList<String> readFile(String filename) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(filename));
        ArrayList<String> contents = new ArrayList<>();
        try {
            String line = br.readLine();
            while (line != null)
            {
                contents.add(line);
                line = br.readLine();
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        } finally {
            br.close();
        }
        return contents;
    }
}
