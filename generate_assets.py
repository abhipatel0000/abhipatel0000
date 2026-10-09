import os

ASSETS_DIR = r"c:\Users\Abhi patel\OneDrive\Desktop\Special Repo\abhipatel0000\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

def write_svg(filename, content):
    path = os.path.join(ASSETS_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated {filename}")

# --- 1. Quick Link Pill Buttons ---
buttons = [
    {
        "name": "github",
        "label": "GitHub",
        "color_dark": "#f0f6fc",
        "color_light": "#0f172a",
        "accent": "#6366f1",
        "icon": '<path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" fill="currentColor"/>',
        "viewBox": "0 0 24 24"
    },
    {
        "name": "email",
        "label": "Email",
        "color_dark": "#f0f6fc",
        "color_light": "#0f172a",
        "accent": "#ea4335",
        "icon": '<path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" fill="currentColor"/>',
        "viewBox": "0 0 24 24"
    },
    {
        "name": "instagram",
        "label": "Instagram",
        "color_dark": "#f0f6fc",
        "color_light": "#0f172a",
        "accent": "#e4405f",
        "icon": '<path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z" fill="currentColor"/>',
        "viewBox": "0 0 24 24"
    },
    {
        "name": "portfolio",
        "label": "Portfolio",
        "color_dark": "#f0f6fc",
        "color_light": "#0f172a",
        "accent": "#00f2fe",
        "icon": '<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z" fill="currentColor"/>',
        "viewBox": "0 0 24 24"
    }
]

for btn in buttons:
    # Dark Button
    dark_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="148" height="38" viewBox="0 0 148 38" fill="none">
  <rect x="0.5" y="0.5" width="147" height="37" rx="18.5" fill="#0d1117" stroke="{btn['accent']}" stroke-width="1.2" stroke-opacity="0.6"/>
  <rect x="0.5" y="0.5" width="147" height="37" rx="18.5" fill="{btn['accent']}" fill-opacity="0.08"/>
  <g transform="translate(18, 10) scale(0.75)" color="{btn['accent']}">
    {btn['icon']}
  </g>
  <text x="78" y="24" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, sans-serif" font-size="13" font-weight="600" fill="#f0f6fc">{btn['label']}</text>
  <path d="M125 15 L129 19 L125 23" fill="none" stroke="{btn['accent']}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''
    write_svg(f"btn-{btn['name']}-dark.svg", dark_svg)

    # Light Button
    light_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="148" height="38" viewBox="0 0 148 38" fill="none">
  <rect x="0.5" y="0.5" width="147" height="37" rx="18.5" fill="#ffffff" stroke="{btn['accent']}" stroke-width="1.2" stroke-opacity="0.5"/>
  <rect x="0.5" y="0.5" width="147" height="37" rx="18.5" fill="{btn['accent']}" fill-opacity="0.05"/>
  <g transform="translate(18, 10) scale(0.75)" color="{btn['accent']}">
    {btn['icon']}
  </g>
  <text x="78" y="24" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, sans-serif" font-size="13" font-weight="600" fill="#0f172a">{btn['label']}</text>
  <path d="M125 15 L129 19 L125 23" fill="none" stroke="{btn['accent']}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''
    write_svg(f"btn-{btn['name']}-light.svg", light_svg)


# --- 2. Section Headers ---
headers = [
    {"name": "projects", "title": "FEATURED PROJECTS", "icon": "🚀", "accent": "#00f2fe", "sub": "Production Architectures & Systems"},
    {"name": "tech", "title": "TECH ARSENAL", "icon": "⚡", "accent": "#6366f1", "sub": "Languages, Frameworks & Infrastructure"},
    {"name": "stats", "title": "ENGINEERING METRICS", "icon": "📊", "accent": "#9d4edd", "sub": "GitHub Activity & Code Distribution"},
    {"name": "snake", "title": "CONTRIBUTION GRAPH", "icon": "🟩", "accent": "#00ff88", "sub": "Daily Commit Trail & Activity"},
    {"name": "experience", "title": "LEADERSHIP & EDUCATION", "icon": "💼", "accent": "#00f2fe", "sub": "Milestones & Institutional Roles"},
    {"name": "creative", "title": "CREATIVE CORNER", "icon": "🎬", "accent": "#f72585", "sub": "Video Production & Visual Media"},
    {"name": "contact", "title": "GET IN TOUCH", "icon": "🤝", "accent": "#6366f1", "sub": "Collaborations, Open Roles & Inquiries"}
]

for h in headers:
    # Dark Header
    dark_head = f'''<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 70" fill="none">
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
    <text x="320" y="23" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="500" fill="#8b949e">/ {h['sub']}</text>
    <line x1="50" y1="36" x2="1180" y2="36" stroke="url(#lineGradDark_{h['name']})" stroke-width="1.5" stroke-linecap="round"/>
  </g>
</svg>'''
    write_svg(f"header-{h['name']}-dark.svg", dark_head)

    # Light Header
    light_head = f'''<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 70" fill="none">
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
    <text x="320" y="23" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="500" fill="#64748b">/ {h['sub']}</text>
    <line x1="50" y1="36" x2="1180" y2="36" stroke="url(#lineGradLight_{h['name']})" stroke-width="1.5" stroke-linecap="round"/>
  </g>
</svg>'''
    write_svg(f"header-{h['name']}-light.svg", light_head)


# --- 3. Currently Status Card ---
currently_dark = '''<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 130" fill="none">
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
</svg>'''
write_svg("currently-dark.svg", currently_dark)

currently_light = '''<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 130" fill="none">
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
</svg>'''
write_svg("currently-light.svg", currently_light)


# --- 4. Featured Project Cards (4 Cards) ---
projects = [
    {
        "id": "aura",
        "title": "AURA",
        "badge": "AI OS ASSISTANT",
        "desc": "Intelligent desktop companion for automated workflows, context reasoning, and voice-controlled system actions.",
        "tags": ["Python", "FastAPI", "PyTorch", "LLM Agents", "Electron"],
        "accent": "#00f2fe",
        "stars": "Featured"
    },
    {
        "id": "stagesync",
        "title": "StageSync",
        "badge": "EVENT MEDIA DELIVERY",
        "desc": "High-throughput asset distribution platform with instant client uploads, lossless compression & live sync.",
        "tags": ["Next.js", "Node.js", "WebSockets", "Docker", "S3"],
        "accent": "#6366f1",
        "stars": "Core Project"
    },
    {
        "id": "bestview",
        "title": "BestView Clone",
        "badge": "HOSPITALITY PLATFORM",
        "desc": "Full-stack resort & luxury stay booking platform featuring real-time room availability, interactive maps & payments.",
        "tags": ["React", "Tailwind CSS", "Spring Boot", "PostgreSQL"],
        "accent": "#9d4edd",
        "stars": "Full-Stack"
    },
    {
        "id": "tradingbot",
        "title": "AI Trading Bot",
        "badge": "ALGORITHMIC TRADING",
        "desc": "Quantitative algorithmic market execution engine with ML predictive signals, risk guardrails & live backtesting.",
        "tags": ["Python", "Scikit-Learn", "Pandas", "FastAPI", "Binance API"],
        "accent": "#f72585",
        "stars": "Quant & AI"
    }
]

for p in projects:
    # Render Tag Badges helper
    def render_tags_dark(tags):
        res = ""
        x = 24
        for tag in tags:
            w = len(tag) * 8 + 16
            res += f'''<g transform="translate({x}, 150)">
              <rect width="{w}" height="24" rx="12" fill="#161b22" stroke="#30363d" stroke-width="1"/>
              <text x="{w/2}" y="16" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="600" fill="#c9d1d9">{tag}</text>
            </g>'''
            x += w + 8
        return res

    def render_tags_light(tags):
        res = ""
        x = 24
        for tag in tags:
            w = len(tag) * 8 + 16
            res += f'''<g transform="translate({x}, 150)">
              <rect width="{w}" height="24" rx="12" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
              <text x="{w/2}" y="16" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="600" fill="#334155">{tag}</text>
            </g>'''
            x += w + 8
        return res

    # Dark Card
    dark_card = f'''<svg xmlns="http://www.w3.org/2000/svg" width="580" height="195" viewBox="0 0 580 195" fill="none">
  <defs>
    <linearGradient id="pGradDark_{p['id']}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#161b22"/>
      <stop offset="100%" stop-color="#0d1117"/>
    </linearGradient>
  </defs>
  <rect width="580" height="195" rx="16" fill="url(#pGradDark_{p['id']})" stroke="#30363d" stroke-width="1.2"/>
  <rect x="1" y="1" width="578" height="193" rx="15" fill="none" stroke="{p['accent']}" stroke-width="1.2" stroke-opacity="0.3"/>
  
  <!-- Header row -->
  <g transform="translate(24, 24)">
    <text x="0" y="20" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="22" font-weight="800" fill="#ffffff">{p['title']}</text>
    <!-- Badge -->
    <g transform="translate(0, 0)">
      <rect x="420" y="4" width="112" height="22" rx="11" fill="{p['accent']}" fill-opacity="0.12" stroke="{p['accent']}" stroke-width="1" stroke-opacity="0.5"/>
      <text x="476" y="19" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="700" fill="{p['accent']}">{p['badge']}</text>
    </g>
  </g>

  <!-- Description -->
  <text x="24" y="80" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="400" fill="#94a3b8" width="530">
    <tspan x="24" dy="0">{p['desc'][:68]}</tspan>
    <tspan x="24" dy="22">{p['desc'][68:]}</tspan>
  </text>

  <!-- Tags -->
  {render_tags_dark(p['tags'])}

  <!-- Arrow Link Icon -->
  <g transform="translate(535, 155)">
    <circle cx="10" cy="10" r="14" fill="#21262d" stroke="{p['accent']}" stroke-width="1" stroke-opacity="0.4"/>
    <path d="M7 13 L13 7 M7 7 L13 7 L13 13" fill="none" stroke="{p['accent']}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
</svg>'''
    write_svg(f"project-{p['id']}-dark.svg", dark_card)

    # Light Card
    light_card = f'''<svg xmlns="http://www.w3.org/2000/svg" width="580" height="195" viewBox="0 0 580 195" fill="none">
  <defs>
    <linearGradient id="pGradLight_{p['id']}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f8fafc"/>
    </linearGradient>
  </defs>
  <rect width="580" height="195" rx="16" fill="url(#pGradLight_{p['id']})" stroke="#e2e8f0" stroke-width="1.2"/>
  <rect x="1" y="1" width="578" height="193" rx="15" fill="none" stroke="{p['accent']}" stroke-width="1.2" stroke-opacity="0.3"/>
  
  <!-- Header row -->
  <g transform="translate(24, 24)">
    <text x="0" y="20" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="22" font-weight="800" fill="#0f172a">{p['title']}</text>
    <!-- Badge -->
    <g transform="translate(0, 0)">
      <rect x="420" y="4" width="112" height="22" rx="11" fill="{p['accent']}" fill-opacity="0.1" stroke="{p['accent']}" stroke-width="1" stroke-opacity="0.4"/>
      <text x="476" y="19" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="700" fill="{p['accent']}">{p['badge']}</text>
    </g>
  </g>

  <!-- Description -->
  <text x="24" y="80" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13.5" font-weight="400" fill="#475569" width="530">
    <tspan x="24" dy="0">{p['desc'][:68]}</tspan>
    <tspan x="24" dy="22">{p['desc'][68:]}</tspan>
  </text>

  <!-- Tags -->
  {render_tags_light(p['tags'])}

  <!-- Arrow Link Icon -->
  <g transform="translate(535, 155)">
    <circle cx="10" cy="10" r="14" fill="#f1f5f9" stroke="{p['accent']}" stroke-width="1" stroke-opacity="0.4"/>
    <path d="M7 13 L13 7 M7 7 L13 7 L13 13" fill="none" stroke="{p['accent']}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
</svg>'''
    write_svg(f"project-{p['id']}-light.svg", light_card)


# --- 5. Tech Arsenal Uniform Grouped SVG Cards ---
categories = [
    {
        "id": "languages",
        "title": "Languages",
        "icon_char": "💻",
        "items": ["TypeScript", "JavaScript", "Python", "Java", "C++", "C", "SQL", "HTML5/CSS3"]
    },
    {
        "id": "frontend",
        "title": "Frontend & UI/UX",
        "icon_char": "⚛️",
        "items": ["Next.js", "React.js", "Vite", "Tailwind CSS", "Redux Toolkit", "Framer Motion", "Figma"]
    },
    {
        "id": "backend",
        "title": "Backend & Microservices",
        "icon_char": "🚀",
        "items": ["Node.js", "FastAPI", "Spring Boot", "Express.js", "Flask", "REST APIs", "WebSockets"]
    },
    {
        "id": "aiml",
        "title": "AI, ML & Agents",
        "icon_char": "🧠",
        "items": ["PyTorch", "TensorFlow", "Scikit-Learn", "LLM Agents", "LangChain", "Pandas", "NumPy"]
    },
    {
        "id": "data",
        "title": "Databases & Cloud",
        "icon_char": "🗄️",
        "items": ["MongoDB", "PostgreSQL", "MySQL", "Redis", "Firebase", "Supabase", "Docker"]
    },
    {
        "id": "tools",
        "title": "DevOps & Tooling",
        "icon_char": "🧰",
        "items": ["Git & GitHub", "GitHub Actions", "Linux / Bash", "Postman", "VS Code", "Maven/Gradle"]
    }
]

# Create one comprehensive 1200x380 Tech Stack SVG Grid (Dark & Light)
def create_tech_grid(theme="dark"):
    is_dark = theme == "dark"
    bg = "#0d1117" if is_dark else "#ffffff"
    card_bg = "#161b22" if is_dark else "#f8fafc"
    border = "#30363d" if is_dark else "#e2e8f0"
    title_col = "#ffffff" if is_dark else "#0f172a"
    sub_col = "#94a3b8" if is_dark else "#64748b"
    pill_bg = "#21262d" if is_dark else "#ffffff"
    pill_border = "#30363d" if is_dark else "#cbd5e1"
    pill_text = "#f0f6fc" if is_dark else "#334155"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 400" fill="none">
  <rect width="1200" height="400" rx="16" fill="{bg}"/>
'''
    # 6 cards arranged in 3 columns x 2 rows
    # Col widths: 375px, Row heights: 175px
    col_coords = [(20, 15), (410, 15), (800, 15), (20, 205), (410, 205), (800, 205)]
    
    for i, cat in enumerate(categories):
        x_pos, y_pos = col_coords[i]
        accent = ["#00f2fe", "#6366f1", "#9d4edd", "#f72585", "#00ff88", "#38bdf8"][i]
        
        svg += f'''  <!-- Card {cat['title']} -->
  <g transform="translate({x_pos}, {y_pos})">
    <rect width="380" height="180" rx="14" fill="{card_bg}" stroke="{border}" stroke-width="1.2"/>
    <rect x="1" y="1" width="378" height="178" rx="13" fill="none" stroke="{accent}" stroke-width="1.2" stroke-opacity="0.25"/>
    
    <!-- Title -->
    <circle cx="24" cy="24" r="4" fill="{accent}"/>
    <text x="36" y="28" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="700" fill="{title_col}">{cat['title']}</text>
    <line x1="20" y1="42" x2="360" y2="42" stroke="{border}" stroke-width="1"/>

    <!-- Pills Grid -->
    <g transform="translate(18, 55)">
'''
        # Arrange items into 2-3 rows inside the card
        px, py = 0, 0
        for item in cat['items']:
            item_w = len(item) * 7.5 + 18
            if px + item_w > 344:
                px = 0
                py += 32
            svg += f'''      <g transform="translate({px}, {py})">
        <rect width="{item_w}" height="24" rx="12" fill="{pill_bg}" stroke="{pill_border}" stroke-width="1"/>
        <text x="{item_w/2}" y="16" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="600" fill="{pill_text}">{item}</text>
      </g>
'''
            px += item_w + 6

        svg += '''    </g>
  </g>
'''
    svg += '</svg>'
    return svg

write_svg("tech-stack-dark.svg", create_tech_grid("dark"))
write_svg("tech-stack-light.svg", create_tech_grid("light"))


# --- 6. Experience / Leadership Minimal Timeline Card ---
exp_dark = '''<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 180" fill="none">
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
</svg>'''
write_svg("experience-dark.svg", exp_dark)

exp_light = '''<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 180" fill="none">
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
</svg>'''
write_svg("experience-light.svg", exp_light)


# --- 7. Creative Corner Card ---
creative_dark = '''<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 120" fill="none">
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
</svg>'''
write_svg("creative-dark.svg", creative_dark)

creative_light = '''<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 120" fill="none">
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
</svg>'''
write_svg("creative-light.svg", creative_light)


# --- 8. Footer (Dark & Light) ---
footer_dark = '''<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 120" fill="none">
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
</svg>'''
write_svg("footer-dark.svg", footer_dark)
write_svg("footer.svg", footer_dark)

footer_light = '''<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%" viewBox="0 0 1200 120" fill="none">
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
</svg>'''
write_svg("footer-light.svg", footer_light)

print("Asset generation complete!")
