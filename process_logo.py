import os
import sys
from PIL import Image

def process_logo(input_path, output_path):
    try:
        # Open the high-res image
        img = Image.open(input_path)
        
        # Convert to RGB (in case it's RGBA or other)
        if img.mode != 'RGB':
            img = img.convert('RGB')
            
        # Resize to match the 1.44" Waveshare screen (128x128)
        # Using Resampling.LANCZOS for high quality downscaling
        img = img.resize((128, 128), Image.Resampling.LANCZOS)
        
        # Save as BMP (standard format for this screen driver)
        img.save(output_path, 'BMP')
        print(f"Successfully processed logo to {output_path}")
    except Exception as e:
        print(f"Error processing image: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 process_logo.py <input_path> <output_path>")
        sys.exit(1)
    process_logo(sys.argv[1], sys.argv[2])
