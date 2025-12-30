import sys
import matplotlib
import numpy

print("--- Python Search Path Order ---")
# This shows the order in which Python looks for files
for path in sys.path[:4]: 
    print(f"Looking in: {path}")

print("\n--- Actual Package Locations ---")

# The .__file__ attribute tells you exactly where the file lives on your disk
print(f"Matplotlib is loaded from: {matplotlib.__file__}")
print(f"Numpy is loaded from:      {numpy.__file__}")

print("\n--- Version Check ---")
print(f"Matplotlib Version: {matplotlib.__version__}")
print(f"Numpy Version:      {numpy.__version__}")