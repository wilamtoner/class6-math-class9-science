import re

palette = {
    'slate': {'50':'#f8fafc', '100':'#f1f5f9', '200':'#e2e8f0', '300':'#cbd5e1', '400':'#94a3b8', '500':'#64748b', '600':'#475569', '700':'#334155', '800':'#1e293b', '900':'#0f172a', '950':'#020617'},
    'blue': {'50':'#eff6ff', '100':'#dbeafe', '200':'#bfdbfe', '300':'#93c5fd', '400':'#60a5fa', '500':'#3b82f6', '600':'#2563eb', '700':'#1d4ed8', '800':'#1e40af', '900':'#1e3a8a', '950':'#172554'},
    'indigo': {'50':'#eef2ff', '100':'#e0e7ff', '200':'#c7d2fe', '300':'#a5b4fc', '400':'#818cf8', '500':'#6366f1', '600':'#4f46e5', '700':'#4338ca', '800':'#3730a3', '900':'#312e81', '950':'#1e1b4b'},
    'emerald': {'50':'#ecfdf5', '100':'#d1fae5', '200':'#a7f3d0', '300':'#6ee7b7', '400':'#34d399', '500':'#10b981', '600':'#059669', '700':'#047857', '800':'#065f46', '900':'#064e3b', '950':'#022c22'},
    'purple': {'50':'#faf5ff', '100':'#f3e8ff', '200':'#e9d5ff', '300':'#d8b4fe', '400':'#c084fc', '500':'#a855f7', '600':'#9333ea', '700':'#7e22ce', '800':'#6b21a8', '900':'#581c87', '950':'#3b0764'},
    'amber': {'50':'#fffbeb', '100':'#fef3c7', '200':'#fde68a', '300':'#fcd34d', '400':'#fbbf24', '500':'#f59e0b', '600':'#d97706', '700':'#b45309', '800':'#92400e', '900':'#78350f', '950':'#451a03'},
    'rose': {'50':'#fff1f2', '100':'#ffe4e6', '200':'#fecdd3', '300':'#fda4af', '400':'#fb7185', '500':'#f43f5e', '600':'#e11d48', '700':'#be123c', '800':'#9f1239', '900':'#881337', '950':'#4c0519'},
    'green': {'50':'#f0fdf4', '100':'#dcfce7', '200':'#bbf7d0', '300':'#86efac', '400':'#4ade80', '500':'#22c55e', '600':'#16a34a', '700':'#15803d', '800':'#166534', '900':'#14532d', '950':'#052e16'},
    'teal': {'50':'#f0fdfa', '100':'#ccfbf1', '200':'#99f6e4', '300':'#5eead4', '400':'#2dd4bf', '500':'#14b8a6', '600':'#0d9488', '700':'#0f766e', '800':'#115e59', '900':'#134e4a', '950':'#042f2e'},
    'orange': {'50':'#fff7ed', '100':'#ffedd5', '200':'#fed7aa', '800':'#9a3412', '900':'#7c2d12'},
    'red': {'50':'#fef2f2', '100':'#fee2e2', '500':'#ef4444', '600':'#dc2626', '700':'#b91c1c', '800':'#991b1b'},
}

def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def css_escape(cls):
    return re.sub(r'([:\/\.\[\]])', r'\\\1', cls)

rules = []
rules_sm = []
rules_md = []
rules_lg = []

with open('scratch/all_classes.txt') as f:
    all_classes = [l.strip() for l in f if l.strip()]

unhandled = []

