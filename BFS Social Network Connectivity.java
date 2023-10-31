import java.util.*;

public class SocialNetworkConnectivity {
    public static int socialNetworkConnectivity(Map<String, List<String>> graph, String sourceUser, String targetUser) {
        Queue<String> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        // Initialize the queue with the source user and mark it as visited.
        queue.add(sourceUser);
        visited.add(sourceUser);

        int separation = 0;

        while (!queue.isEmpty()) {
            int levelSize = queue.size();

            for (int i = 0; i < levelSize; i++) {
                String currentUser = queue.poll();

                // Check if the current user is the target user.
                if (currentUser.equals(targetUser)) {
                    return separation;  // Separation level between source and target users.
                }

                // Explore the friends (neighbors) of the current user.
                List<String> friends = graph.get(currentUser);
                if (friends != null) {
                    for (String friend : friends) {
                        if (!visited.contains(friend)) {
                            // Enqueue the friend and mark them as visited.
                            queue.add(friend);
                            visited.add(friend);
                        }
                    }
                }
            }

            separation++; // Increment the separation level after exploring one level of connections.
        }

        // If we reach this point, there's no connection between the source and target users.
        return -1;  // Indicate that there is no connection.
    }

    public static void main(String[] args) {
        // Define the social network graph as an adjacency list.
        Map<String, List<String>> socialNetwork = new HashMap<>();
        socialNetwork.put("Alice", Arrays.asList("Bob", "Carol"));
        socialNetwork.put("Bob", Arrays.asList("David", "Eve"));
        socialNetwork.put("Carol", Collections.singletonList("Frank"));
        socialNetwork.put("David", Collections.singletonList("Grace"));
        socialNetwork.put("Eve", Collections.emptyList());
        socialNetwork.put("Frank", Collections.emptyList());
        socialNetwork.put("Grace", Collections.emptyList());

        String sourceUser = "Alice";
        String targetUser = "Grace";

        int separation = socialNetworkConnectivity(socialNetwork, sourceUser, targetUser);
        if (separation != -1) {
            System.out.println("The degree of separation between " + sourceUser + " and " + targetUser + " is " + separation + ".");
        } else {
            System.out.println("There is no connection between " + sourceUser + " and " + targetUser + ".");
        }
    }
}
