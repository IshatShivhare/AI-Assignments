#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> readEdges() {
    vector<vector<int>> matrix;
    string line;
    while (getline(cin, line) && !line.empty()) {
        vector<int> row;
        istringstream stream(line);
        int number;
        while (stream >> number) {
            row.push_back(number);
        }
        matrix.push_back(row);
    }
    return matrix;
}

class Graph {
private:
    int numVertices;
    vector<vector<int>> adjLists;

public:
    Graph(vector<vector<int>> edges) {
        numVertices = edges.size();
        adjLists.resize(numVertices);
        for (int i = 0; i < numVertices; ++i) {
            for (int j = 0; j < numVertices; ++j) {
                if (edges[i][j] == 1) {
                    adjLists[i].push_back(j);
                }
            }
        }        
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
    void BFS(int startVertex) {
        vector<bool> visited(numVertices, false);
        queue<int> q;

        visited[startVertex] = true;
        q.push(startVertex);

        while (!q.empty()) {
            int v = q.front();
            cout << v << " ";
            q.pop();

            for (int i : adjLists[v]) {
                if (!visited[i]) {
                    visited[i] = true;
                    q.push(i);
                }
            }
        }
    }
};

int main() {
    cout << "Question 2" << endl;
    cout << "Enter the adjacency matrix: " << endl;
    vector<vector<int>> edges = readEdges();
    
    Graph g(edges);
    g.printGraph();

    int startVertex;
    cout << "Enter the start vertex for BFS: ";
    cin >> startVertex;
    g.BFS(startVertex);
   
}