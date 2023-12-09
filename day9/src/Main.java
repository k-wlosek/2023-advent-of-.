import java.io.IOException;
import java.util.ArrayList;

// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) throws IOException {
        ArrayList<String> contents = Helper.readFile("input");
        ArrayList<ArrayList<ArrayList<Integer>>> allHistories = Helper.createHistories(contents);
        Integer sum = solve_part1(allHistories);
        System.out.println("sum = " + sum);

        // Ensure part1 solution doesn't interfere with part2
        allHistories = Helper.createHistories(contents);
        Integer sum2 = solve_part2(allHistories);
        System.out.println("sum2 = " + sum2);
    }

    public static Integer solve_part1(ArrayList<ArrayList<ArrayList<Integer>>> allHistories)
    {
        for (ArrayList<ArrayList<Integer>> history:
             allHistories) {
            for (int i = history.size()-1; i >= 0; i--) {
                ArrayList<Integer> current = history.get(i);
                // Check if all values in a list are the same
                boolean allSame = current.stream().allMatch(num -> num.equals(current.get(0)));
                if (allSame)
                {
                    // If all the same, add last value
                    current.add(current.get(current.size()-1));
                }
                else
                {
                    // Add value that is last_in_previous + last_in_current
                    ArrayList<Integer> previous = history.get(i+1);
                    current.add(
                            previous.get(previous.size()-1) + current.get(current.size()-1)
                    );
                }
            }
        }
        // Collect last values
        Integer sum = 0;
        for (ArrayList<ArrayList<Integer>> history:
             allHistories) {
            ArrayList<Integer> firstList = history.get(0);
            sum += firstList.get(firstList.size()-1);
        }
        return sum;
    }

    public static Integer solve_part2(ArrayList<ArrayList<ArrayList<Integer>>> allHistories)
    {
        for (ArrayList<ArrayList<Integer>> history:
                allHistories) {
            for (int i = history.size()-1; i >= 0; i--) {
                ArrayList<Integer> current = history.get(i);
                // Check if all values in a list are the same
                boolean allSame = current.stream().allMatch(num -> num.equals(current.get(0)));
                if (allSame)
                {
                    // If all the same, prepend first value
                    current.add(0, current.get(0));
                }
                else
                {
                    // Add value that is first_in_current - first_in_previous
                    ArrayList<Integer> previous = history.get(i+1);
                    current.add(
                            0,
                            current.get(0) - previous.get(0)
                    );
                }
            }
        }
        // Collect first values
        Integer sum = 0;
        for (ArrayList<ArrayList<Integer>> history:
                allHistories) {
            ArrayList<Integer> firstList = history.get(0);
            sum += firstList.get(0);
        }
        return sum;
    }

}