import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")
plt.rcParams.update({"font.size": 10, "figure.autolayout": True})

# ---------------------------------------------------------
# 1. DATA INITIALIZATION & STEP-BY-STEP CALCULATIONS
# ---------------------------------------------------------
# Original 2D dataset (e.g., Math vs. Physics exam scores)
X_raw = np.array([
    [4.0, 5.0],
    [8.0, 10.0],
    [13.0, 11.0],
    [7.0, 8.0],
    [13.0, 16.0]
])
n_samples, n_features = X_raw.shape

# Step 1: Mean Centering
mean_vec = np.mean(X_raw, axis=0)
X_centered = X_raw - mean_vec

# Step 2: Covariance Matrix (ddof=1 for sample covariance)
cov_matrix = np.cov(X_centered, rowvar=False)

# Step 3: Eigendecomposition
eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

# Sort eigenvalues and eigenvectors in descending order
idx = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

# Variance calculations
total_variance = np.sum(eigenvalues)
explained_var_ratio = eigenvalues / total_variance

# Step 4: Projection Matrix W & Transformed 1D Data Y
W = eigenvectors[:, :1]  # Top-1 Principal Component direction
Y_1d = X_centered @ W   # 1D coordinates along PC1

# Reconstruct 2D projected coordinates for visualization
X_projected_2d = Y_1d @ W.T

# ---------------------------------------------------------
# 2. MULTI-PANEL DASHBOARD VISUALIZATION
# ---------------------------------------------------------
fig = plt.figure(figsize=(18, 11))
grid = plt.GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.3)

# ---------------------------------------------------------
# Panel 1: Raw Data & Mean Center Shift
# ---------------------------------------------------------
ax1 = fig.add_subplot(grid[0, 0])
ax1.scatter(X_raw[:, 0], X_raw[:, 1], color="#1f77b4", s=90, label="Raw Points", zorder=4)
ax1.scatter(mean_vec[0], mean_vec[1], color="red", marker="X", s=150, label=f"Mean $(\\mu)=({mean_vec[0]:.1f}, {mean_vec[1]:.1f})$", zorder=5)

# Mean dashed lines
ax1.axvline(mean_vec[0], color="red", linestyle="--", alpha=0.5)
ax1.axhline(mean_vec[1], color="red", linestyle="--", alpha=0.5)

for i, (x, y) in enumerate(X_raw):
    ax1.annotate(f"P{i+1}({x:.0f},{y:.0f})", (x + 0.3, y - 0.2), fontsize=9)

ax1.set_title("Step 1: Raw Data & Mean Center", fontweight="bold")
ax1.set_xlabel("Math Score ($X_1$)")
ax1.set_ylabel("Physics Score ($X_2$)")
ax1.legend(loc="upper left")

# ---------------------------------------------------------
# Panel 2: Covariance Matrix Heatmap
# ---------------------------------------------------------
ax2 = fig.add_subplot(grid[0, 1])
labels = ["Math ($X_1$)", "Physics ($X_2$)"]
sns.heatmap(
    cov_matrix, 
    annot=True, 
    fmt=".2f", 
    cmap="Blues", 
    cbar=True, 
    xticklabels=labels, 
    yticklabels=labels, 
    ax=ax2,
    annot_kws={"size": 13, "weight": "bold"}
)
ax2.set_title("Step 2: Covariance Matrix $(\\Sigma = \\frac{1}{n-1}X^TX)$", fontweight="bold")

# ---------------------------------------------------------
# Panel 3: Eigenvalues & Explained Variance (Scree Plot)
# ---------------------------------------------------------
ax3 = fig.add_subplot(grid[0, 2])
bars = ax3.bar(
    ["PC1", "PC2"], 
    explained_var_ratio * 100, 
    color=["#2ca02c", "#d62728"], 
    width=0.45, 
    alpha=0.85
)
ax3.set_ylabel("Explained Variance (%)")
ax3.set_ylim(0, 115)
ax3.set_title("Step 3: Variance Ratio by Eigenvalues", fontweight="bold")

for bar, val, eig in zip(bars, explained_var_ratio * 100, eigenvalues):
    ax3.text(
        bar.get_x() + bar.get_width() / 2, 
        val + 3, 
        f"{val:.1f}%\n($\\lambda={eig:.2f}$)", 
        ha="center", 
        fontweight="bold"
    )

