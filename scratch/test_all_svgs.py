# -*- coding: utf-8 -*-
"""
Test all SVG generators for Unit 4 Lab
"""

def get_homology_svg(organ):
    if organ == 'bat':
        return '''<svg viewBox="0 0 420 150" class="w-full h-auto select-none">
          <text x="210" y="18" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">🦇 चमेराको पखेटा (Bat Wing - Flying)</text>
          <!-- Patagium Membrane (Purple Translucent) -->
          <path d="M 60,65 Q 160,-10 390,20 Q 380,130 180,120 Q 80,100 60,65 Z" fill="#9333ea" fill-opacity="0.18" stroke="#a855f7" stroke-width="1.2" stroke-dasharray="3,3"/>
          <!-- Humerus -->
          <rect x="30" y="58" width="55" height="14" rx="4" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
          <text x="57" y="69" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Humerus</text>
          <!-- Radius & Ulna -->
          <rect x="95" y="55" width="80" height="10" rx="3" fill="#38bdf8" stroke="#0284c7" stroke-width="1.2"/>
          <text x="135" y="63" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Radius (Long)</text>
          <!-- Carpals -->
          <circle cx="185" cy="60" r="8" fill="#f59e0b" stroke="#b45309" stroke-width="1.2"/>
          <text x="185" y="63" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Carpals</text>
          <!-- Thumb with claw -->
          <path d="M 185,52 L 195,35 L 205,32" stroke="#34d399" stroke-width="2.5" fill="none" stroke-linecap="round"/>
          <!-- 4 Ultra-Long Elongated Fingers (Digits 2, 3, 4, 5) -->
          <path d="M 188,56 Q 260,35 375,25" stroke="#34d399" stroke-width="2.2" fill="none"/>
          <path d="M 190,60 Q 280,65 390,70" stroke="#34d399" stroke-width="2.2" fill="none"/>
          <path d="M 188,64 Q 270,95 365,115" stroke="#34d399" stroke-width="2" fill="none"/>
          <path d="M 185,68 Q 230,110 280,125" stroke="#34d399" stroke-width="2" fill="none"/>
          <text x="320" y="140" fill="#34d399" font-size="9" font-weight="bold">अत्यधिक लामा ४ औँलाहरू (Phalanges)</text>
        </svg>'''
    elif organ == 'whale':
        return '''<svg viewBox="0 0 420 150" class="w-full h-auto select-none">
          <text x="210" y="18" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">🐋 ह्वेलको फ्लिपर (Whale Flipper - Swimming Paddle)</text>
          <!-- Flipper Outer Contour (Soft Cyan Paddle) -->
          <path d="M 40,65 Q 120,25 320,50 Q 380,85 310,115 Q 130,115 40,65 Z" fill="#0284c7" fill-opacity="0.15" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="3,3"/>
          <!-- Short Heavy Humerus -->
          <rect x="50" y="52" width="45" height="28" rx="6" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
          <text x="72" y="70" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Humerus</text>
          <!-- Short Broad Radius & Ulna -->
          <rect x="105" y="44" width="45" height="18" rx="4" fill="#38bdf8" stroke="#0284c7" stroke-width="1.2"/>
          <rect x="105" y="68" width="45" height="18" rx="4" fill="#38bdf8" stroke="#0284c7" stroke-width="1.2"/>
          <text x="127" y="56" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Radius</text>
          <text x="127" y="80" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Ulna</text>
          <!-- Compact Carpals -->
          <rect x="158" y="48" width="22" height="36" rx="4" fill="#f59e0b" stroke="#b45309" stroke-width="1.2"/>
          <!-- Multiple Flattened Phalange Rays (Hyperphalangy) -->
          <g stroke="#34d399" stroke-width="4" stroke-linecap="round" fill="none">
            <line x1="188" y1="52" x2="270" y2="52"/>
            <line x1="188" y1="62" x2="330" y2="68"/>
            <line x1="188" y1="72" x2="320" y2="84"/>
            <line x1="188" y1="80" x2="280" y2="98"/>
            <line x1="188" y1="88" x2="240" y2="108"/>
          </g>
          <text x="260" y="135" fill="#34d399" font-size="9" font-weight="bold" text-anchor="middle">पौडी खेल्ने प्याडल (Flattened Phalanges)</text>
        </svg>'''
    elif organ == 'horse':
        return '''<svg viewBox="0 0 420 150" class="w-full h-auto select-none">
          <text x="210" y="18" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">🐎 घोडाको अगाडिको खुट्टा (Horse Forelimb - Running)</text>
          <!-- Powerful Humerus -->
          <rect x="40" y="55" width="60" height="22" rx="5" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
          <text x="70" y="69" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Humerus</text>
          <!-- Long Fused Radius & Ulna -->
          <rect x="110" y="58" width="95" height="16" rx="4" fill="#38bdf8" stroke="#0284c7" stroke-width="1.5"/>
          <text x="155" y="69" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Radius-Ulna (Fused)</text>
          <!-- Knee (Carpals) -->
          <rect x="215" y="56" width="22" height="20" rx="4" fill="#f59e0b" stroke="#b45309" stroke-width="1.2"/>
          <text x="226" y="69" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Carpals</text>
          <!-- Elongated Cannon Bone (3rd Metacarpal) -->
          <rect x="245" y="60" width="75" height="12" rx="3" fill="#34d399" stroke="#059669" stroke-width="1.5"/>
          <text x="282" y="70" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">3rd Metacarpal</text>
          <!-- Single 3rd Digit (Phalanges) + Hoof -->
          <rect x="328" y="58" width="30" height="16" rx="3" fill="#34d399" stroke="#059669" stroke-width="1.5"/>
          <path d="M 364,52 L 388,52 L 392,80 L 364,80 Z" fill="#475569" stroke="#1e293b" stroke-width="2"/>
          <text x="378" y="69" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">खुर (Hoof)</text>
          <text x="280" y="135" fill="#94a3b8" font-size="9" text-anchor="middle">तेस्रो औँला मात्र बलियो भई खुर बनेको (Digit 3)</text>
        </svg>'''
    elif organ == 'cat':
        return '''<svg viewBox="0 0 420 150" class="w-full h-auto select-none">
          <text x="210" y="18" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">🐆 चीता वा बिरालोको अगाडिको खुट्टा (Cat Forelimb - Leaping/Hunting)</text>
          <!-- Curved Humerus -->
          <rect x="40" y="52" width="65" height="20" rx="5" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
          <text x="72" y="65" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">Humerus</text>
          <!-- Radius & Ulna -->
          <rect x="115" y="47" width="80" height="13" rx="3" fill="#38bdf8" stroke="#0284c7" stroke-width="1.2"/>
          <rect x="115" y="67" width="80" height="13" rx="3" fill="#38bdf8" stroke="#0284c7" stroke-width="1.2"/>
          <text x="155" y="57" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Radius</text>
          <text x="155" y="77" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Ulna</text>
          <!-- Carpals -->
          <rect x="205" y="52" width="22" height="24" rx="4" fill="#f59e0b" stroke="#b45309" stroke-width="1.2"/>
          <!-- Metacarpals & Claws -->
          <g stroke="#34d399" stroke-width="3" stroke-linecap="round" fill="none">
            <line x1="235" y1="52" x2="300" y2="42"/>
            <line x1="235" y1="58" x2="315" y2="52"/>
            <line x1="235" y1="65" x2="320" y2="66"/>
            <line x1="235" y1="72" x2="310" y2="80"/>
            <line x1="235" y1="78" x2="280" y2="92"/>
          </g>
          <!-- Curved Claws (तीखा नङ्ग्राहरू) -->
          <path d="M 300,42 Q 315,38 312,32 M 315,52 Q 330,48 327,42 M 320,66 Q 335,66 332,60 M 310,80 Q 325,84 322,90" stroke="#f43f5e" stroke-width="2.5" fill="none" stroke-linecap="round"/>
          <text x="270" y="135" fill="#f43f5e" font-size="9" font-weight="bold" text-anchor="middle">शिकार समात्ने तीखा नङ्ग्राहरू (Retractile Claws)</text>
        </svg>'''
    else: # human
        return '''<svg viewBox="0 0 420 150" class="w-full h-auto select-none">
          <text x="210" y="18" fill="#e2e8f0" font-size="12" font-weight="bold" text-anchor="middle">🖐️ मानिसको हात (Human Hand - Grasping/Tools)</text>
          <!-- Humerus -->
          <rect x="30" y="52" width="75" height="22" rx="5" fill="#a855f7" stroke="#7e22ce" stroke-width="1.5"/>
          <text x="67" y="66" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">Humerus (बाहु)</text>
          <!-- Joint -->
          <circle cx="115" cy="63" r="5" fill="#cbd5e1"/>
          <!-- Radius & Ulna -->
          <rect x="128" y="45" width="75" height="15" rx="3" fill="#38bdf8" stroke="#0284c7" stroke-width="1.2"/>
          <rect x="128" y="66" width="75" height="15" rx="3" fill="#38bdf8" stroke="#0284c7" stroke-width="1.2"/>
          <text x="165" y="56" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Radius (रेडियस)</text>
          <text x="165" y="77" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Ulna (अल्ना)</text>
          <!-- Carpals (8 Wrist Bones) -->
          <rect x="212" y="47" width="24" height="34" rx="4" fill="#f59e0b" stroke="#b45309" stroke-width="1.2"/>
          <text x="224" y="67" fill="#ffffff" font-size="7" font-weight="bold" text-anchor="middle">Carpals</text>
          <!-- 5 Digits with Opposable Thumb -->
          <!-- Opposable Thumb -->
          <path d="M 238,48 L 265,30 L 290,26" stroke="#34d399" stroke-width="3" fill="none" stroke-linecap="round"/>
          <text x="295" y="24" fill="#34d399" font-size="8" font-weight="bold">बुढी औँला (Thumb)</text>
          <!-- 4 Fingers -->
          <g stroke="#34d399" stroke-width="2.5" stroke-linecap="round" fill="none">
            <path d="M 238,55 L 295,48 L 335,46"/>
            <path d="M 238,62 L 310,60 L 350,60"/>
            <path d="M 238,69 L 305,72 L 340,75"/>
            <path d="M 238,76 L 285,85 L 320,90"/>
          </g>
          <text x="280" y="135" fill="#34d399" font-size="9" font-weight="bold" text-anchor="middle">५ ओटा औँलाहरू (Metacarpals & 14 Phalanges)</text>
        </svg>'''

print("All homology SVGs compiled successfully!")
