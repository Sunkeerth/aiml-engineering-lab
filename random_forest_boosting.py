# ==========================================
# STEP 1: Import Required Libraries
# ==========================================
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report

print("Libraries imported successfully!\n")

# ==========================================
# STEP 2: Load the Image Dataset
# ==========================================
# We load the digits dataset. It contains 1,797 images of handwritten digits (0 through 9).
# Each image is small: 8x8 pixels in grayscale.
digits = datasets.load_digits()
#  i need an image to show in the terminal so i can visually see it 


# 'images' contains the raw 2D grid structure (8x8 matrices) for viewing purposes
image_samples = digits.images

# 'data' automatically flattens the 8x8 grid into a 1D row of 64 pixel-features (columns)
# This format is required so a boosting algorithm can read it like a table.
X = digits.data  
y = digits.target  

print(f"Shape of the input data (X): {X.shape}")  # Should print (1797, 64) for 1,797 images of 64 pixels each.
print(f"Shape of the target data (y): {y.shape}")
#  show an input image in the terminal so i can visually see it
print(f"Total images loaded: {X.shape[0]}")
print(f"Each image is flattened into: {X.shape[1]} features (pixel intensity values)")
print(f"Target classes (labels): {set(y)}")


# ==========================================
# STEP 3: Visualize a Sample Image (Optional)
# ==========================================
# Let's look at what one of these image inputs looks like
plt.figure(figsize=(3, 3))
plt.imshow(image_samples[1], cmap=plt.cm.gray_r, interpolation='nearest')
plt.title(f"Label/Target: {y[1]}")
plt.axis('off')
plt.show()

# ==========================================
# STEP 4: Split Data into Training and Testing Sets
# ==========================================
# 80% of the images are used to train our boosting trees, 20% are kept hidden to test it.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training set size: {X_train.shape[0]} images")
print(f"Testing set size:  {X_test.shape[0]} images\n")

# ==========================================
# STEP 5: Initialize and Train the Boosting Model
# ==========================================
# We use Gradient Boosting. Behind the scenes, it will build sequential decision trees 
# where each tree tries to correct the classification errors of the previous trees.
# 
# Parameters explained:
# - n_estimators=100: We will build 100 sequential trees.
# - learning_rate=0.1: The 'baby step' shrink factor to prevent overfitting.
# - max_depth=3: Limits how deep each individual tree can grow.
boosting_model = GradientBoostingClassifier(
    n_estimators=100, 
    learning_rate=0.1, 
    max_depth=3, 
    random_state=42
)

print("Training the Boosting model (this may take a few seconds)...")
boosting_model.fit(X_train, y_train)
print("Training complete!\n")

# ==========================================
# STEP 6: Make Predictions and Evaluate
# ==========================================
# Pass our hidden test images into the trained boosting ensemble
y_pred = boosting_model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%\n")

# Print detailed precision/recall performance per digit number
print("Detailed Classification Report:")
print(classification_report(y_test, y_pred))

# ==========================================
# STEP 7: Test Prediction on a New Sample Image
# ==========================================
# Let's test predicting a single unseen test image index, say index 10
sample_index = 10
single_image_features = X_test[sample_index].reshape(1, -1) # Reshape back to 2D row format for model
predicted_digit = boosting_model.predict(single_image_features)[0]
actual_digit = y_test[sample_index]

print(f"Boosting Model Predicted Digit: {predicted_digit}")
print(f"Actual True Digit: {actual_digit}")