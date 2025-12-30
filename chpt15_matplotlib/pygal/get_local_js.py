import urllib.request

# The URL of the official Pygal javascript "brain"
url = "http://kozea.github.io/pygal.js/2.0.x/pygal-tooltips.min.js"

# Save it to the same folder where you are running your code
urllib.request.urlretrieve(url, "pygal-tooltips.min.js")

print("Download complete: 'pygal-tooltips.min.js' is now in your folder.")