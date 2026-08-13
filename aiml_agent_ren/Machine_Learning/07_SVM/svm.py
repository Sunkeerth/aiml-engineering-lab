import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import make_blobs,make_circles

def plot_svm_2d():
    """
    Creates a linearly separable 2D dataset and fits a standard Linear SVM.
    Visualizes the data points, the hyperplane (decision boundary), and the margins.
    """
    print("Generating 2D Linear SVM Plot...")
    
    # 1. Generate a dataset with 2 distinct clusters (e.g., Apples and Lemons)
    # Centers=2 ensures binary classification. random_state ensures reproducibility.
    X, y = make_blobs(n_samples=100, centers=2, random_state=6, cluster_std=1.2)

    # 2. Initialize and train the Support Vector Machine
    # We use a 'linear' kernel because the data can be separated by a straight line
    # C is a large number (1000) to enforce a strict "Hard Margin"
    model = svm.SVC(kernel='linear', C=1000)
    model.fit(X, y)

    # 3. Set up the Matplotlib figure
    plt.figure(figsize=(8, 6))
    
    # Plot the data points, coloring them based on their class (y)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn', edgecolors='k')

    # 4. Create a grid of points to evaluate the model across the whole plot
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # Create a 30x30 meshgrid covering the plot area
    xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 30),
                         np.linspace(ylim[0], ylim[1], 30))
    
    # Flatten the grid, predict the distance to the boundary for each point
    Z = model.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # 5. Plot the decision boundary and the margins
    # level=0 is the hyperplane. levels=[-1, 1] are the margin boundaries
    ax.contour(xx, yy, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
               linestyles=['--', '-', '--'])

    # 6. Highlight the Support Vectors (the points resting exactly on the margins)
    ax.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], 
               s=150, linewidth=2, facecolors='none', edgecolors='blue', 
               label='Support Vectors')

    plt.title("2D Linear SVM (Maximized Margin)")
    plt.xlabel("Feature 1 (e.g., Weight)")
    plt.ylabel("Feature 2 (e.g., Redness)")
    plt.legend()
    plt.show()

def plot_svm_3d():
    """
    Creates a non-linear circular dataset that cannot be separated in 2D.
    Manually applies a mathematical transformation (Kernel Trick) to project 
    the data into 3D, allowing a flat plane to separate the classes.
    """
    print("Generating 3D Kernel Trick Plot...")
    
    # 1. Generate a non-linear dataset (a circle within a circle)
    # factor=0.3 controls how small the inner circle is compared to the outer
    X, y = make_circles(n_samples=200, factor=0.3, noise=0.05, random_state=0)

    # 2. The Kernel Transformation Function
    # We create a 3rd dimension (Z) based on the distance from the center.
    # Mathematically: Z = e^(-(X1^2 + X2^2)) -> A Radial Basis-style transformation
    def calculate_3d_projection(X):
        return np.exp(-(X[:, 0]**2 + X[:, 1]**2))
    
    # Calculate the new Z axis for all points
    Z_axis = calculate_3d_projection(X)

    # 3. Set up a 3D Matplotlib figure
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the points in 3D space. 
    # Notice how the inner circle (red) gets pushed up, and the outer circle (yellow) stays low.
    ax.scatter3D(X[:, 0], X[:, 1], Z_axis, c=y, s=50, cmap='autumn', edgecolors='k')

    # 4. Draw a flat 2D plane cutting through the 3D space
    # This plane perfectly separates the high red points from the low yellow points
    xx, yy = np.meshgrid(np.linspace(-1.5, 1.5, 10), np.linspace(-1.5, 1.5, 10))
    
    # Z=0.5 is an arbitrary flat height for visual demonstration of a hyperplane
    zz = np.full(xx.shape, 0.5) 
    ax.plot_surface(xx, yy, zz, alpha=0.3, color='blue')

    ax.set_title("3D Projection (The Kernel Trick)")
    ax.set_xlabel("X1")
    ax.set_ylabel("X2")
    ax.set_zlabel("Z (Calculated 3rd Dimension)")
    
    # Adjust viewing angle for better visibility
    ax.view_init(elev=20, azim=45)
    plt.show()

def main():

    """
    Main function to execute the SVM visualizations.
    """
    # plot_svm_2d()
    plot_svm_3d()

if __name__== "__main__":
    main()
