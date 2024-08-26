import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def read_pairs(n, dataset_name=""):
    pairs = []
    for i in range(n):
        x = float(input(f"Enter x value for pair {i+1} in {dataset_name}: "))
        y = int(input(f"Enter y value for pair {i+1} in {dataset_name}: "))
        pairs.append((x, y))
    return np.array(pairs)

def knn_classifier():
    N = int(input("Enter the number of training pairs (N): "))
    print("Please provide the training pairs (x, y):")
    TrainS = read_pairs(N, "TrainS")
    X_train = TrainS[:, 0].reshape(-1, 1)
    y_train = TrainS[:, 1]

    M = int(input("Enter the number of test pairs (M): "))
    print("Please provide the test pairs (x, y):")
    TestS = read_pairs(M, "TestS")
    X_test = TestS[:, 0].reshape(-1, 1)
    y_test = TestS[:, 1]

    best_k = 1
    best_accuracy = 0

    for k in range(1, 11):
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(X_train, y_train)
        y_pred = knn.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        print(f"Accuracy for k={k}: {accuracy:.4f}")

        if accuracy > best_accuracy:
            best_k = k
            best_accuracy = accuracy

    print(f"\nThe best k value is: {best_k}")
    print(f"The corresponding test accuracy is: {best_accuracy:.4f}")

# Run the kNN classifier function
if __name__ == "__main__":
    knn_classifier()
