#!/usr/bin/env python3
"""
Convert WEBP images to JPEG for PowerPoint compatibility
"""

from PIL import Image
import os

# Convert DavidRaymes.webp to .jpg
if os.path.exists("images/DavidRaymes.webp"):
    img = Image.open("images/DavidRaymes.webp")
    # Convert to RGB if necessary (WEBP might have alpha channel)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    img.save("images/DavidRaymes.jpg", "JPEG", quality=90)
    print("Converted DavidRaymes.webp to DavidRaymes.jpg")
else:
    print("DavidRaymes.webp not found")