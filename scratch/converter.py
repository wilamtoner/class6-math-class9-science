# Complete Unicode to Preeti and Preeti to Unicode converter
import re

def unicode_to_preeti(text):
    if not text:
        return ""
    
    # 1. Handle special conjuncts and exceptions first
    # Reph (र्) conversion:
    # In Devanagari: र + ् + [consonant] -> [consonant] + '{' in Preeti
    # E.g. गर्म -> ud{, कार्य -> sfo{, पूर्ण -> k\"0f{
    
    # Handle 'त्र': 'q'
    # 'ज्ञ': '1'
    # 'क्ष': 'If' (क् + ष)
    
    # Let's define the comprehensive mapping dictionary
    mapping = {
        '०': '0', '१': '!', '२': '@', '३': '#', '४': '$',
        '५': '%', '६': '^', '७': '&', '८': '*', '९': '(',
        'अ': 'c', 'आ': 'cf', 'इ': 'O', 'ई': 'O{', 'उ': 'p',
        'ऊ': 'pm', 'ऋ': 'C', 'ए': 'P', 'ऐ': 'P}', 'ओ': 'cf]',
        'औ': 'cf}', 'क': 's', 'ख': 'v', 'ग': 'u', 'घ': '3',
        'ङ': 'ª', 'च': 'r', 'छ': '5', 'ज': 'h', 'झ': 'H',
        'ञ': '`', 'ट': '6', 'ठ': '7', 'ड': '8', 'ढ': '9',
        'ण': '0f', 'त': 't', 'थ': 'y', 'द': 'b', 'ध': 'w',
        'न': 'g', 'प': 'k', 'फ': 'km', 'ब': 'a', 'भ': 'e',
        'म': 'd', 'य': 'o', 'र': '/', 'ल': 'n', 'व': 'j',
        'श': 'z', 'ष': 'if', 'स': ';', 'ह': 'x',
        'ा': 'f', 'ी': 'L', 'ु': "'", 'ू': '"', 'ृ': 'f]',
        'े': ']', 'ै': '}', 'ो': 'f]', 'ौ': 'f}',
        'ं': '+', 'ँ': 'F', 'ः': ':', '्': '्', '।': '.'
    }
    
    # Complex rules:
    # 1. R-vowel and Reph
    # 2. Hraswa I-kar (ि) reordering:
    # In Unicode: consonant + halanta + consonant + ि  OR consonant + ि
    # In Preeti: 'l' is placed BEFORE the full syllable!
    
    # Let's test with regex reordering
    s = text
    
    # Pre-process 'र्' (Reph): 'र्' followed by consonant/cluster -> syllable + '{'
    s = re.sub(r'र्([क-ह](?:्[क-ह])*(?:[ाीुूेैोौ]|\')?)', r'\1{', s)
    
    # Pre-process 'ि' (chhoti i): consonant cluster + 'ि' -> 'l' + consonant cluster
    # e.g. कि -> lक, स्थि -> lस्थ, क्सि -> lक्स
    s = re.sub(r'(([क-ह]्)*[क-ह])ि', r'l\1', s)
    
    # Specific conjuncts
    s = s.replace('क्ष', 'If')
    s = s.replace('त्र', 'q')
    s = s.replace('ज्ञ', '1')
    s = s.replace('श्र', '>')
    s = s.replace('द्ध', '4')
    s = s.replace('द्व', '2')
    s = s.replace('त्त', 'Q')
    s = s.replace('न्न', 'G')
    s = s.replace('म्म', 'M')
    s = s.replace('ल्ल', 'N')
    
    # Half letters (consonant + halanta)
    half_map = {
        'क्': 'S', 'ख्': 'V', 'ग्': 'U', 'घ्': '3\\',
        'च्': 'R', 'छ्': '5\\', 'ज्': 'H', 'झ्': 'H\\',
        'ञ्': '~', 'ट्': '6\\', 'ठ्': '7\\', 'ड्': '8\\',
        'ढ्': '9\\', 'ण्': '0', 'त्': 'T', 'थ्': 'Y',
        'द्': 'b\\', 'ध्': 'W', 'न्': 'G', 'प्': 'K',
        'फ्': 'km\\', 'ब्': 'B', 'भ्': 'E', 'म्': 'D',
        'य्': 'O\\', 'ल्': 'N', 'व्': 'J', 'श्': 'Z',
        'ष्': 'I', 'स्': ';', 'ह्': 'x\\'
    }
    for k, v in half_map.items():
        s = s.replace(k, v)
        
    # Replace remaining individual characters
    res = []
    for ch in s:
        if ch in mapping:
            res.append(mapping[ch])
        else:
            res.append(ch)
            
    return ''.join(res)

sample = "कक्षा ६ गणित - डिजिटल गुरु"
converted = unicode_to_preeti(sample)
print("Input :", sample)
print("Preeti:", converted)
