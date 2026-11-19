#!/usr/bin/env python3
"""Generate unique brand-styled SVG hero/content images per page."""
import os

OUT = 'public/images'
os.makedirs(OUT, exist_ok=True)

# Per-page config: filename, title lines, subtitle, accent color, motif
PAGES = [
    ('home-hero', ['From Iranian', 'Orchards to', 'Global Markets'],
     'Premium Iranian Apples', '#E8B542', 'orchard'),
    ('red-apple', ['Red Apple', 'Export from Iran'],
     'Wholesale Iranian Red Apples', '#C0392B', 'apple'),
    ('golden-apple', ['Golden Apple', 'Export from Iran'],
     'Iranian Golden Apples', '#D4A017', 'apple'),
    ('green-apple', ['Green Apple', 'Supply from Iran'],
     'Bulk Iranian Green Apples', '#4A7C3F', 'apple'),
    ('varieties', ['Iranian Apple', 'Varieties'],
     'Red, Golden & Green Classes', '#2B5443', 'three'),
    ('quality', ['Apple Quality', '& Specifications'],
     'Grading for Export', '#2B5443', 'shield'),
    ('packaging', ['Iranian Apple', 'Packaging for Export'],
     'Cartons, Ventilation & Pallets', '#8A6D3B', 'box'),
    ('process', ['How to Import', 'Fresh Apples from Iran'],
     'The Export Process', '#2B5443', 'route'),
    ('destinations', ['Iranian Apple', 'Export Destinations'],
     'Regional & International Markets', '#1D372D', 'globe'),
    ('about', ['Iranian Apple Sourcing', '& Export'],
     'About SibExport', '#2B5443', 'leaf'),
    ('faq', ['Buyer', 'Questions', 'Answered'],
     'Frequently Asked Questions', '#2B5443', 'qa'),
    ('blog-guide', ['Iranian Apple Export:', 'A Practical Guide for', 'International Buyers'],
     'Export Insights', '#2B5443', 'doc'),
    ('quotation', ['Request a', 'Quotation'],
     'Wholesale Apple Inquiries', '#E8B542', 'form'),
    ('contact', ['Contact', 'SibExport'],
     'WhatsApp · Phone · Email', '#2B5443', 'chat'),
    ('blog', ['Blog & Export', 'Insights'],
     'Guides for Apple Importers', '#8A6D3B', 'pen'),
    ('privacy', ['Privacy', 'Policy'],
     'How We Handle Your Information', '#4B5057', 'lock'),
    ('notfound', ['Page', 'Not Found'],
     'Error 404', '#4B5057', 'compass'),
]


