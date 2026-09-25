import sys

def patch_index():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    with open('scratch/c9u6_html.html', 'r', encoding='utf-8') as f:
        c9u6_html = f.read()

    with open('scratch/c9u6_js.js', 'r', encoding='utf-8') as f:
        c9u6_js = f.read()

    # 1. Inject HTML before c9-placeholder-view
    placeholder_idx = html.find('<div id="c9-placeholder-view"')
    if placeholder_idx == -1:
        print("Could not find placeholder")
        return

    html = html[:placeholder_idx] + c9u6_html + "\n" + html[placeholder_idx:]

    # 2. Inject JS before closing </body>
    script_idx = html.rfind('</body>')
    html = html[:script_idx] + f"\n<script>\n{c9u6_js}\n</script>\n" + html[script_idx:]

    # 3. Update switchGrade9Unit to handle unitNum == 6
    # Current behavior relies on a loop for 1 to 5. We need to patch the switchGrade9Unit function.

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("Done HTML/JS injection")

patch_index()
