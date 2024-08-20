import numpy as np
from sklearn.metrics import precision_score, recall_score

def get_user_input():
    N = int(input("Enter the number of (x, y) points: "))
    points = np.zeros((N, 2), dtype=int)  # Initialize an N x 2 array
    
    for i in range(N):
        x = int(input(f"Enter x value for point {i+1} (0 or 1): "))
        y = int(input(f"Enter y value for point {i+1} (0 or 1): "))
        points[i] = [x, y]
    
    return points

def calculate_metrics(points):
    X = points[:, 0]  # Ground truth (correct) class labels
    Y = points[:, 1]  # Predicted class labels

    precision = precision_score(X, Y)
    recall = recall_score(X, Y)
    
    return precision, recall

def main():
    points = get_user_input()
    precision, recall = calculate_metrics(points)
    
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()
