import urllib.request
import os

assets_dir = r"D:\www\325-public\assets"

images = [
    ("hero-lobby.jpg", "https://aka.doubaocdn.com/s/FH3zZiNo8f"),
    ("ch1-invitation.jpg", "https://aka.doubaocdn.com/s/htDTVXreUu"),
    ("ch2-building.jpg", "https://aka.doubaocdn.com/s/zbTUqLVEZL"),
    ("ch3-room.jpg", "https://aka.doubaocdn.com/s/cOcY2G0pen"),
    ("ch4-oldcity.jpg", "https://aka.doubaocdn.com/s/n0BvJ9l371"),
    ("ch5-salon.jpg", "https://aka.doubaocdn.com/s/6i2q2ctUVT"),
    ("ch6-sunset.jpg", "https://aka.doubaocdn.com/s/AD5FFAxwPL"),
    ("appendix-books.jpg", "https://aka.doubaocdn.com/s/1sRVH6uJRJ"),
]

for filename, url in images:
    filepath = os.path.join(assets_dir, filename)
    print(f"Downloading {filename}...")
    urllib.request.urlretrieve(url, filepath)
    size = os.path.getsize(filepath)
    print(f"  Done: {size} bytes")

print("All images downloaded.")
