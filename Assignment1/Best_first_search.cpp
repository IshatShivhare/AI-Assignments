#include <bits/stdc++.h>
using namespace std;

// Define a structure to represent a graph edge
struct Edge {
    int to;
    int weight;
};

// Define the graph as an adjacency list
class Graph {
public:
    unordered_map<char, vector<Edge>> adjList;

    void addEdge(char u, char v, int weight) {
        adjList[u].push_back({v, weight});
        adjList[v].push_back({u, weight}); // For undirected graph
    }
};

// Comparator for the priority queue
struct Compare {
    bool operator()(pair<char, int> a, pair<char, int> b) {
        return a.second > b.second;
    }
};

void bestFirstSearch(Graph &graph, char start, char goal) {
    // Priority queue to pick the smallest-cost node
    priority_queue<pair<char, int>, vector<pair<char, int>>, Compare> pq;
    unordered_map<char, bool> visited;
    unordered_map<char, char> parent;

    // Add the start node with cost 0
    pq.push({start, 0});
    parent[start] = '\0'; // Mark start as root

    while (!pq.empty()) {
        char current = pq.top().first;
        int currentCost = pq.top().second;
        pq.pop();

        // Skip if already visited
        if (visited[current]) continue;
        visited[current] = true;

        // Print visiting node
        cout << "Visited Node: " << current << " with cost: " << currentCost << endl;

        // If we reach the goal, trace the path and exit
        if (current == goal) {
            cout << "Goal Node " << goal << " found!" << endl;

            // Trace path
            vector<char> path;
            for (char at = goal; at != '\0'; at = parent[at]) {
                path.push_back(at);
            }
            reverse(path.begin(), path.end());

            cout << "Path: ";
            for (char node : path) {
                cout << node << " ";
            }
            cout << endl;
            return;
        }

        // Explore neighbors
        for (auto &edge : graph.adjList[current]) {
            if (!visited[edge.to]) {
                pq.push({edge.to, edge.weight});
                parent[edge.to] = current;
            }
        }
    }

    cout << "Goal Node " << goal << " not reachable from Start Node " << start << endl;
}

int main() {
    Graph graph;
    graph.addEdge('S', 'A', 3);
    graph.addEdge('S', 'B', 6);
    graph.addEdge('S', 'C', 5);
    graph.addEdge('A', 'D', 9);
    graph.addEdge('A', 'E', 8);
    graph.addEdge('B', 'F', 12);
    graph.addEdge('B', 'G', 14);
    graph.addEdge('C', 'H', 7);
    graph.addEdge('H', 'I', 5);
    graph.addEdge('H', 'J', 6);
    graph.addEdge('I', 'K', 1);
    graph.addEdge('I', 'L', 10);
    graph.addEdge('I', 'M', 2);

    char startNode = 'S';
    char goalNode1 = 'I';
    char goalNode2 = 'J';

    cout << "Best-First Search from Node " << startNode << " to Node " << goalNode1 << ":\n";
    bestFirstSearch(graph, startNode, goalNode1);

    cout << "\nBest-First Search from Node " << startNode << " to Node " << goalNode2 << ":\n";
    bestFirstSearch(graph, startNode, goalNode2);

    return 0;
}
