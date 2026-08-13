import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

"""THE CONSTRUCTOR (__init__): Runs automatically during object creation.
    It sets up learning controls and builds empty internal memory slots. 
    
    1. Learning Rate (α): The size of the steps taken down the error hill.
            self.lr = learning_rate
    2. Iterations: Total number of times the model loops to learn from data.
             self.n_iterations = n_iterations
    3. Weights Placeholder: Sitting empty (None) because the model does 
        not know how many input columns (features) exist until fit() is called.
            self.weights = None
    4. Bias Placeholder: Sitting empty (None) because the model does not
        know how many input columns (features) exist until fit() is called.
            self.bias = None
    5. History Tracker: An empty list bucket used to store the loss score 
        at every single loop iteration so we can plot the progress chart later.
            self.loss_history = []
"""

class LogisticRegressionFromScratch:
    def __init__(self,learning_rate=0.1,n_iterations=1000):
        self.lr=learning_rate
        self.n_iterations=n_iterations
        self.weights=None
        self.bias=None
        self.loss_history=[]

    def _sigmoid(self,z):
        z=np.clip(z,-500,500)
        # When Python tries to calculate np.exp(-z) with an extreme negative number (like e^(3500)), the value becomes so massive that the computer runs out of memory. This triggers a nasty error called "Numerical Overflow" and crashes your script.
        # np.clip(z, -500, 500) solves this by forcing all numbers to stay within a safe zone:
        return 1.0/(1.0+np.exp(-z))
        # S-Curve Formula: Returns 1.0 for high values, 0.0 for low values,
        #    and exactly 0.5 when z is 0.

    # =========================================================================
    # THE LOSS CALCULATOR: Computes the overall average Binary Cross-Entropy 
    # score for the dataset. Uses an epsilon buffer to prevent math crashes.
    # =========================================================================
    def _compute_loss(self, y_true, y_pred):
        # 1. Total Rows: Get total number of data points to compute an average.
        m = len(y_true)
        
        # 2. Safety Buffer (Epsilon): A tiny number (0.000000000000001) used 
        #    to prevent the computer from ever calculating log(0).
        eps = 1e-15
        
        # 3. Apply Guardrail: Squeezes predictions slightly inside [eps, 1-eps] 
        #    so that no prediction is a perfect 0 or 1, protecting the log math.
        y_pred = np.clip(y_pred, eps, 1 - eps)
        
        # 4. Math Execution: Sums up single row log-penalties, divides by total 
        #    rows 'm' to get the average, and flips the sign to positive.
        loss = -(1 / m) * np.sum(
            y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred)
        )
        return loss
        # =========================================================================
    # THE TRAINING ENGINE (fit): Runs the optimization loop over the data.
    # It initializes weights to 0, checks errors, and applies gradient updates.
    # =========================================================================
    def fit(self, X, y):
        # 1. Inspect Data: Extract number of rows (samples) and columns (features).
        n_samples, n_features = X.shape
        # X.shape: Reads your input data grid (matrix). n_samples is the number of rows, and n_features is the number of columns (features).
        
        # 2. Reset Brain: Start training with weights at 0.0 for every column,
        #    and the base bias offset at 0.0.
        self.weights = np.zeros(n_features)
        self.bias = 0.0

        # 3. Optimization Loop: Train repeatedly for 'n_iterations' rounds.
        for i in range(self.n_iterations):
            # Step A: Compute raw linear combinations (z = w*x + b)
            linear_model = np.dot(X, self.weights) + self.bias
            # np.dot(X, self.weights): Multiplies every single feature value by its matching weight and adds them together. This is the straight-line linear regression calculation.
            
            # Step B: Pass z through Sigmoid curve to get probability outputs (ŷ)
            y_pred = self._sigmoid(linear_model)
            # self._sigmoid(...): Immediately takes that straight-line answer and passes it through the S-curve function we just reviewed. This outputs a clean list of predicted probabilities (y_pred) between 0 and 1.

            # Step C: Compute slopes (gradients) using clean calculus forms.
            # Multiply transposed features (X.T) by raw error to see column blame.
            dw = (1 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / n_samples) * np.sum(y_pred - y)
            # Subtracts the true answers from the model's guesses. This is the raw error.np.dot(X.T, ...): This is matrix multiplication math at lightning speed. It flips the data matrix (X.T means transpose)
            #  and multiplies it by the errors. This isolates how much each individual feature's weight is to blame for the incorrect guess.(1 / n_samples): Divides by the total rows to get the average slope, matching the exact calculus miracle formulas we documented earlier.

            # Step D: Apply Gradient Descent step to tweak weights and bias down the hill.
            self.weights -= self.lr * dw
            # -= self.lr * dw: The minus-equals sign is critical! It means "step down the hill". The code multiplies the slope (dw) by the learning rate (self.lr) and subtracts it from the current weights to adjust them toward accuracy.
            self.bias -= self.lr * db

            # Step E: Score the current performance and append it to our progress tracking log.
            loss = self._compute_loss(y, y_pred)
            self.loss_history.append(loss)

    def predict_proba(self,X):

        # np.dot(X, self.weights) + self.bias: It takes the input features of your new data (X), multiplies them by the finalized, smart self.weights, and adds the self.bias. This gives you a raw, unbounded linear score (\(z\))
        linear_model=np.dot(X,self.weights)+self.bias
        return self._sigmoid(linear_model)
        # return self._sigmoid(linear_model): It immediately passes that raw linear score into your safe _sigmoid function. This squishes the raw score into a clean probability percentage.


    def predict(self,X,threshold=0.5):
        probabilities=self.predict_proba(X)
        # What it does: It calls the function we just looked at to get the exact decimal probability scores (between 0.0 and 1.0) for your input data X.
        # Applying the Decision Gate (The Threshold) . (probabilities >= threshold) 
        return (probabilities>=threshold).astype(int)
        # 2. Filter and Convert: Checks if probability passes the decision gate,
        #    then .astype(int) flips True to 1 and False to 0.

