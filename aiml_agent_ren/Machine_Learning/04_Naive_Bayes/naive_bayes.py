import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
import seaborn as sns

# ==========================================
# STEP 1: LOAD THE DATASET
# ==========================================
# Load the CSV file containing glucose, bloodpressure, and diabetes labels
csv_path = '/home/sunkeerth/archive/Naive-Bayes-Classification-Data.csv'
df = pd.read_csv(csv_path)

# Quick sanity check on the loaded data (use df.head() with parentheses to call the function)
print('--- Dataset Sample ---')
print(df.head())
print('\nTotal Records:', len(df))


# ==========================================
# STEP 2: GAUSSIAN NAIVE BAYES FROM SCRATCH
# ==========================================
class ScratchGaussianNaiveBayes:
  """Gaussian Naive Bayes implementation using Maximum A Posteriori (MAP) decision rule

  and Log-Likelihood to prevent floating-point underflow.
  """

  def fit(self, X, y):
    """TRAINING PHASE:

    Learns 3 key parameters from the dataset:
    1. Prior Probability P(y): How common each class is.
    2. Mean (mu): Center of the bell curve for each feature given class y.
    3. Variance (sigma^2): Spread of the bell curve for each feature given class
    y.
    """
    # np.unique finds all distinct labels (in our case: 0 and 1)
    self.classes = np.unique(y)
    self.params = {}

    for c in self.classes:
      # Filter data to only rows where diabetes == c
      X_c = X[y == c]

      self.params[c] = {
          # Prior P(y) = (Number of samples in class c) / (Total samples)
          'prior': len(X_c) / len(X),
          # Mean (mu) = Average feature value for class c
          'mean': X_c.mean(axis=0).values,
          # Variance (sigma^2) = Feature variance for class c (ddof=0 for population variance)
          'var': X_c.var(axis=0, ddof=0).values,
      }

  def _gaussian_log_pdf(self, x, mean, var):
    """GAUSSIAN LOG-LIKELIHOOD:

    Standard Gaussian PDF: P(x|y) = 1/sqrt(2*pi*var) * exp(-(x - mean)^2 /
    (2*var)) Taking natural log (ln) transforms multiplications into
    additions:
    ln P(x|y) = -0.5 * ln(2 * pi * var) - ((x - mean)^2) / (2 * var)
    """
    eps = 1e-9  # Tiny epsilon added to variance to prevent division by zero
    coeff = -0.5 * np.log(2 * np.pi * (var + eps))
    exponent = -0.5 * ((x - mean) ** 2) / (var + eps)
    return coeff + exponent

  def predict(self, X):
    """PREDICTION PHASE:

    For each sample, computes:
    Log-Posterior = ln P(y) + sum(ln P(x_i | y))
    Chooses the class with the highest score (argmax).
    """
    X = np.array(X)
    log_posteriors = []

    for c in self.classes:
      # Step A: Get ln P(y) (Log-Prior)
      log_prior = np.log(self.params[c]['prior'])

      # Step B: Compute log-likelihood for all features and sum them up
      # Summing over axis=1 performs the Naive independence multiplication in log-space
      log_likelihood = np.sum(
          self._gaussian_log_pdf(
              X, self.params[c]['mean'], self.params[c]['var']
          ),
          axis=1,
      )

      # Step C: Total log posterior score for class c
      log_posteriors.append(log_prior + log_likelihood)

    # Shape becomes: (num_samples, num_classes)
    log_posteriors = np.vstack(log_posteriors).T

    # Return the class label corresponding to the maximum probability score
    return self.classes[np.argmax(log_posteriors, axis=1)]


# ==========================================
# STEP 3: TRAIN & EVALUATE THE MODEL
# ==========================================
# Separate features (X) and target label (y)
X = df[['glucose', 'bloodpressure']]
y = df['diabetes']

# Instantiate and fit
model = ScratchGaussianNaiveBayes()
model.fit(X, y)

# Predict on the training data and calculate accuracy
y_pred = model.predict(X)
accuracy = np.mean(y_pred == y)
print(f'\nModel Accuracy: {accuracy * 100:.2f}%')


