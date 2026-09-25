// Test full Preeti JS logic

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
  'q': 'त्र', '1': 'ज्ञ', 'Q': 'त्त', 'G': 'न्न', 'M': 'म्म', 'N': 'ल्ल',
  '?': 'रु', '¿': 'रू',
  'S': 'क्', 'V': 'ख्', 'U': 'ग्', 'R': 'च्', 'T': 'त्', 'Y': 'थ्',
  'W': 'ध्', 'K': 'प्', 'B': 'ब्', 'E': 'भ्', 'D': 'म्', 'Z': 'श्', 'I': 'ष्',
  'f]': 'ो', 'f}': 'ौ', 'f': 'ा', 'L': 'ी', "'": 'ु', '"': 'ू',
  ']': 'े', '}': 'ै', '+': 'ं', 'F': 'ँ', ':': 'ः'
};

function unicodeToPreeti(text) {
  if (!text) return '';
  let str = text;

  // 1. Reph conversion: र्[consonant cluster] -> [consonant cluster]{
  str = str.replace(/र्([क-ह](?:्[क-ह])*(?:[ाीुूेैोौ]|\')?)/g, '$1{');

  // 2. Chhoti i (ि) reordering:
  str = str.replace(/(([क-ह]्)*[क-ह])ि/g, 'l$1');

  // 3. Conjuncts
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

  // 4. Halanta consonants
  const halfConsonants = {
    'क्': 'S', 'ख्': 'V', 'ग्': 'U', 'घ्': '3\\',
    'च्': 'R', 'छ्': '5\\', 'ज्': 'H', 'झ्': 'H\\',
    'ञ्': '~', 'ट्': '6\\', 'ठ्': '7\\', 'ड्': '8\\',
    'ढ्': '9\\', 'ण्': '0', 'त्': 'T', 'थ्': 'Y',
    'द्': 'b\\', 'ध्': 'W', 'न्': 'G', 'प्': 'K',
    'फ्': 'km\\', 'ब्': 'B', 'भ्': 'E', 'म्': 'D',
    'य्': 'O\\', 'ल्': 'N', 'व्': 'J', 'श्': 'Z',
    'ष्': 'I', 'स्': ';', 'ह्': 'x\\'
  };
  for (const [k, v] of Object.entries(halfConsonants)) {
    str = str.replaceAll(k, v);
  }

  // 5. Remaining single characters
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
  let str = text;

  // 1. Reph: [cluster]{ -> र्[cluster]
  str = str.replace(/([a-zA-Z0-9_\-~`!@#$%^&*()=+[\]{}|;:,.<>?¿]+)\{/g, 'र्$1');

  // 2. Chhoti i (l[cluster] -> [cluster]ि)
  str = str.replace(/l([a-zA-Z0-9_\-~`!@#$%^&*()=+[\]{}|;:,.<>?¿]+)/g, '$1ि');

  const sortedKeys = Object.keys(PREETI_TO_UNICODE_MAP).sort((a, b) => b.length - a.length);
  for (const key of sortedKeys) {
    str = str.replaceAll(key, PREETI_TO_UNICODE_MAP[key]);
  }

  return str;
}

console.log('Testing Preeti conversion functions:');
console.log('1. Unicode -> Preeti:');
const p1 = unicodeToPreeti('कक्षा ६ गणित: रेखा र कोणहरू');
console.log('   Input:  कक्षा ६ गणित: रेखा र कोणहरू');
console.log('   Preeti: ' + p1);

console.log('2. Preeti -> Unicode:');
const u1 = preetiToUnicode('sIff ^ ul0ft: /]vf / sf]0fx¿');
console.log('   Input:  sIff ^ ul0ft: /]vf / sf]0fx¿');
console.log('   Unicode:' + u1);
