import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    N = int(input("Enter the number of points (N): "))
    
    if N <= 0:
        print("Error: N must be a positive integer.")
        return
    
    k = int(input("Enter the number of neighbors (k): "))
    
    if k <= 0 or k > N:
        print("Error: k must be a positive integer less than or equal to N.")
        return
    
    X = []
    y = []
    
    for i in range(N):
        x = float(input(f"Enter x value for point {i + 1}: "))
        y_value = float(input(f"Enter y value for point {i + 1}: "))
        X.append([x])  # X should be a 2D array for sklearn
        y.append(y_value)
    
    X = np.array(X)
    y = np.array(y)
    
    variance = np.var(y)
    print(f"Variance of labels in the training dataset: {variance:.2f}")
    
    knn_regressor = KNeighborsRegressor(n_neighbors=k)
    knn_regressor.fit(X, y)
    
    X_input = float(input("Enter X for prediction: "))
    
    y_pred = knn_regressor.predict([[X_input]])
    print(f"Predicted Y for X={X_input}: {y_pred[0]:.2f}")

if __name__ == "__main__":
    main()