def motif(kind, color):
    c = color
    if kind == 'apple':
        return f'''<g transform="translate(820,140)" opacity="0.92">
      <ellipse cx="110" cy="210" rx="120" ry="112" fill="{c}"/>
      <ellipse cx="78" cy="172" rx="34" ry="44" fill="#ffffff" opacity="0.22"/>
      <path d="M110 100 C108 74 120 58 142 50" stroke="#6B4F2A" stroke-width="9" fill="none" stroke-linecap="round"/>
      <path d="M118 84 C142 66 172 66 190 84 C172 100 140 102 118 84 Z" fill="#4A7C3F"/>
    </g>'''
    if kind == 'three':
        return f'''<g transform="translate(790,150)">
      <ellipse cx="60" cy="200" rx="72" ry="68" fill="#C0392B"/>
      <ellipse cx="176" cy="200" rx="72" ry="68" fill="#D4A017"/>
      <ellipse cx="118" cy="112" rx="72" ry="68" fill="#4A7C3F"/>
      <path d="M118 48 C116 30 126 18 144 12" stroke="#6B4F2A" stroke-width="7" fill="none" stroke-linecap="round"/>
      <ellipse cx="40" cy="180" rx="18" ry="24" fill="#ffffff" opacity="0.2"/>
    </g>'''
    if kind == 'box':
        return f'''<g transform="translate(800,130)" opacity="0.92">
      <rect x="0" y="60" width="220" height="180" rx="10" fill="#B98A4E"/>
      <rect x="0" y="60" width="220" height="42" rx="10" fill="#A3743D"/>
      <rect x="86" y="102" width="48" height="80" rx="6" fill="#F3E4C8" opacity="0.85"/>
      <path d="M0 102 L-52 132 M220 102 L272 132" stroke="#A3743D" stroke-width="10" stroke-linecap="round"/>
      <ellipse cx="110" cy="24" rx="64" ry="26" fill="{c}" opacity="0.35"/>
      <ellipse cx="42" cy="120" rx="14" ry="18" fill="#ffffff" opacity="0.2"/>
    </g>'''
    if kind == 'shield':
        return f'''<g transform="translate(820,130)" opacity="0.92">
      <path d="M110 0 L210 40 V120 C210 186 166 226 110 244 C54 226 10 186 10 120 V40 Z" fill="{c}"/>
      <path d="M64 122 L98 156 L160 88" stroke="#E8B542" stroke-width="16" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </g>'''
    if kind == 'route':
        return f'''<g transform="translate(770,120)" opacity="0.92" fill="none">
      <circle cx="40" cy="200" r="26" fill="#E8B542"/>
      <circle cx="220" cy="40" r="26" fill="#ffffff" opacity="0.9"/>
      <path d="M40 200 C110 200 90 40 220 40" stroke="{c}" stroke-width="10" stroke-linecap="round" stroke-dasharray="2 26"/>
      <circle cx="130" cy="118" r="14" fill="{c}" opacity="0.7"/>
    </g>'''
    if kind == 'globe':
        return f'''<g transform="translate(800,120)" opacity="0.9" fill="none" stroke="{c}" stroke-width="8">
      <circle cx="120" cy="130" r="112" fill="#ffffff" opacity="0.08"/>
      <ellipse cx="120" cy="130" rx="52" ry="112"/>
      <path d="M8 130 H232 M28 66 H212 M28 194 H212"/>
      <circle cx="182" cy="86" r="16" fill="#E8B542" stroke="none"/>
    </g>'''
    if kind == 'orchard':
        return f'''<g transform="translate(760,110)" opacity="0.9">
      <circle cx="150" cy="120" r="86" fill="{c}" opacity="0.28"/>
      <ellipse cx="90" cy="220" rx="64" ry="60" fill="#C0392B"/>
      <ellipse cx="216" cy="220" rx="64" ry="60" fill="#D4A017"/>
      <path d="M90 164 C88 140 100 124 122 118" stroke="#6B4F2A" stroke-width="8" fill="none" stroke-linecap="round"/>
      <path d="M216 164 C214 140 226 124 248 118" stroke="#6B4F2A" stroke-width="8" fill="none" stroke-linecap="round"/>
    </g>'''
    if kind == 'leaf':
        return f'''<g transform="translate(810,130)" opacity="0.92">
      <path d="M110 240 C30 190 30 90 110 20 C190 90 190 190 110 240 Z" fill="#4A7C3F"/>
      <path d="M110 240 V40" stroke="#2B5443" stroke-width="8" stroke-linecap="round"/>
      <path d="M110 200 C88 188 74 170 68 148 M110 160 C132 148 146 130 152 108 M110 120 C88 108 76 92 72 72" stroke="#2B5443" stroke-width="6" fill="none" stroke-linecap="round"/>
    </g>'''
    if kind == 'qa':
        return f'''<g transform="translate(820,120)" opacity="0.92">
      <circle cx="110" cy="120" r="106" fill="#ffffff" opacity="0.1"/>
      <text x="110" y="168" font-family="Arial, sans-serif" font-size="140" font-weight="bold" fill="{c}" text-anchor="middle">?</text>
      <circle cx="196" cy="196" r="34" fill="#E8B542"/>
      <path d="M184 196 L194 206 L212 182" stroke="#1D372D" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </g>'''
    if kind == 'doc':
        return f'''<g transform="translate(820,110)" opacity="0.92">
      <rect x="20" y="0" width="180" height="240" rx="14" fill="#ffffff" opacity="0.92"/>
      <rect x="44" y="36" width="132" height="12" rx="6" fill="{c}"/>
      <rect x="44" y="70" width="132" height="8" rx="4" fill="#9AA39D"/>
      <rect x="44" y="92" width="132" height="8" rx="4" fill="#9AA39D"/>
      <rect x="44" y="114" width="96" height="8" rx="4" fill="#9AA39D"/>
      <rect x="44" y="156" width="60" height="52" rx="8" fill="{c}" opacity="0.25"/>
      <circle cx="182" cy="210" r="36" fill="#E8B542"/>
      <path d="M166 210 L178 222 L200 194" stroke="#1D372D" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </g>'''
    if kind == 'form':
        return f'''<g transform="translate(810,110)" opacity="0.92">
      <rect x="0" y="0" width="220" height="260" rx="16" fill="#ffffff" opacity="0.94"/>
      <rect x="26" y="34" width="70" height="12" rx="6" fill="{c}"/>
      <rect x="26" y="60" width="168" height="26" rx="8" fill="#E8ECE9"/>
      <rect x="26" y="106" width="70" height="12" rx="6" fill="{c}"/>
      <rect x="26" y="132" width="168" height="26" rx="8" fill="#E8ECE9"/>
      <rect x="26" y="196" width="168" height="40" rx="10" fill="{c}"/>
      <path d="M96 216 L108 228 L128 204" stroke="#1D372D" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </g>'''
    if kind == 'chat':
        return f'''<g transform="translate(810,130)" opacity="0.92">
      <path d="M0 40 C0 18 18 0 40 0 H180 C202 0 220 18 220 40 V130 C220 152 202 170 180 170 H80 L20 220 V170 C8 166 0 152 0 134 Z" fill="#25d366"/>
      <path d="M56 62 C56 110 96 148 144 148 L162 122 L128 100 L112 114 C92 104 78 88 72 68 L88 78 L108 46 Z" fill="#ffffff"/>
      <circle cx="230" cy="190" r="40" fill="{c}"/>
      <path d="M214 190 L226 202 L248 176" stroke="#1D372D" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </g>'''
    if kind == 'pen':
        return f'''<g transform="translate(820,120)" opacity="0.92">
      <rect x="0" y="0" width="200" height="250" rx="14" fill="#ffffff" opacity="0.9"/>
      <rect x="28" y="34" width="144" height="10" rx="5" fill="#9AA39D"/>
      <rect x="28" y="58" width="144" height="10" rx="5" fill="#9AA39D"/>
      <rect x="28" y="82" width="100" height="10" rx="5" fill="#9AA39D"/>
      <path d="M150 160 L220 90 L246 116 L176 186 L142 196 Z" fill="{c}"/>
      <path d="M150 160 L176 186" stroke="#ffffff" stroke-width="5"/>
    </g>'''
    if kind == 'lock':
        return f'''<g transform="translate(830,130)" opacity="0.92">
      <rect x="20" y="100" width="180" height="150" rx="16" fill="{c}"/>
      <path d="M60 100 V66 C60 34 86 10 110 10 C134 10 160 34 160 66 V100" stroke="{c}" stroke-width="18" fill="none"/>
      <circle cx="110" cy="160" r="22" fill="#E8B542"/>
      <rect x="102" y="170" width="16" height="36" rx="8" fill="#E8B542"/>
    </g>'''
    if kind == 'compass':
        return f'''<g transform="translate(810,110)" opacity="0.9" fill="none" stroke="{c}" stroke-width="9">
      <circle cx="120" cy="130" r="110"/>
      <path d="M170 80 L136 136 L70 180 L104 124 Z" fill="#E8B542" stroke="none"/>
    </g>'''
    return ''


