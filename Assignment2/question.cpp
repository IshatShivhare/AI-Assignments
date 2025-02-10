#include <iostream>
#include <vector>
#include <cmath>

// Activation function for the perceptron
int activationFunction(float weightedSum) {
    return weightedSum >= 0 ? 1 : 0;
}

// Train perceptron using Rosenblatt's update rule
void trainPerceptron(std::vector<std::vector<int>> inputs, std::vector<int> outputs, std::vector<float>& weights, float learningRate, int epochs) {
    int n = inputs[0].size(); // Number of inputs per sample
    for (int epoch = 0; epoch < epochs; ++epoch) {
        for (size_t i = 0; i < inputs.size(); ++i) {
            float weightedSum = 0;
            for (int j = 0; j < n; ++j) {
                weightedSum += inputs[i][j] * weights[j];
            }
            int predicted = activationFunction(weightedSum);
            int error = outputs[i] - predicted;
            for (int j = 0; j < n; ++j) {
                weights[j] += learningRate * error * inputs[i][j];
            }
        }
    }
}

// Display weights
void displayWeights(const std::vector<float>& weights) {
    std::cout << "Weights: ";
    for (const auto& w : weights) {
        std::cout << w << " ";
    }
    std::cout << std::endl;
}

int main() {
    // Define logic gates and their outputs
    std::vector<std::vector<int>> ANDGateInputs = {{0, 0}, {0, 1}, {1, 0}, {1, 1}};
    std::vector<int> ANDGateOutputs = {0, 0, 0, 1};

    std::vector<std::vector<int>> ORGateInputs = {{0, 0}, {0, 1}, {1, 0}, {1, 1}};
    std::vector<int> ORGateOutputs = {0, 1, 1, 1};

    std::vector<std::vector<int>> XORGateInputs = {{0, 0}, {0, 1}, {1, 0}, {1, 1}};
    std::vector<int> XORGateOutputs = {0, 1, 1, 0};

    // Initialize weights and parameters
    std::vector<float> weights(ANDGateInputs[0].size(), 0.5); // Initial weights
    float learningRate = 0.1;
    int epochs = 100;

    // Train and display weights for AND Gate
    std::cout << "Training AND Gate...\n";
    trainPerceptron(ANDGateInputs, ANDGateOutputs, weights, learningRate, epochs);
    displayWeights(weights);

    // Reset weights and train for OR Gate
    weights.assign(weights.size(), 0.5);
    std::cout << "\nTraining OR Gate...\n";
    trainPerceptron(ORGateInputs, ORGateOutputs, weights, learningRate, epochs);
    displayWeights(weights);

    // Attempt XOR Gate (Perceptron limitation)
    weights.assign(weights.size(), 0.5);
    std::cout << "\nTraining XOR Gate...\n";
    trainPerceptron(XORGateInputs, XORGateOutputs, weights, learningRate, epochs);
    displayWeights(weights);

    std::cout << "\nNote: XOR Gate cannot be learned by a single-layer perceptron.\n";
    return 0;
}
