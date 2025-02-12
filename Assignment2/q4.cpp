#include <iostream> 
#include <vector> 
#include <cmath> 
using namespace std; 
class Perceptron { 
private: 
int n; 
string str; 
vector<vector<int>> inputs; 
vector<int> outputs; 
vector<int> weights; 
 
    void generateInputs() { 
        int rows = 1 << n; 
        inputs.resize(rows, vector<int>(n + 1)); 
        for (int i = 0; i < rows; ++i) { 
            for (int j = 0; j < n; ++j) { 
                inputs[i][j] = (i & (1 << j)) ? 1 : 0; 
            } 
            inputs[i][n] = (outputs[i] == 0) ? -1 : 1; 
        } 
    } 
 
    void train() { 
        while (true) { 
            bool changed = false; 
            for (int i = 0; i < inputs.size(); ++i) { 
                int sum = weights[0]; 
                for (int j = 0; j < n + 1; ++j) { 
                    sum += weights[j + 1] * inputs[i][j]; 
                } 
                int pred = (sum >= 0) ? 1 : 0; 
                int diff = outputs[i] - pred; 
                if (diff != 0) { 
                    changed = true; 
                    weights[0] += diff; 
                    for (int j = 0; j < n + 1; ++j) { 
                        weights[j + 1] += diff * inputs[i][j]; 
                    } 
                } 
            } 
            if (!changed) break; 
        } 
        printWeights(); 
    } 
 
    void printWeights() { 
        cout << str << " -> Weights" << endl; 
        for (int i = 0; i < weights.size(); ++i) { 
            cout << "W" << i << " = " << weights[i] << " "; 
        } 
        cout << endl; 
    } 
 
public: 
    Perceptron(int n, string str, vector<int> outputs) { 
        this->n = n; 
        this->str = str; 
        this->outputs = outputs; 
        weights.resize(n + 2, 0); 
        generateInputs(); 
        train(); 
    } 
}; 
 
int main() { 
    Perceptron p1(2, "x XOR y", {0, 1, 1, 0}); 
    Perceptron p2(3,"x XOR y XOR z",{0,1,1,0,1,0,0,1}); 
    return 0; 
} 