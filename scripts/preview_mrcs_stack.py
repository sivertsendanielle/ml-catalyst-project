import os
import mrcfile
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Paths
# -----------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, "../data")
mrc_filename = "100_movie_gc.mrcs"
file_path = os.path.join(data_dir, mrc_filename)

# -----------------------------
# Load .mrcs stack
# -----------------------------
with mrcfile.open(file_path, permissive=True) as mrc:
    stack = mrc.data

num_frames = stack.shape[0]
print(f"Stack shape: {stack.shape}")

# -----------------------------
# Per-frame statistics
# -----------------------------
print("\nPer-frame statistics:")
for i in range(num_frames):
    frame = stack[i]
    print(f"Frame {i}: min={frame.min():.2f}, max={frame.max():.2f}, mean={frame.mean():.2f}")

# -----------------------------
# Display all frames as thumbnails
# -----------------------------
cols = 4  # number of columns in figure
rows = int(np.ceil(num_frames / cols))

fig, axes = plt.subplots(rows, cols, figsize=(3*cols, 3*rows))

for i in range(rows*cols):
    ax = axes.flatten()[i]
    if i < num_frames:
        frame = stack[i]
        vmin, vmax = np.percentile(frame, [1, 99])  # automatic contrast scaling
        ax.imshow(frame, cmap='gray', vmin=vmin, vmax=vmax)
        ax.set_title(f"Frame {i}")
    ax.axis('off')

plt.tight_layout()
plt.show()
