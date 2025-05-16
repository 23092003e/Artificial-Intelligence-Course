import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.01, n_iter=1000):
        self.learning_rate = learning_rate
        self.n_iter = n_iter
        self.weights = None
        self.bias = None
        
    def fit(self, X, y):
        """
        Train the perceptron using training data
        
        Parameters:
        X: {array-like}, shape = [n_samples, n_features]
            Training vectors, where n_samples is the number of samples and n_features is the number of features.
        y: array-like, shape = [n_samples]
            Target values.
        """
        
        n_samples, n_features = X.shape
        
        #Initialize weights and bias
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Learning loop
        for _ in range(self.n_iter):
            for idx, x_i in enumerate(X):
                # Calculate prediction
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_function(linear_output)
                
                # Update weights and bias
                update = self.learning_rate * (y[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update
                
    def predict(self, X):
        """ 
        Predict using the perceptron
        
        Parameters:
        
        X: numpy arrray of shape (n_samples, n_features)
        Return:
        y_predicted: numpt array of shape (n_samples,)

        """
        
        linear_output = np.dot(X, self.weights) + self.bias
        return self.activation_function(linear_output)
    
    def activation_function(self, x):
        "Step function as activation function"
        return np.where(x >= 0, 1, 0)

    def calculate_error(self, X, y):
        "Error rate of the model"
        predictions = self.predict(X)
        
        error = np.mean(predictions != y)
        return error

    