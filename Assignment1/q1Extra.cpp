#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> readEdgesFromFile(const string& filename) {
    vector<vector<int>> matrix;
    ifstream file(filename);
    string line;
    while (getline(file, line)) {
        vector<int> row;
        istringstream stream(line);
        int number;
        while (stream >> number) {
            row.push_back(number);
        }
        matrix.push_back(row);
    }
    file.close();
    return matrix;
}

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
    cout << "Enter the adjacency matrix: " << endl;
    vector<vector<int>> edges = readEdges();
    
    Graph g(edges);
    g.printGraph();

    int startVertex;
    cout << "Enter the start vertex for DFS: ";
    cin >> startVertex;
    g.DFS(startVertex);
    
    return 0;
}