import numpy as np
from perceptron import Perceptron
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

# Load iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Normalize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train one perceptron for each class (One-vs-All)
perceptrons = []
y_train_binary_all = []
y_test_pred_all = []

for target_class in range(3):
    # Create binary labels (1 for target class, 0 for others)
    y_train_binary = np.where(y_train == target_class, 1, 0)
    y_test_binary = np.where(y_test == target_class, 1, 0)
    y_train_binary_all.append(y_train_binary)
    
    # Train perceptron for this class
    perceptron = Perceptron(learning_rate=0.01, n_iter=100)
    perceptron.fit(X_train, y_train_binary)
    perceptrons.append(perceptron)
    
    # Get predictions for this class
    y_test_pred = perceptron.predict(X_test)
    y_test_pred_all.append(y_test_pred)

# Combine predictions from all perceptrons
y_test_pred_combined = np.argmax(np.array(y_test_pred_all), axis=0)

# Calculate and print metrics
print("\nClassification Report:")
print(classification_report(y_test, y_test_pred_combined, target_names=iris.target_names))

print("\nConfusion Matrix:")
conf_matrix = confusion_matrix(y_test, y_test_pred_combined)
print(conf_matrix)

# Plot confusion matrix
plt.figure(figsize=(10, 8))
plt.imshow(conf_matrix, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.colorbar()
tick_marks = np.arange(len(iris.target_names))
plt.xticks(tick_marks, iris.target_names, rotation=45)
plt.yticks(tick_marks, iris.target_names)
plt.xlabel('Predicted Label')
plt.ylabel('True Label')

# Add text annotations to the confusion matrix
thresh = conf_matrix.max() / 2
for i, j in np.ndindex(conf_matrix.shape):
    plt.text(j, i, format(conf_matrix[i, j], 'd'),
             horizontalalignment="center",
             color="white" if conf_matrix[i, j] > thresh else "black")

plt.tight_layout()
plt.show()

# Plot decision boundaries (using first two features)
plt.figure(figsize=(12, 4))

# Training data plot
plt.subplot(1, 3, 1)
for idx, species in enumerate(iris.target_names):
    plt.scatter(X_train[y_train == idx, 0], X_train[y_train == idx, 1], 
               label=species)

plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title('Training Data')
plt.legend()

# Create a mesh grid for decision boundary
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

# Plot decision boundaries for each class
for idx, (perceptron, target_name) in enumerate(zip(perceptrons, iris.target_names)):
    plt.subplot(1, 3, idx + 1)
    
    # Create mesh grid points with all features set to mean except first two
    mesh_points = np.c_[xx.ravel(), yy.ravel(), 
                       np.full(xx.ravel().shape, X[:, 2].mean()),
                       np.full(xx.ravel().shape, X[:, 3].mean())]
    
    # Get predictions for mesh points
    Z = perceptron.predict(mesh_points)
    Z = Z.reshape(xx.shape)
    
    # Plot decision boundary and training points
    plt.contourf(xx, yy, Z, alpha=0.4)
    for class_idx, species in enumerate(iris.target_names):
        plt.scatter(X_train[y_train == class_idx, 0], 
                   X_train[y_train == class_idx, 1],
                   label=species)
    
    plt.xlabel(iris.feature_names[0])
    plt.ylabel(iris.feature_names[1])
    plt.title(f'Decision Boundary for {target_name}')
    plt.legend()

plt.tight_layout()
plt.show()

# Print feature importance for each class
print("\nFeature Importance:")
for idx, (perceptron, target_name) in enumerate(zip(perceptrons, iris.target_names)):
    print(f"\nClass: {target_name}")
    for name, weight in zip(iris.feature_names, perceptron.weights):
        print(f"{name}: {weight:.4f}")
    print(f"Bias: {perceptron.bias:.4f}") 