# ==============================================================================
# STEP 1: IMPORT REQUIRED LIBRARIES
# ==============================================================================

# Import pyplot from matplotlib as 'plt' so we can create custom-sized figures,
# add titles, and render visual diagrams on our screen.
import matplotlib.pyplot as plt

# Import the built-in 'load_iris' function from scikit-learn's datasets module
# so we can load a clean, beginner-friendly dataset without downloading files.
from sklearn.datasets import load_iris

# Import 'train_test_split' from scikit-learn's model_selection module to
# slice our dataset into separate training and testing portions.
from sklearn.model_selection import train_test_split

# Import 'DecisionTreeClassifier' (the machine learning algorithm) and
# 'plot_tree' (the visualization tool) from scikit-learn's tree module.
from sklearn.tree import DecisionTreeClassifier, plot_tree

# ==============================================================================
# STEP 2: LOAD DATA & SEPARATE FEATURES FROM LABELS
# ==============================================================================

# Call load_iris() and store the entire dataset object (features, labels, and
# metadata) into a variable named 'iris'.
iris = load_iris()

# Extract the 2D feature matrix (150 flowers x 4 measurements: sepal/petal
# length/width) into 'x' so the model has the input clues it needs to learn.
x = iris.data

# Extract the 1D target array (150 correct flower category numbers: 0, 1, or 2)
# into 'y' so we can show the model the correct answers during training.
y = iris.target

# ==============================================================================
# STEP 3: SPLIT DATA INTO TRAINING (80%) AND TESTING (20%) SETS
# ==============================================================================

# Split 'x' and 'y' into four distinct arrays: x_train, x_test, y_train, y_test.
# test_size=0.2 holds out 20% (30 flowers) as an untouched final exam.
# random_state=42 locks the random shuffle seed so that we get the exact same
# 80/20 data split every time we run the script (essential for reproducibility).
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# ==============================================================================
# STEP 4: CREATE & TRAIN THE DECISION TREE MODEL
# ==============================================================================

# Create an untrained Decision Tree model object and configure its rules:
# criterion='entropy' tells the tree to use Information Gain / Entropy to pick splits.
# max_depth=3 stops the tree from growing more than 3 levels deep to prevent overfitting.
# random_state=42 ensures tie-breaker splits are decided identically every time.
model = DecisionTreeClassifier(
    criterion="entropy", max_depth=3, random_state=42
)

# Train the model by feeding it the training features (x_train) and their correct
# labels (y_train). This is where the mathematical splitting rules are learned.
model.fit(x_train, y_train)

# ==============================================================================
# STEP 5: EVALUATE MODEL ACCURACY ON UNSEEN TEST DATA
# ==============================================================================

# Test the trained model on x_test, compare its predictions against the true
# answers in y_test, and store the accuracy decimal (e.g., 0.9667) in 'accuracy'.
accuracy = model.score(x_test, y_test)

# Print the accuracy score formatted to two decimal places (e.g., "96.67%")
# so we can immediately see how well our model performs on unseen data.
print(f"Accuracy: {accuracy * 100:.2f}%")

# ==============================================================================
# STEP 6: DRAW & DISPLAY THE VISUAL DECISION TREE DIAGRAM
# ==============================================================================

# Create a blank plot figure 14 inches wide by 8 inches tall at 100 DPI
# resolution so the node boxes and text aren't cramped or blurry.
plt.figure(figsize=(14, 8), dpi=100)

# Draw the trained tree flowchart using plot_tree():
# feature_names replaces "X[0]" with readable names like "petal length (cm)".
# class_names=list(...) replaces class numbers (0,1,2) with flower names ("setosa", etc.).
# filled=True color-codes nodes by their majority class and purity level.
# rounded=True gives the boxes rounded corners for a cleaner aesthetic.
# fontsize=10 sets the internal box text size to be legible.
plot_tree(
    model,
    feature_names=iris.feature_names,
    class_names=list(iris.target_names),
    filled=True,
    rounded=True,
    fontsize=10,
)

# Add a clear title centered above the tree diagram.
plt.title("Decision Tree Classifier - Iris Dataset", fontsize=14)

# Adjust padding automatically so the tree fits within the canvas margins.
plt.tight_layout()

# Render the final diagram window on the screen for inspection.
plt.show()