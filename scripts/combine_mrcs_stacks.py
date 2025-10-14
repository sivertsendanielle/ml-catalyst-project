import mrcfile
import numpy as np

# -----------------------------
# Absolute paths of all six stacks
# -----------------------------
mrc_files = [
    "/Users/daniellesivertsen/Documents/GitHub/ml-catalyst-project/data/100_movie_gc.mrcs",
    "/Users/daniellesivertsen/Documents/GitHub/ml-catalyst-project/data/101_movie_gc.mrcs",
    "/Users/daniellesivertsen/Documents/GitHub/ml-catalyst-project/data/102_movie_gc.mrcs",
    "/Users/daniellesivertsen/Documents/GitHub/ml-catalyst-project/data/103_movie_gc.mrcs",
    "/Users/daniellesivertsen/Documents/GitHub/ml-catalyst-project/data/104_movie_gc.mrcs",
    "/Users/daniellesivertsen/Documents/GitHub/ml-catalyst-project/data/105_movie_gc.mrcs"
]

# -----------------------------
# Load stacks and check dimensions
# -----------------------------
loaded_stacks = []
shape_ref = None

for file_path in mrc_files:
    with mrcfile.open(file_path, permissive=True) as mrc:
        stack = mrc.data
        print(f"Loaded {file_path}, shape: {stack.shape}")

        if shape_ref is None:
            shape_ref = stack.shape[1:]  # height x width
        else:
            if stack.shape[1:] != shape_ref:
                raise ValueError(f"Stack {file_path} has different spatial dimensions ({stack.shape[1:]}) than previous stacks ({shape_ref})")

        loaded_stacks.append(stack)

# -----------------------------
# Concatenate along frame axis
# -----------------------------
combined_stack = np.concatenate(loaded_stacks, axis=0)
print(f"Combined stack shape: {combined_stack.shape}")

# -----------------------------
# Save combined stack to new .mrcs file
# -----------------------------
output_file = "/Users/daniellesivertsen/Documents/GitHub/ml-catalyst-project/data/combined_stack.mrcs"
with mrcfile.new(output_file, overwrite=True) as mrc:
    mrc.set_data(combined_stack.astype(np.float32))

print(f"Combined stack saved to {output_file}")
