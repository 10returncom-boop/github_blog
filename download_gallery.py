import urllib.request
import os

assets_dir = r"D:\www\325-public\assets"

images = [
    ("gallery-staircase.jpg", "https://aka.doubaocdn.com/s/uUL3b6biF5"),
    ("gallery-bar.jpg", "https://aka.doubaocdn.com/s/VhbjdXGbne"),
    ("gallery-restaurant.jpg", "https://aka.doubaocdn.com/s/kxHwFUot2V"),
    ("gallery-room-detail.jpg", "https://aka.doubaocdn.com/s/LhZkvqdK8N"),
    ("gallery-bathtub.jpg", "https://aka.doubaocdn.com/s/MaHeutkVuW"),
    ("gallery-entrance.jpg", "https://aka.doubaocdn.com/s/Gw4iJ8UiED"),
    ("gallery-alley.jpg", "https://aka.doubaocdn.com/s/RX84swy3Vr"),
    ("gallery-deco-detail.jpg", "https://aka.doubaocdn.com/s/irt9zrgQr4"),
    ("gallery-rooftop.jpg", "https://aka.doubaocdn.com/s/pZQCVTLWVI"),
]

for filename, url in images:
    filepath = os.path.join(assets_dir, filename)
    print(f"Downloading {filename}...")
    urllib.request.urlretrieve(url, filepath)
    size = os.path.getsize(filepath)
    print(f"  Done: {size} bytes")

print("All gallery images downloaded.")
