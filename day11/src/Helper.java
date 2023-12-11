import java.io.*;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.LongStream;

public class Helper {
    public static ArrayList<String> readFile(String filename) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(new File(filename)));
        ArrayList<String> res = new ArrayList<>();
        String line = br.readLine();
        while (line != null)
        {
            res.add(line);
            line = br.readLine();
        }
        br.close();
        return res;
    }

    public static ArrayList<Point> locateGalaxies(ArrayList<String> input)
    {
        ArrayList<Point> galaxies = new ArrayList<>();
        for (int i = 0; i < input.size(); i++) {
            for (int j = 0; j < input.get(i).length(); j++) {
                if (input.get(i).charAt(j) == '#')
                    galaxies.add(new Point(i, j));
            }
        }
        return galaxies;
    }

    public static void offsetGalaxiesBy(ArrayList<Point> galaxies, int compressedGalaxySize, int offset)
    {
        Set<Long> galaxiesXPositions = galaxies.stream().map(galaxy -> galaxy.x).collect(Collectors.toSet());
        Set<Long> galaxiesYPositions = galaxies.stream().map(galaxy -> galaxy.y).collect(Collectors.toSet());
        List<Long> voidX = LongStream.rangeClosed(0, compressedGalaxySize - 1).filter(x -> !galaxiesXPositions.contains(x)).boxed().toList();
        List<Long> voidY = LongStream.rangeClosed(0, compressedGalaxySize - 1).filter(y -> !galaxiesYPositions.contains(y)).boxed().toList();

        for (Point galaxy:
            galaxies) {
            Long deltaX = voidX.stream().filter(emptyColumn -> galaxy.x > emptyColumn).count();
            Long deltaY = voidY.stream().filter(emptyLine -> galaxy.y > emptyLine).count();
            Point newPosition = galaxy.add(new Point(deltaX * (offset - 1), deltaY * (offset - 1)));
            galaxy.x = newPosition.x;
            galaxy.y = newPosition.y;
        }
    }

    public static long part_1(ArrayList<String> input) {
        ArrayList<Point> galaxies = locateGalaxies(input);
        offsetGalaxiesBy(galaxies, input.size(), 2);

        var sum = 0L;

        for (var i = 0; i < galaxies.size() - 1; i++) {
            for (var j = i; j < galaxies.size(); j++) {
                sum += galaxies.get(i).manhattan(galaxies.get(j));
            }
        }

        return sum;
    }

    public static long part_2(ArrayList<String> input) {
        ArrayList<Point> galaxies = locateGalaxies(input);
        offsetGalaxiesBy(galaxies, input.size(), 1000000);

        var sum = 0L;

        for (var i = 0; i < galaxies.size() - 1; i++) {
            for (var j = i; j < galaxies.size(); j++) {
                sum += galaxies.get(i).manhattan(galaxies.get(j));
            }
        }

        return sum;
    }
}
