with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

target = "container.style.gridTemplateColumns = `repeat(${GRID_COLS}, 32px)`;"
replacement = "container.style.display = 'grid';\n  container.style.gridTemplateColumns = `repeat(${GRID_COLS}, 32px)`;\n  container.style.gap = '4px';\n  container.style.width = 'fit-content';"

assert target in html, 'Target not found in index.html'
html = html.replace(target, replacement, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('index.html updated successfully with grid fix!')
