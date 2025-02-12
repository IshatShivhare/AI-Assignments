#include <bits/stdc++.h>
using namespace std;

class Graph {
private:
    int numVertices;
    vector<list<int>> adjLists;

public:
    Graph(int numVertices) {
        this->numVertices = numVertices;
        adjLists.resize(numVertices);
    }

    void addEdge(int src, int dest) {
        adjLists[src].push_back(dest);
        adjLists[dest].push_back(src);
    }

    void printGraph() {
        for (int i = 0; i < numVertices; ++i) {
            cout << "Vertex " << i << ":";
            for (int vertex : adjLists[i]) {
                cout << " -> " << vertex;
            }
            cout << endl;
        }
    }

    void DFSUtil(int v, vector<bool>& visited) {
        visited[v] = true;
        cout << v << " ";

        for (int i : adjLists[v]) {
            if (!visited[i]) {
                DFSUtil(i, visited);
            }
        }
    }

    void DFS(int startVertex) {
        vector<bool> visited(numVertices, false);
        DFSUtil(startVertex, visited);
    }


};

int main() {

    cout << "\n Quedtion 1 \n";

    Graph g1(5);

    g1.addEdge(0, 3);
    g1.addEdge(0, 4);
    g1.addEdge(1, 3);
    g1.addEdge(1, 4);
    g1.addEdge(2, 3);
    g1.addEdge(2, 4);

    cout << "Graph 1:" << endl;
    g1.printGraph();
    cout << "DFS traversal starting from vertex 0:" << endl;
    g1.DFS(0);

    cout << endl;
    Graph g2(5);
    g2.addEdge(0, 1);
    g2.addEdge(0, 2);
    g2.addEdge(0, 3);
    g2.addEdge(1, 2);
    g2.addEdge(2, 4);
    cout << "Graph 2:" << endl;
    g2.printGraph();
    cout << "DFS traversal starting from vertex 0:" << endl;
    g2.DFS(0);

    return 0;
}