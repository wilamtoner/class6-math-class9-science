
    const UNICODE_TO_PREETI_MAP = {
      '०': ')', '१': '!', '२': '@', '३': '#', '४': '$',
      '५': '%', '६': '^', '७': '&', '८': '*', '९': '(',
      '।': '.', '॥': '..',
      '(': '-', ')': '_',
      'अ': 'c', 'आ': 'cf', 'इ': 'O', 'ई': 'O{', 'उ': 'p',
      'ऊ': 'pm', 'ऋ': 'C', 'ए': 'P', 'ऐ': 'P}', 'ओ': 'cf]',
      'औ': 'cf}',
      'क': 's', 'ख': 'v', 'ग': 'u', 'घ': '3', 'ङ': 'ª',
      'च': 'r', 'छ': '5', 'ज': 'h', 'झ': '¡', 'ञ': '`',
      'ट': '6', 'ठ': '7', 'ड': '8', 'ढ': '9', 'ण': '0f',
      'त': 't', 'थ': 'y', 'द': 'b', 'ध': 'w', 'न': 'g',
      'प': 'k', 'फ': 'km', 'ब': 'a', 'भ': 'e', 'म': 'd',
      'य': 'o', 'र': '/', 'ल': 'n', 'व': 'j', 'श': 'z',
      'ष': 'if', 'स': ';', 'ह': 'x',
      'ा': 'f', 'ी': 'L', 'ु': "'", 'ू': '"', 'ृ': '[',
      'े': ']', 'ै': '}', 'ो': 'f]', 'ौ': 'f}',
      'ं': '+', 'ँ': 'F', 'ः': 'M', '्': '\\'
    };

    const halfConsonants = {
      'क्': 'S', 'ख्': 'V', 'ग्': 'U', 'घ्': '3\\',
      'ङ्': 'ª\\', 'च्': 'R', 'छ्': '5\\', 'ज्': 'H', 'झ्': '¡\\',
      'ञ्': '~', 'ट्': '6\\', 'ठ्': '7\\', 'ड्': '8\\',
      'ढ्': '9\\', 'ण्': '0', 'त्': 'T', 'थ्': 'Y',
      'द्': 'b\\', 'ध्': 'W', 'न्': 'G', 'प्': 'K',
      'फ्': 'km\\', 'ब्': 'B', 'भ्': 'E', 'म्': 'D',
      'य्': 'o\\', 'ल्': 'N', 'व्': 'J', 'श्': 'Z',
      'ष्': 'I', 'स्': ':', 'ह्': 'X'
    };

    const PREETI_TO_UNICODE_MAP = {
      ')': '०', '!': '१', '@': '२', '#': '३', '$': '४',
      '%': '५', '^': '६', '&': '७', '*': '८', '(': '९',
      '-': '(', '_': ')',
      '.': '।', '..': '॥',
      'sIff': 'कक्षा', 'If': 'क्ष', 'q': 'त्र', '1': 'ज्ञ', '>': 'श्र',
      'cf}': 'औ', 'cf]': 'ओ', 'cf': 'आ', 'c': 'अ',
      'O{': 'ई', 'O': 'इ', 'pm': 'ऊ', 'p': 'उ',
      'P}': 'ऐ', 'P': 'ए', 'C': 'ऋ',
      'km': 'फ', '0f': 'ण', 'if': 'ष',
      's': 'क', 'v': 'ख', 'u': 'ग', '3': 'घ', 'ª': 'ङ',
      'r': 'च', '5': 'छ', 'h': 'ज', '¡': 'झ', '`': 'ञ',
      '6': 'ट', '7': 'ठ', '8': 'ड', '9': 'ढ', '0': 'ण्',
      't': 'त', 'y': 'थ', 'b': 'द', 'w': 'ध', 'g': 'न',
      'k': 'प', 'a': 'ब', 'e': 'भ', 'd': 'म',
      'o': 'य', '/': 'र', 'n': 'ल', 'j': 'व', 'z': 'श',
      ';': 'स', 'x': 'ह',
      'Q': 'त्त', 'G': 'न्', 'N': 'ल्',
      '?': 'रु', '¿': 'रू',
      'S': 'क्', 'V': 'ख्', 'U': 'ग्', 'R': 'च्', 'T': 'त्', 'Y': 'थ्',
      'W': 'ध्', 'K': 'प्', 'B': 'ब्', 'E': 'भ्', 'D': 'म्', 'Z': 'श्',
      'H': 'ज्', 'J': 'व्', 'X': 'ह्', '~': 'ञ्', 'I': 'ष्',
      ':': 'स्', 'M': ':',
      'f]': 'ो', 'f}': 'ौ', 'f': 'ा', 'L': 'ी', "'": 'ु', '"': 'ू',
      ']': 'े', '}': 'ै', '+': 'ं', 'F': 'ँ', '\\': '्', '[': 'ृ',
      '4': 'द्ध', '2': 'द्व', 'Í': 'ङ्क', 'Î': 'ङ्ख', 'Ë': 'ङ्ग'
    };

    function unicodeToPreeti(text) {
      if (!text) return '';
      let str = text;

      // Colon to Preeti M (visarga/colon)
      str = str.replace(/:/g, 'M');

      // Reph conversion
      str = str.replace(/र्([क-ह](?:्[क-ह])*(?:[ाीुूेैोौ]|')?)/g, '$1{');

      // Chhoti i (ि) reordering
      str = str.replace(/(([क-ह]्)*[क-ह])ि/g, 'l$1');

      // Conjuncts
      str = str.replace(/कक्षा/g, 'sIff');
      str = str.replace(/क्ष/g, 'If');
      str = str.replace(/त्र/g, 'q');
      str = str.replace(/ज्ञ/g, '1');
      str = str.replace(/श्र/g, '>');
      str = str.replace(/द्ध/g, '4');
      str = str.replace(/द्व/g, '2');
      str = str.replace(/त्त/g, 'Q');
      str = str.replace(/रु/g, '?');
      str = str.replace(/रू/g, '¿');

      // Half consonants
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

      // Reph handling: consonant + optional matra + { -> र् + consonant + optional matra
      s = s.replace(/([a-zA-Z0-9ª\`\/;:\\]|km|if|0f)(f\]|f\}|[fL\'\"\]\}])?\{/g, (m, c, v) => {
        return 'र्' + c + (v || '');
      });

      // Chhoti i (l) handling: l + consonant -> consonant + ि
      s = s.replace(/l(km|if|0f|[svu3ªr5h\`67890tybwgkaedojzn\/;xKMNGQSTRWVBDEIZHX~]|S|V|U|R|T|Y|W|K|B|E|D|Z|H|J|X)/g, '$1ि');

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
          inp.value = 'पाठ १४: रेखा र कोणहरू (Lines and Angles)\nआसन्न कोण, शीर्षाभिमुख कोण, र एकान्तर कोण।\nनेपाल सरकार पाठ्यक्रम विकास केन्द्र (CDC) कक्षा ६ गणित।';
          handleU2PLiveConvert();
        }
      } else if (type === 'preeti') {
        const inp = document.getElementById('p2u-input');
        if (inp) {
          inp.value = "kf7 !$: /]vf / sf]0fx¿ (Lines and Angles)\\ncf;Gg sf]0f, zLiff{led\\'v sf]0f, / PsfGt/ sf]0f.\\ng]kfn ;/sf/ kf7\\\\oqmd ljsf; s]Gb| (CDC) sIff ^ ul0ft.";
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
      const savedFont = localStorage.getItem('class6_font_choice') || 'preeti';
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
  