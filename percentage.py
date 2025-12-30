import requests

# 1. The RAW URL for the specific notebook
url = "https://raw.githubusercontent.com/jakevdp/PythonDataScienceHandbook/master/notebooks/04.00-Introduction-To-Matplotlib.ipynb"
filename = "matplotlib_numpy_tutorial.ipynb"

print(f"Downloading {filename}...")

# 2. Request the file
response = requests.get(url)

# 3. Save it to your current folder
if response.status_code == 200:
    with open(filename, 'wb') as f:
        f.write(response.content)
    print("Success! File saved.")
    print("You can now open 'matplotlib_numpy_tutorial.ipynb' in Jupyter.")
else:
    print(f"Error: Unable to download (Status: {response.status_code})")