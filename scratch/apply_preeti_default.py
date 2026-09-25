import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update font-face to include Preeti as primary Unicode font and Preeti-Legacy
font_face_old = re.search(r"@font-face\s*\{\s*font-family:\s*'Preeti';.*?\}(?=\s*\.font-preeti)", content, re.DOTALL)
if font_face_old:
    font_face_block = font_face_old.group(0)
    print("Found existing Preeti @font-face")

# Replace or define font-faces
replacement_font_faces = """@font-face {
      font-family: 'Preeti';
      src: url('assets/fonts/preeti-unicode.ttf') format('truetype'),
           url('assets/fonts/preeti.otf') format('opentype');
      font-weight: normal;
      font-style: normal;
      font-display: swap;
    }

    """ + font_face_old.group(0).replace("font-family: 'Preeti'", "font-family: 'Preeti-Legacy'")

content = content.replace(font_face_old.group(0), replacement_font_faces, 1)
print("Updated @font-face with Preeti (Unicode) and Preeti-Legacy")

# 2. Update CSS classes
old_css = """.font-preeti {
      font-family: 'Preeti', 'Mukta', -apple-system, sans-serif !important;
      letter-spacing: 0.01em;
    }"""

new_css = """.font-preeti {
      font-family: 'Preeti', 'Mukta', -apple-system, sans-serif !important;
      letter-spacing: 0.01em;
    }
    
    .font-preeti-legacy {
      font-family: 'Preeti-Legacy', 'Preeti', sans-serif !important;
      font-size: 1.15em;
      letter-spacing: 0.01em;
    }

    body.font-mode-preeti {
      font-family: 'Preeti', 'Mukta', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }

    body.font-mode-mukta {
      font-family: 'Mukta', 'Noto Sans Devanagari', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }

    body.font-mode-system {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }"""

content = content.replace(old_css, new_css, 1)

# 3. Update body default font-family
content = re.sub(
    r"body\s*\{\s*font-family:\s*'Mukta'[^;]*;",
    "body { font-family: 'Preeti', 'Mukta', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;",
    content,
    count=1
)
print("Set body font-family default to Preeti")

# 4. Update the Preeti modal preview container to use font-preeti-legacy
content = content.replace(
    'id="u2p-preeti-preview" class="font-preeti',
    'id="u2p-preeti-preview" class="font-preeti-legacy'
)

# 5. Update global font select dropdown
old_select = """<select id="global-font-select" onchange="changeGlobalFont(this.value)" class="bg-indigo-900/80 text-white text-xs font-bold rounded-lg px-2 py-0.5 border border-white/30 focus:outline-none focus:ring-1 focus:ring-amber-300 cursor-pointer">
            <option value="mukta">मुक्ता (Mukta - युनिकोड)</option>
            <option value="preeti">प्रिती (Preeti - नेपाली फन्ट)</option>
            <option value="system">प्रणाली (System Sans)</option>
          </select>"""

new_select = """<select id="global-font-select" onchange="changeGlobalFont(this.value, true)" class="bg-indigo-900/80 text-white text-xs font-bold rounded-lg px-2 py-0.5 border border-white/30 focus:outline-none focus:ring-1 focus:ring-amber-300 cursor-pointer">
            <option value="preeti" selected>प्रिती (Preeti - डिफल्ट)</option>
            <option value="mukta">मुक्ता (Mukta - युनिकोड)</option>
            <option value="system">प्रणाली (System Sans)</option>
          </select>"""

content = content.replace(old_select, new_select, 1)

# 6. Update JS default font
content = content.replace(
    "const savedFont = localStorage.getItem('class6_font_choice') || 'mukta';",
    "const savedFont = localStorage.getItem('class6_font_choice') || 'preeti';"
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"index.html saved! Total chars: {len(content)}")
