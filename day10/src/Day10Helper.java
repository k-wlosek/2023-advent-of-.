import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.*;

public class Day10Helper {
    public static Integer[] findStartingPoint(ArrayList<String> puzzleInput) {
        Integer[] result = new Integer[2];
        for (int i = 0; i < puzzleInput.size(); i++) {
            char[] lineAsCharArray = puzzleInput.get(i).toCharArray();
            for (int j = 0; j < lineAsCharArray.length; j++) {
                if (lineAsCharArray[j] == 'S') {
                    result[0] = i;
                    result[1] = j;
                    return result;
                }
            }
        }
        return null;
    }

    public static ArrayList<String> MfindLoop(ArrayList<String> puzzleInput, Integer[] startingPoint) {
        int lines = puzzleInput.size();
        int lineLength = puzzleInput.get(0).length();

        Graph graph = new Graph();
        for (int k = 0; k < puzzleInput.size(); k++) {
            for (int l = 0; l < puzzleInput.get(0).length(); l++) {
                graph.addVertex(new Integer[]{k, l});
            }
        }
//        graph.printAdjacencyList();

        for (int k = 0; k < puzzleInput.size(); k++) {
            for (int l = 0; l < puzzleInput.get(0).length(); l++) {
                int i = k;
                int j = l;

                Integer[] current = new Integer[]{i, j};

                Integer[] east = new Integer[]{i, j + 1};
                Boolean canAddEast = east[1] < lineLength;

                Integer[] west = new Integer[]{i, j - 1};
                Boolean canAddWest = west[1] >= 0;

                Integer[] north = new Integer[]{i - 1, j};
                Boolean canAddNorth = north[0] >= 0;

                Integer[] south = new Integer[]{i + 1, j};
                Boolean canAddSouth = south[0] < lines;

                switch (puzzleInput.get(i).charAt(j)) {
                    case '|':
                        if (canAddNorth) graph.addEdge(current, north);
                        if (canAddSouth) graph.addEdge(current, south);
                        break;
                    case '-':
                        if (canAddEast) graph.addEdge(current, east);
                        if (canAddWest) graph.addEdge(current, west);
                        break;
                    case 'L':
                        if (canAddNorth) graph.addEdge(current, north);
                        if (canAddEast) graph.addEdge(current, east);
                        break;
                    case 'J':
                        if (canAddNorth) graph.addEdge(current, north);
                        if (canAddWest) graph.addEdge(current, west);
                        break;
                    case '7':
                        if (canAddSouth) graph.addEdge(current, south);
                        if (canAddWest) graph.addEdge(current, west);
                        break;
                    case 'F':
                        if (canAddSouth) graph.addEdge(current, south);
                        if (canAddEast) graph.addEdge(current, east);
                        break;
                    case '.':
                        break;
                    case 'S':
                        if (canAddNorth) graph.addEdge(current, north);
                        if (canAddSouth) graph.addEdge(current, south);
                        if (canAddEast) graph.addEdge(current, east);
                        if (canAddWest) graph.addEdge(current, west);
                        break;
                }
            }
        }
//        graph.printAdjacencyList();
        Map<Integer[], List<Integer[]>> fixed = graph.mergeLists();
        for (Map.Entry<Integer[], List<Integer[]>> entry : fixed.entrySet()) {
            System.out.print(Arrays.toString(entry.getKey()) + ": ");
            for (Integer[] neighbor : entry.getValue()) {
                System.out.print(Arrays.toString(neighbor) + " ");
            }
            System.out.println();
        }

        Set<Integer[]> visitedNodes = new HashSet<>();
        List<Integer[]> pathToLongestLoop = new ArrayList<>();
        pathToLongestLoop.add(startingPoint);

        List<Integer[]> loop = findLongestLoop(fixed, startingPoint);
        System.out.println("loop = " + loop);

        return new ArrayList<>();
    }

    public static List<Integer[]> findLongestLoop(Map<Integer[], List<Integer[]>> adjList, Integer[] start) {
        Set<Integer[]> visited = new HashSet<>();
        List<Integer[]> path = new ArrayList<>();
        List<Integer[]> longestLoop = new ArrayList<>();

        dfs(adjList, start, visited, path, longestLoop);

        return longestLoop;
    }

    private static void dfs(Map<Integer[], List<Integer[]>> adjList, Integer[] node, Set<Integer[]> visited, List<Integer[]> path, List<Integer[]> longestLoop) {
        visited.add(node);
        path.add(node);

        for (Integer[] neighbor : adjList.getOrDefault(node, Collections.emptyList())) {
            if (path.contains(neighbor)) {
                // Loop found
                List<Integer[]> currentLoop = new ArrayList<>(path.subList(path.indexOf(neighbor), path.size()));
                if (currentLoop.size() > longestLoop.size()) {
                    longestLoop.clear();
                    longestLoop.addAll(currentLoop);
                }
            }

            if (!visited.contains(neighbor)) {
                dfs(adjList, neighbor, visited, path, longestLoop);
            }
        }

        path.remove(path.size() - 1);  // Backtrack
    }
}
