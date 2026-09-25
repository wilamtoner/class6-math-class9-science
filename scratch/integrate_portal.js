const fs = require('fs');

let indexHtml = fs.readFileSync('index.html', 'utf8');

// 1. Upgrade Header with Grade Switcher
const oldHeaderLogoAndTitle = `<div class="flex items-center space-x-3">
        <div class="w-11 h-11 rounded-2xl bg-white/20 backdrop-blur-md flex items-center justify-center font-black text-2xl shadow-inner border border-white/30">६</div>
        <div>
          <h1 class="text-xl md:text-2xl font-black tracking-tight">कक्षा ६ गणित — डिजिटल गुरु</h1>
          <p class="text-xs text-blue-200">नेपाल सरकार, पाठ्यक्रम विकास केन्द्र (CDC) को नयाँ पाठ्यक्रममा आधारित पूर्ण अध्ययन तथा समाधान पोर्टल</p>
        </div>
      </div>`;

const newHeaderLogoAndTitle = `<div class="flex flex-wrap items-center gap-4">
        <div class="flex items-center space-x-3">
          <div id="portal-grade-badge" class="w-11 h-11 rounded-2xl bg-white/20 backdrop-blur-md flex items-center justify-center font-black text-2xl shadow-inner border border-white/30">६</div>
          <div>
            <h1 id="portal-title" class="text-xl md:text-2xl font-black tracking-tight">कक्षा ६ गणित — डिजिटल गुरु</h1>
            <p id="portal-subtitle" class="text-xs text-blue-200">नेपाल सरकार, पाठ्यक्रम विकास केन्द्र (CDC) को नयाँ पाठ्यक्रममा आधारित पूर्ण अध्ययन तथा समाधान पोर्टल</p>
          </div>
        </div>

        <!-- Grade / Subject Switcher Pills -->
        <div class="flex items-center p-1 bg-black/25 backdrop-blur-md rounded-2xl border border-white/20 shadow-inner">
          <button id="btn-grade-6" onclick="selectGrade(6)" class="px-3.5 py-1.5 rounded-xl text-xs font-black transition flex items-center gap-1.5 bg-white text-blue-900 shadow-sm cursor-pointer">
            <span>📐 कक्षा ६ : गणित</span>
          </button>
          <button id="btn-grade-9" onclick="selectGrade(9)" class="px-3.5 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 text-white/90 hover:text-white hover:bg-white/10 cursor-pointer">
            <span>🔬 कक्षा ९ : विज्ञान तथा प्रविधि</span>
          </button>
        </div>
      </div>`;

if (!indexHtml.includes(oldHeaderLogoAndTitle)) {
  console.error("Could not find oldHeaderLogoAndTitle");
  process.exit(1);
}
indexHtml = indexHtml.replace(oldHeaderLogoAndTitle, newHeaderLogoAndTitle);
console.log("1. Upgraded header with Grade Switcher.");

// 2. Update Sidebar heading and badges, and insert Class 9 Sidebar list
const oldSidebarHead = `<div class="mb-3 flex items-center justify-between">
        <h2 class="text-xs font-bold text-slate-500 uppercase tracking-wider">पाठ सूची (Chapters)</h2>
        <span class="text-xs bg-blue-100 text-blue-800 font-black px-2.5 py-0.5 rounded-full">२० पाठहरू</span>
      </div>`;

const newSidebarHead = `<div class="mb-3 flex items-center justify-between">
        <h2 id="sidebar-list-heading" class="text-xs font-bold text-slate-500 uppercase tracking-wider">पाठ सूची (गणित)</h2>
        <span id="sidebar-count-badge" class="text-xs bg-blue-100 text-blue-800 font-black px-2.5 py-0.5 rounded-full">२० पाठहरू</span>
      </div>`;

indexHtml = indexHtml.replace(oldSidebarHead, newSidebarHead);

