const UNICODE_TO_PREETI_MAP = {
  '०': '0', '१': '!', '२': '@', '३': '#', '४': '$',
  '५': '%', '६': '^', '७': '&', '८': '*', '९': '(',
  '।': '.', '॥': '..',
  'अ': 'c', 'आ': 'cf', 'इ': 'O', 'ई': 'O{', 'उ': 'p',
  'ऊ': 'pm', 'ऋ': 'C', 'ए': 'P', 'ऐ': 'P}', 'ओ': 'cf]',
  'औ': 'cf}',
  'क': 's', 'ख': 'v', 'ग': 'u', 'घ': '3', 'ङ': 'ª',
  'च': 'r', 'छ': '5', 'ज': 'h', 'झ': '¡', 'ञ': '`',
  'ट': '6', 'ठ': '7', 'ड': '8', 'ढ': '9', 'ण': '0f',
  'त': 't', 'थ': 'y', 'द': 'b', 'ध': 'w', 'न': 'g',
  'प': 'k', 'फ': 'km', 'ब': 'a', 'भ': 'e', 'म': 'd',
  'य': 'o', 'र': '/', 'ल': 'n', 'व': 'j', 'श': 'z',
  'ष': 'i', 'स': ';', 'ह': 'x',
  'ा': 'f', 'ी': 'L', 'ु': "'", 'ू': '"', 'ृ': 'C',
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
  'ष्': 'i\\', 'स्': ':', 'ह्': 'X'
};

const PREETI_TO_UNICODE_MAP = {
  '0': '०', '!': '१', '@': '२', '#': '३', '$': '४',
  '%': '५', '^': '६', '&': '७', '*': '८', '(': '९',
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
  ';': 'स', ':': 'स्', 'x': 'ह',
  'Q': 'त्त', 'G': 'न्', 'M': 'ः', 'N': 'ल्',
  '?': 'रु', '¿': 'रू',
  'S': 'क्', 'V': 'ख्', 'U': 'ग्', 'R': 'च्', 'T': 'त्', 'Y': 'थ्',
  'W': 'ध्', 'K': 'प्', 'B': 'ब्', 'E': 'भ्', 'D': 'म्', 'Z': 'श्',
  'H': 'ज्', 'J': 'व्', 'X': 'ह्', '~': 'ञ्',
  'f]': 'ो', 'f}': 'ौ', 'f': 'ा', 'L': 'ी', "'": 'ु', '"': 'ू',
  ']': 'े', '}': 'ै', '+': 'ं', 'F': 'ँ', '\\': '्',
  '4': 'द्ध', '2': 'द्व', 'Í': 'ङ्क', 'Î': 'ङ्ख', 'Ë': 'ङ्ग'
};

function unicodeToPreeti(text) {
  if (!text) return '';
  let str = text;

  // Reph conversion: र् + consonant (+ optional vowels) -> consonant (+ optional vowels) + {
  str = str.replace(/र्([क-ह](?:्[क-ह])*(?:[ाीुूेैोौ]|')?)/g, '$1{');

  // Chhoti i (ि) reordering: consonant(s) + ि -> l + consonant(s)
  str = str.replace(/(([क-ह]्)*[क-ह])ि/g, 'l$1');

  // Specific conjuncts
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

  // Single characters
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
  s = s.replace(/l(km|if|0f|[svu3ªr5h`67890tybwgkaedojzn\/;xKMNGQSTRWVBDEIZHX~]|S|V|U|R|T|Y|W|K|B|E|D|Z|H|J|X)/g, '$1ि');

  const keys = Object.keys(PREETI_TO_UNICODE_MAP).sort((a,b) => b.length - a.length);
  for (const k of keys) {
    s = s.replaceAll(k, PREETI_TO_UNICODE_MAP[k]);
  }
  return s;
}

const words = [
  'कक्षा ६ गणित',
  'तथ्याङ्कशास्त्र',
  'निर्देशाङ्क ज्यामिति',
  'क्षेत्रमिति',
  'परिमिति, क्षेत्रफल र आयतन',
  'ठोस वस्तुहरू',
  'सममिति र टेसेलेसन'
];

words.forEach(w => {
  const p = unicodeToPreeti(w);
  const u = preetiToUnicode(p);
  console.log(`Original: ${w} -> Preeti: [${p}] -> Unicode: [${u}] -> Match: ${w === u ? 'YES' : 'NO'}`);
});
