import numpy as np

class KNNRegression:
    def __init__(self, k):
        self.k = k
        self.data_points = np.empty((0, 2))  # Initialize an empty array for storing (x, y) points

    def add_point(self, x, y):
        point = np.array([[x, y]])
        self.data_points = np.vstack((self.data_points, point))

    def predict(self, x):
        if self.data_points.shape[0] < self.k:
            raise ValueError("Not enough data points for the given k")
        
        distances = np.abs(self.data_points[:, 0] - x)
        nearest_indices = np.argsort(distances)[:self.k]
        nearest_y = self.data_points[nearest_indices, 1]
      
        return np.mean(nearest_y)

def main():
    try:
        N = int(input("Enter the number of data points (N): "))
        if N <= 0:
            raise ValueError("N must be a positive integer")

        k = int(input("Enter the number of neighbors (k): "))
        if k <= 0:
            raise ValueError("k must be a positive integer")

        knn = KNNRegression(k)

        for _ in range(N):
            x = float(input("Enter x value: "))
            y = float(input("Enter y value: "))
            knn.add_point(x, y)

        X = float(input("Enter the X value for prediction: "))

        result = knn.predict(X)
        print(f"The predicted Y value is: {result}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