const c9SidebarHtml = fs.readFileSync('scratch/c9_sidebar.html', 'utf8');

// Insert c9SidebarHtml right after chapter-list closing tag
const chapterListClose = `      </div>\n    </aside>`;
if (!indexHtml.includes(chapterListClose)) {
  console.error("Could not find chapterListClose");
  process.exit(1);
}
indexHtml = indexHtml.replace(chapterListClose, `      </div>\n${c9SidebarHtml}\n    </aside>`);
console.log("2. Inserted Class 9 Sidebar list.");

// 3. Insert Grade 9 Container with Unit 1 view and placeholder
const c9View1 = fs.readFileSync('scratch/c9u1_view.html', 'utf8');
const grade9ContainerHtml = `
    <!-- ================= GRADE 9 CONTAINER ================= -->
    <div id="grade9-container" class="hidden flex-1 min-w-0 flex flex-col">
      ${c9View1}

      <!-- Placeholder View for Units 2 to 19 -->
      <div id="c9-placeholder-view" class="hidden flex-1 min-w-0 flex flex-col items-center justify-center p-8 bg-slate-50 border border-slate-200 rounded-3xl text-center space-y-4 my-auto">
        <div class="w-16 h-16 rounded-3xl bg-cyan-100 text-cyan-700 flex items-center justify-center text-3xl font-bold">
          🔬
        </div>
        <div>
          <h3 id="c9-placeholder-title" class="text-xl font-black text-slate-800">एकाइ २: सजीवहरूको वर्गीकरण</h3>
          <p id="c9-placeholder-desc" class="text-xs md:text-sm text-slate-500 mt-1 max-w-md">यस एकाइको सम्पूर्ण अध्ययन सामग्री तथा अभ्यास समाधान तयारीमा छ। हाल एकाइ १: वैज्ञानिक अध्ययन पूर्ण रूपमा तयार छ।</p>
        </div>
        <button onclick="switchGrade9Unit(1)" class="px-5 py-2.5 bg-cyan-600 hover:bg-cyan-500 text-white font-bold text-xs rounded-xl shadow-md transition cursor-pointer">
          ← एकाइ १: वैज्ञानिक अध्ययन खोल्नुहोस्
        </button>
      </div>
    </div>
`;

// Insert right after Chapter 20 end marker
const ch20EndMarker = `      <!-- ================= END CHAPTER 20 ================= -->`;
if (!indexHtml.includes(ch20EndMarker)) {
  console.error("Could not find ch20EndMarker");
  process.exit(1);
}
indexHtml = indexHtml.replace(ch20EndMarker, `${ch20EndMarker}\n\n${grade9ContainerHtml}`);
console.log("3. Inserted Grade 9 container and Unit 1 view.");

// 4. Append Class 9 Script and multi-grade controllers
const c9Script = fs.readFileSync('scratch/c9u1_script.js', 'utf8');

