import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

# Set a seed so the random numbers are predictable every time you run it
np.random.seed(42)

class KMeansAdvanced:
    def __init__(self, k=3, max_iters=100, init_method='kmeans++'):
        """
        Initializes the algorithm's settings.
        k: The number of clusters we want to find.
        max_iters: A safety net to prevent infinite loops if data won't converge.
        init_method: Can be 'random' (basic) or 'kmeans++' (advanced).
        """
        self.k = k
        self.max_iters = max_iters
        self.init_method = init_method
        self.centroids = None
        self.clusters = None

    def _euclidean_distance(self, x1, x2):
        """
        MATH FORMULA APPLIED: The Pythagorean theorem for multidimensional space.
        Calculates the straight-line distance between two data points.
        """
        return np.sqrt(np.sum((x1 - x2) ** 2))

    def _initialize_centroids(self, X):
        """
        Places the initial cluster centers (centroids) on the graph.
        """
        n_samples, n_features = X.shape
        
        if self.init_method == 'random':
            # BASIC METHOD: Pick 'k' random points from the dataset
            random_indices = np.random.choice(n_samples, self.k, replace=False)
            self.centroids = X[random_indices]
        
        elif self.init_method == 'kmeans++':
            # ADVANCED METHOD: Spatially distribute the starting centroids
            
            # 1. Pick the very first centroid completely at random
            self.centroids = [X[np.random.randint(n_samples)]]
            
            # 2. Pick the remaining (k-1) centroids
            for _ in range(1, self.k):
                distances = []
                # For every point in the dataset, find its distance to the CLOSEST existing centroid
                for x in X:
                    min_dist = min([self._euclidean_distance(x, c) for c in self.centroids])
                    distances.append(min_dist)
                
                distances = np.array(distances)
                
                # Square the distances to exaggerate them. Points further away get a higher probability weight.
                probs = distances ** 2 / np.sum(distances ** 2)
                
                # Select the next centroid randomly, but heavily favor points that are far away
                next_centroid_idx = np.random.choice(n_samples, p=probs)
                self.centroids.append(X[next_centroid_idx])
            
            self.centroids = np.array(self.centroids)

    def _assign_clusters(self, X):
        """
        EXPECTATION STEP: Groups the data.
        Calculates the distance from every point to every centroid, assigning 
        each point to whichever centroid is closest.
        """
        clusters = [[] for _ in range(self.k)] # Create empty lists for each cluster
        
        for point_idx, x in enumerate(X):
            # Calculate distance from this specific point 'x' to all centroids
            distances = [self._euclidean_distance(x, c) for c in self.centroids]
            
            # Find the index of the smallest distance
            closest_centroid_idx = np.argmin(distances)
            
            # Add the point's ID to that centroid's cluster list
            clusters[closest_centroid_idx].append(point_idx)
            
        return clusters

    def _update_centroids(self, X, clusters):
        """
        MAXIMIZATION STEP: Moves the centroids.
        Calculates the exact middle (mean) of all the points currently assigned 
        to a cluster, and moves the centroid to that coordinate.
        """
        # Create a blank array to hold the new coordinates
        new_centroids = np.zeros((self.k, X.shape[1]))
        
        for cluster_idx, cluster in enumerate(clusters):
            if len(cluster) == 0:
                # Edge case: If a cluster ended up with zero points, leave it where it is
                new_centroids[cluster_idx] = self.centroids[cluster_idx]
            else:
                # Calculate the mathematical average of all points in this cluster
                cluster_mean = np.mean(X[cluster], axis=0)
                new_centroids[cluster_idx] = cluster_mean
                
        return new_centroids

    def fit_and_visualize(self, X):
        """
        The main loop that runs the Expectation-Maximization process and plots it.
        """
        # Step 1: Place initial centroids
        self._initialize_centroids(X)
        
        for i in range(self.max_iters):
            # Step 2: Assign data points to the closest centroid
            self.clusters = self._assign_clusters(X)
            
            # PAUSE TO VISUALIZE: Plot the current state of the graph
            self.plot_iteration(X, i)
            
            # Keep a backup of the old coordinates so we can check if they moved
            old_centroids = self.centroids.copy()
            
            # Step 3: Move centroids to the center of their new clusters
            self.centroids = self._update_centroids(X, self.clusters)
            
            # Step 4: Check for Convergence (Did the centroids stop moving?)
            distances = [self._euclidean_distance(old_centroids[j], self.centroids[j]) for j in range(self.k)]
            
            if sum(distances) == 0:
                print(f"Algorithm successfully converged after {i + 1} iterations!")
                # Plot the final converged state
                self.plot_iteration(X, i + 1, final=True)
                break

    def plot_iteration(self, X, iteration, final=False):
        """
        Creates a scatter plot showing the data points and the current centroid locations.
        """
        plt.figure(figsize=(8, 5))
        # Define a color palette for our clusters
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
        
        # Draw the data points
        for cluster_idx, cluster in enumerate(self.clusters):
            points = X[cluster]
            plt.scatter(points[:, 0], points[:, 1], s=40, color=colors[cluster_idx % len(colors)], alpha=0.6)
            
        # Draw the centroids as large black stars
        plt.scatter(self.centroids[:, 0], self.centroids[:, 1], s=350, marker='*', c='black', edgecolor='white', linewidth=1.5, label='Centroids')
        
        title = f'Iteration {iteration}' if not final else 'Final Converged State'
        plt.title(title, fontsize=14, fontweight='bold')
        plt.xlabel("Feature 1")
        plt.ylabel("Feature 2")
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.4)
        
        # Display the plot
        plt.show()

# ==========================================
# RUNNING THE CODE
# ==========================================

# 1. Generate fake data (300 points naturally grouped into 4 distinct blobs)
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=1.2, random_state=42)

# 2. Initialize our advanced K-Means class looking for 4 clusters
# Try changing 'kmeans++' to 'random' to see how the initialization behaves differently!
kmeans = KMeansAdvanced(k=4, max_iters=20, init_method='kmeans++')

# 3. Run the algorithm and watch the charts generate step-by-step
kmeans.fit_and_visualize(X)