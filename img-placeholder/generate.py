import os
from PIL import Image, ImageDraw, ImageFont

# Paths
ORIGINALS_DIR = 'img-placeholder/originals'
PLACEHOLDERS_DIR = 'img-placeholder/placeholders'

# Create output directory if it doesn't exist
os.makedirs(PLACEHOLDERS_DIR, exist_ok=True)

# Try to use a common font, fallback to default
try:
    font = ImageFont.truetype("arial.ttf", 36)
except:
    font = ImageFont.load_default(36)

for filename in os.listdir(ORIGINALS_DIR):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(ORIGINALS_DIR, filename)
        with Image.open(img_path) as img:
            w, h = img.size
            # Create a gray background
            placeholder = Image.new('RGB', (w, h), color=(200, 200, 200))
            draw = ImageDraw.Draw(placeholder)
            text = f"{w} x {h}"
            # Calculate text size and position using textbbox
            bbox = draw.textbbox((0, 0), text, font=font)
            text_w = bbox[2] - bbox[0]
            text_h = bbox[3] - bbox[1]
            text_x = (w - text_w) // 2
            text_y = (h - text_h) // 2
            # Draw text
            draw.text((text_x, text_y), text, fill=(80, 80, 80), font=font)
            # Save placeholder
            out_path = os.path.join(PLACEHOLDERS_DIR, filename)
            placeholder.save(out_path)
            print(f"Created placeholder for {filename}")