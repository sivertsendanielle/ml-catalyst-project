import mrcfile
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os

# -----------------------------
# Path to your combined stack
# -----------------------------
file_path = "/Users/daniellesivertsen/Documents/GitHub/ml-catalyst-project/data/combined_stack.mrcs"

if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found: {file_path}")

# -----------------------------
# Load stack
# -----------------------------
with mrcfile.open(file_path, permissive=True) as mrc:
    data = mrc.data

print(f"Loaded stack: {file_path}")
print(f"Stack shape: {data.shape}")

# -----------------------------
# Normalize data for display
# -----------------------------
vmin, vmax = np.percentile(data, (1, 99))
data = np.clip(data, vmin, vmax)
data = (data - vmin) / (vmax - vmin)

# -----------------------------
# Create interactive animation
# -----------------------------
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(data[0], cmap="gray")
ax.set_title("Frame 1")
ax.axis("off")

for i in range(data.shape[0]):
    im.set_data(data[i])
    ax.set_title(f"Frame {i+1}/{data.shape[0]}")
    plt.pause(0.1)  # Adjust speed (0.05–0.2 for typical stacks)

plt.ioff()  # Turn off interactive mode after playback
plt.show()
