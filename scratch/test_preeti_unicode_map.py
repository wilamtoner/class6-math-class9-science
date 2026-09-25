from fontTools.ttLib import TTFont

font = TTFont('assets/fonts/Preeti Normal/Preeti Normal.otf')
cmap = font.getBestCmap()

char_to_ascii = {
    0x0905: 'c', 0x0915: 's', 0x0916: 'v', 0x0917: 'u', 0x0918: '3',
    0x091A: 'r', 0x091B: '5', 0x091C: 'h', 0x091D: 'H',
    0x091F: '6', 0x0920: '7', 0x0921: '8', 0x0922: '9', 0x0923: '0',
    0x0924: 't', 0x0925: 'y', 0x0926: 'b', 0x0927: 'w', 0x0928: 'g',
    0x092A: 'k', 0x092B: 'm', 0x092C: 'a', 0x092D: 'e', 0x092E: 'd',
    0x092F: 'o', 0x0930: '/', 0x0932: 'n', 0x0935: 'j', 0x0936: 'z',
    0x0937: 'i', 0x0938: ';', 0x0939: 'x',
    0x0966: '0', 0x0967: '!', 0x0968: '@', 0x0969: '#', 0x096A: '$',
    0x096B: '%', 0x096C: '^', 0x096D: '&', 0x096E: '*', 0x096F: '(',
    0x093E: 'f', 0x0940: 'L', 0x0941: "'", 0x0942: '"', 0x0947: ']',
    0x0948: '}', 0x0902: '+', 0x0901: 'F', 0x0903: ':', 0x0964: '.'
}

new_entries = {}
for ucode, target in char_to_ascii.items():
    ascii_code = ord(target) if isinstance(target, str) else target
    if ascii_code in cmap:
        glyph_name = cmap[ascii_code]
        new_entries[ucode] = glyph_name

print(f"Successfully mapped {len(new_entries)} Devanagari Unicode characters directly to Preeti glyphs!")
