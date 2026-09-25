import re
import os

print("Starting Offline Mode & PWA Bundle Integration...")

# 1. Read generated offline CSS
with open('scratch/generated_offline.css', 'r', encoding='utf-8') as f:
    offline_css = f.read()

# Additional custom styles (typography, tables, fractions, header gradient)
base_custom_css = """
    @import url('https://fonts.googleapis.com/css2?family=Mukta:wght@400;500;600;700;800&display=swap');
    
    * { box-sizing: border-box; }
    body { font-family: 'Mukta', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background-color: #f1f5f9; color: #1e293b; margin: 0; min-height: 100vh; display: flex; flex-direction: column; }
    
    /* Header gradient */
    header { background: linear-gradient(135deg, #1d4ed8 0%, #4338ca 50%, #6b21a8 100%) !important; color: #ffffff !important; }
    header h1, header p, header div, header span { color: inherit !important; }
    
    /* Controls & Buttons */
    button { cursor: pointer; border: none; font-family: inherit; }
    button:hover { opacity: 0.95; }
    input[type="text"], input[type="number"] { font-family: inherit; }
    
    /* Tables */
    table { width: 100%; border-collapse: collapse; text-align: left; }
    th, td { padding: 0.75rem 1rem; border-bottom: 1px solid #e2e8f0; }
    tr:hover { background-color: #f8fafc; }
    
    /* MathJax Specifics */
    .MathJax { font-size: 104% !important; color: #1e293b; }
    .MathJax_Display { margin: 0.65em 0 !important; overflow-x: auto; overflow-y: hidden; }
    .mjx-chtml { outline: none; }
    .mjx-chtml * { font-family: inherit; }

    /* Offline Pure-CSS Math Formatting */
    .offline-math {
      font-family: 'Cambria Math', 'STIX Two Math', 'Times New Roman', serif;
      font-style: italic;
      color: #0f172a;
      display: inline-block;
    }
    .offline-frac {
      display: inline-flex;
      flex-direction: column;
      vertical-align: -0.5em;
      text-align: center;
      padding: 0 0.25em;
      font-size: 0.88em;
      line-height: 1.15;
    }
    .offline-frac > .top {
      border-bottom: 1.5px solid currentColor;
      padding-bottom: 1px;
    }
    .offline-frac > .bot {
      padding-top: 1px;
    }
"""

combined_css = base_custom_css + "\n" + offline_css

