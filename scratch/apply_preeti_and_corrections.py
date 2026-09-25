import base64
import os
import re

# 1. Read Preeti Font
with open('assets/fonts/Preeti Normal/Preeti Normal.otf', 'rb') as f:
    font_bytes = f.read()
font_b64 = base64.b64encode(font_bytes).decode('ascii')
print(f"Preeti Font base64 encoded: {len(font_b64)} chars")

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Add Preeti @font-face and utility classes into <style>
font_face_css = f"""
    @font-face {{
      font-family: 'Preeti';
      src: url('data:font/otf;base64,{font_b64}') format('opentype'),
           url('assets/fonts/preeti.otf') format('opentype'),
           url('assets/fonts/Preeti Normal/Preeti Normal.otf') format('opentype');
      font-weight: normal;
      font-style: normal;
      font-display: swap;
    }}
    
    .font-preeti {{
      font-family: 'Preeti', 'Mukta', -apple-system, sans-serif !important;
      letter-spacing: 0.01em;
    }}
    
    .font-mukta {{
      font-family: 'Mukta', 'Noto Sans Devanagari', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }}

    .font-system {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }}

    body.font-mode-preeti h1, 
    body.font-mode-preeti h2, 
    body.font-mode-preeti h3, 
    body.font-mode-preeti .use-preeti {{
      font-family: 'Preeti', 'Mukta', sans-serif;
    }}
"""

# Insert right after <style>
if "@font-face" not in content or "font-family: 'Preeti'" not in content:
    content = content.replace("<style>", "<style>\n" + font_face_css, 1)
    print("Inserted Preeti @font-face CSS into <style>")
else:
    print("Preeti @font-face already in style")

# 3. Update Header with Font Switcher and Preeti Converter button
header_search = r'(<span id="offline-status-badge"[^>]*>.*?</span>)'
header_tools_html = """<!-- Font Switcher Control -->
        <div class="inline-flex items-center gap-1.5 bg-white/20 backdrop-blur-md px-2.5 py-1 rounded-full text-xs font-bold border border-white/30 text-white shadow-xs" title="फन्ट छनौट गर्नुहोस्">
          <span class="opacity-90">🔤</span>
          <select id="global-font-select" onchange="changeGlobalFont(this.value)" class="bg-indigo-900/80 text-white text-xs font-bold rounded-lg px-2 py-0.5 border border-white/30 focus:outline-none focus:ring-1 focus:ring-amber-300 cursor-pointer">
            <option value="mukta">मुक्ता (Mukta - युनिकोड)</option>
            <option value="preeti">प्रिती (Preeti - नेपाली फन्ट)</option>
            <option value="system">प्रणाली (System Sans)</option>
          </select>
        </div>

        <!-- Preeti Converter & Typing Pad Modal Button -->
        <button onclick="togglePreetiModal(true)" class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-black bg-amber-400 text-slate-900 hover:bg-amber-300 transition cursor-pointer shadow-md hover:scale-105 active:scale-95" title="युनिकोड ↔ प्रिती रुपान्तरक तथा टाइपिङ प्याड">
          <span>⌨️ प्रिती रुपान्तरक</span>
        </button>

        \\1"""

if "global-font-select" not in content:
    content = re.sub(header_search, header_tools_html, content, count=1, flags=re.DOTALL)
    print("Inserted Font Switcher & Preeti Converter button into header")
else:
    print("Header tools already present")

