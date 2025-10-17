#!/usr/bin/env python3
"""
Create circular versions of team member photos
"""

from PIL import Image, ImageDraw
import os

def create_circular_image(input_path, output_path, size=(400, 400)):
    """Create a circular version of an image with better head framing"""
    if not os.path.exists(input_path):
        print(f"Image not found: {input_path}")
        return False
    
    # Open image
    img = Image.open(input_path).convert("RGBA")
    
    # Get original dimensions
    orig_width, orig_height = img.size
    
    # Create a square crop that's more centered on the face
    # Use 80% of the smaller dimension to get more of the head
    crop_size = int(min(orig_width, orig_height) * 0.8)
    
    # Center the crop horizontally, and position vertically to get more head/face
    left = (orig_width - crop_size) // 2
    # Position crop higher to get more head, less body
    top = max(0, int((orig_height - crop_size) * 0.3))  # 30% from top instead of center
    
    # Crop to square focusing on head area
    img_cropped = img.crop((left, top, left + crop_size, top + crop_size))
    
    # Resize to target size
    img_resized = img_cropped.resize(size, Image.Resampling.LANCZOS)
    
    # Create a circular mask
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)
    
    # Apply the mask
    output = Image.new('RGBA', size, (0, 0, 0, 0))
    output.paste(img_resized, (0, 0))
    output.putalpha(mask)
    
    # Save as PNG to preserve transparency
    output.save(output_path, 'PNG')
    print(f"Created circular image with better head framing: {output_path}")
    return True

def main():
    # Create circular versions of all team photos
    images_to_process = [
        ("images/AlexanderPertsemlidis.jpg", "images/AlexanderPertsemlidis_circular.png"),
        ("images/LeoBleris.jpg", "images/LeoBleris_circular.png"),
        ("images/YiorgosMakris.jpg", "images/YiorgosMakris_circular.png"),
        ("images/DavidRaymes.jpg", "images/DavidRaymes_circular.png"),
        ("images/SteveGuengerich.jpg", "images/SteveGuengerich_circular.png")
    ]
    
    for input_path, output_path in images_to_process:
        create_circular_image(input_path, output_path)

if __name__ == "__main__":
    main()