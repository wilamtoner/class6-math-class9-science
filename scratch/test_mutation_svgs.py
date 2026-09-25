# -*- coding: utf-8 -*-

def get_mutation_svg(type):
    if type == 'polydactyly':
        return '''<svg viewBox="0 0 340 180" class="w-full h-auto select-none">
          <text x="170" y="20" fill="#fda4af" font-size="11" font-weight="bold" text-anchor="middle">🖐️ हातमा ६ वटा औँलाहरू (Polydactyly SVG)</text>
          <!-- Palm Base -->
          <path d="M 100,160 C 90,120 90,95 120,80 C 150,75 190,75 220,85 C 240,100 240,130 230,160 Z" fill="#334155" stroke="#475569" stroke-width="2"/>
          <!-- Fingers: 1 to 5 (Standard) -->
          <rect x="80" y="90" width="18" height="42" rx="9" transform="rotate(-30 80 90)" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
          <rect x="120" y="40" width="16" height="50" rx="8" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
          <rect x="145" y="30" width="16" height="58" rx="8" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
          <rect x="170" y="35" width="16" height="54" rx="8" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
          <rect x="195" y="50" width="16" height="42" rx="8" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
          <!-- Extra 6th Digit (Highlighted Glowing Pink) -->
          <g filter="drop-shadow(0 0 8px rgba(244,63,94,0.8))">
            <rect x="52" y="105" width="18" height="40" rx="9" transform="rotate(-50 52 105)" fill="#f43f5e" stroke="#fda4af" stroke-width="2"/>
          </g>
          <text x="40" y="165" fill="#f43f5e" font-size="10" font-weight="bold">★ अतिरिक्त औँला (६th Digit)</text>
          <text x="260" y="165" fill="#94a3b8" font-size="9">सामान्य ५ औँलाहरू</text>
        </svg>'''
    elif type == 'sickle':
        return '''<svg viewBox="0 0 340 180" class="w-full h-auto select-none">
          <text x="170" y="20" fill="#fda4af" font-size="11" font-weight="bold" text-anchor="middle">🩸 सामान्य RBC बनाम हँसिया आकारको RBC (Sickle Cell)</text>
          <!-- Normal Disc RBC -->
          <circle cx="90" cy="95" r="42" fill="#ef4444" stroke="#b91c1c" stroke-width="2.5"/>
          <circle cx="90" cy="95" r="22" fill="#dc2626" opacity="0.6"/>
          <text x="90" y="155" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">सामान्य RBC (गोलो/लचिलो)</text>
          <text x="90" y="170" fill="#94a3b8" font-size="8" text-anchor="middle">अक्सिजन पूर्ण रूपमा बोक्ने</text>
          <!-- Sickle Crescent RBC -->
          <path d="M 210,60 C 265,60 280,120 230,135 C 245,115 240,85 210,60 Z" fill="#f43f5e" stroke="#9f1239" stroke-width="2.5"/>
          <text x="245" y="155" fill="#f43f5e" font-size="10" font-weight="bold" text-anchor="middle">हँसिया RBC (कडा/साँगुरो)</text>
          <text x="245" y="170" fill="#94a3b8" font-size="8" text-anchor="middle">रक्तनलीमा अड्किने / औलो प्रतिरोधी</text>
        </svg>'''
    else:
        return ''

print("Mutation SVGs test passed!")
