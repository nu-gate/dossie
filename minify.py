#!/usr/bin/env python3
import base64
import re
import os

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Image files to convert
images = {
    'assets/images/logo.png': 'image/png',
    'assets/images/intro.webp': 'image/webp',
    'assets/images/david_velez..jpeg': 'image/jpeg',
    'assets/images/founders.jpg': 'image/jpeg',
    'assets/images/cards.png': 'image/png',
    'assets/images/ipo.jpeg': 'image/jpeg'
}

# Convert images to base64 and replace in HTML
for img_path, mime_type in images.items():
    if os.path.exists(img_path):
        with open(img_path, 'rb') as img_file:
            img_data = img_file.read()
            b64_data = base64.b64encode(img_data).decode('utf-8')
            data_uri = f'data:{mime_type};base64,{b64_data}'

            # Replace the image source in HTML
            html = html.replace(f'src="{img_path}"', f'src="{data_uri}"')
            print(f'Converted: {img_path}')
    else:
        print(f'Warning: {img_path} not found')

# Minification steps
# Remove HTML comments (except IE conditional comments)
html = re.sub(r'<!--(?!\[if).*?-->', '', html, flags=re.DOTALL)

# Remove multiple spaces
html = re.sub(r'\s+', ' ', html)

# Remove spaces around tags
html = re.sub(r'>\s+<', '><', html)

# Remove spaces after opening tags and before closing tags
html = re.sub(r'>\s+', '>', html)
html = re.sub(r'\s+<', '<', html)

# Trim
html = html.strip()

# Write minified HTML
with open('index.min.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\nMinified HTML created: index.min.html')
print(f'Original size: {os.path.getsize("index.html")} bytes')
print(f'Minified size: {os.path.getsize("index.min.html")} bytes')