# ==========================================
# STEP 4: STEP-BY-STEP VISUALIZATION & SAVING
# ==========================================
# Create a figure with 3 subplots side-by-side
fig, axes = plt.subplots(1, 3, figsize=(20, 6))

# --- PLOT 1: Raw Data Distribution ---
# Visualizes raw feature points separated by class (Diabetic vs Non-Diabetic)
sns.scatterplot(
    data=df,
    x='glucose',
    y='bloodpressure',
    hue='diabetes',
    palette={0: '#1f77b4', 1: '#d62728'},
    alpha=0.6,
    ax=axes[0],
)
axes[0].set_title(
    'Step 1: Raw Data Distribution\n(Glucose vs Blood Pressure)',
    fontsize=13,
    fontweight='bold',
)
axes[0].set_xlabel('Glucose', fontsize=11)
axes[0].set_ylabel('Blood Pressure', fontsize=11)
axes[0].legend(title='Diabetes', labels=['0 (No)', '1 (Yes)'])
axes[0].grid(True, linestyle='--', alpha=0.5)

# --- PLOT 2: Fitted Gaussian Likelihood Curves ---
# Visualizes how Naive Bayes fits a 1D Normal curve P(BP | Class) for each class
x_bp_range = np.linspace(40, 110, 300)

# Extract learned parameters for blood pressure (index 1 of feature list)
mu_bp_0 = model.params[0]['mean'][1]
std_bp_0 = np.sqrt(model.params[0]['var'][1])

mu_bp_1 = model.params[1]['mean'][1]
std_bp_1 = np.sqrt(model.params[1]['var'][1])

# Plot PDF curves
axes[1].plot(
    x_bp_range,
    stats.norm.pdf(x_bp_range, mu_bp_0, std_bp_0),
    label=f'Class 0 (No): $\mu$={mu_bp_0:.1f}, $\sigma$={std_bp_0:.1f}',
    color='#1f77b4',
    lw=2.5,
)
axes[1].plot(
    x_bp_range,
    stats.norm.pdf(x_bp_range, mu_bp_1, std_bp_1),
    label=f'Class 1 (Yes): $\mu$={mu_bp_1:.1f}, $\sigma$={std_bp_1:.1f}',
    color='#d62728',
    lw=2.5,
)

axes[1].set_title(
    'Step 2: Gaussian Likelihood Fit $P(x_i|y)$\n(Blood Pressure Bell Curve)',
    fontsize=13,
    fontweight='bold',
)
axes[1].set_xlabel('Blood Pressure', fontsize=11)
axes[1].set_ylabel('Probability Density', fontsize=11)
axes[1].legend()
axes[1].grid(True, linestyle='--', alpha=0.5)

# --- PLOT 3: Decision Boundary ---
# Generate a 2D mesh grid over the feature space to evaluate predictions across the whole plane
x_min, x_max = df['glucose'].min() - 5, df['glucose'].max() + 5
y_min, y_max = df['bloodpressure'].min() - 5, df['bloodpressure'].max() + 5

gx, gy = np.meshgrid(
    np.linspace(x_min, x_max, 250), np.linspace(y_min, y_max, 250)
)
grid_coords = np.c_[gx.ravel(), gy.ravel()]

# Predict class for every point on the grid
grid_predictions = model.predict(grid_coords).reshape(gx.shape)

# Draw decision regions and overlay original data points
axes[2].contourf(gx, gy, grid_predictions, alpha=0.25, cmap='coolwarm')
axes[2].scatter(
    df['glucose'],
    df['bloodpressure'],
    c=df['diabetes'],
    cmap='coolwarm',
    edgecolors='k',
    s=25,
    alpha=0.6,
)
axes[2].set_title(
    'Step 3: Learned Decision Boundary\n(Scratch Naive Bayes Prediction Space)',
    fontsize=13,
    fontweight='bold',
)
axes[2].set_xlabel('Glucose', fontsize=11)
axes[2].set_ylabel('Blood Pressure', fontsize=11)
axes[2].grid(True, linestyle='--', alpha=0.5)

# Save the visualization plot locally
plt.tight_layout()
output_image_name = 'naive_bayes_step_by_step.png'
plt.savefig(output_image_name, dpi=300)
print(f'\nVisualization successfully saved as: {output_image_name}')

# Display window
plt.show()