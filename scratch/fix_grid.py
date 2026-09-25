with open('scratch/ch19_script.js', 'r', encoding='utf-8') as f:
    code = f.read()

target = "  container.style.gridTemplateColumns = `repeat(${GRID_COLS}, 32px)`;"
replacement = "  container.style.display = 'grid';\n  container.style.gridTemplateColumns = `repeat(${GRID_COLS}, 32px)`;\n  container.style.gap = '4px';\n  container.style.width = 'fit-content';"

assert target in code, 'Target not found in ch19_script.js'
code = code.replace(target, replacement, 1)

with open('scratch/ch19_script.js', 'w', encoding='utf-8') as f:
    f.write(code)

print('scratch/ch19_script.js updated successfully!')