const multiGradeScript = `
// ================= MULTI-GRADE CONTROLLER =================
let currentGrade = 6;
let activeChapter6 = 1;
let activeUnit9 = 1;

function selectGrade(grade) {
  currentGrade = grade;
  try { localStorage.setItem('digital_guru_grade', grade); } catch(e) {}

  const btn6 = document.getElementById('btn-grade-6');
  const btn9 = document.getElementById('btn-grade-9');
  const badge = document.getElementById('portal-grade-badge');
  const title = document.getElementById('portal-title');
  const subtitle = document.getElementById('portal-subtitle');
  const sideHeading = document.getElementById('sidebar-list-heading');
  const sideBadge = document.getElementById('sidebar-count-badge');
  const list6 = document.getElementById('chapter-list');
  const list9 = document.getElementById('unit-list-grade9');
  const grade9Container = document.getElementById('grade9-container');

  if (grade === 6) {
    if (btn6) btn6.className = 'px-3.5 py-1.5 rounded-xl text-xs font-black transition flex items-center gap-1.5 bg-white text-blue-900 shadow-sm cursor-pointer';
    if (btn9) btn9.className = 'px-3.5 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 text-white/90 hover:text-white hover:bg-white/10 cursor-pointer';
    if (badge) badge.textContent = '६';
    if (title) title.textContent = 'कक्षा ६ गणित — डिजिटल गुरु';
    if (subtitle) subtitle.textContent = 'नेपाल सरकार, पाठ्यक्रम विकास केन्द्र (CDC) को नयाँ पाठ्यक्रममा आधारित पूर्ण अध्ययन तथा समाधान पोर्टल';
    if (sideHeading) sideHeading.textContent = 'पाठ सूची (गणित)';
    if (sideBadge) { sideBadge.textContent = '२० पाठहरू'; sideBadge.className = 'text-xs bg-blue-100 text-blue-800 font-black px-2.5 py-0.5 rounded-full'; }
    if (list6) list6.classList.remove('hidden');
    if (list9) list9.classList.add('hidden');
    if (grade9Container) grade9Container.classList.add('hidden');
    switchChapter(activeChapter6);
  } else {
    if (btn6) btn6.className = 'px-3.5 py-1.5 rounded-xl text-xs font-bold transition flex items-center gap-1.5 text-white/90 hover:text-white hover:bg-white/10 cursor-pointer';
    if (btn9) btn9.className = 'px-3.5 py-1.5 rounded-xl text-xs font-black transition flex items-center gap-1.5 bg-white text-cyan-900 shadow-sm cursor-pointer';
    if (badge) badge.textContent = '९';
    if (title) title.textContent = 'कक्षा ९ विज्ञान तथा प्रविधि — डिजिटल गुरु';
    if (subtitle) subtitle.textContent = 'नेपाल सरकार, पाठ्यक्रम विकास केन्द्र (CDC) को अनिवार्य विज्ञान तथा प्रविधि पूर्ण अध्ययन तथा समाधान पोर्टल';
    if (sideHeading) sideHeading.textContent = 'एकाइ सूची (विज्ञान)';
    if (sideBadge) { sideBadge.textContent = '१९ एकाइहरू'; sideBadge.className = 'text-xs bg-cyan-100 text-cyan-800 font-black px-2.5 py-0.5 rounded-full'; }
    if (list6) list6.classList.add('hidden');
    if (list9) list9.classList.remove('hidden');

    // Hide all Class 6 views
    for (let i = 1; i <= 20; i++) {
      const v = document.getElementById('chapter-view-' + i);
      if (v) v.classList.add('hidden');
    }
    if (grade9Container) grade9Container.classList.remove('hidden');
    switchGrade9Unit(activeUnit9);
  }
}

function switchGrade9Unit(unitNum) {
  activeUnit9 = unitNum;
  for (let u = 1; u <= 19; u++) {
    const btn = document.getElementById('side-c9-' + u);
    if (btn) {
      if (u === unitNum) {
        btn.className = 'w-full text-left px-3.5 py-2.5 rounded-xl transition flex items-center justify-between text-xs md:text-sm bg-cyan-600 text-white font-bold shadow-sm';
      } else {
        btn.className = 'w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700 font-medium';
      }
    }
  }

  const v1 = document.getElementById('c9-view-1');
  const vPlaceholder = document.getElementById('c9-placeholder-view');

  if (unitNum === 1) {
    if (v1) v1.classList.remove('hidden');
    if (vPlaceholder) vPlaceholder.classList.add('hidden');
    setTabC9U1('concepts');
    calculateScientificNotation();
    selectC9U1Instrument('ruler');
  } else {
    if (v1) v1.classList.add('hidden');
    if (vPlaceholder) {
      vPlaceholder.classList.remove('hidden');
      const pTitle = document.getElementById('c9-placeholder-title');
      const btn = document.getElementById('side-c9-' + unitNum);
      if (pTitle && btn) {
        pTitle.textContent = btn.querySelector('.truncate div:first-child')?.textContent || ('एकाइ ' + unitNum);
      }
    }
  }

  const url = new URL(window.location);
  url.searchParams.set('grade', '9');
  url.searchParams.set('unit', unitNum);
  url.searchParams.delete('ch');
  try { window.history.replaceState({}, '', url); } catch(e) {}
}

${c9Script}
`;

