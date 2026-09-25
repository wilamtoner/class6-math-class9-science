import base64
import os
import re

# Read Preeti OTF
font_path = 'assets/fonts/Preeti Normal/Preeti Normal.otf'
with open(font_path, 'rb') as f:
    font_bytes = f.read()

font_b64 = base64.b64encode(font_bytes).decode('ascii')
print(f'Preeti OTF base64 length: {len(font_b64)}')

# Verify index.html exists
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print(f'Current index.html lines: {len(html.splitlines())}, chars: {len(html)}')
