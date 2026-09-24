import urllib.request
import os

url = "https://aka.doubaocdn.com/s/w6l8wKUprJ"
filepath = r"D:\www\325-public\assets\appendix-blueprint.jpg"
print(f"Downloading blueprint...")
urllib.request.urlretrieve(url, filepath)
size = os.path.getsize(filepath)
print(f"Done: {size} bytes")