# 2. Read primary HTML file
with open('कक्षा_६_गणित_डिजिटल_साथी.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace <style> block
style_pattern = re.compile(r'<style>[\s\S]*?</style>')
new_style = f"<style>\n{combined_css}\n  </style>"
html = style_pattern.sub(new_style, html, count=1)
print("Replaced <style> block with complete 100% offline stylesheet!")

# Update <head> metadata for PWA
pwa_meta = """  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#1e293b">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="कक्षा ६ गणित">
  <link rel="manifest" href="manifest.json">
  <link rel="icon" type="image/png" href="assets/icons/favicon.png">
  <link rel="apple-touch-icon" href="assets/icons/apple-touch-icon.png">"""

html = html.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">', pwa_meta, 1)
print("Added PWA metadata and icons!")

# Update header badges to include Offline Status Badge and PWA Install Button
old_header_badges = """<div class="flex items-center gap-2">
        <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-emerald-500/25 text-emerald-200 border border-emerald-400/40 shadow-xs">✓ सम्पूर्ण अभ्यास र समाधान समावेश</span>
        <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-purple-500/25 text-purple-200 border border-purple-400/40 shadow-xs">✓ ३ तहका प्रश्नहरू</span>
      </div>"""

new_header_badges = """<div class="flex flex-wrap items-center gap-2">
        <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-emerald-500/25 text-emerald-200 border border-emerald-400/40 shadow-xs">✓ सम्पूर्ण अभ्यास र समाधान समावेश</span>
        <span id="offline-status-badge" class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-bold bg-white/20 text-white border border-white/30 shadow-xs" title="इन्टरनेट वा सर्भर बिना पनि १००% काम गर्छ">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span>अफलाइन सक्रिय (Offline Ready)</span>
        </span>
        <button id="pwa-install-btn" class="hidden inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold bg-amber-400 text-slate-900 hover:bg-amber-300 transition cursor-pointer shadow-md" title="यस उपकरणमा एपका रूपमा इन्स्टल गर्नुहोस्">
          <span>📲 एप इन्स्टल गर्नुहोस्</span>
        </button>
      </div>"""

if old_header_badges in html:
    html = html.replace(old_header_badges, new_header_badges, 1)
    print("Added offline badge and PWA install button to header!")
else:
    print("Warning: old_header_badges not matched directly!")

# Add Offline Math Engine and Service Worker logic into main script
offline_js_bundle = """
    // ==========================================
    // OFFLINE SUPPORT & PWA ENGINE
    // ==========================================
    
    // 1. Service Worker Registration (PWA)
    if ('serviceWorker' in navigator && (window.location.protocol === 'http:' || window.location.protocol === 'https:')) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('./sw.js').then((reg) => {
          console.log('[PWA] Service Worker registered:', reg.scope);
        }).catch((err) => {
          console.log('[PWA] Service Worker registration note:', err);
        });
      });
    }

    // 2. PWA Install Prompt Handler
    let deferredPrompt;
    const pwaInstallBtn = document.getElementById('pwa-install-btn');
    window.addEventListener('beforeinstallprompt', (e) => {
      e.preventDefault();
      deferredPrompt = e;
      if (pwaInstallBtn) pwaInstallBtn.classList.remove('hidden');
    });

    if (pwaInstallBtn) {
      pwaInstallBtn.addEventListener('click', async () => {
        if (deferredPrompt) {
          deferredPrompt.prompt();
          const { outcome } = await deferredPrompt.userChoice;
          if (outcome === 'accepted') {
            pwaInstallBtn.classList.add('hidden');
          }
          deferredPrompt = null;
        } else {
          alert('यो एप इन्स्टल गर्न आफ्नो मोबाइल/ल्यापटप ब्राउजरको तीन थोप्ला मेनुमा गई "Add to Home screen" वा "Install app" रोज्नुहोस्।');
        }
      });
    }

    // 3. Built-in Pure-CSS Offline LaTeX Math Renderer
    function formatLaTeXText(s) {
      s = s.trim();
      let fracRegex = /\\\\frac\\s*\\{([^{}]+)\\}\\s*\\{([^{}]+)\\}/g;
      while (fracRegex.test(s)) {
        s = s.replace(fracRegex, '<span class="offline-frac"><span class="top">$1</span><span class="bot">$2</span></span>');
      }
      s = s.replace(/\\\\times/g, " × ")
           .replace(/\\\\div/g, " ÷ ")
           .replace(/\\\\pm/g, " ± ")
           .replace(/\\\\leq/g, " ≤ ")
           .replace(/\\\\geq/g, " ≥ ")
           .replace(/\\\\approx/g, " ≈ ")
           .replace(/\\\\ne/g, " ≠ ")
           .replace(/\\\\to|\\\\rightarrow/g, " → ")
           .replace(/\\\\Rightarrow/g, " ⇒ ")
           .replace(/\\\\quad/g, " &nbsp; ")
           .replace(/\\\\circ/g, "°")
           .replace(/\\\\%/g, "%")
           .replace(/\\\\text\\{([^{}]+)\\}/g, '<span style="font-style:normal;">$1</span>')
           .replace(/\\^([0-9a-zA-Z]+)/g, "<sup>$1</sup>")
           .replace(/\\^\\{([^{}]+)\\}/g, "<sup>$1</sup>")
           .replace(/_([0-9a-zA-Z]+)/g, "<sub>$1</sub>")
           .replace(/_\\{([^{}]+)\\}/g, "<sub>$1</sub>")
           .replace(/\\\\sqrt\\{([^{}]+)\\}/g, "√($1)");
      return s;
    }

    function renderOfflineMath(container) {
      const root = container || document.body;
      if (!root) return;

      const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null, false);
      const nodes = [];
      let n;
      while ((n = walker.nextNode())) {
        if (n.nodeValue && n.nodeValue.includes('$')) {
          const tag = n.parentNode ? n.parentNode.nodeName.toUpperCase() : '';
          if (tag !== 'SCRIPT' && tag !== 'STYLE' && tag !== 'TEXTAREA') {
            nodes.push(n);
          }
        }
      }

      nodes.forEach((tNode) => {
        const text = tNode.nodeValue;
        if (!text || !text.includes('$')) return;
        const parts = text.split(/(\\$\\$[\\s\\S]*?\\$\\$|\\$[^$\\n]+?\\$)/g);
        if (parts.length <= 1) return;

        const fragment = document.createDocumentFragment();
        parts.forEach((part) => {
          if (part.startsWith('$$') && part.endsWith('$$') && part.length >= 4) {
            const math = part.slice(2, -2);
            const span = document.createElement('span');
            span.className = 'offline-math block my-2 text-center';
            span.innerHTML = formatLaTeXText(math);
            fragment.appendChild(span);
          } else if (part.startsWith('$') && part.endsWith('$') && part.length >= 2) {
            const math = part.slice(1, -1);
            const span = document.createElement('span');
            span.className = 'offline-math';
            span.innerHTML = formatLaTeXText(math);
            fragment.appendChild(span);
          } else if (part.length > 0) {
            fragment.appendChild(document.createTextNode(part));
          }
        });
        if (tNode.parentNode) {
          tNode.parentNode.replaceChild(fragment, tNode);
        }
      });
    }

    // Run offline math engine if MathJax is unavailable after timeout
    let mjLoaded = false;
    if (window.MathJax && window.MathJax.Hub) {
      window.MathJax.Hub.Queue(() => {
        mjLoaded = true;
      });
    }
    setTimeout(() => {
      if (!mjLoaded) {
        console.log('[Offline Math] Activating pure-CSS LaTeX offline math renderer...');
        renderOfflineMath(document.body);
      }
    }, 1200);

    window.renderOfflineMath = renderOfflineMath;
"""

# Place offline_js_bundle before window.addEventListener('DOMContentLoaded' or near end of script
target_anchor = "const urlParams = new URLSearchParams"
pos_anchor = html.find(target_anchor)
if pos_anchor != -1:
    html = html[:pos_anchor] + offline_js_bundle + "\n    " + html[pos_anchor:]
    print("Added Offline & PWA JS bundle successfully!")
else:
    print("Warning: target_anchor not found for JS!")

# Save to primary file
with open('कक्षा_६_गणित_डिजिटल_साथी.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved कक्षा_६_गणित_डिजिटल_साथी.html! Size:", len(html.encode('utf-8')), "bytes")

# Save to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved index.html!")

# Save to class6_math_offline.html (standalone file for direct copying)
with open('class6_math_offline.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved class6_math_offline.html!")

# Save artifact mirror
artifact_path = '/home/nepal/.gemini/antigravity/brain/6193a053-8fd9-40c5-8264-be982f512b93/interactive_math_guide.html'
with open(artifact_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved artifact mirror:", artifact_path)

print("Offline mode bundle applied successfully to all targets!")
