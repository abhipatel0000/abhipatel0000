import os
import xml.etree.ElementTree as ET

ASSETS_DIR = r"c:\Users\Abhi patel\OneDrive\Desktop\Special Repo\abhipatel0000\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

def write_svg(filename, content):
    path = os.path.join(ASSETS_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated {filename}")

def escape_xml(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# --- 0. Hero Banners (Dark & Light) ---
def create_hero_banner(theme="dark"):
    is_dark = theme == "dark"
    bg_grad = """
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16" />
      <stop offset="45%" stop-color="#0d1117" />
      <stop offset="85%" stop-color="#14132b" />
      <stop offset="100%" stop-color="#090d16" />
    </linearGradient>
    """ if is_dark else """
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="50%" stop-color="#f8fafc" />
      <stop offset="100%" stop-color="#f1f5f9" />
    </linearGradient>
    """
    
    accent_grad = """
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f2fe" />
      <stop offset="35%" stop-color="#6366f1" />
      <stop offset="70%" stop-color="#9d4edd" />
      <stop offset="100%" stop-color="#f72585" />
    </linearGradient>
    """ if is_dark else """
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="35%" stop-color="#4f46e5" />
      <stop offset="70%" stop-color="#7c3aed" />
      <stop offset="100%" stop-color="#db2777" />
    </linearGradient>
    """

    divider_grad = """
    <linearGradient id="dividerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f2fe" stop-opacity="0" />
      <stop offset="20%" stop-color="#00f2fe" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#6366f1" stop-opacity="1" />
      <stop offset="80%" stop-color="#f72585" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#f72585" stop-opacity="0" />
    </linearGradient>
    """ if is_dark else """
    <linearGradient id="dividerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0" />
      <stop offset="20%" stop-color="#0284c7" stop-opacity="0.6" />
      <stop offset="50%" stop-color="#4f46e5" stop-opacity="0.8" />
      <stop offset="80%" stop-color="#db2777" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#db2777" stop-opacity="0" />
    </linearGradient>
    """

    status_bg = """
    <linearGradient id="statusBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f2fe" stop-opacity="0.12" />
      <stop offset="100%" stop-color="#00ff88" stop-opacity="0.08" />
    </linearGradient>
    """ if is_dark else """
    <linearGradient id="statusBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#059669" stop-opacity="0.05" />
    </linearGradient>
    """

    grid_stroke = "#6366f1" if is_dark else "#4f46e5"
    grid_opacity = "0.07" if is_dark else "0.05"
    dot_color = "#00f2fe" if is_dark else "#4f46e5"
    
    title_color = "#ffffff" if is_dark else "#0f172a"
    sub_color = "#94a3b8" if is_dark else "#475569"
    border_color = 'stroke="url(#accentGrad)" stroke-width="1.2" stroke-opacity="0.4"' if is_dark else 'stroke="#cbd5e1" stroke-width="1.2"'
    corner_c1 = "#00f2fe" if is_dark else "#0284c7"
    corner_c2 = "#f72585" if is_dark else "#db2777"
    corner_c3 = "#9d4edd" if is_dark else "#7c3aed"
    
    pulse_dot_color = "#00ff88" if is_dark else "#059669"
    status_text_color = "#00ff88" if is_dark else "#059669"
    
    type_col_1 = "#00f2fe" if is_dark else "#0284c7"
    type_col_2 = "#c77dff" if is_dark else "#7c3aed"
    type_col_3 = "#00ff88" if is_dark else "#059669"
    type_col_4 = "#f72585" if is_dark else "#db2777"

    chip_bg = '#ffffff" fill-opacity="0.04' if is_dark else '#ffffff'
    chip_text_col = "#c9d1d9" if is_dark else "#334155"

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 340" fill="none">
  <defs>
    {bg_grad}
    {accent_grad}
    {divider_grad}
    {status_bg}
    <filter id="meshGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="32" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <filter id="softGlow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <pattern id="techGrid" width="36" height="36" patternUnits="userSpaceOnUse">
      <path d="M 36 0 L 0 0 0 36" fill="none" stroke="{grid_stroke}" stroke-width="0.75" stroke-opacity="{grid_opacity}" />
      <circle cx="36" cy="0" r="0.8" fill="{dot_color}" fill-opacity="0.2" />
    </pattern>
  </defs>

  <style>
    @keyframes pulseOrb1 {{
      0%, 100% {{ transform: translate(0, 0) scale(1); opacity: 0.18; }}
      50% {{ transform: translate(30px, -20px) scale(1.1); opacity: 0.28; }}
    }}
    @keyframes pulseOrb2 {{
      0%, 100% {{ transform: translate(0, 0) scale(1); opacity: 0.16; }}
      50% {{ transform: translate(-30px, 20px) scale(1.08); opacity: 0.24; }}
    }}
    @keyframes livePulse {{
      0%, 100% {{ opacity: 1; transform: scale(1); }}
      50% {{ opacity: 0.35; transform: scale(0.85); }}
    }}
    @keyframes cycle1 {{
      0%, 20% {{ opacity: 1; transform: translateY(0); }}
      24%, 96% {{ opacity: 0; transform: translateY(6px); }}
      100% {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes cycle2 {{
      0%, 24% {{ opacity: 0; transform: translateY(6px); }}
      28%, 48% {{ opacity: 1; transform: translateY(0); }}
      52%, 100% {{ opacity: 0; transform: translateY(6px); }}
    }}
    @keyframes cycle3 {{
      0%, 52% {{ opacity: 0; transform: translateY(6px); }}
      56%, 76% {{ opacity: 1; transform: translateY(0); }}
      80%, 100% {{ opacity: 0; transform: translateY(6px); }}
    }}
    @keyframes cycle4 {{
      0%, 80% {{ opacity: 0; transform: translateY(6px); }}
      84%, 96% {{ opacity: 1; transform: translateY(0); }}
      100% {{ opacity: 0; transform: translateY(6px); }}
    }}

    .orb-1 {{ animation: pulseOrb1 10s ease-in-out infinite; }}
    .orb-2 {{ animation: pulseOrb2 12s ease-in-out infinite; }}
    .status-dot {{ animation: livePulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite; transform-origin: 430px 44px; }}

    .carousel-line-1 {{ animation: cycle1 16s ease-in-out infinite; }}
    .carousel-line-2 {{ animation: cycle2 16s ease-in-out infinite; }}
    .carousel-line-3 {{ animation: cycle3 16s ease-in-out infinite; }}
    .carousel-line-4 {{ animation: cycle4 16s ease-in-out infinite; }}
  </style>

  <!-- Card Background -->
  <rect width="1200" height="340" rx="20" fill="url(#bgGrad)" />
  <rect width="1200" height="340" rx="20" fill="url(#techGrid)" />

  <!-- Glowing Mesh Orbs -->
  <g class="orb-1">
    <circle cx="180" cy="90" r="130" fill="{corner_c1}" filter="url(#meshGlow)" />
    <circle cx="1060" cy="240" r="150" fill="{corner_c3}" filter="url(#meshGlow)" />
  </g>
  <g class="orb-2">
    <circle cx="600" cy="50" r="120" fill="#6366f1" filter="url(#meshGlow)" />
    <circle cx="980" cy="80" r="100" fill="{corner_c2}" filter="url(#meshGlow)" />
  </g>

  <!-- Outer Border -->
  <rect x="1" y="1" width="1198" height="338" rx="19" fill="none" {border_color} />

  <!-- Corner Brackets -->
  <path d="M 24 44 L 24 24 L 44 24" fill="none" stroke="{corner_c1}" stroke-width="2" stroke-linecap="round" opacity="0.8" />
  <path d="M 1176 44 L 1176 24 L 1156 24" fill="none" stroke="{corner_c2}" stroke-width="2" stroke-linecap="round" opacity="0.8" />
  <path d="M 24 296 L 24 316 L 44 316" fill="none" stroke="{corner_c1}" stroke-width="2" stroke-linecap="round" opacity="0.8" />
  <path d="M 1176 296 L 1176 316 L 1156 316" fill="none" stroke="{corner_c3}" stroke-width="2" stroke-linecap="round" opacity="0.8" />

  <!-- Top Live Status Pill: OPEN TO PROJECTS & COLLABS -->
  <g>
    <rect x="420" y="28" width="360" height="32" rx="16" fill="url(#statusBg)" stroke="{corner_c1}" stroke-width="1" stroke-opacity="0.4" />
    <circle cx="442" cy="44" r="4" fill="{pulse_dot_color}" class="status-dot" />
    <text x="456" y="49" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" fill="{status_text_color}" letter-spacing="0.8">OPEN TO PROJECTS &amp; COLLABS</text>
  </g>

  <!-- Hero Main Heading -->
  <text x="600" y="125" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif" font-size="48" font-weight="800" fill="{title_color}" letter-spacing="-0.8">
    Hi, I'm <tspan fill="url(#accentGrad)" filter="url(#softGlow)">Abhi Patel</tspan>
  </text>

  <!-- Subtitle -->
  <text x="600" y="165" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="19" font-weight="500" fill="{sub_color}" letter-spacing="0.2">
    Full-Stack Engineer &amp; AI Solutions Architect
  </text>

  <!-- Glowing Line -->
  <line x1="380" y1="190" x2="820" y2="190" stroke="url(#dividerGrad)" stroke-width="1.8" stroke-linecap="round" />

  <!-- Animated Typing / Role Carousel -->
  <g transform="translate(600, 230)" text-anchor="middle">
    <!-- Item 1 -->
    <g class="carousel-line-1">
      <text font-family="'JetBrains Mono', 'Fira Code', 'Courier New', monospace" font-size="17" font-weight="600" fill="{type_col_1}">
        <tspan fill="#6366f1">&gt;</tspan> Next.js · React · Node.js · FastAPI · Spring Boot
      </text>
    </g>

    <!-- Item 2 -->
    <g class="carousel-line-2">
      <text font-family="'JetBrains Mono', 'Fira Code', 'Courier New', monospace" font-size="17" font-weight="600" fill="{type_col_2}">
        <tspan fill="#f72585">&gt;</tspan> Building AI/ML Systems, LLM Agents &amp; Intelligent Workflows
      </text>
    </g>

    <!-- Item 3 -->
    <g class="carousel-line-3">
      <text font-family="'JetBrains Mono', 'Fira Code', 'Courier New', monospace" font-size="17" font-weight="600" fill="{type_col_3}">
        <tspan fill="{type_col_1}">&gt;</tspan> Architecting High-Performance APIs, Microservices &amp; Databases
      </text>
    </g>

    <!-- Item 4 -->
    <g class="carousel-line-4">
      <text font-family="'JetBrains Mono', 'Fira Code', 'Courier New', monospace" font-size="17" font-weight="600" fill="{type_col_4}">
        <tspan fill="#6366f1">&gt;</tspan> Crafting Premium UI/UX &amp; Cinematic Visual Experiences
      </text>
    </g>
  </g>

  <!-- Bottom Badges: Location, University, Tech Lead @ ISAC -->
  <g transform="translate(255, 274)">
    <!-- Badge 1: Location -->
    <rect x="0" y="0" width="190" height="34" rx="17" fill="{chip_bg}" stroke="{corner_c1}" stroke-width="1" stroke-opacity="0.3" />
    <path d="M 22 17 C 22 13 25 10 29 10 C 33 10 36 13 36 17 C 36 21 29 26 29 26 C 29 26 22 21 22 17 Z M 27 17 A 2 2 0 1 0 31 17 A 2 2 0 1 0 27 17 Z" fill="{corner_c1}" />
    <text x="108" y="21" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" fill="{chip_text_col}">Ahmedabad, India</text>

    <!-- Badge 2: University -->
    <rect x="210" y="0" width="240" height="34" rx="17" fill="{chip_bg}" stroke="#6366f1" stroke-width="1" stroke-opacity="0.3" />
    <path d="M 230 14 L 241 8 L 252 14 L 241 20 Z M 234 18.5 V 23.5 C 234 23.5 237 26 241 26 C 245 26 248 23.5 248 23.5 V 18.5" fill="none" stroke="#6366f1" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" />
    <text x="340" y="21" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" fill="{chip_text_col}">Indus University '27</text>

    <!-- Badge 3: Tech Lead @ ISAC -->
    <rect x="470" y="0" width="220" height="34" rx="17" fill="{chip_bg}" stroke="{corner_c3}" stroke-width="1" stroke-opacity="0.4" />
    <path d="M 492 11 L 486 18 L 493 18 L 488 25 L 497 16 L 491 16 Z" fill="{corner_c3}" />
    <text x="590" y="21" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" fill="{chip_text_col}">Tech Lead @ ISAC</text>
  </g>
</svg>"""

write_svg("banner-dark.svg", create_hero_banner("dark"))
write_svg("banner.svg", create_hero_banner("dark"))
write_svg("banner-light.svg", create_hero_banner("light"))


# --- 1. Quick Link Pill Buttons ---
buttons = [
    {
        "name": "github",
        "label": "GitHub",
        "accent": "#6366f1",
        "icon": '<path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" fill="currentColor"/>'
    },
    {
        "name": "email",
        "label": "Email",
        "accent": "#ea4335",
        "icon": '<path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" fill="currentColor"/>'
    },
    {
        "name": "instagram",
        "label": "Instagram",
        "accent": "#e4405f",
        "icon": '<path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z" fill="currentColor"/>'
    },
    {
        "name": "portfolio",
        "label": "Portfolio",
        "accent": "#00f2fe",
        "icon": '<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z" fill="currentColor"/>'
    },
    {
        "name": "linkedin",
        "label": "LinkedIn",
        "accent": "#0077b5",
        "icon": '<path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 8.76a1.68 1.68 0 1 0 0-3.36 1.68 1.68 0 0 0 0 3.36M7.86 18.5v-8.37H5.07v8.37h2.79z" fill="currentColor"/>'
    }
]

for btn in buttons:
    dark_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="148" height="38" viewBox="0 0 148 38" fill="none">
  <rect x="0.5" y="0.5" width="147" height="37" rx="18.5" fill="#0d1117" stroke="{btn['accent']}" stroke-width="1.2" stroke-opacity="0.6"/>
  <rect x="0.5" y="0.5" width="147" height="37" rx="18.5" fill="{btn['accent']}" fill-opacity="0.08"/>
  <g transform="translate(18, 10) scale(0.75)" color="{btn['accent']}">
    {btn['icon']}
  </g>
  <text x="78" y="24" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" fill="#f0f6fc">{btn['label']}</text>
  <path d="M125 15 L129 19 L125 23" fill="none" stroke="{btn['accent']}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""
    write_svg(f"btn-{btn['name']}-dark.svg", dark_svg)

    light_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="148" height="38" viewBox="0 0 148 38" fill="none">
  <rect x="0.5" y="0.5" width="147" height="37" rx="18.5" fill="#ffffff" stroke="{btn['accent']}" stroke-width="1.2" stroke-opacity="0.5"/>
  <rect x="0.5" y="0.5" width="147" height="37" rx="18.5" fill="{btn['accent']}" fill-opacity="0.05"/>
  <g transform="translate(18, 10) scale(0.75)" color="{btn['accent']}">
    {btn['icon']}
  </g>
  <text x="78" y="24" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" fill="#0f172a">{btn['label']}</text>
  <path d="M125 15 L129 19 L125 23" fill="none" stroke="{btn['accent']}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""
    write_svg(f"btn-{btn['name']}-light.svg", light_svg)


# --- 2. Section Headers ---
headers = [
    {"name": "projects", "title": "FEATURED PROJECTS", "accent": "#00f2fe", "sub": "Production Architectures &amp; Systems"},
    {"name": "tech", "title": "TECH ARSENAL", "accent": "#6366f1", "sub": "Languages, Frameworks &amp; Infrastructure"},
    {"name": "stats", "title": "ENGINEERING METRICS", "accent": "#9d4edd", "sub": "GitHub Activity &amp; Code Distribution"},
    {"name": "snake", "title": "CONTRIBUTION GRAPH", "accent": "#00ff88", "sub": "Daily Commit Trail &amp; Activity"},
    {"name": "experience", "title": "LEADERSHIP &amp; EDUCATION", "accent": "#00f2fe", "sub": "Milestones &amp; Institutional Roles"},
    {"name": "creative", "title": "CREATIVE CORNER", "accent": "#f72585", "sub": "Video Production &amp; Visual Media"},
    {"name": "contact", "title": "GET IN TOUCH", "accent": "#6366f1", "sub": "Collaborations, Open Roles &amp; Inquiries"}
]

for h in headers:
    dark_head = f"""<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 70" fill="none">
  <defs>
    <linearGradient id="lineGradDark_{h['name']}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{h['accent']}" stop-opacity="0.8"/>
      <stop offset="60%" stop-color="{h['accent']}" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <g transform="translate(10, 16)">
    <rect x="0" y="0" width="36" height="36" rx="8" fill="#161b22" stroke="{h['accent']}" stroke-width="1.2" stroke-opacity="0.5"/>
    <circle cx="18" cy="18" r="4" fill="{h['accent']}"/>
    <text x="50" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="800" fill="#ffffff" letter-spacing="1">{h['title']}</text>
    <text x="350" y="23" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="500" fill="#8b949e">/ {h['sub']}</text>
    <line x1="50" y1="36" x2="1180" y2="36" stroke="url(#lineGradDark_{h['name']})" stroke-width="1.5" stroke-linecap="round"/>
  </g>
</svg>"""
    write_svg(f"header-{h['name']}-dark.svg", dark_head)

    light_head = f"""<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 70" fill="none">
  <defs>
    <linearGradient id="lineGradLight_{h['name']}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{h['accent']}" stop-opacity="0.8"/>
      <stop offset="60%" stop-color="{h['accent']}" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <g transform="translate(10, 16)">
    <rect x="0" y="0" width="36" height="36" rx="8" fill="#f1f5f9" stroke="{h['accent']}" stroke-width="1.2" stroke-opacity="0.5"/>
    <circle cx="18" cy="18" r="4" fill="{h['accent']}"/>
    <text x="50" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="800" fill="#0f172a" letter-spacing="1">{h['title']}</text>
    <text x="350" y="23" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="500" fill="#64748b">/ {h['sub']}</text>
    <line x1="50" y1="36" x2="1180" y2="36" stroke="url(#lineGradLight_{h['name']})" stroke-width="1.5" stroke-linecap="round"/>
  </g>
</svg>"""
    write_svg(f"header-{h['name']}-light.svg", light_head)


# --- 3. Currently Status Card ---
currently_dark = """<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 130" fill="none">
  <defs>
    <linearGradient id="curBgDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#161b22" />
      <stop offset="100%" stop-color="#0d1117" />
    </linearGradient>
  </defs>
  <style>
    @keyframes curPulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.3; transform: scale(0.8); }
    }
    .p-dot { animation: curPulse 2s infinite ease-in-out; transform-origin: center; }
  </style>
  <rect width="1200" height="130" rx="16" fill="url(#curBgDark)" stroke="#30363d" stroke-width="1.2"/>
  
  <!-- Column 1: Building -->
  <g transform="translate(30, 25)">
    <rect x="0" y="0" width="265" height="80" rx="12" fill="#0d1117" stroke="#00f2fe" stroke-width="1" stroke-opacity="0.3"/>
    <circle cx="20" cy="25" r="4" fill="#00f2fe" class="p-dot"/>
    <text x="32" y="29" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" fill="#00f2fe" letter-spacing="0.5">CURRENTLY BUILDING</text>
    <text x="20" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" fill="#f0f6fc">AURA &amp; StageSync</text>
    <text x="20" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="400" fill="#8b949e">AI OS Agent &amp; Event Platform</text>
  </g>

  <!-- Column 2: Learning -->
  <g transform="translate(320, 25)">
    <rect x="0" y="0" width="265" height="80" rx="12" fill="#0d1117" stroke="#6366f1" stroke-width="1" stroke-opacity="0.3"/>
    <circle cx="20" cy="25" r="4" fill="#6366f1" class="p-dot"/>
    <text x="32" y="29" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" fill="#6366f1" letter-spacing="0.5">DEEP DIVING INTO</text>
    <text x="20" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" fill="#f0f6fc">Agentic LLM Workflows</text>
    <text x="20" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="400" fill="#8b949e">Autonomous Multi-Agent Systems</text>
  </g>

  <!-- Column 3: Exploring -->
  <g transform="translate(610, 25)">
    <rect x="0" y="0" width="265" height="80" rx="12" fill="#0d1117" stroke="#9d4edd" stroke-width="1" stroke-opacity="0.3"/>
    <circle cx="20" cy="25" r="4" fill="#9d4edd" class="p-dot"/>
    <text x="32" y="29" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" fill="#9d4edd" letter-spacing="0.5">EXPLORING</text>
    <text x="20" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" fill="#f0f6fc">High-Concurrency Backends</text>
    <text x="20" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="400" fill="#8b949e">FastAPI, Spring Boot &amp; WebSockets</text>
  </g>

  <!-- Column 4: Open To -->
  <g transform="translate(900, 25)">
    <rect x="0" y="0" width="270" height="80" rx="12" fill="#0d1117" stroke="#00ff88" stroke-width="1" stroke-opacity="0.3"/>
    <circle cx="20" cy="25" r="4" fill="#00ff88" class="p-dot"/>
    <text x="32" y="29" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" fill="#00ff88" letter-spacing="0.5">OPEN TO</text>
    <text x="20" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" fill="#f0f6fc">High-Impact Collaborations</text>
    <text x="20" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="400" fill="#8b949e">Full-Stack &amp; AI Engineering</text>
  </g>
</svg>"""
write_svg("currently-dark.svg", currently_dark)

currently_light = """<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 130" fill="none">
  <defs>
    <linearGradient id="curBgLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc" />
      <stop offset="100%" stop-color="#ffffff" />
    </linearGradient>
  </defs>
  <style>
    @keyframes curPulseL {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.3; transform: scale(0.8); }
    }
    .p-dot-l { animation: curPulseL 2s infinite ease-in-out; transform-origin: center; }
  </style>
  <rect width="1200" height="130" rx="16" fill="url(#curBgLight)" stroke="#e2e8f0" stroke-width="1.2"/>
  
  <!-- Column 1: Building -->
  <g transform="translate(30, 25)">
    <rect x="0" y="0" width="265" height="80" rx="12" fill="#ffffff" stroke="#0284c7" stroke-width="1" stroke-opacity="0.3"/>
    <circle cx="20" cy="25" r="4" fill="#0284c7" class="p-dot-l"/>
    <text x="32" y="29" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" fill="#0284c7" letter-spacing="0.5">CURRENTLY BUILDING</text>
    <text x="20" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" fill="#0f172a">AURA &amp; StageSync</text>
    <text x="20" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="400" fill="#64748b">AI OS Agent &amp; Event Platform</text>
  </g>

  <!-- Column 2: Learning -->
  <g transform="translate(320, 25)">
    <rect x="0" y="0" width="265" height="80" rx="12" fill="#ffffff" stroke="#4f46e5" stroke-width="1" stroke-opacity="0.3"/>
    <circle cx="20" cy="25" r="4" fill="#4f46e5" class="p-dot-l"/>
    <text x="32" y="29" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" fill="#4f46e5" letter-spacing="0.5">DEEP DIVING INTO</text>
    <text x="20" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" fill="#0f172a">Agentic LLM Workflows</text>
    <text x="20" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="400" fill="#64748b">Autonomous Multi-Agent Systems</text>
  </g>

  <!-- Column 3: Exploring -->
  <g transform="translate(610, 25)">
    <rect x="0" y="0" width="265" height="80" rx="12" fill="#ffffff" stroke="#7c3aed" stroke-width="1" stroke-opacity="0.3"/>
    <circle cx="20" cy="25" r="4" fill="#7c3aed" class="p-dot-l"/>
    <text x="32" y="29" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" fill="#7c3aed" letter-spacing="0.5">EXPLORING</text>
    <text x="20" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" fill="#0f172a">High-Concurrency Backends</text>
    <text x="20" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="400" fill="#64748b">FastAPI, Spring Boot &amp; WebSockets</text>
  </g>

  <!-- Column 4: Open To -->
  <g transform="translate(900, 25)">
    <rect x="0" y="0" width="270" height="80" rx="12" fill="#ffffff" stroke="#059669" stroke-width="1" stroke-opacity="0.3"/>
    <circle cx="20" cy="25" r="4" fill="#059669" class="p-dot-l"/>
    <text x="32" y="29" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="700" fill="#059669" letter-spacing="0.5">OPEN TO</text>
    <text x="20" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="600" fill="#0f172a">High-Impact Collaborations</text>
    <text x="20" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="400" fill="#64748b">Full-Stack &amp; AI Engineering</text>
  </g>
</svg>"""
write_svg("currently-light.svg", currently_light)


# --- 4. Featured Project Cards (4 Cards) ---
projects = [
    {
        "id": "aura",
        "title": "AURA",
        "badge": "AI OS ASSISTANT",
        "desc": "Intelligent desktop companion for automated workflows, context reasoning, and voice-controlled system actions.",
        "tags": ["Python", "FastAPI", "PyTorch", "LLM Agents", "Electron"],
        "accent": "#00f2fe"
    },
    {
        "id": "stagesync",
        "title": "StageSync",
        "badge": "EVENT MEDIA DELIVERY",
        "desc": "High-throughput asset distribution platform with instant client uploads, lossless compression &amp; live sync.",
        "tags": ["Next.js", "Node.js", "WebSockets", "Docker", "S3"],
        "accent": "#6366f1"
    },
    {
        "id": "bestview",
        "title": "BestView Clone",
        "badge": "HOSPITALITY PLATFORM",
        "desc": "Full-stack resort &amp; luxury stay booking platform featuring real-time room availability, interactive maps &amp; payments.",
        "tags": ["React", "Tailwind CSS", "Spring Boot", "PostgreSQL"],
        "accent": "#9d4edd"
    },
    {
        "id": "tradingbot",
        "title": "AI Trading Bot",
        "badge": "ALGORITHMIC TRADING",
        "desc": "Quantitative algorithmic market execution engine with ML predictive signals, risk guardrails &amp; live backtesting.",
        "tags": ["Python", "Scikit-Learn", "Pandas", "FastAPI", "Binance API"],
        "accent": "#f72585"
    }
]

for p in projects:
    def render_tags_dark(tags):
        res = ""
        x = 24
        for tag in tags:
            tag_escaped = escape_xml(tag)
            w = len(tag) * 8 + 16
            res += f"""<g transform="translate({x}, 150)">
              <rect width="{w}" height="24" rx="12" fill="#161b22" stroke="#30363d" stroke-width="1"/>
              <text x="{w/2}" y="16" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="600" fill="#c9d1d9">{tag_escaped}</text>
            </g>"""
            x += w + 8
        return res

    def render_tags_light(tags):
        res = ""
        x = 24
        for tag in tags:
            tag_escaped = escape_xml(tag)
            w = len(tag) * 8 + 16
            res += f"""<g transform="translate({x}, 150)">
              <rect width="{w}" height="24" rx="12" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
              <text x="{w/2}" y="16" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="600" fill="#334155">{tag_escaped}</text>
            </g>"""
            x += w + 8
        return res

    # Dark Card
    dark_card = f"""<svg xmlns="http://www.w3.org/2000/svg" width="580" height="195" viewBox="0 0 580 195" fill="none">
  <defs>
    <linearGradient id="pGradDark_{p['id']}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#161b22"/>
      <stop offset="100%" stop-color="#0d1117"/>
    </linearGradient>
  </defs>
  <rect width="580" height="195" rx="16" fill="url(#pGradDark_{p['id']})" stroke="#30363d" stroke-width="1.2"/>
  <rect x="1" y="1" width="578" height="193" rx="15" fill="none" stroke="{p['accent']}" stroke-width="1.2" stroke-opacity="0.3"/>
  
  <g transform="translate(24, 24)">
    <text x="0" y="20" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="22" font-weight="800" fill="#ffffff">{p['title']}</text>
    <g transform="translate(0, 0)">
      <rect x="400" y="4" width="132" height="22" rx="11" fill="{p['accent']}" fill-opacity="0.12" stroke="{p['accent']}" stroke-width="1" stroke-opacity="0.5"/>
      <text x="466" y="19" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="700" fill="{p['accent']}">{p['badge']}</text>
    </g>
  </g>

  <text x="24" y="80" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="400" fill="#94a3b8">
    <tspan x="24" dy="0">{p['desc']}</tspan>
  </text>

  {render_tags_dark(p['tags'])}

  <g transform="translate(535, 155)">
    <circle cx="10" cy="10" r="14" fill="#21262d" stroke="{p['accent']}" stroke-width="1" stroke-opacity="0.4"/>
    <path d="M7 13 L13 7 M7 7 L13 7 L13 13" fill="none" stroke="{p['accent']}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
</svg>"""
    write_svg(f"project-{p['id']}-dark.svg", dark_card)

    # Light Card
    light_card = f"""<svg xmlns="http://www.w3.org/2000/svg" width="580" height="195" viewBox="0 0 580 195" fill="none">
  <defs>
    <linearGradient id="pGradLight_{p['id']}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f8fafc"/>
    </linearGradient>
  </defs>
  <rect width="580" height="195" rx="16" fill="url(#pGradLight_{p['id']})" stroke="#e2e8f0" stroke-width="1.2"/>
  <rect x="1" y="1" width="578" height="193" rx="15" fill="none" stroke="{p['accent']}" stroke-width="1.2" stroke-opacity="0.3"/>
  
  <g transform="translate(24, 24)">
    <text x="0" y="20" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="22" font-weight="800" fill="#0f172a">{p['title']}</text>
    <g transform="translate(0, 0)">
      <rect x="400" y="4" width="132" height="22" rx="11" fill="{p['accent']}" fill-opacity="0.1" stroke="{p['accent']}" stroke-width="1" stroke-opacity="0.4"/>
      <text x="466" y="19" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="700" fill="{p['accent']}">{p['badge']}</text>
    </g>
  </g>

  <text x="24" y="80" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="400" fill="#475569">
    <tspan x="24" dy="0">{p['desc']}</tspan>
  </text>

  {render_tags_light(p['tags'])}

  <g transform="translate(535, 155)">
    <circle cx="10" cy="10" r="14" fill="#f1f5f9" stroke="{p['accent']}" stroke-width="1" stroke-opacity="0.4"/>
    <path d="M7 13 L13 7 M7 7 L13 7 L13 13" fill="none" stroke="{p['accent']}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
</svg>"""
    write_svg(f"project-{p['id']}-light.svg", light_card)


# --- 5. Tech Arsenal Uniform Grouped SVG Cards ---
categories = [
    {
        "id": "languages",
        "title": "Languages",
        "items": ["TypeScript", "JavaScript", "Python", "Java", "C++", "C", "SQL", "HTML5 / CSS3"]
    },
    {
        "id": "frontend",
        "title": "Frontend &amp; UI/UX",
        "items": ["Next.js", "React.js", "Vite", "Tailwind CSS", "Redux Toolkit", "Framer Motion", "Figma"]
    },
    {
        "id": "backend",
        "title": "Backend &amp; Microservices",
        "items": ["Node.js", "FastAPI", "Spring Boot", "Express.js", "Flask", "REST APIs", "WebSockets"]
    },
    {
        "id": "aiml",
        "title": "AI, ML &amp; Agents",
        "items": ["PyTorch", "TensorFlow", "Scikit-Learn", "LLM Agents", "LangChain", "Pandas", "NumPy"]
    },
    {
        "id": "data",
        "title": "Databases &amp; Cloud",
        "items": ["MongoDB", "PostgreSQL", "MySQL", "Redis", "Firebase", "Supabase", "Docker"]
    },
    {
        "id": "tools",
        "title": "DevOps &amp; Tooling",
        "items": ["Git &amp; GitHub", "GitHub Actions", "Linux / Bash", "Postman", "VS Code", "Maven/Gradle"]
    }
]

def create_tech_grid(theme="dark"):
    is_dark = theme == "dark"
    bg = "#0d1117" if is_dark else "#ffffff"
    card_bg = "#161b22" if is_dark else "#f8fafc"
    border = "#30363d" if is_dark else "#e2e8f0"
    title_col = "#ffffff" if is_dark else "#0f172a"
    pill_bg = "#21262d" if is_dark else "#ffffff"
    pill_border = "#30363d" if is_dark else "#cbd5e1"
    pill_text = "#f0f6fc" if is_dark else "#334155"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 400" fill="none">
  <rect width="1200" height="400" rx="16" fill="{bg}"/>
"""
    col_coords = [(20, 15), (410, 15), (800, 15), (20, 205), (410, 205), (800, 205)]
    
    for i, cat in enumerate(categories):
        x_pos, y_pos = col_coords[i]
        accent = ["#00f2fe", "#6366f1", "#9d4edd", "#f72585", "#00ff88", "#38bdf8"][i]
        
        svg += f"""  <!-- Card {cat['id']} -->
  <g transform="translate({x_pos}, {y_pos})">
    <rect width="380" height="180" rx="14" fill="{card_bg}" stroke="{border}" stroke-width="1.2"/>
    <rect x="1" y="1" width="378" height="178" rx="13" fill="none" stroke="{accent}" stroke-width="1.2" stroke-opacity="0.25"/>
    
    <circle cx="24" cy="24" r="4" fill="{accent}"/>
    <text x="36" y="28" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="{title_col}">{cat['title']}</text>
    <line x1="20" y1="42" x2="360" y2="42" stroke="{border}" stroke-width="1"/>

    <g transform="translate(18, 55)">
"""
        px, py = 0, 0
        for item in cat['items']:
            raw_len = len(item.replace("&amp;", "&"))
            item_w = raw_len * 7.5 + 18
            if px + item_w > 344:
                px = 0
                py += 32
            svg += f"""      <g transform="translate({px}, {py})">
        <rect width="{item_w}" height="24" rx="12" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1"/>
        <text x="{item_w/2}" y="16" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="600" fill="{pill_text}">{item}</text>
      </g>
"""
            px += item_w + 6

        svg += """    </g>
  </g>
"""
    svg += '</svg>'
    return svg

write_svg("tech-stack-dark.svg", create_tech_grid("dark"))
write_svg("tech-stack-light.svg", create_tech_grid("light"))


# --- 6. Experience / Leadership Minimal Timeline Card ---
exp_dark = """<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 180" fill="none">
  <defs>
    <linearGradient id="expBgDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#161b22"/>
      <stop offset="100%" stop-color="#0d1117"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="180" rx="16" fill="url(#expBgDark)" stroke="#30363d" stroke-width="1.2"/>

  <!-- Left: ISAC -->
  <g transform="translate(30, 25)">
    <rect width="550" height="130" rx="12" fill="#0d1117" stroke="#00f2fe" stroke-width="1" stroke-opacity="0.3"/>
    <circle cx="25" cy="28" r="5" fill="#00f2fe"/>
    <text x="40" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="17" font-weight="700" fill="#ffffff">Technical Lead</text>
    <text x="40" y="52" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" fill="#00f2fe">Indus Student Activity Cell (ISAC)</text>
    <text x="460" y="32" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" fill="#8b949e">2024 – Present</text>
    <line x1="25" y1="68" x2="525" y2="68" stroke="#30363d" stroke-width="1"/>
    <text x="25" y="92" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" font-weight="400" fill="#c9d1d9">Spearheading student technology initiatives, managing event platforms &amp; leading developer teams.</text>
    <text x="25" y="112" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" font-weight="400" fill="#8b949e">Mentoring peers in full-stack engineering, scalable workflows, and project execution.</text>
  </g>

  <!-- Right: Indus University -->
  <g transform="translate(620, 25)">
    <rect width="550" height="130" rx="12" fill="#0d1117" stroke="#6366f1" stroke-width="1" stroke-opacity="0.3"/>
    <circle cx="25" cy="28" r="5" fill="#6366f1"/>
    <text x="40" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="17" font-weight="700" fill="#ffffff">B.Tech in Computer Science &amp; Engg</text>
    <text x="40" y="52" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" fill="#6366f1">Indus University, Ahmedabad</text>
    <text x="460" y="32" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" fill="#8b949e">2023 – 2027</text>
    <line x1="25" y1="68" x2="525" y2="68" stroke="#30363d" stroke-width="1"/>
    <text x="25" y="92" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" font-weight="400" fill="#c9d1d9">Deep dive into Algorithms, Distributed Systems, Software Engineering &amp; AI architectures.</text>
    <text x="25" y="112" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" font-weight="400" fill="#8b949e">Building scalable academic &amp; extracurricular software platforms with modern tech stacks.</text>
  </g>
</svg>"""
write_svg("experience-dark.svg", exp_dark)

exp_light = """<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 180" fill="none">
  <defs>
    <linearGradient id="expBgLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f8fafc"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="180" rx="16" fill="url(#expBgLight)" stroke="#e2e8f0" stroke-width="1.2"/>

  <!-- Left: ISAC -->
  <g transform="translate(30, 25)">
    <rect width="550" height="130" rx="12" fill="#ffffff" stroke="#0284c7" stroke-width="1" stroke-opacity="0.3"/>
    <circle cx="25" cy="28" r="5" fill="#0284c7"/>
    <text x="40" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="17" font-weight="700" fill="#0f172a">Technical Lead</text>
    <text x="40" y="52" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" fill="#0284c7">Indus Student Activity Cell (ISAC)</text>
    <text x="460" y="32" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" fill="#64748b">2024 – Present</text>
    <line x1="25" y1="68" x2="525" y2="68" stroke="#e2e8f0" stroke-width="1"/>
    <text x="25" y="92" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" font-weight="400" fill="#334155">Spearheading student technology initiatives, managing event platforms &amp; leading developer teams.</text>
    <text x="25" y="112" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" font-weight="400" fill="#64748b">Mentoring peers in full-stack engineering, scalable workflows, and project execution.</text>
  </g>

  <!-- Right: Indus University -->
  <g transform="translate(620, 25)">
    <rect width="550" height="130" rx="12" fill="#ffffff" stroke="#4f46e5" stroke-width="1" stroke-opacity="0.3"/>
    <circle cx="25" cy="28" r="5" fill="#4f46e5"/>
    <text x="40" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="17" font-weight="700" fill="#0f172a">B.Tech in Computer Science &amp; Engg</text>
    <text x="40" y="52" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="600" fill="#4f46e5">Indus University, Ahmedabad</text>
    <text x="460" y="32" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" fill="#64748b">2023 – 2027</text>
    <line x1="25" y1="68" x2="525" y2="68" stroke="#e2e8f0" stroke-width="1"/>
    <text x="25" y="92" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" font-weight="400" fill="#334155">Deep dive into Algorithms, Distributed Systems, Software Engineering &amp; AI architectures.</text>
    <text x="25" y="112" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12.5" font-weight="400" fill="#64748b">Building scalable academic &amp; extracurricular software platforms with modern tech stacks.</text>
  </g>
</svg>"""
write_svg("experience-light.svg", exp_light)


# --- 7. Creative Corner Card ---
creative_dark = """<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 120" fill="none">
  <defs>
    <linearGradient id="crBgDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#161b22"/>
      <stop offset="100%" stop-color="#0d1117"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="120" rx="16" fill="url(#crBgDark)" stroke="#30363d" stroke-width="1.2"/>
  
  <g transform="translate(30, 24)">
    <rect width="55" height="55" rx="12" fill="#f72585" fill-opacity="0.12" stroke="#f72585" stroke-width="1"/>
    <text x="27.5" y="35" text-anchor="middle" font-size="24">🎬</text>
    
    <text x="75" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="700" fill="#ffffff">Video Editing, Motion &amp; Visual Storytelling</text>
    <text x="75" y="46" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="400" fill="#94a3b8">Cinematic storytelling, pacing, sound design, motion graphics &amp; high-energy sports (cricket) media editing.</text>
  </g>
</svg>"""
write_svg("creative-dark.svg", creative_dark)

creative_light = """<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 120" fill="none">
  <defs>
    <linearGradient id="crBgLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f8fafc"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="120" rx="16" fill="url(#crBgLight)" stroke="#e2e8f0" stroke-width="1.2"/>
  
  <g transform="translate(30, 24)">
    <rect width="55" height="55" rx="12" fill="#f472b6" fill-opacity="0.15" stroke="#db2777" stroke-width="1"/>
    <text x="27.5" y="35" text-anchor="middle" font-size="24">🎬</text>
    
    <text x="75" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="700" fill="#0f172a">Video Editing, Motion &amp; Visual Storytelling</text>
    <text x="75" y="46" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="400" fill="#475569">Cinematic storytelling, pacing, sound design, motion graphics &amp; high-energy sports (cricket) media editing.</text>
  </g>
</svg>"""
write_svg("creative-light.svg", creative_light)


# --- 8. Footer (Dark & Light) ---
footer_dark = """<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 120" fill="none">
  <defs>
    <linearGradient id="ftBgDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16" />
      <stop offset="50%" stop-color="#14132b" />
      <stop offset="100%" stop-color="#090d16" />
    </linearGradient>
    <linearGradient id="ftWaveDark" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f2fe" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#6366f1" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#f72585" stop-opacity="0.6"/>
    </linearGradient>
    <filter id="ftGlow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <style>
    @keyframes waveFloat1 {
      0%, 100% { transform: translateX(0); }
      50% { transform: translateX(-30px); }
    }
    @keyframes waveFloat2 {
      0%, 100% { transform: translateX(0); }
      50% { transform: translateX(30px); }
    }
    .w1 { animation: waveFloat1 7s ease-in-out infinite; }
    .w2 { animation: waveFloat2 9s ease-in-out infinite; }
  </style>
  <rect width="1200" height="120" rx="16" fill="url(#ftBgDark)" stroke="#30363d" stroke-width="1.2"/>
  <path class="w1" d="M -50 35 Q 250 15 550 35 T 1150 30 T 1300 40" fill="none" stroke="url(#ftWaveDark)" stroke-width="2" opacity="0.8" filter="url(#ftGlow)"/>
  <path class="w2" d="M -50 42 Q 300 55 650 30 T 1250 35" fill="none" stroke="#00f2fe" stroke-width="1.2" opacity="0.3"/>
  
  <text x="600" y="78" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#f0f6fc" letter-spacing="0.8">
    DESIGNED &amp; ARCHITECTED BY ABHI PATEL • THANKS FOR VISITING
  </text>
  <text x="600" y="98" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500" fill="#8b949e">
    Ahmedabad, India • B.Tech CSE '27 • ISAC Tech Lead
  </text>
</svg>"""
write_svg("footer-dark.svg", footer_dark)
write_svg("footer.svg", footer_dark)

footer_light = """<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 120" fill="none">
  <defs>
    <linearGradient id="ftBgLight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="50%" stop-color="#f8fafc" />
      <stop offset="100%" stop-color="#f1f5f9" />
    </linearGradient>
    <linearGradient id="ftWaveLight" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#4f46e5" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#db2777" stop-opacity="0.6"/>
    </linearGradient>
  </defs>
  <style>
    @keyframes waveFloat1L {
      0%, 100% { transform: translateX(0); }
      50% { transform: translateX(-30px); }
    }
    @keyframes waveFloat2L {
      0%, 100% { transform: translateX(0); }
      50% { transform: translateX(30px); }
    }
    .w1-l { animation: waveFloat1L 7s ease-in-out infinite; }
    .w2-l { animation: waveFloat2L 9s ease-in-out infinite; }
  </style>
  <rect width="1200" height="120" rx="16" fill="url(#ftBgLight)" stroke="#e2e8f0" stroke-width="1.2"/>
  <path class="w1-l" d="M -50 35 Q 250 15 550 35 T 1150 30 T 1300 40" fill="none" stroke="url(#ftWaveLight)" stroke-width="2" opacity="0.8"/>
  <path class="w2-l" d="M -50 42 Q 300 55 650 30 T 1250 35" fill="none" stroke="#0284c7" stroke-width="1.2" opacity="0.3"/>
  
  <text x="600" y="78" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="#0f172a" letter-spacing="0.8">
    DESIGNED &amp; ARCHITECTED BY ABHI PATEL • THANKS FOR VISITING
  </text>
  <text x="600" y="98" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500" fill="#64748b">
    Ahmedabad, India • B.Tech CSE '27 • ISAC Tech Lead
  </text>
</svg>"""
write_svg("footer-light.svg", footer_light)

print("Asset generation complete!")