for fname, lines, subtitle, accent, mkind in PAGES:
    tspans = ''.join(
        f'<tspan x="80" dy="{0 if i == 0 else 1.15}em">{l}</tspan>'
        for i, l in enumerate(lines)
    )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630" role="img" aria-label="{' '.join(lines)} — {subtitle}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#1D372D"/>
      <stop offset="0.55" stop-color="#2B5443"/>
      <stop offset="1" stop-color="#0E1F18"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="630" fill="url(#bg)"/>
  <circle cx="1060" cy="70" r="220" fill="#E8B542" opacity="0.07"/>
  <circle cx="90" cy="580" r="180" fill="#4A7C3F" opacity="0.12"/>
  {motif(mkind, accent)}
  <text x="80" y="200" font-family="Arial, Helvetica, sans-serif" font-size="{52 if len(lines) < 3 else 44}" font-weight="bold" fill="#ffffff">
    {tspans}
  </text>
  <text x="80" y="{212 + len(lines) * 64}" font-family="Arial, Helvetica, sans-serif" font-size="26" fill="#E8B542">{subtitle}</text>
  <text x="80" y="560" font-family="Arial, Helvetica, sans-serif" font-size="24" fill="#CFE0D6">SibExport · sibexport.ir</text>
  <rect x="80" y="470" width="56" height="6" rx="3" fill="#E8B542"/>
</svg>
'''
    with open(f'{OUT}/{fname}.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f'{OUT}/{fname}.svg')

# Inline content images (wide banner style, lighter background)
BANNER = [
    ('banner-origin', 'Apple orchards of West Azerbaijan', 'orchard'),
    ('banner-specs', 'Written specifications govern every order', 'doc'),
    ('banner-packing', 'Export cartons protect fruit in transit', 'box'),
    ('banner-inspect', 'Three inspection points in every order', 'shield'),
    ('banner-market', 'Regional markets served from Urmia', 'globe'),
    ('banner-season', 'Harvest and storage through the seasons', 'three'),
    ('banner-rfq', 'Your inquiry prepared for WhatsApp', 'chat'),
    ('banner-docs', 'Export documentation coordination', 'route'),
]
for fname, label, mkind in BANNER:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="480" viewBox="0 0 1200 480" role="img" aria-label="{label}">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#24463A"/>
      <stop offset="1" stop-color="#0E1F18"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="480" fill="url(#g)"/>
  <circle cx="1080" cy="60" r="180" fill="#E8B542" opacity="0.08"/>
  <circle cx="60" cy="440" r="140" fill="#4A7C3F" opacity="0.12"/>
  <g transform="scale(0.72) translate(880,60)">{motif(mkind, '#E8B542').replace('translate(8','translate(0').replace('translate(7','translate(0').replace('translate(810','translate(0').replace('translate(820','translate(0').replace('translate(830','translate(0')}</g>
  <text x="70" y="250" font-family="Arial, Helvetica, sans-serif" font-size="40" font-weight="bold" fill="#ffffff">{label}</text>
  <text x="70" y="300" font-family="Arial, Helvetica, sans-serif" font-size="22" fill="#CFE0D6">SibExport · sibexport.ir</text>
  <rect x="70" y="330" width="48" height="5" rx="2.5" fill="#E8B542"/>
</svg>
'''
    with open(f'{OUT}/{fname}.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f'{OUT}/{fname}.svg')
