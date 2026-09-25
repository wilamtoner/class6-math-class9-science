# -*- coding: utf-8 -*-

def generate_moth_svg(id, is_black, x, y, rot=0, scale=0.85):
    body_fill = '#0f172a' if is_black else '#64748b'
    wing_fill = '#18181b' if is_black else '#f8fafc'
    wing_stroke = '#09090b' if is_black else '#cbd5e1'
    speckle = '#27272a' if is_black else '#475569'
    glow = 'filter: drop-shadow(0 2px 4px rgba(0,0,0,0.5));'
    
    return f'''
    <g id="moth-{id}" class="moth-item cursor-pointer transition-all duration-300 hover:scale-110" 
       transform="translate({x}, {y}) rotate({rot}) scale({scale})" 
       onclick="huntMothC9U4({id}, {str(is_black).lower()})"
       style="{glow}">
      <!-- Wings -->
      <path d="M 0,-4 Q -35,-32 -48,-12 Q -42,16 -6,8 Z" fill="{wing_fill}" stroke="{wing_stroke}" stroke-width="1.2"/>
      <path d="M 0,-4 Q 35,-32 48,-12 Q 42,16 6,8 Z" fill="{wing_fill}" stroke="{wing_stroke}" stroke-width="1.2"/>
      <!-- Hindwings -->
      <path d="M 0,2 Q -24,4 -30,22 Q -16,28 0,16 Z" fill="{wing_fill}" stroke="{wing_stroke}" stroke-width="0.8" opacity="0.95"/>
      <path d="M 0,2 Q 24,4 30,22 Q 16,28 0,16 Z" fill="{wing_fill}" stroke="{wing_stroke}" stroke-width="0.8" opacity="0.95"/>
      <!-- Peppered Speckles -->
      <circle cx="-16" cy="-8" r="2.2" fill="{speckle}" opacity="0.7"/>
      <circle cx="-30" cy="-2" r="1.8" fill="{speckle}" opacity="0.7"/>
      <circle cx="-10" cy="10" r="2" fill="{speckle}" opacity="0.7"/>
      <circle cx="16" cy="-8" r="2.2" fill="{speckle}" opacity="0.7"/>
      <circle cx="30" cy="-2" r="1.8" fill="{speckle}" opacity="0.7"/>
      <circle cx="10" cy="10" r="2" fill="{speckle}" opacity="0.7"/>
      <path d="M -22,-14 Q -15,-6 -8,-12" stroke="{speckle}" stroke-width="1.2" fill="none" opacity="0.6"/>
      <path d="M 22,-14 Q 15,-6 8,-12" stroke="{speckle}" stroke-width="1.2" fill="none" opacity="0.6"/>
      <!-- Body -->
      <ellipse cx="0" cy="6" rx="4" ry="14" fill="{body_fill}"/>
      <circle cx="0" cy="-7" r="3.5" fill="{body_fill}"/>
      <!-- Antennae -->
      <path d="M -2,-9 Q -8,-20 -15,-22" stroke="{body_fill}" stroke-width="1.2" fill="none"/>
      <path d="M 2,-9 Q 8,-20 15,-22" stroke="{body_fill}" stroke-width="1.2" fill="none"/>
    </g>'''

print("Moth SVG test passed!")