// Insert multiGradeScript right before const urlParams = new URLSearchParams
const routerInitMarker = `const urlParams = new URLSearchParams(window.location.search);`;
if (!indexHtml.includes(routerInitMarker)) {
  console.error("Could not find routerInitMarker");
  process.exit(1);
}

// Update router initialization to handle grade parameter
const updatedRouterInit = `
${multiGradeScript}

  const urlParams = new URLSearchParams(window.location.search);
  const gradeParam = urlParams.get('grade');
  const unitParam = urlParams.get('unit');
  const activeChParam = urlParams.get('ch');

  if (gradeParam === '9') {
    selectGrade(9);
    if (unitParam) switchGrade9Unit(parseInt(unitParam, 10));
  } else if (activeChParam) {
    selectGrade(6);
    switchChapter(parseInt(activeChParam, 10));
  } else {
    let savedG = 6;
    try { savedG = localStorage.getItem('digital_guru_grade') === '9' ? 9 : 6; } catch(e) {}
    if (savedG === 9) {
      selectGrade(9);
    } else {
      selectGrade(6);
    }
  }
`;

indexHtml = indexHtml.replace(routerInitMarker, updatedRouterInit);
console.log("4. Appended multi-grade scripts and router.");

// Update search input to filter active list
const oldSearchInputListener = `const searchInput = document.getElementById('search-input');
  if (searchInput) {
    searchInput.addEventListener('input', function(e) {
      const q = e.target.value.toLowerCase().trim();
      for (let i = 1; i <= 20; i++) {
        const btn = document.getElementById('side-ch-' + i);
        if (btn) {
          const match = btn.innerText.toLowerCase().includes(q);
          btn.style.display = match ? '' : 'none';
        }
      }
    });
  }`;

const newSearchInputListener = `const searchInput = document.getElementById('search-input');
  if (searchInput) {
    searchInput.addEventListener('input', function(e) {
      const q = e.target.value.toLowerCase().trim();
      if (currentGrade === 6) {
        for (let i = 1; i <= 20; i++) {
          const btn = document.getElementById('side-ch-' + i);
          if (btn) {
            const match = btn.innerText.toLowerCase().includes(q);
            btn.style.display = match ? '' : 'none';
          }
        }
      } else {
        for (let u = 1; u <= 19; u++) {
          const btn = document.getElementById('side-c9-' + u);
          if (btn) {
            const match = btn.innerText.toLowerCase().includes(q);
            btn.style.display = match ? '' : 'none';
          }
        }
      }
    });
  }`;

if (indexHtml.includes(oldSearchInputListener)) {
  indexHtml = indexHtml.replace(oldSearchInputListener, newSearchInputListener);
  console.log("5. Updated search input filter for multi-grade lists.");
}

// 6. Update footer text to reflect multi-grade
indexHtml = indexHtml.replace('कक्षा ६ गणित डिजिटल गुरु | नेपाल सरकार पाठ्यक्रम विकास केन्द्र (CDC) नयाँ पाठ्यक्रममा आधारित', 'नेपाल डिजिटल विद्यालय (कक्षा ६ गणित र कक्षा ९ विज्ञान तथा प्रविधि) | नेपाल सरकार पाठ्यक्रम विकास केन्द्र (CDC) नयाँ पाठ्यक्रममा आधारित');

fs.writeFileSync('index.html', indexHtml);
console.log("Successfully integrated into index.html! New size:", indexHtml.length);
