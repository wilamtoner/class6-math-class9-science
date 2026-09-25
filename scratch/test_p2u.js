function p2u(str) {
  let s = str;
  // Reorder 'l' before consonant/cluster to after consonant + 'ि'
  s = s.replace(/l(km|if|0f|[svu3ªr5hH`67890tybwgkaedojzn\/;x])/g, '$1ि');
  // Reorder reph '{' after consonant to 'र्' before consonant
  s = s.replace(/(km|if|0f|[svu3ªr5hH`67890tybwgkaedojzn\/;x])\{/g, 'र्$1');
  
  const map = {
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

  const keys = Object.keys(map).sort((a,b) => b.length - a.length);
  for (const k of keys) {
    s = s.replaceAll(k, map[k]);
  }
  return s;
}

console.log('Result for: sIff ^ ul0ft: /]vf / sf]0fx¿');
console.log(p2u('sIff ^ ul0ft: /]vf / sf]0fx¿'));
