import os
import mrcfile
import sys

print("=== Script started ===")

script_dir = os.path.dirname(os.path.abspath(__file__))
print("Script directory:", script_dir)

data_dir = os.path.join(script_dir, "../data")
print("Data directory:", data_dir)

mrc_filename = "100_movie_gc.mrcs"
file_path = os.path.join(data_dir, mrc_filename)
print("Full file path:", file_path)

if not os.path.exists(file_path):
    print("ERROR: File does NOT exist at this path!")
    sys.exit(1)
else:
    print("File found!")

try:
    with mrcfile.open(file_path, permissive=True) as mrc:
        data = mrc.data
except Exception as e:
    print("ERROR: Failed to open MRC file:", e)
    sys.exit(1)

print("Successfully opened MRC file.")

if data.ndim == 2:
    print("Single-frame MRC detected.")
    print("Shape:", data.shape)
elif data.ndim == 3:
    print("Multi-frame stack detected.")
    print("Number of frames:", data.shape[0])
    print("Frame shape (H x W):", data.shape[1:])
else:
    print("Unexpected data shape:", data.shape)

print("=== Script finished ===")