if __name__=="__main__":
    X,y=make_classification(n_samples=200,n_features=2,n_redundant=0,n_clusters_per_class=1,random_state=42)
    #  It generates a synthetic, clean toy dataset.n_samples=200: Creates 200 virtual data rows.n_features=2: Creates 2 columns (Feature 1 and Feature 2) so we can easily plot them on a 2D X, Y graph.random_state=42: Locks the random number generator. This guarantees you get the exact same dataset every single time you hit run.
    model=LogisticRegressionFromScratch(learning_rate=0.1,n_iterations=1000)
    #  Calls the constructor __init__ that you commented earlier, configures the settings, and triggers the fit engine loop to calculate the smart weights over 1,000 iterations.
    model.fit(X,y)

    fig,(ax1,ax2)=plt.subplots(1,2,figsize=(14,5))
    # What it does: Creates a single wide window (fig) split neatly into two separate side-by-side plotting zones: ax1 (Left Side) and ax2 (Right Side).

    # Left: Loss History
    ax1.plot(model.loss_history, color="navy", lw=2)
    # What it does: Creates a single wide window (fig) split neatly into two separate side-by-side plotting zones: ax1 (Left Side) and ax2 (Right Side).
    ax1.set_title("Training Loss (Binary Cross-Entropy)")
    ax1.set_xlabel("Iteration")
    ax1.set_ylabel("Loss")
    ax1.grid(True, linestyle="--", alpha=0.6)

    # Right: Decision Boundary
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                         np.linspace(y_min, y_max, 200))
    # Finds the minimum and maximum boundaries of your dataset points and creates a massive grid mesh (a dense matrix of 40,000 miniature coordinates) to paint the background. 

    grid_points = np.c_[xx.ravel(), yy.ravel()]
    probs = model.predict_proba(grid_points).reshape(xx.shape)
    # What it does: Passes all 40,000 background grid points through your predict_proba function to see what probability score your model assigns to every single spot on the map.

    ax2.contourf(xx, yy, probs, levels=20, cmap="RdBu", alpha=0.6)
    ax2.contour(xx, yy, probs, levels=[0.5], colors="black", linewidths=2)
    # contourf: Fills the background with color based on confidence. Safe Class 0 regions are painted in shades of red, and Class 1 regions are painted in shades of blue.
    # contour: Draws a solid black line exactly where the model calculates a 0.5 (50%) probability. This is your model's decision boundary wall.
    ax2.scatter(X[y==0, 0], X[y==0, 1], color="red", edgecolor="k", label="Class 0")
    ax2.scatter(X[y==1, 0], X[y==1, 1], color="blue", edgecolor="k", label="Class 1")
    # contourf: Fills the background with color based on confidence. Safe Class 0 regions are painted in shades of red, and Class 1 regions are painted in shades of blue.contour: Draws a solid black line exactly where the model calculates a 0.5 (50%) probability. This is your model's decision boundary wall.s
    ax2.set_title("Decision Boundary (Threshold = 0.5)")
    ax2.set_xlabel("Feature 1")
    ax2.set_ylabel("Feature 2")
    ax2.legend()
    
    plt.tight_layout()
    plt.show()