# Import the necessary dataset loader to get our image data
from sklearn.datasets import load_digits

# Import the train_test_split function to divide our data for final evaluation
from sklearn.model_selection import train_test_split

# Import the RandomForestClassifier, which handles the Bagging mathematically behind the scenes
from sklearn.ensemble import RandomForestClassifier

# Import metrics to evaluate how well our forest performed
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt

""" Bagging with Random Forest :
[ ORIGINAL IMAGE DATASET ] 
(e.g., 1,437 training images of digits 0-9, each flattened into 64 pixel values)
         │
         ├─────────────────────────┬─────────────────────────┐
         ▼                         ▼                         ▼
  [ Bootstrap Sample 1 ]    [ Bootstrap Sample 2 ]    [ Bootstrap Sample 100 ]
  (Random selection of      (Random selection of      (Random selection of
   images with replacement)  images with replacement)  images with replacement)
         │                         │                         │
         ▼                         ▼                         ▼
  [ Random Feature 8 ]      [ Random Feature 12 ]     [ Random Feature 33 ]
  (Tree only looks at a     (Tree only looks at a     (Tree only looks at a
   subset of pixels,         subset of pixels,         subset of pixels,
   e.g., sqrt(64) = 8)       e.g., sqrt(64) = 8)       e.g., sqrt(64) = 8)
         │                         │                         │
         ▼                         ▼                         ▼
  [ Tree Model 1 ]          [ Tree Model 2 ]          [ Tree Model 100 ]
  (Built independently      (Built independently      (Built independently
   in PARALLEL)              in PARALLEL)              in PARALLEL)
         │                         │                         │
         └─────────────────────────┼─────────────────────────┘
                                   │
                                   ▼
                      [ MAJORITY VOTE AGGREGATION ]
                     * Tree 1 votes: "It's a 7"
                     * Tree 2 votes: "It's a 3"
                     * Tree 100 votes: "It's a 7"
                                   │
                                   ▼
                   [ FINAL PREDICTED RESULT: "7" ] 
"""


# ---------------------------------------------------------
# STEP 1: LOAD AND PREPARE THE IMAGE DATA
# ---------------------------------------------------------

# Load the digits dataset (a collection of 8x8 pixel images of numbers)
digits = load_digits()

# Extract the raw image data. 'X' is traditionally used for the input features.
# In this dataset, the 8x8 images (64 pixels) are already flattened into a 1D array of 64 numbers.
X = digits.data
print(f"Shape of the input data (X): {X.shape}")  # Should print (1797, 64) for 1,797 images of 64 pixels each.
# how print an image or example a or any 1 image 
import matplotlib.pyplot as plt

# Visualize the first image in the dataset
plt.imshow(digits.images[20], cmap='gray')
plt.title(f"True Label: {digits.target[20]}")
plt.show()

# Extract the target labels (the actual number the image represents, 0 through 9). 'y' is the target.
y = digits.target

# Split the dataset: 80% for training the forest, 20% for a final, unseen test.
# random_state=42 ensures we get the exact same random split every time we run the code.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# ---------------------------------------------------------
# STEP 2: CONFIGURE THE RANDOM FOREST (THE BAGGING PROCESS)
# ---------------------------------------------------------

# Initialize the Random Forest model with specific hyperparameters to demonstrate Bagging
rf_model = RandomForestClassifier(
    # n_estimators=100 tells the algorithm to build exactly 100 independent Decision Trees.
    # This is the "Aggregating" part of Bagging (gathering 100 votes).
    n_estimators=100,
    
    # bootstrap=True tells the algorithm to use "Sampling with Replacement" for each of the 100 trees.
    # If set to False, every tree would use the exact same dataset, ruining the ensemble effect.
    bootstrap=True,
    
    # max_features='sqrt' is the "Feature Bagging" twist. 
    # Since we have 64 pixels (features), each tree split will only randomly look at 8 pixels (sqrt of 64).
    # This forces the trees to learn different patterns and de-correlates them.
    max_features='sqrt',
    
    # oob_score=True tells the algorithm to calculate the Out-of-Bag error automatically.
    # It will test each tree on the ~36.8% of images it did NOT see during its specific bootstrap draw.
    oob_score=True,
    
    # random_state ensures reproducibility for the random bootstrapping and feature selection.
    random_state=42
)


# ---------------------------------------------------------
# STEP 3: TRAIN THE ENSEMBLE
# ---------------------------------------------------------

# The .fit() command builds the entire forest. 
# Under the hood, it creates 100 bootstrapped datasets and trains 100 independent trees in parallel.
rf_model.fit(X_train, y_train)


# ---------------------------------------------------------
# STEP 4: EVALUATE THE OUT-OF-BAG (OOB) SCORE
# ---------------------------------------------------------

# Extract the built-in OOB score calculated during training. 
# This acts as a free validation score without needing to touch our X_test data.
oob_accuracy = rf_model.oob_score_

# Print the OOB accuracy formatted as a percentage.
print(f"Out-of-Bag (OOB) Accuracy: {oob_accuracy * 100:.2f}%")


# ---------------------------------------------------------
# STEP 5: FINAL PREDICTION AND AGGREGATION
# ---------------------------------------------------------

# Pass the 20% holdout test images through the forest.
# Each of the 100 trees casts a vote for what digit they think each image is. 
# The forest automatically tallies the votes and outputs the majority winner for each image.
predictions = rf_model.predict(X_test)

# Compare the aggregated majority votes against the actual true labels to get our final accuracy.
final_accuracy = accuracy_score(y_test, predictions)

# Print the final accuracy on the unseen test data.
print(f"Final Test Accuracy: {final_accuracy * 100:.2f}%")