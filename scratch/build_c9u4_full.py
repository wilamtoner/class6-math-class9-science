# -*- coding: utf-8 -*-
"""
Class 9 Science Unit 4 (Evolution - क्रम विकास)
Generates:
  1. scratch/c9u4_html.html
  2. scratch/c9u4_js.js
"""
import re
import os

print("Building Grade 9 Unit 4 (Evolution) Full Component...")

# Read Tab 1 from generate_c9u4_all.py
with open("scratch/generate_c9u4_all.py", "r", encoding="utf-8") as f:
    gen_script = f.read()

idx_tab1_start = gen_script.find('tab1_html = """') + len('tab1_html = """')
idx_tab1_end = gen_script.find('"""\n\nprint("Tab 1 ready.")')
tab1_html = gen_script[idx_tab1_start:idx_tab1_end]

# Read Solutions and Notes
with open("solutions/class9_science/unit04_evolution_solutions.md", "r", encoding="utf-8") as f:
    sol_md = f.read()

with open("notes/class9_science/04_evolution.md", "r", encoding="utf-8") as f:
    notes_md = f.read()

def clean_inline_md(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    return text

def parse_md_table(lines):
    table_lines = [l.strip() for l in lines if l.strip().startswith('|') and l.strip().endswith('|')]
    if len(table_lines) < 3:
        return ""
    headers = [clean_inline_md(c.strip()) for c in table_lines[0].split('|')[1:-1]]
    body_rows = []
    for row in table_lines[2:]:
        body_rows.append([clean_inline_md(c.strip()) for c in row.split('|')[1:-1]])
    
    col_w = f"w-1/{len(headers)}"
    thead = '<thead class="bg-slate-100 text-slate-700 font-bold"><tr>' + ''.join(
        f'<th class="p-2.5 border-b border-r border-slate-200 {col_w}">{h}</th>' for h in headers
    ) + '</tr></thead>'
    tbody = '<tbody class="divide-y divide-slate-200 text-slate-600">'
    for row in body_rows:
        tbody += '<tr>' + ''.join(f'<td class="p-2.5 border-r border-slate-200 align-top">{c}</td>' for c in row) + '</tr>'
    tbody += '</tbody>'
    return f'<div class="overflow-x-auto"><table class="w-full text-xs text-left border border-slate-200 bg-white rounded-xl overflow-hidden">{thead}{tbody}</table></div>'

# =========================================================================
# TAB 2: EXERCISES
# =========================================================================
# Split solutions by ###
sol_parts = re.split(r'\n###\s+', sol_md)
# Part 2: MCQs
# Part 3: Reasons
# Part 4: Differences
# Part 5: Detailed QA
# Part 6: Practical Projects

# Parse MCQs
mcq_raw = sol_parts[2]
mcq_items = re.split(r'\n####\s+', mcq_raw)[1:]
mcq_html_cards = []
for item in mcq_items:
    lines = item.strip().split('\n')
    q_title = clean_inline_md(lines[0])
    
    opts = []
    correct_opt = ""
    exp_text = ""
    for l in lines[1:]:
        l_str = l.strip()
        if l_str.startswith('- '):
            opt_line = l_str[2:].strip()
            if '(✓)' in opt_line or '✓' in opt_line:
                clean_opt = opt_line.replace('(✓)', '').replace('✓', '').strip()
                opts.append((clean_opt, True))
            else:
                opts.append((opt_line, False))
        elif 'कारण' in l_str or 'पुष्टि' in l_str or 'नोट' in l_str or 'स्पष्टीकरण' in l_str:
            exp_text = clean_inline_md(l_str.replace('- ', '').strip())
    
    opts_html = '<div class="space-y-1 text-xs">'
    for opt_text, is_corr in opts:
        if is_corr:
            opts_html += f'<div class="p-2 rounded-xl bg-emerald-100/70 border border-emerald-300 font-bold text-emerald-900 flex items-center justify-between"><span>{opt_text}</span><span class="text-emerald-700">✓ सही उत्तर</span></div>'
        else:
            opts_html += f'<div class="p-2 rounded-xl bg-white border border-slate-200 text-slate-600">{opt_text}</div>'
    opts_html += '</div>'
    
    exp_html = f'<p class="text-[11px] text-slate-500 pt-1">{exp_text}</p>' if exp_text else ''
    mcq_html_cards.append(f'''
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <span class="text-xs font-bold text-purple-600 block">{q_title}</span>
              {opts_html}
              {exp_html}
            </div>
    ''')

# Parse Reasons
reasons_raw = sol_parts[3]
reason_items = re.split(r'\n####\s+', reasons_raw)[1:]
reason_html_cards = []
for item in reason_items:
    lines = item.strip().split('\n')
    q_title = clean_inline_md(lines[0])
    ans_lines = [clean_inline_md(l.strip()) for l in lines[1:] if l.strip()]
    ans_text = " ".join(ans_lines).replace('- **उत्तर:**', '<strong>उत्तर:</strong>').replace('**उत्तर:**', '<strong>उत्तर:</strong>')
    reason_html_cards.append(f'''
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 text-amber-900">
                {q_title}
              </h4>
              <div class="text-xs text-slate-700 leading-relaxed bg-white p-3 rounded-xl border border-slate-200">
                {ans_text}
              </div>
            </div>
    ''')

# Parse Differences
diff_raw = sol_parts[4]
diff_items = re.split(r'\n####\s+', diff_raw)[1:]
diff_html_cards = []
for item in diff_items:
    lines = item.strip().split('\n')
    q_title = clean_inline_md(lines[0])
    tbl_html = parse_md_table(lines[1:])
    diff_html_cards.append(f'''
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 text-purple-900">{q_title}</h4>
              {tbl_html}
            </div>
    ''')

# Parse Detailed QA
qa_raw = sol_parts[5]
qa_items = re.split(r'\n####\s+', qa_raw)[1:]
qa_html_cards = []
for item in qa_items:
    lines = item.strip().split('\n')
    q_title = clean_inline_md(lines[0])
    
    # Check for table inside QA (e.g., Lamarck vs Darwin)
    if any(l.strip().startswith('|') for l in lines[1:]):
        tbl_html = parse_md_table(lines[1:])
        qa_html_cards.append(f'''
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 flex items-center gap-2">
                <span class="text-purple-700 font-black">{q_title[:4]}</span>
                <span>{q_title[4:].strip()}</span>
              </h4>
              {tbl_html}
            </div>
        ''')
    elif 'आर्कियोप्टेरिक्स' in q_title:
        # Special badge for Archaeopteryx
        content_lines = lines[1:]
        body_p = []
        for l in content_lines:
            l_str = clean_inline_md(l.strip())
            if l_str:
                if l_str.startswith('##### '):
                    body_p.append(f'<strong class="block text-slate-900 mt-2">{l_str[6:]}</strong>')
                elif l_str.startswith('- **उत्तर:**') or l_str.startswith('- उत्तर:'):
                    body_p.append(f'<p class="text-slate-600 pl-2">{l_str[2:]}</p>')
                elif l_str.startswith('- '):
                    body_p.append(f'<p class="text-slate-700">{l_str[2:]}</p>')
                else:
                    body_p.append(f'<p>{l_str}</p>')
        body_html = "".join(body_p)
        qa_html_cards.append(f'''
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-3">
              <div class="flex items-center justify-between border-b border-slate-200 pb-2">
                <h4 class="text-xs md:text-sm font-bold text-slate-900 flex items-center gap-2">
                  <span class="text-emerald-700 font-black">{q_title[:4]}</span>
                  <span>{q_title[4:].strip()}</span>
                </h4>
                <span class="text-[10px] px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 font-bold">संयोजक कडी विश्लेषण</span>
              </div>
              <div class="p-3 rounded-xl bg-slate-900 text-slate-200 flex items-center gap-3 text-xs">
                <div class="w-12 h-12 rounded-xl bg-amber-500/20 border border-amber-500/40 flex items-center justify-center text-2xl shrink-0">🦅</div>
                <div>
                  <strong class="text-amber-400 block font-mono">ARCHAEOPTERYX LITHOGRAPHICA FOSSIL</strong>
                  <p class="text-[11px] text-slate-400">जुरासिक कालको पत्रे चट्टानमा फेला परेको सरीसृप र चरा बीचको जीवावशेष कडी</p>
                </div>
              </div>
              <div class="space-y-2 text-xs text-slate-700 leading-relaxed bg-white p-3.5 rounded-xl border border-slate-200">
                {body_html}
              </div>
            </div>
        ''')
    elif 'Polydactyly' in q_title or '६ ओटा औँला' in q_title or '६ वटा औँला' in q_title:
        # Special badge for Polydactyly
        content_lines = lines[1:]
        body_p = []
        for l in content_lines:
            l_str = clean_inline_md(l.strip())
            if l_str:
                if l_str.startswith('##### '):
                    body_p.append(f'<strong class="block text-slate-900 mt-2">{l_str[6:]}</strong>')
                elif l_str.startswith('- **उत्तर:**') or l_str.startswith('- उत्तर:'):
                    body_p.append(f'<p class="text-slate-600 pl-2">{l_str[2:]}</p>')
                elif l_str.startswith('- '):
                    body_p.append(f'<p class="text-slate-700">{l_str[2:]}</p>')
                else:
                    body_p.append(f'<p>{l_str}</p>')
        body_html = "".join(body_p)
        qa_html_cards.append(f'''
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-3">
              <div class="flex items-center justify-between border-b border-slate-200 pb-2">
                <h4 class="text-xs md:text-sm font-bold text-slate-900 flex items-center gap-2">
                  <span class="text-rose-700 font-black">{q_title[:4]}</span>
                  <span>{q_title[4:].strip()}</span>
                </h4>
                <span class="text-[10px] px-2 py-0.5 rounded-full bg-rose-100 text-rose-800 font-bold">उत्परिवर्तन विश्लेषण</span>
              </div>
              <div class="p-3 rounded-xl bg-slate-900 text-slate-200 flex items-center gap-3 text-xs">
                <div class="w-12 h-12 rounded-xl bg-rose-500/20 border border-rose-500/40 flex items-center justify-center text-2xl shrink-0">🖐️</div>
                <div>
                  <strong class="text-rose-400 block font-mono">POLYDACTYLY (६ वटा औँलाहरू)</strong>
                  <p class="text-[11px] text-slate-400">वंशाणुमा भएको आकस्मिक उत्परिवर्तन (Gene Mutation) को प्रत्यक्ष उदाहरण</p>
                </div>
              </div>
              <div class="space-y-2 text-xs text-slate-700 leading-relaxed bg-white p-3.5 rounded-xl border border-slate-200">
                {body_html}
              </div>
            </div>
        ''')
    else:
        # Standard Q&A
        body_p = []
        for l in lines[1:]:
            l_str = clean_inline_md(l.strip())
            if l_str:
                if l_str.startswith('- '):
                    body_p.append(f'<li class="ml-4 list-disc">{l_str[2:]}</li>')
                elif l_str.startswith('1. ') or l_str.startswith('२. ') or l_str.startswith('३. ') or l_str.startswith('४. ') or l_str.startswith('५. ') or l_str.startswith('१. '):
                    body_p.append(f'<p class="pt-1">{l_str}</p>')
                else:
                    body_p.append(f'<p>{l_str}</p>')
        body_html = "".join(body_p).replace('**उत्तर:**', '<strong>उत्तर:</strong>')
        qa_html_cards.append(f'''
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 flex items-center gap-2">
                <span class="text-blue-600 font-black">{q_title[:4]}</span>
                <span>{q_title[4:].strip()}</span>
              </h4>
              <div class="text-xs text-slate-700 leading-relaxed bg-white p-3.5 rounded-xl border border-slate-200 space-y-2">
                {body_html}
              </div>
            </div>
        ''')

# Parse Projects
proj_raw = sol_parts[6]
proj_items = re.split(r'\n####\s+', proj_raw)[1:]
proj_html_cards = []
for item in proj_items:
    lines = item.strip().split('\n')
    q_title = clean_inline_md(lines[0])
    body_p = []
    for l in lines[1:]:
        l_str = clean_inline_md(l.strip())
        if l_str:
            if l_str.startswith('- '):
                body_p.append(f'<p class="pt-1">{l_str[2:]}</p>')
            else:
                body_p.append(f'<p>{l_str}</p>')
    body_html = "".join(body_p)
    proj_html_cards.append(f'''
            <div class="bg-slate-50 rounded-2xl p-4 border border-slate-200 space-y-2">
              <h4 class="text-xs md:text-sm font-bold text-slate-900 text-emerald-900 flex items-center gap-2">
                <span>🌱 {q_title}</span>
              </h4>
              <div class="text-xs text-slate-700 leading-relaxed bg-white p-3.5 rounded-xl border border-slate-200 space-y-2">
                {body_html}
              </div>
            </div>
    ''')

tab2_html = f'''  <!-- ================= TAB 2: EXERCISES ================= -->
  <div id="c9u4-view-exercises" class="hidden space-y-6">
    <!-- Category Filter Bar -->
    <div class="flex items-center justify-between border-b border-slate-200 pb-3 flex-wrap gap-2">
      <div class="text-xs font-bold text-slate-500">
        प्रश्न प्रकार अनुसार छान्नुहोस्:
      </div>
      <div class="flex flex-wrap gap-1.5">
        <button onclick="filterC9U4Exercises('all')" id="c9u4-exbtn-all" class="px-3 py-1.5 rounded-xl text-xs font-black transition bg-purple-600 text-white shadow-sm cursor-pointer whitespace-nowrap">
          सबै अभ्यास
        </button>
        <button onclick="filterC9U4Exercises('mcq')" id="c9u4-exbtn-mcq" class="px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap">
          १. बहुवैकल्पिक (MCQs)
        </button>
        <button onclick="filterC9U4Exercises('reason')" id="c9u4-exbtn-reason" class="px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap">
          २. कारण दिनुहोस्
        </button>
        <button onclick="filterC9U4Exercises('diff')" id="c9u4-exbtn-diff" class="px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap">
          ३. फरक लेख्नुहोस्
        </button>
        <button onclick="filterC9U4Exercises('qa')" id="c9u4-exbtn-qa" class="px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap">
          ४. विस्तृत प्रश्नोत्तर
        </button>
        <button onclick="filterC9U4Exercises('project')" id="c9u4-exbtn-project" class="px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap">
          ५. परियोजना कार्यहरू
        </button>
      </div>
    </div>

    <!-- Exercise Cards Grid -->
    <div class="space-y-6">

      <!-- ================= 1. MCQS ================= -->
      <div class="c9u4-ex-card" data-cat="mcq">
        <div class="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm space-y-4">
          <div class="flex items-center justify-between border-b border-slate-100 pb-3">
            <h3 class="font-black text-slate-900 text-base flex items-center gap-2">
              <span class="w-7 h-7 rounded-xl bg-purple-100 text-purple-700 flex items-center justify-center text-xs font-black">१</span>
              <span>तल दिइएका प्रश्नहरूको सही उत्तरमा ठीक चिह्न (✓) लगाउनुहोस् (MCQs):</span>
            </h3>
            <span class="text-xs bg-purple-50 text-purple-700 border border-purple-200 font-bold px-2.5 py-0.5 rounded-full">पाठ्यपुस्तक पृष्ठ ४६</span>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            {"".join(mcq_html_cards)}
          </div>
        </div>
      </div>

      <!-- ================= 2. REASONS ================= -->
      <div class="c9u4-ex-card" data-cat="reason">
        <div class="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm space-y-4">
          <div class="flex items-center justify-between border-b border-slate-100 pb-3">
            <h3 class="font-black text-slate-900 text-base flex items-center gap-2">
              <span class="w-7 h-7 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center text-xs font-black">२</span>
              <span>कारण दिनुहोस् (Give reasons):</span>
            </h3>
            <span class="text-xs bg-amber-50 text-amber-700 border border-amber-200 font-bold px-2.5 py-0.5 rounded-full">कारण खुलाउने (पृष्ठ ४६)</span>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            {"".join(reason_html_cards)}
          </div>
        </div>
      </div>

      <!-- ================= 3. DIFFERENCES ================= -->
      <div class="c9u4-ex-card" data-cat="diff">
        <div class="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm space-y-4">
          <div class="flex items-center justify-between border-b border-slate-100 pb-3">
            <h3 class="font-black text-slate-900 text-base flex items-center gap-2">
              <span class="w-7 h-7 rounded-xl bg-purple-100 text-purple-700 flex items-center justify-center text-xs font-black">३</span>
              <span>फरक छुट्याउनुहोस् (Distinguish between):</span>
            </h3>
            <span class="text-xs bg-purple-50 text-purple-700 border border-purple-200 font-bold px-2.5 py-0.5 rounded-full">तुलनात्मक तालिका (पृष्ठ ४६-४७)</span>
          </div>
          <div class="space-y-4">
            {"".join(diff_html_cards)}
          </div>
        </div>
      </div>

      <!-- ================= 4. DETAILED Q&A ================= -->
      <div class="c9u4-ex-card" data-cat="qa">
        <div class="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm space-y-4">
          <div class="flex items-center justify-between border-b border-slate-100 pb-3">
            <h3 class="font-black text-slate-900 text-base flex items-center gap-2">
              <span class="w-7 h-7 rounded-xl bg-blue-100 text-blue-700 flex items-center justify-center text-xs font-black">४</span>
              <span>विस्तृत प्रश्नोत्तर (Detailed Q&A - प्रश्न क देखि त):</span>
            </h3>
            <span class="text-xs bg-blue-50 text-blue-700 border border-blue-200 font-bold px-2.5 py-0.5 rounded-full">पाठ्यपुस्तक पृष्ठ ४७-४८</span>
          </div>
          <div class="space-y-4">
            {"".join(qa_html_cards)}
          </div>
        </div>
      </div>

      <!-- ================= 5. PRACTICAL PROJECTS ================= -->
      <div class="c9u4-ex-card" data-cat="project">
        <div class="bg-white border border-slate-200 rounded-3xl p-6 shadow-sm space-y-4">
          <div class="flex items-center justify-between border-b border-slate-100 pb-3">
            <h3 class="font-black text-slate-900 text-base flex items-center gap-2">
              <span class="w-7 h-7 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center text-xs font-black">५</span>
              <span>पाठ्यपुस्तक परियोजना कार्यहरू (Practical Projects):</span>
            </h3>
            <span class="text-xs bg-emerald-50 text-emerald-700 border border-emerald-200 font-bold px-2.5 py-0.5 rounded-full">प्रयोगात्मक ३ कार्यहरू</span>
          </div>
          <div class="space-y-4">
            {"".join(proj_html_cards)}
          </div>
        </div>
      </div>

    </div>
  </div>
'''

# =========================================================================
# TAB 3: 16 TIERED MODEL QUESTIONS
# =========================================================================
notes_parts = re.split(r'\n###\s+', notes_md)
tier_k_raw = [p for p in notes_parts if "समूह 'क'" in p][0]
tier_u_raw = [p for p in notes_parts if "समूह 'ख'" in p][0]
tier_ha_raw = [p for p in notes_parts if "समूह 'ग'" in p][0]

def parse_tier_group(raw_group, tier_code, badge_bg, badge_txt, tier_label, weight):
    items = re.split(r'\n####\s+', raw_group)[1:]
    cards = []
    for item in items:
        lines = item.strip().split('\n')
        q_title = clean_inline_md(lines[0])
        body_p = []
        for l in lines[1:]:
            l_str = clean_inline_md(l.strip())
            if l_str:
                if l_str.startswith('- **नमुना उत्तर:**') or l_str.startswith('- **उत्तर:**') or l_str.startswith('**उत्तर:**'):
                    body_p.append(f'<strong class="text-slate-900 block pt-1">{l_str[2:]}</strong>')
                elif l_str.startswith('- ') or l_str.startswith('• '):
                    body_p.append(f'<p class="pt-0.5">{l_str[2:]}</p>')
                elif l_str.startswith('1. ') or l_str.startswith('२. ') or l_str.startswith('३. ') or l_str.startswith('४. ') or l_str.startswith('१. '):
                    body_p.append(f'<p class="pt-1">{l_str}</p>')
                else:
                    body_p.append(f'<p>{l_str}</p>')
        body_html = "".join(body_p)
        cards.append(f'''
      <div class="c9u4-tier-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-2" data-tier="{tier_code}">
        <div class="flex items-center justify-between">
          <span class="text-xs font-black px-2.5 py-0.5 rounded-full {badge_bg} {badge_txt}">{tier_label}</span>
          <span class="text-xs text-slate-400 font-mono">अंकभार: {weight}</span>
        </div>
        <h4 class="text-sm font-bold text-slate-900">{q_title}</h4>
        <div class="text-xs text-slate-700 bg-slate-50 p-3.5 rounded-2xl border border-slate-100 leading-relaxed space-y-1.5">
          {body_html}
        </div>
      </div>
        ''')
    return cards

k_cards = parse_tier_group(tier_k_raw, 'k', 'bg-blue-100', 'text-blue-800', "ज्ञानात्मक (Knowledge)", '१')
u_cards = parse_tier_group(tier_u_raw, 'u', 'bg-emerald-100', 'text-emerald-800', "बोधात्मक (Understanding)", '२')
ha_cards = parse_tier_group(tier_ha_raw, 'ha', 'bg-purple-100', 'text-purple-800', "उच्च दक्षता (Higher Ability)", '४')

tab3_html = f'''  <!-- ================= TAB 3: 16 TIERED MODEL QUESTIONS ================= -->
  <div id="c9u4-view-tiers" class="hidden space-y-6">
    <!-- Tier Filter Bar -->
    <div class="flex items-center justify-between border-b border-slate-200 pb-3 flex-wrap gap-2">
      <div class="text-xs font-bold text-slate-500">
        तहगत वर्गीकरण अनुसार प्रश्नहरू छान्नुहोस्:
      </div>
      <div class="flex flex-wrap gap-1.5">
        <button onclick="filterC9U4Tiers('all')" id="c9u4-tierbtn-all" class="px-3 py-1.5 rounded-xl text-xs font-black transition bg-purple-600 text-white shadow-sm cursor-pointer whitespace-nowrap">
          सबै १६ प्रश्नहरू
        </button>
        <button onclick="filterC9U4Tiers('k')" id="c9u4-tierbtn-k" class="px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap">
          समूह 'क': ज्ञानात्मक (५ प्रश्न)
        </button>
        <button onclick="filterC9U4Tiers('u')" id="c9u4-tierbtn-u" class="px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap">
          समूह 'ख': बोधात्मक (६ प्रश्न)
        </button>
        <button onclick="filterC9U4Tiers('ha')" id="c9u4-tierbtn-ha" class="px-3 py-1.5 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap">
          समूह 'ग': उच्च दक्षता (५ प्रश्न)
        </button>
      </div>
    </div>

    <!-- Tiered Questions Container -->
    <div class="space-y-4">
      {"".join(k_cards)}
      {"".join(u_cards)}
      {"".join(ha_cards)}
    </div>
  </div>
'''

# =========================================================================
# TAB 4: SELF-ASSESSMENT QUIZ
# =========================================================================
tab4_html = """  <!-- ================= TAB 4: SELF-ASSESSMENT QUIZ ================= -->
  <div id="c9u4-view-quiz" class="hidden space-y-6">
    <!-- Quiz Header Banner -->
    <div class="bg-gradient-to-r from-purple-600 to-indigo-700 rounded-3xl p-6 text-white shadow-md flex flex-wrap items-center justify-between gap-4">
      <div>
        <span class="text-xs font-bold uppercase tracking-wider bg-white/20 px-3 py-1 rounded-full">
          इन्टरएक्टिभ वस्तुगत परीक्षा
        </span>
        <h3 class="text-2xl font-black mt-2">एकाइ ४: क्रम विकास (Evolution) - स्वमूल्याङ्कन क्विज</h3>
        <p class="text-xs md:text-sm text-purple-100 mt-1">
          १० ओटा बहुवैकल्पिक प्रश्नहरूको उत्तर दिनुहोस् र आफ्नो प्राप्ताङ्क तुरुन्त जाँच्नुहोस्।
        </p>
      </div>

      <div class="flex items-center gap-4">
        <div class="bg-white/10 backdrop-blur-md border border-white/20 px-5 py-3 rounded-2xl text-center">
          <span class="text-xs text-purple-200 block font-semibold">तपाईंको प्राप्ताङ्क</span>
          <span id="c9u4-quiz-score-badge" class="text-2xl font-black text-white">० / १०</span>
        </div>
        <button onclick="resetC9U4Quiz()" class="px-4 py-2.5 rounded-xl bg-white/20 hover:bg-white/30 text-white text-xs font-bold transition cursor-pointer">
          पुनः सुरु गर्नुहोस्
        </button>
      </div>
    </div>

    <!-- Quiz Question Cards Container -->
    <div id="c9u4-quiz-container" class="space-y-4">
      <!-- Populated dynamically by JS -->
    </div>
  </div>
</div>
<!-- ================= END CLASS 9 UNIT 4 CONTAINER ================= -->
"""

full_html = tab1_html + tab2_html + tab3_html + tab4_html

# Check for double virama
assert '\u094d\u094d' not in full_html, "Double virama detected in full_html!"

html_path = "scratch/c9u4_html.html"
with open(html_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Successfully generated {html_path} ({len(full_html)} bytes, {len(full_html.splitlines())} lines).")
