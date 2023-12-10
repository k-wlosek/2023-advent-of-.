import java.util.*;

class Graph {
    public Map<Integer[], List<Integer[]>> getAdjacencyList() {
        return adjacencyList;
    }

    private Map<Integer[], List<Integer[]>> adjacencyList;

    public Graph() {
        this.adjacencyList = new HashMap<>();
    }

    public void addVertex(Integer[] vertex) {
        adjacencyList.putIfAbsent(vertex, new ArrayList<>());
    }

    public void addEdge(Integer[] source, Integer[] destination) {

        addVertex(source);
        addVertex(destination);

        adjacencyList.get(source).add(destination);

    }

    public List<Integer[]> getAdjacentVertices(Integer[] vertex) {
        return adjacencyList.getOrDefault(vertex, new ArrayList<>());
    }

    public void printAdjacencyList() {
        for (Map.Entry<Integer[], List<Integer[]>> entry : adjacencyList.entrySet()) {
            System.out.print(Arrays.toString(entry.getKey()) + ": ");
            for (Integer[] neighbor : entry.getValue()) {
                System.out.print(Arrays.toString(neighbor) + " ");
            }
            System.out.println();
        }
    }

    public Map<Integer[], List<Integer[]>> mergeLists() {
        Map<Integer[], List<Integer[]>> mergedMap = new HashMap<>();

        for (Map.Entry<Integer[], List<Integer[]>> entry : this.adjacencyList.entrySet()) {
            Integer[] key = entry.getKey();
            List<Integer[]> value = entry.getValue();

            // If the key is already present in mergedMap, merge the lists
            if (containsKeyWithEqualElements(mergedMap, key)) {
                mergedMap.get(findKeyWithEqualElements(mergedMap, key)).addAll(value);
            } else {
                // If the key is not present, add it to mergedMap with a new list
                List<Integer[]> newList = new ArrayList<>(value);
                mergedMap.put(key, newList);
            }
        }

        return mergedMap;
    }

    private static boolean containsKeyWithEqualElements(Map<Integer[], List<Integer[]>> map, Integer[] key) {
        return map.keySet().stream().anyMatch(existingKey -> Arrays.deepEquals(existingKey, key));
    }

    private static Integer[] findKeyWithEqualElements(Map<Integer[], List<Integer[]>> map, Integer[] key) {
        return map.keySet().stream().filter(existingKey -> Arrays.deepEquals(existingKey, key)).findFirst().orElse(null);
    }
}