# ---------------------------------------------------------
# Panel 4: Centered Data with Eigenvectors (PC1 & PC2 Axes)
# ---------------------------------------------------------
ax4 = fig.add_subplot(grid[1, 0])
ax4.scatter(X_centered[:, 0], X_centered[:, 1], color="#9467bd", s=80, label="Centered Data $(X - \\mu)$", zorder=4)
ax4.axhline(0, color="gray", linestyle=":", alpha=0.6)
ax4.axvline(0, color="gray", linestyle=":", alpha=0.6)

# Plot Eigenvector arrows scaled by 2 * sqrt(eigenvalue) for standard deviation spread
scale_1 = 2 * np.sqrt(eigenvalues[0])
scale_2 = 2 * np.sqrt(eigenvalues[1])

# PC1 Vector Arrow
ax4.quiver(
    0, 0, 
    eigenvectors[0, 0] * scale_1, eigenvectors[1, 0] * scale_1, 
    angles="xy", scale_units="xy", scale=1, 
    color="#2ca02c", width=0.015, 
    label=f"PC1 Vector $v_1$ [{eigenvectors[0,0]:.2f}, {eigenvectors[1,0]:.2f}]"
)
# PC2 Vector Arrow
ax4.quiver(
    0, 0, 
    eigenvectors[0, 1] * scale_2, eigenvectors[1, 1] * scale_2, 
    angles="xy", scale_units="xy", scale=1, 
    color="#d62728", width=0.015, 
    label=f"PC2 Vector $v_2$ [{eigenvectors[0,1]:.2f}, {eigenvectors[1,1]:.2f}]"
)

ax4.set_title("Step 4: Eigenvectors (Directions of Variance)", fontweight="bold")
ax4.set_xlabel("Centered $X_1$")
ax4.set_ylabel("Centered $X_2$")
ax4.legend(loc="upper left", fontsize=8.5)

# ---------------------------------------------------------
# Panel 5: Orthogonal Projections onto PC1
# ---------------------------------------------------------
ax5 = fig.add_subplot(grid[1, 1])

# Plot continuous PC1 line
pc1_line_t = np.linspace(-10, 10, 100)
pc1_line_x = pc1_line_t * eigenvectors[0, 0]
pc1_line_y = pc1_line_t * eigenvectors[1, 0]
ax5.plot(pc1_line_x, pc1_line_y, color="#2ca02c", linestyle="--", linewidth=1.8, label="PC1 Subspace Line")

# Centered points and their projected 2D coordinates on the line
ax5.scatter(X_centered[:, 0], X_centered[:, 1], color="#9467bd", s=70, label="Original Centered Points", zorder=4)
ax5.scatter(X_projected_2d[:, 0], X_projected_2d[:, 1], color="#ff7f0e", s=80, marker="o", label="Projected Points on PC1", zorder=5)

# Draw orthogonal projection drop lines (residuals)
for i in range(n_samples):
    ax5.plot(
        [X_centered[i, 0], X_projected_2d[i, 0]], 
        [X_centered[i, 1], X_projected_2d[i, 1]], 
        color="red", linestyle=":", linewidth=1.5,
        label="Orthogonal Drop Line" if i == 0 else ""
    )

ax5.axhline(0, color="gray", linestyle=":", alpha=0.4)
ax5.axvline(0, color="gray", linestyle=":", alpha=0.4)
ax5.set_title("Step 5: Orthogonal Projection (2D $\\rightarrow$ 1D)", fontweight="bold")
ax5.set_xlabel("Centered $X_1$")
ax5.set_ylabel("Centered $X_2$")
ax5.legend(loc="upper left", fontsize=8)

# ---------------------------------------------------------
# Panel 6: Final 1D Transformed Feature Space
# ---------------------------------------------------------
ax6 = fig.add_subplot(grid[1, 2])
ax6.scatter(Y_1d, np.zeros_like(Y_1d), color="#ff7f0e", s=110, zorder=4, label="Reduced Points $Y = XW$")
ax6.axhline(0, color="#2ca02c", linestyle="-", linewidth=2.5, alpha=0.7)

for i, val in enumerate(Y_1d):
    ax6.annotate(f"P{i+1}: {val[0]:.2f}", (val[0], 0.04), rotation=30, ha="center", fontsize=9, fontweight="bold")

ax6.set_yticks([])
ax6.set_ylim(-0.2, 0.25)
ax6.set_title(f"Step 6: Final 1D Subspace ({explained_var_ratio[0]*100:.1f}% Variance Retained)", fontweight="bold")
ax6.set_xlabel("Principal Component 1 Coordinate ($Y$)")
ax6.legend(loc="upper left")

plt.show()