# 4. Prepare Preeti Modal HTML
modal_html = """
  <!-- Preeti ↔ Unicode Converter Modal -->
  <div id="preeti-modal" class="hidden fixed inset-0 z-[100] flex items-center justify-center bg-slate-900/60 backdrop-blur-sm p-4 overflow-y-auto transition-opacity" style="display: none;">
    <div class="relative w-full max-w-4xl bg-white rounded-3xl shadow-2xl border border-slate-200 overflow-hidden my-6 max-h-[92vh] flex flex-col">
      <!-- Modal Header -->
      <div class="bg-gradient-to-r from-blue-700 via-indigo-700 to-purple-800 text-white px-6 py-4 flex items-center justify-between">
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 rounded-2xl bg-white/20 flex items-center justify-center text-xl font-black shadow-inner border border-white/30">⌨️</div>
          <div>
            <h3 class="text-lg font-black tracking-tight">नेपाली फन्ट रुपान्तरक तथा प्रिती ल्याब</h3>
            <p class="text-xs text-blue-100">युनिकोड (Unicode) र परम्परागत प्रिती (Preeti) फन्ट बीच तत्काल रूपान्तरण</p>
          </div>
        </div>
        <button onclick="togglePreetiModal(false)" class="text-white/80 hover:text-white hover:bg-white/20 p-2 rounded-xl transition cursor-pointer" title="बन्द गर्नुहोस्">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
        </button>
      </div>

      <!-- Modal Tabs -->
      <div class="flex border-b border-slate-200 bg-slate-50 px-6 pt-3 gap-2 overflow-x-auto text-sm font-bold">
        <button id="preeti-tab-btn-u2p" onclick="setPreetiTab('u2p')" class="px-4 py-2.5 rounded-t-xl bg-white text-blue-700 border-t border-l border-r border-slate-200 shadow-xs cursor-pointer">
          युनिकोड ➔ प्रिती (Unicode ➔ Preeti)
        </button>
        <button id="preeti-tab-btn-p2u" onclick="setPreetiTab('p2u')" class="px-4 py-2.5 rounded-t-xl text-slate-600 hover:text-blue-700 hover:bg-slate-100 transition cursor-pointer">
          प्रिती ➔ युनिकोड (Preeti ➔ Unicode)
        </button>
        <button id="preeti-tab-btn-keys" onclick="setPreetiTab('keys')" class="px-4 py-2.5 rounded-t-xl text-slate-600 hover:text-blue-700 hover:bg-slate-100 transition cursor-pointer">
          किबोर्ड गाइड (Keyboard Reference)
        </button>
      </div>

      <!-- Modal Content Body -->
      <div class="p-6 overflow-y-auto flex-1 space-y-6">
        
        <!-- Tab 1: Unicode to Preeti -->
        <div id="preeti-panel-u2p" class="space-y-4">
          <div class="flex items-center justify-between text-xs">
            <span class="font-bold text-slate-600">युनिकोड इनपुट बक्स (यहाँ नेपाली युनिकोड टाइप वा पेस्ट गर्नुहोस्):</span>
            <div class="flex gap-2">
              <button onclick="loadPreetiSample('math')" class="text-blue-600 hover:underline font-bold cursor-pointer">📋 कक्षा ६ गणित नमूना लोड</button>
              <button onclick="clearPreetiInputs()" class="text-rose-500 hover:underline font-bold cursor-pointer">🧹 खाली गर्नुहोस्</button>
            </div>
          </div>

          <textarea id="u2p-input" oninput="handleU2PLiveConvert()" rows="4" placeholder="यहाँ नेपालीमा लेख्नुहोस् (जस्तै: कक्षा ६ गणित — रेखा र कोणहरू, आसन्न कोण, शीर्षाभिमुख कोण)..." class="w-full p-4 rounded-2xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-500 text-base font-mukta leading-relaxed"></textarea>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- Left Output: Visual Preeti Rendering -->
            <div class="bg-gradient-to-br from-blue-50/70 to-indigo-50/50 p-4 rounded-2xl border border-blue-200">
              <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-black text-blue-900 uppercase">🔤 प्रिती फन्ट दृश्य (Preeti Font Preview)</span>
                <span class="text-[10px] bg-blue-200/80 text-blue-900 px-2 py-0.5 rounded-full font-bold">Preeti Normal Font</span>
              </div>
              <div id="u2p-preeti-preview" class="font-preeti text-2xl text-slate-900 bg-white p-3 rounded-xl border border-blue-100 min-h-[90px] break-words whitespace-pre-wrap select-all">sIff ^ ul0ft — /]vf / sf]0fx¿</div>
              <p class="text-[11px] text-blue-700/80 mt-1.5">यो तपाईंले प्रदान गर्नुभएको Preeti Normal.otf फन्टबाट सिधै रेन्डर भएको हो।</p>
            </div>

            <!-- Right Output: Raw Preeti ASCII for Word / InDesign -->
            <div class="bg-slate-50 p-4 rounded-2xl border border-slate-200">
              <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-black text-slate-700 uppercase">📋 वर्ड तथा डिजाइनका लागि कोड (Preeti Text)</span>
                <button onclick="copyPreetiText('u2p-ascii', this)" class="text-xs bg-blue-600 hover:bg-blue-700 text-white font-bold px-3 py-1 rounded-lg transition cursor-pointer shadow-xs">कपी गर्नुहोस्</button>
              </div>
              <textarea id="u2p-ascii" readonly rows="3" class="w-full font-mono text-sm bg-white p-3 rounded-xl border border-slate-200 text-slate-800 resize-none select-all">sIff ^ ul0ft — /]vf / sf]0fx¿</textarea>
              <p class="text-[11px] text-slate-500 mt-1.5">यसलाई कपी गरेर MS Word वा Photoshop मा Preeti Font छनौट गरी पेस्ट गर्नुहोस्।</p>
            </div>
          </div>
        </div>

        <!-- Tab 2: Preeti to Unicode -->
        <div id="preeti-panel-p2u" class="hidden space-y-4">
          <div class="flex items-center justify-between text-xs">
            <span class="font-bold text-slate-600">प्रिती इनपुट बक्स (यहाँ प्रिती फन्टमा लेखिएको कोड पेस्ट गर्नुहोस्):</span>
            <div class="flex gap-2">
              <button onclick="loadPreetiSample('preeti')" class="text-blue-600 hover:underline font-bold cursor-pointer">📋 प्रिती नमूना लोड</button>
              <button onclick="clearPreetiInputs()" class="text-rose-500 hover:underline font-bold cursor-pointer">🧹 खाली गर्नुहोस्</button>
            </div>
          </div>

          <textarea id="p2u-input" oninput="handleP2ULiveConvert()" rows="4" placeholder="यहाँ प्रिती कोड पेस्ट गर्नुहोस् (जस्तै: sIff ^ ul0ft — /]vf / sf]0fx¿)..." class="w-full p-4 rounded-2xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-500 font-mono text-base leading-relaxed"></textarea>

          <div class="bg-emerald-50/70 p-4 rounded-2xl border border-emerald-200">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-black text-emerald-900 uppercase">✓ रूपान्तरित नेपाली युनिकोड (Converted Unicode)</span>
              <button onclick="copyPreetiText('p2u-output', this)" class="text-xs bg-emerald-600 hover:bg-emerald-700 text-white font-bold px-3 py-1 rounded-lg transition cursor-pointer shadow-xs">युनिकोड कपी गर्नुहोस्</button>
            </div>
            <textarea id="p2u-output" readonly rows="3" class="w-full font-mukta text-lg bg-white p-3 rounded-xl border border-emerald-200 text-slate-900 resize-none select-all"></textarea>
          </div>
        </div>

        <!-- Tab 3: Preeti Keyboard Cheat Sheet -->
        <div id="preeti-panel-keys" class="hidden space-y-4">
          <div class="p-4 bg-amber-50 rounded-2xl border border-amber-200 text-xs text-amber-900 font-medium">
            💡 <strong>सुझाव:</strong> प्रिती किबोर्डमा कुन बटनले कुन नेपाली अक्षर निकाल्छ तलको तालिकाबाट हेर्न सक्नुहुन्छ।
          </div>

          <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-3 text-xs">
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
              <span class="font-bold text-blue-700">क</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">s</code><br>
              <span class="font-bold text-blue-700">ख</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">v</code><br>
              <span class="font-bold text-blue-700">ग</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">u</code><br>
              <span class="font-bold text-blue-700">घ</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">3</code><br>
              <span class="font-bold text-blue-700">ङ</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">ª</code>
            </div>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
              <span class="font-bold text-blue-700">च</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">r</code><br>
              <span class="font-bold text-blue-700">छ</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">5</code><br>
              <span class="font-bold text-blue-700">ज</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">h</code><br>
              <span class="font-bold text-blue-700">झ</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">H</code><br>
              <span class="font-bold text-blue-700">ञ</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">`</code>
            </div>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
              <span class="font-bold text-blue-700">ट</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">6</code><br>
              <span class="font-bold text-blue-700">ठ</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">7</code><br>
              <span class="font-bold text-blue-700">ड</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">8</code><br>
              <span class="font-bold text-blue-700">ढ</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">9</code><br>
              <span class="font-bold text-blue-700">ण</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">0f</code>
            </div>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
              <span class="font-bold text-blue-700">त</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">t</code><br>
              <span class="font-bold text-blue-700">थ</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">y</code><br>
              <span class="font-bold text-blue-700">द</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">b</code><br>
              <span class="font-bold text-blue-700">ध</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">w</code><br>
              <span class="font-bold text-blue-700">न</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">g</code>
            </div>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
              <span class="font-bold text-blue-700">प</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">k</code><br>
              <span class="font-bold text-blue-700">फ</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">km</code><br>
              <span class="font-bold text-blue-700">ब</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">a</code><br>
              <span class="font-bold text-blue-700">भ</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">e</code><br>
              <span class="font-bold text-blue-700">म</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">d</code>
            </div>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
              <span class="font-bold text-blue-700">य</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">o</code><br>
              <span class="font-bold text-blue-700">र</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">/</code><br>
              <span class="font-bold text-blue-700">ल</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">n</code><br>
              <span class="font-bold text-blue-700">व</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">j</code><br>
              <span class="font-bold text-blue-700">स</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">;</code>
            </div>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
              <span class="font-bold text-blue-700">ा (आकार)</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">f</code><br>
              <span class="font-bold text-blue-700">ि (ह्रस्व)</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">l</code><br>
              <span class="font-bold text-blue-700">ी (दीर्घ)</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">L</code><br>
              <span class="font-bold text-blue-700">े (एकार)</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">]</code><br>
              <span class="font-bold text-blue-700">ै (ऐकार)</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">}</code>
            </div>
            <div class="p-3 bg-slate-50 rounded-xl border border-slate-200">
              <span class="font-bold text-blue-700">१..०</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">!@#$%^&*()</code><br>
              <span class="font-bold text-blue-700">क्ष</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">If</code><br>
              <span class="font-bold text-blue-700">त्र</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">q</code><br>
              <span class="font-bold text-blue-700">ज्ञ</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">1</code><br>
              <span class="font-bold text-blue-700">।</span> = <code class="font-mono bg-white px-1.5 py-0.5 rounded border">.</code>
            </div>
          </div>
        </div>

      </div>

      <!-- Modal Footer -->
      <div class="bg-slate-50 px-6 py-3 border-t border-slate-200 flex items-center justify-between">
        <span class="text-xs text-slate-500">नेपाल सरकार CDC कक्षा ६ गणित पाठ्यक्रमको डिजिटल साथी</span>
        <button onclick="togglePreetiModal(false)" class="px-5 py-2 rounded-xl bg-slate-200 hover:bg-slate-300 font-bold text-slate-800 text-xs transition cursor-pointer">बन्द गर्नुहोस्</button>
      </div>
    </div>
  </div>
"""

