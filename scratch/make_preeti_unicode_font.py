from fontTools.ttLib import TTFont

font = TTFont('assets/fonts/Preeti Normal/Preeti Normal.otf')
best_cmap = font.getBestCmap()

char_to_ascii = {
    # Independent vowels
    0x0905: 'c',   # अ
    0x0906: 'c',   # आ
    0x0907: 'O',   # इ
    0x0908: 'O',   # ई
    0x0909: 'p',   # उ
    0x090A: 'p',   # ऊ
    0x090B: 'C',   # ऋ
    0x090F: 'P',   # ए
    0x0910: 'P',   # ऐ
    0x0913: 'c',   # ओ
    0x0914: 'c',   # औ

    # Consonants
    0x0915: 's',   # क
    0x0916: 'v',   # ख
    0x0917: 'u',   # ग
    0x0918: '3',   # घ
    0x0919: 0xaa,  # ङ
    0x091A: 'r',   # च
    0x091B: '5',   # छ
    0x091C: 'h',   # ज
    0x091D: 'H',   # झ
    0x091E: '`',   # ञ
    0x091F: '6',   # ट
    0x0920: '7',   # ठ
    0x0921: '8',   # ड
    0x0922: '9',   # ढ
    0x0923: '0',   # ण
    0x0924: 't',   # त
    0x0925: 'y',   # थ
    0x0926: 'b',   # द
    0x0927: 'w',   # ध
    0x0928: 'g',   # न
    0x092A: 'k',   # प
    0x092B: 'm',   # फ
    0x092C: 'a',   # ब
    0x092D: 'e',   # भ
    0x092E: 'd',   # म
    0x092F: 'o',   # य
    0x0930: '/',   # र
    0x0932: 'n',   # ल
    0x0935: 'j',   # व
    0x0936: 'z',   # श
    0x0937: 'i',   # ष
    0x0938: ';',   # स
    0x0939: 'x',   # ह

    # Digits
    0x0966: '0',   # ०
    0x0967: '!',   # १
    0x0968: '@',   # २
    0x0969: '#',   # ३
    0x096A: '$',   # ४
    0x096B: '%',   # ५
    0x096C: '^',   # ६
    0x096D: '&',   # ७
    0x096E: '*',   # ८
    0x096F: '(',   # ९

    # Matras & Signs
    0x093E: 'f',   # ा
    0x093F: 'l',   # ि
    0x0940: 'L',   # ी
    0x0941: "'",   # ु
    0x0942: '"',   # ू
    0x0943: 'f',   # ृ
    0x0947: ']',   # े
    0x0948: '}',   # ै
    0x094B: 'f',   # ो
    0x094C: 'f',   # ौ
    0x0902: '+',   # ं
    0x0901: 'F',   # ँ
    0x0903: ':',   # ः
    0x094D: 'd',   # ्
    0x0964: '.',   # ।
    0x0965: '.'    # ॥
}

for subtable in font['cmap'].tables:
    if subtable.format == 4:
        for ucode, target in char_to_ascii.items():
            ascii_code = ord(target) if isinstance(target, str) else target
            if ascii_code in best_cmap:
                subtable.cmap[ucode] = best_cmap[ascii_code]

font.save('assets/fonts/Preeti-Unicode.otf')
print('Successfully saved assets/fonts/Preeti-Unicode.otf!')