for cls in all_classes:
    sel = '.' + css_escape(cls)
    
    # Check media queries first
    if cls.startswith('sm:'):
        sub = cls[3:]
        if sub == 'grid-cols-2':
            rules_sm.append(f"{sel} {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}")
            continue
        elif sub == 'grid-cols-3':
            rules_sm.append(f"{sel} {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }}")
            continue
            
    if cls.startswith('md:'):
        sub = cls[3:]
        if sub == 'flex-row':
            rules_md.append(f"{sel} {{ flex-direction: row; }}")
            continue
        elif sub == 'w-80':
            rules_md.append(f"{sel} {{ width: 20rem; flex-shrink: 0; }}")
            continue
        elif sub.startswith('grid-cols-'):
            n = sub.split('-')[-1]
            rules_md.append(f"{sel} {{ grid-template-columns: repeat({n}, minmax(0, 1fr)); }}")
            continue
        elif sub == 'col-span-2':
            rules_md.append(f"{sel} {{ grid-column: span 2 / span 2; }}")
            continue
        elif sub == 'items-center':
            rules_md.append(f"{sel} {{ align-items: center; }}")
            continue
        elif sub == 'self-center':
            rules_md.append(f"{sel} {{ align-self: center; }}")
            continue
        elif sub == 'p-6':
            rules_md.append(f"{sel} {{ padding: 1.5rem; }}")
            continue
        elif sub == 'p-8':
            rules_md.append(f"{sel} {{ padding: 2rem; }}")
            continue
        elif sub == 'text-sm':
            rules_md.append(f"{sel} {{ font-size: 0.875rem; line-height: 1.25rem; }}")
            continue
        elif sub == 'text-base':
            rules_md.append(f"{sel} {{ font-size: 1rem; line-height: 1.5rem; }}")
            continue
        elif sub == 'text-lg':
            rules_md.append(f"{sel} {{ font-size: 1.125rem; line-height: 1.75rem; }}")
            continue
        elif sub == 'text-2xl':
            rules_md.append(f"{sel} {{ font-size: 1.5rem; line-height: 2rem; }}")
            continue
        elif sub == 'text-3xl':
            rules_md.append(f"{sel} {{ font-size: 1.875rem; line-height: 2.25rem; }}")
            continue
            
    if cls.startswith('lg:'):
        sub = cls[3:]
        if sub == 'grid-cols-3':
            rules_lg.append(f"{sel} {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }}")
            continue

    # Hover
    if cls.startswith('hover:'):
        sub = cls[6:]
        if sub.startswith('bg-'):
            color_part = sub[3:]
            if color_part == 'white/20':
                rules.append(f"{sel}:hover {{ background-color: rgba(255, 255, 255, 0.2); }}")
                continue
            parts = color_part.split('-')
            cname = parts[0]
            shade = parts[1]
            hex_val = palette[cname][shade]
            rules.append(f"{sel}:hover {{ background-color: {hex_val}; }}")
            continue

    # Focus
    if cls.startswith('focus:'):
        sub = cls[6:]
        if sub == 'outline-none':
            rules.append(f"{sel}:focus {{ outline: 2px solid transparent; outline-offset: 2px; }}")
            continue
        elif sub == 'ring-2':
            rules.append(f"{sel}:focus {{ box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.5); }}")
            continue
        elif sub.startswith('ring-'):
            rules.append(f"{sel}:focus {{ box-shadow: 0 0 0 2px #3b82f6; }}")
            continue

    # Basic display / layout
    if cls == 'block': rules.append(f"{sel} {{ display: block; }}"); continue
    if cls == 'inline-block': rules.append(f"{sel} {{ display: inline-block; }}"); continue
    if cls == 'inline-flex': rules.append(f"{sel} {{ display: inline-flex; }}"); continue
    if cls == 'flex': rules.append(f"{sel} {{ display: flex; }}"); continue
    if cls == 'flex-col': rules.append(f"{sel} {{ flex-direction: column; }}"); continue
    if cls == 'flex-1': rules.append(f"{sel} {{ flex: 1 1 0%; }}"); continue
    if cls == 'flex-wrap': rules.append(f"{sel} {{ flex-wrap: wrap; }}"); continue
    if cls == 'grid': rules.append(f"{sel} {{ display: grid; }}"); continue
    if cls == 'hidden': rules.append(f"{sel} {{ display: none !important; }}"); continue

    if cls.startswith('grid-cols-'):
        n = cls.split('-')[-1]
        rules.append(f"{sel} {{ grid-template-columns: repeat({n}, minmax(0, 1fr)); }}")
        continue

    if cls == 'items-center': rules.append(f"{sel} {{ align-items: center; }}"); continue
    if cls == 'items-start': rules.append(f"{sel} {{ align-items: flex-start; }}"); continue
    if cls == 'justify-between': rules.append(f"{sel} {{ justify-content: space-between; }}"); continue
    if cls == 'justify-center': rules.append(f"{sel} {{ justify-content: center; }}"); continue
    if cls == 'justify-end': rules.append(f"{sel} {{ justify-content: flex-end; }}"); continue
    if cls == 'self-start': rules.append(f"{sel} {{ align-self: flex-start; }}"); continue

    # Positioning & Dimensions
    if cls == 'relative': rules.append(f"{sel} {{ position: relative; }}"); continue
    if cls == 'sticky': rules.append(f"{sel} {{ position: sticky; }}"); continue
    if cls == 'top-0': rules.append(f"{sel} {{ top: 0px; }}"); continue
    if cls == 'z-50': rules.append(f"{sel} {{ z-index: 50; }}"); continue
    if cls == 'w-full': rules.append(f"{sel} {{ width: 100%; }}"); continue
    if cls == 'w-1/2': rules.append(f"{sel} {{ width: 50%; }}"); continue
    if cls == 'w-1/3': rules.append(f"{sel} {{ width: 33.333333%; }}"); continue
    if cls == 'w-1/4': rules.append(f"{sel} {{ width: 25%; }}"); continue
    if cls == 'w-16': rules.append(f"{sel} {{ width: 4rem; }}"); continue
    if cls == 'w-11': rules.append(f"{sel} {{ width: 2.75rem; }}"); continue
    if cls == 'w-8': rules.append(f"{sel} {{ width: 2rem; }}"); continue
    if cls == 'w-7': rules.append(f"{sel} {{ width: 1.75rem; }}"); continue
    if cls == 'w-6': rules.append(f"{sel} {{ width: 1.5rem; }}"); continue
    if cls == 'w-3': rules.append(f"{sel} {{ width: 0.75rem; }}"); continue
    if cls == 'h-full': rules.append(f"{sel} {{ height: 100%; }}"); continue
    if cls == 'h-fit': rules.append(f"{sel} {{ height: fit-content; }}"); continue
    if cls == 'h-11': rules.append(f"{sel} {{ height: 2.75rem; }}"); continue
    if cls == 'h-8': rules.append(f"{sel} {{ height: 2rem; }}"); continue
    if cls == 'h-7': rules.append(f"{sel} {{ height: 1.75rem; }}"); continue
    if cls == 'h-6': rules.append(f"{sel} {{ height: 1.5rem; }}"); continue
    if cls == 'h-3': rules.append(f"{sel} {{ height: 0.75rem; }}"); continue
    if cls == 'min-h-screen': rules.append(f"{sel} {{ min-height: 100vh; }}"); continue
    if cls == 'max-w-7xl': rules.append(f"{sel} {{ max-width: 80rem; margin-left: auto; margin-right: auto; }}"); continue
    if cls == 'max-w-3xl': rules.append(f"{sel} {{ max-width: 48rem; }}"); continue
    if cls == 'max-w-2xl': rules.append(f"{sel} {{ max-width: 42rem; }}"); continue
    if cls == 'max-w-xl': rules.append(f"{sel} {{ max-width: 36rem; }}"); continue
    if cls == 'max-h-[72vh]': rules.append(f"{sel} {{ max-height: 72vh; }}"); continue
    if cls == 'min-w-[550px]': rules.append(f"{sel} {{ min-width: 550px; }}"); continue
    if cls == 'min-w-[660px]': rules.append(f"{sel} {{ min-width: 660px; }}"); continue

    # Overflow
    if cls == 'overflow-hidden': rules.append(f"{sel} {{ overflow: hidden; }}"); continue
    if cls == 'overflow-visible': rules.append(f"{sel} {{ overflow: visible; }}"); continue
    if cls == 'overflow-x-auto': rules.append(f"{sel} {{ overflow-x: auto; }}"); continue
    if cls == 'overflow-y-auto': rules.append(f"{sel} {{ overflow-y: auto; }}"); continue

    # Margins & Paddings
    if cls == 'mx-auto': rules.append(f"{sel} {{ margin-left: auto; margin-right: auto; }}"); continue
    
    # Spacing mapping
    spacemap = {
        '0.5': '0.125rem', '1': '0.25rem', '1.5': '0.375rem', '2': '0.5rem', '2.5': '0.625rem',
        '3': '0.75rem', '3.5': '0.875rem', '4': '1rem', '5': '1.25rem', '6': '1.5rem'
    }
    
    m_p = re.match(r'^(p|px|py|pt|pb|pl|pr|m|mx|my|mt|mb)-([0-9\.]+)$', cls)
    if m_p:
        prop = m_p.group(1)
        val_str = m_p.group(2)
        val = spacemap.get(val_str, f"{float(val_str)*0.25}rem")
        if prop == 'p': rules.append(f"{sel} {{ padding: {val}; }}")
        elif prop == 'px': rules.append(f"{sel} {{ padding-left: {val}; padding-right: {val}; }}")
        elif prop == 'py': rules.append(f"{sel} {{ padding-top: {val}; padding-bottom: {val}; }}")
        elif prop == 'pt': rules.append(f"{sel} {{ padding-top: {val}; }}")
        elif prop == 'pb': rules.append(f"{sel} {{ padding-bottom: {val}; }}")
        elif prop == 'pl': rules.append(f"{sel} {{ padding-left: {val}; }}")
        elif prop == 'pr': rules.append(f"{sel} {{ padding-right: {val}; }}")
        elif prop == 'm': rules.append(f"{sel} {{ margin: {val}; }}")
        elif prop == 'mx': rules.append(f"{sel} {{ margin-left: {val}; margin-right: {val}; }}")
        elif prop == 'my': rules.append(f"{sel} {{ margin-top: {val}; margin-bottom: {val}; }}")
        elif prop == 'mt': rules.append(f"{sel} {{ margin-top: {val}; }}")
        elif prop == 'mb': rules.append(f"{sel} {{ margin-bottom: {val}; }}")
        continue

    # Gap & Space-x/y
    m_gap = re.match(r'^gap-([0-9\.]+)$', cls)
    if m_gap:
        val = spacemap.get(m_gap.group(1), f"{float(m_gap.group(1))*0.25}rem")
        rules.append(f"{sel} {{ gap: {val}; }}")
        continue

    m_space = re.match(r'^space-(x|y)-([0-9\.]+)$', cls)
    if m_space:
        xy = m_space.group(1)
        val = spacemap.get(m_space.group(2), f"{float(m_space.group(2))*0.25}rem")
        if xy == 'y':
            rules.append(f"{sel} > * + * {{ margin-top: {val}; }}")
        else:
            rules.append(f"{sel} > * + * {{ margin-left: {val}; }}")
        continue

    # Typography
    if cls == 'text-xs': rules.append(f"{sel} {{ font-size: 0.75rem; line-height: 1rem; }}"); continue
    if cls == 'text-sm': rules.append(f"{sel} {{ font-size: 0.875rem; line-height: 1.25rem; }}"); continue
    if cls == 'text-base': rules.append(f"{sel} {{ font-size: 1rem; line-height: 1.5rem; }}"); continue
    if cls == 'text-lg': rules.append(f"{sel} {{ font-size: 1.125rem; line-height: 1.75rem; }}"); continue
    if cls == 'text-xl': rules.append(f"{sel} {{ font-size: 1.25rem; line-height: 1.75rem; }}"); continue
    if cls == 'text-2xl': rules.append(f"{sel} {{ font-size: 1.5rem; line-height: 2rem; }}"); continue
    if cls == 'text-[10px]': rules.append(f"{sel} {{ font-size: 10px; line-height: 14px; }}"); continue
    if cls == 'text-[11px]': rules.append(f"{sel} {{ font-size: 11px; line-height: 15px; }}"); continue
    
    if cls == 'font-mono': rules.append(f"{sel} {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }}"); continue
    if cls == 'font-sans': rules.append(f"{sel} {{ font-family: 'Mukta', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}"); continue
    if cls == 'font-normal': rules.append(f"{sel} {{ font-weight: 400; }}"); continue
    if cls == 'font-medium': rules.append(f"{sel} {{ font-weight: 500; }}"); continue
    if cls == 'font-semibold': rules.append(f"{sel} {{ font-weight: 600; }}"); continue
    if cls == 'font-bold': rules.append(f"{sel} {{ font-weight: 700; }}"); continue
    if cls == 'font-extrabold': rules.append(f"{sel} {{ font-weight: 800; }}"); continue
    if cls == 'font-black': rules.append(f"{sel} {{ font-weight: 900; }}"); continue
    
    if cls == 'text-left': rules.append(f"{sel} {{ text-align: left; }}"); continue
    if cls == 'text-center': rules.append(f"{sel} {{ text-align: center; }}"); continue
    if cls == 'text-right': rules.append(f"{sel} {{ text-align: right; }}"); continue
    if cls == 'leading-relaxed': rules.append(f"{sel} {{ line-height: 1.625; }}"); continue
    if cls == 'tracking-tight': rules.append(f"{sel} {{ letter-spacing: -0.025em; }}"); continue
    if cls == 'tracking-wider': rules.append(f"{sel} {{ letter-spacing: 0.05em; }}"); continue
    if cls == 'uppercase': rules.append(f"{sel} {{ text-transform: uppercase; }}"); continue
    if cls == 'whitespace-nowrap': rules.append(f"{sel} {{ white-space: nowrap; }}"); continue
    if cls == 'list-disc': rules.append(f"{sel} {{ list-style-type: disc; }}"); continue

    # Rounded
    if cls == 'rounded': rules.append(f"{sel} {{ border-radius: 0.25rem; }}"); continue
    if cls == 'rounded-lg': rules.append(f"{sel} {{ border-radius: 0.5rem; }}"); continue
    if cls == 'rounded-xl': rules.append(f"{sel} {{ border-radius: 0.75rem; }}"); continue
    if cls == 'rounded-2xl': rules.append(f"{sel} {{ border-radius: 1rem; }}"); continue
    if cls == 'rounded-3xl': rules.append(f"{sel} {{ border-radius: 1.5rem; }}"); continue
    if cls == 'rounded-full': rules.append(f"{sel} {{ border-radius: 9999px; }}"); continue

    # Borders & Dividers
    if cls == 'border': rules.append(f"{sel} {{ border: 1px solid #e2e8f0; }}"); continue
    if cls == 'border-t': rules.append(f"{sel} {{ border-top: 1px solid #e2e8f0; }}"); continue
    if cls == 'border-b': rules.append(f"{sel} {{ border-bottom: 1px solid #e2e8f0; }}"); continue
    if cls == 'border-l-4': rules.append(f"{sel} {{ border-left-width: 4px; border-left-style: solid; }}"); continue
    if cls == 'border-collapse': rules.append(f"{sel} {{ border-collapse: collapse; }}"); continue
    if cls == 'divide-y': rules.append(f"{sel} > * + * {{ border-top-width: 1px; border-top-style: solid; }}"); continue
    if cls == 'divide-slate-100': rules.append(f"{sel} > * + * {{ border-color: #f1f5f9; }}"); continue
    if cls == 'divide-slate-200': rules.append(f"{sel} > * + * {{ border-color: #e2e8f0; }}"); continue

    # Border colors
    if cls.startswith('border-white/'):
        op = float(cls.split('/')[-1]) / 100.0
        rules.append(f"{sel} {{ border-color: rgba(255, 255, 255, {op}); }}")
        continue

    m_bc = re.match(r'^border-([a-z]+)-([0-9]+)(?:/([0-9]+))?$', cls)
    if m_bc:
        cname, shade, op = m_bc.group(1), m_bc.group(2), m_bc.group(3)
        if cname in palette and shade in palette[cname]:
            hex_val = palette[cname][shade]
            if op:
                r, g, b = hex_to_rgb(hex_val)
                alpha = float(op) / 100.0
                rules.append(f"{sel} {{ border-color: rgba({r}, {g}, {b}, {alpha}); }}")
            else:
                rules.append(f"{sel} {{ border-color: {hex_val}; }}")
            continue

    # Background colors
    if cls == 'bg-white': rules.append(f"{sel} {{ background-color: #ffffff; }}"); continue
    if cls.startswith('bg-white/'):
        op = float(cls.split('/')[-1]) / 100.0
        rules.append(f"{sel} {{ background-color: rgba(255, 255, 255, {op}); }}")
        continue

    m_bg = re.match(r'^bg-([a-z]+)-([0-9]+)(?:/([0-9]+))?$', cls)
    if m_bg:
        cname, shade, op = m_bg.group(1), m_bg.group(2), m_bg.group(3)
        if cname in palette and shade in palette[cname]:
            hex_val = palette[cname][shade]
            if op:
                r, g, b = hex_to_rgb(hex_val)
                alpha = float(op) / 100.0
                rules.append(f"{sel} {{ background-color: rgba({r}, {g}, {b}, {alpha}); }}")
            else:
                rules.append(f"{sel} {{ background-color: {hex_val}; }}")
            continue

    # Text colors
    if cls == 'text-white': rules.append(f"{sel} {{ color: #ffffff; }}"); continue
    m_tc = re.match(r'^text-([a-z]+)-([0-9]+)$', cls)
    if m_tc:
        cname, shade = m_tc.group(1), m_tc.group(2)
        if cname in palette and shade in palette[cname]:
            rules.append(f"{sel} {{ color: {palette[cname][shade]}; }}")
            continue

    # Gradients
    if cls == 'bg-gradient-to-r': rules.append(f"{sel} {{ background-image: linear-gradient(to right, var(--tw-gradient-stops, transparent)); }}"); continue
    if cls == 'bg-gradient-to-br': rules.append(f"{sel} {{ background-image: linear-gradient(to bottom right, var(--tw-gradient-stops, transparent)); }}"); continue

    m_from = re.match(r'^from-([a-z]+)-([0-9]+)$', cls)
    if m_from:
        c, s = m_from.group(1), m_from.group(2)
        if c in palette and s in palette[c]:
            rules.append(f"{sel} {{ --tw-gradient-from: {palette[c][s]}; --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to, rgba(255,255,255,0)); }}")
            continue

    m_via = re.match(r'^via-([a-z]+)-([0-9]+)$', cls)
    if m_via:
        c, s = m_via.group(1), m_via.group(2)
        if c in palette and s in palette[c]:
            rules.append(f"{sel} {{ --tw-gradient-stops: var(--tw-gradient-from), {palette[c][s]}, var(--tw-gradient-to, rgba(255,255,255,0)); }}")
            continue

    m_to = re.match(r'^to-([a-z]+)-([0-9]+)$', cls)
    if m_to:
        c, s = m_to.group(1), m_to.group(2)
        if c in palette and s in palette[c]:
            rules.append(f"{sel} {{ --tw-gradient-to: {palette[c][s]}; }}")
            continue

    # Shadows & Effects
    if cls == 'shadow-xs': rules.append(f"{sel} {{ box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05); }}"); continue
    if cls == 'shadow-sm': rules.append(f"{sel} {{ box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1); }}"); continue
    if cls == 'shadow-lg': rules.append(f"{sel} {{ box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1); }}"); continue
    if cls == 'shadow-xl': rules.append(f"{sel} {{ box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1); }}"); continue
    if cls == 'shadow-inner': rules.append(f"{sel} {{ box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.06); }}"); continue
    if cls == 'backdrop-blur-sm': rules.append(f"{sel} {{ backdrop-filter: blur(4px); -webkit-backdrop-filter: blur(4px); }}"); continue
    if cls == 'backdrop-blur-md': rules.append(f"{sel} {{ backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); }}"); continue
    if cls == 'opacity-75': rules.append(f"{sel} {{ opacity: 0.75; }}"); continue
    if cls == 'opacity-80': rules.append(f"{sel} {{ opacity: 0.8; }}"); continue

    if cls == 'cursor-pointer': rules.append(f"{sel} {{ cursor: pointer; }}"); continue
    if cls == 'transition': rules.append(f"{sel} {{ transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter; transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1); transition-duration: 150ms; }}"); continue
    if cls == 'transition-all': rules.append(f"{sel} {{ transition-property: all; transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1); transition-duration: 150ms; }}"); continue
    if cls == 'duration-200': rules.append(f"{sel} {{ transition-duration: 200ms; }}"); continue
    if cls == 'accent-blue-600': rules.append(f"{sel} {{ accent-color: #2563eb; }}"); continue

    unhandled.append(cls)

print('Handled base rules:', len(rules))
print('Handled sm rules:', len(rules_sm))
print('Handled md rules:', len(rules_md))
print('Handled lg rules:', len(rules_lg))
print('Unhandled classes:', len(unhandled), unhandled)

full_css = "/* === OFFLINE STANDALONE EMBEDDED CSS ENGINE === */\n"
full_css += "\n".join(rules)
full_css += "\n\n@media (min-width: 640px) {\n  " + "\n  ".join(rules_sm) + "\n}\n"
full_css += "\n@media (min-width: 768px) {\n  " + "\n  ".join(rules_md) + "\n}\n"
full_css += "\n@media (min-width: 1024px) {\n  " + "\n  ".join(rules_lg) + "\n}\n"

with open('scratch/generated_offline.css', 'w') as f:
    f.write(full_css)

print('Generated scratch/generated_offline.css successfully! Size:', len(full_css), 'bytes')