# Insert modal before </body>
if 'id="preeti-modal"' not in content:
    content = content.replace("</body>", modal_html + "\n</body>", 1)
    print("Inserted Preeti Modal HTML before </body>")
else:
    print("Preeti modal already present")

# 5. Add JavaScript Functions
js_code = """
  <!-- Preeti Engine and Utilities -->
  <script>
    const UNICODE_TO_PREETI_MAP = {
      '०': '0', '१': '!', '२': '@', '३': '#', '४': '$',
      '५': '%', '६': '^', '७': '&', '८': '*', '९': '(',
      '।': '.', '॥': '..',
      'अ': 'c', 'आ': 'cf', 'इ': 'O', 'ई': 'O{', 'उ': 'p',
      'ऊ': 'pm', 'ऋ': 'C', 'ए': 'P', 'ऐ': 'P}', 'ओ': 'cf]',
      'औ': 'cf}',
      'क': 's', 'ख': 'v', 'ग': 'u', 'घ': '3', 'ङ': 'ª',
      'च': 'r', 'छ': '5', 'ज': 'h', 'झ': 'H', 'ञ': '`',
      'ट': '6', 'ठ': '7', 'ड': '8', 'ढ': '9', 'ण': '0f',
      'त': 't', 'थ': 'y', 'द': 'b', 'ध': 'w', 'न': 'g',
      'प': 'k', 'फ': 'km', 'ब': 'a', 'भ': 'e', 'म': 'd',
      'य': 'o', 'र': '/', 'ल': 'n', 'व': 'j', 'श': 'z',
      'ष': 'if', 'स': ';', 'ह': 'x',
      'ा': 'f', 'ी': 'L', 'ु': "'", 'ू': '"', 'ृ': 'f]',
      'े': ']', 'ै': '}', 'ो': 'f]', 'ौ': 'f}',
      'ं': '+', 'ँ': 'F', 'ः': ':'
    };

    const PREETI_TO_UNICODE_MAP = {
      '0': '०', '!': '१', '@': '२', '#': '३', '$': '४',
      '%': '५', '^': '६', '&': '७', '*': '८', '(': '९',
      '.': '।',
      'sIff': 'कक्षा', 'If': 'क्ष', 'q': 'त्र', '1': 'ज्ञ', '>': 'श्र',
      'cf}': 'औ', 'cf]': 'ओ', 'cf': 'आ', 'c': 'अ',
      'O{': 'ई', 'O': 'इ', 'pm': 'ऊ', 'p': 'उ',
      'P}': 'ऐ', 'P': 'ए', 'C': 'ऋ',
      'km': 'फ', '0f': 'ण', 'if': 'ष',
      's': 'क', 'v': 'ख', 'u': 'ग', '3': 'घ', 'ª': 'ङ',
      'r': 'च', '5': 'छ', 'h': 'ज', 'H': 'झ', '`': 'ञ',
      '6': 'ट', '7': 'ठ', '8': 'ड', '9': 'ढ', '0': 'ण्',
      't': 'त', 'y': 'थ', 'b': 'द', 'w': 'ध', 'g': 'न',
      'k': 'प', 'a': 'ब', 'e': 'भ', 'd': 'म',
      'o': 'य', '/': 'र', 'n': 'ल', 'j': 'व', 'z': 'श',
      ';': 'स', 'x': 'ह',
      'Q': 'त्त', 'G': 'न्न', 'M': 'म्म', 'N': 'ल्ल',
      '?': 'रु', '¿': 'रू',
      'S': 'क्', 'V': 'ख्', 'U': 'ग्', 'R': 'च्', 'T': 'त्', 'Y': 'थ्',
      'W': 'ध्', 'K': 'प्', 'B': 'ब्', 'E': 'भ्', 'D': 'म्', 'Z': 'श्', 'I': 'ष्',
      'f]': 'ो', 'f}': 'ौ', 'f': 'ा', 'L': 'ी', "'": 'ु', '"': 'ू',
      ']': 'े', '}': 'ै', '+': 'ं', 'F': 'ँ', ':': 'ः'
    };

    function unicodeToPreeti(text) {
      if (!text) return '';
      let str = text;

      // Reph conversion
      str = str.replace(/र्([क-ह](?:्[क-ह])*(?:[ाीुूेैोौ]|\')?)/g, '$1{');

      // Chhoti i (ि) reordering
      str = str.replace(/(([क-ह]्)*[क-ह])ि/g, 'l$1');

      // Conjuncts
      str = str.replace(/क्ष/g, 'If');
      str = str.replace(/त्र/g, 'q');
      str = str.replace(/ज्ञ/g, '1');
      str = str.replace(/श्र/g, '>');
      str = str.replace(/द्ध/g, '4');
      str = str.replace(/द्व/g, '2');
      str = str.replace(/त्त/g, 'Q');
      str = str.replace(/न्न/g, 'G');
      str = str.replace(/म्म/g, 'M');
      str = str.replace(/ल्ल/g, 'N');
      str = str.replace(/रु/g, '?');
      str = str.replace(/रू/g, '¿');

      // Half consonants
      const halfConsonants = {
        'क्': 'S', 'ख्': 'V', 'ग्': 'U', 'घ्': '3\\\\',
        'च्': 'R', 'छ्': '5\\\\', 'ज्': 'H', 'झ्': 'H\\\\',
        'ञ्': '~', 'ट्': '6\\\\', 'ठ्': '7\\\\', 'ड्': '8\\\\',
        'ढ्': '9\\\\', 'ण्': '0', 'त्': 'T', 'थ्': 'Y',
        'द्': 'b\\\\', 'ध्': 'W', 'न्': 'G', 'प्': 'K',
        'फ्': 'km\\\\', 'ब्': 'B', 'भ्': 'E', 'म्': 'D',
        'य्': 'O\\\\', 'ल्': 'N', 'व्': 'J', 'श्': 'Z',
        'ष्': 'I', 'स्': ';', 'ह्': 'x\\\\'
      };
      for (const [k, v] of Object.entries(halfConsonants)) {
        str = str.replaceAll(k, v);
      }

      let out = '';
      for (let i = 0; i < str.length; i++) {
        const ch = str[i];
        if (UNICODE_TO_PREETI_MAP[ch] !== undefined) {
          out += UNICODE_TO_PREETI_MAP[ch];
        } else {
          out += ch;
        }
      }
      return out;
    }

    function preetiToUnicode(text) {
      if (!text) return '';
      let s = text;
      s = s.replace(/l(km|if|0f|[svu3ªr5hH`67890tybwgkaedojzn\/;x])/g, '$1ि');
      s = s.replace(/(km|if|0f|[svu3ªr5hH`67890tybwgkaedojzn\/;x])\\{/g, 'र्$1');

      const keys = Object.keys(PREETI_TO_UNICODE_MAP).sort((a,b) => b.length - a.length);
      for (const k of keys) {
        s = s.replaceAll(k, PREETI_TO_UNICODE_MAP[k]);
      }
      return s;
    }

    function togglePreetiModal(show) {
      const modal = document.getElementById('preeti-modal');
      if (!modal) return;
      if (show) {
        modal.classList.remove('hidden');
        modal.style.display = 'flex';
        // Auto convert initial text
        handleU2PLiveConvert();
      } else {
        modal.classList.add('hidden');
        modal.style.display = 'none';
      }
    }

    // Close on Escape key
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') togglePreetiModal(false);
    });

    function setPreetiTab(tab) {
      const u2p = document.getElementById('preeti-panel-u2p');
      const p2u = document.getElementById('preeti-panel-p2u');
      const keys = document.getElementById('preeti-panel-keys');
      const bU2P = document.getElementById('preeti-tab-btn-u2p');
      const bP2U = document.getElementById('preeti-tab-btn-p2u');
      const bKeys = document.getElementById('preeti-tab-btn-keys');

      const activeClass = 'px-4 py-2.5 rounded-t-xl bg-white text-blue-700 border-t border-l border-r border-slate-200 shadow-xs cursor-pointer';
      const inactiveClass = 'px-4 py-2.5 rounded-t-xl text-slate-600 hover:text-blue-700 hover:bg-slate-100 transition cursor-pointer';

      if (u2p) u2p.classList.toggle('hidden', tab !== 'u2p');
      if (p2u) p2u.classList.toggle('hidden', tab !== 'p2u');
      if (keys) keys.classList.toggle('hidden', tab !== 'keys');

      if (bU2P) bU2P.className = (tab === 'u2p') ? activeClass : inactiveClass;
      if (bP2U) bP2U.className = (tab === 'p2u') ? activeClass : inactiveClass;
      if (bKeys) bKeys.className = (tab === 'keys') ? activeClass : inactiveClass;
    }

    function handleU2PLiveConvert() {
      const input = document.getElementById('u2p-input');
      const preview = document.getElementById('u2p-preeti-preview');
      const ascii = document.getElementById('u2p-ascii');
      if (!input || !preview || !ascii) return;

      const txt = input.value.trim() || 'कक्षा ६ गणित — रेखा र कोणहरू';
      const converted = unicodeToPreeti(txt);
      preview.textContent = converted;
      ascii.value = converted;
    }

    function handleP2ULiveConvert() {
      const input = document.getElementById('p2u-input');
      const output = document.getElementById('p2u-output');
      if (!input || !output) return;

      const txt = input.value.trim();
      output.value = preetiToUnicode(txt);
    }

    function loadPreetiSample(type) {
      if (type === 'math') {
        const inp = document.getElementById('u2p-input');
        if (inp) {
          inp.value = 'पाठ १४: रेखा र कोणहरू (Lines and Angles)\\nआसन्न कोण, शीर्षाभिमुख कोण, र एकान्तर कोण।\\nनेपाल सरकार पाठ्यक्रम विकास केन्द्र (CDC) कक्षा ६ गणित।';
          handleU2PLiveConvert();
        }
      } else if (type === 'preeti') {
        const inp = document.getElementById('p2u-input');
        if (inp) {
          inp.value = 'kf7 !$: /]vf / sf]0fx¿ (Lines and Angles)\\ncf;Gg sf]0f, zLiff{led\'v sf]0f, / PsfGt/ sf]0f.\\ng]kfn ;/sf/ kf7\\oqmd ljsf; s]Gb| (CDC) sIff ^ ul0ft.';
          handleP2ULiveConvert();
        }
      }
    }

    function clearPreetiInputs() {
      const uInp = document.getElementById('u2p-input');
      const pInp = document.getElementById('p2u-input');
      if (uInp) uInp.value = '';
      if (pInp) pInp.value = '';
      handleU2PLiveConvert();
      handleP2ULiveConvert();
    }

    function copyPreetiText(targetId, btn) {
      const el = document.getElementById(targetId);
      if (!el) return;
      const text = el.value || el.textContent;
      navigator.clipboard.writeText(text).then(() => {
        const orig = btn.innerHTML;
        btn.innerHTML = '✓ कपी भयो!';
        btn.classList.add('bg-emerald-600');
        setTimeout(() => {
          btn.innerHTML = orig;
          btn.classList.remove('bg-emerald-600');
        }, 1500);
      });
    }

    function changeGlobalFont(fontChoice) {
      document.body.classList.remove('font-mode-mukta', 'font-mode-preeti', 'font-mode-system');
      if (fontChoice === 'preeti') {
        document.body.classList.add('font-mode-preeti');
      } else if (fontChoice === 'system') {
        document.body.classList.add('font-mode-system');
      } else {
        document.body.classList.add('font-mode-mukta');
      }
      try {
        localStorage.setItem('class6_font_choice', fontChoice);
      } catch (e) {}
    }

    // Restore saved font preference on load
    try {
      const savedFont = localStorage.getItem('class6_font_choice') || 'mukta';
      const sel = document.getElementById('global-font-select');
      if (sel) sel.value = savedFont;
      changeGlobalFont(savedFont);
    } catch(e) {}

    // Expose globals
    window.unicodeToPreeti = unicodeToPreeti;
    window.preetiToUnicode = preetiToUnicode;
    window.togglePreetiModal = togglePreetiModal;
    window.setPreetiTab = setPreetiTab;
    window.handleU2PLiveConvert = handleU2PLiveConvert;
    window.handleP2ULiveConvert = handleP2ULiveConvert;
    window.loadPreetiSample = loadPreetiSample;
    window.clearPreetiInputs = clearPreetiInputs;
    window.copyPreetiText = copyPreetiText;
    window.changeGlobalFont = changeGlobalFont;
  </script>
"""

# Insert js_code before </body>
if "unicodeToPreeti" not in content:
    content = content.replace("</body>", js_code + "\n</body>", 1)
    print("Inserted Preeti JS logic before </body>")
else:
    print("Preeti JS logic already present")

# 6. Also update switchChapter to remember last visited chapter
if "localStorage.setItem('class6_last_ch'" not in content:
    content = content.replace(
        "function switchChapter(chNum) {",
        "function switchChapter(chNum) {\n      try { localStorage.setItem('class6_last_ch', chNum); } catch(e){}"
    )
    print("Added localStorage persistence to switchChapter")

# Write to index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully updated index.html! New lines: {len(content.splitlines())}, chars: {len(content)}")
