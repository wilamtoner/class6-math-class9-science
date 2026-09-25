const fs = require('fs');

const units = [
  { n: 1, title: 'एकाइ १: वैज्ञानिक अध्ययन', sub: 'Scientific Study', p: 'पृष्ठ १-१६' },
  { n: 2, title: 'एकाइ २: सजीवहरूको वर्गीकरण', sub: 'Classification', p: 'पृष्ठ १७-२६' },
  { n: 3, title: 'एकाइ ३: च्याउ', sub: 'Fungi / Mushroom', p: 'पृष्ठ २७-३५' },
  { n: 4, title: 'एकाइ ४: क्रम विकास', sub: 'Evolution', p: 'पृष्ठ ३६-४८' },
  { n: 5, title: 'एकाइ ५: शारीरिक संरचना र जीवन प्रक्रिया', sub: 'Anatomy & Life', p: 'पृष्ठ ४९-७९' },
  { n: 6, title: 'एकाइ ६: प्रकृति र वातावरण', sub: 'Environment', p: 'पृष्ठ ८०-९६' },
  { n: 7, title: 'एकाइ ७: बल र चाल', sub: 'Force & Motion', p: 'पृष्ठ ९७-१२६' },
  { n: 8, title: 'एकाइ ८: सरल यन्त्र', sub: 'Simple Machines', p: 'पृष्ठ १२७-१४०' },
  { n: 9, title: 'एकाइ ९: ऊर्जा', sub: 'Energy', p: 'पृष्ठ १४१-१५५' },
  { n: 10, title: 'एकाइ १०: तरङ्ग', sub: 'Wave', p: 'पृष्ठ १५६-१७२' },
  { n: 11, title: 'एकाइ ११: विद्युत्', sub: 'Electricity', p: 'पृष्ठ १७३-१९३' },
  { n: 12, title: 'एकाइ १२: ब्रह्माण्ड', sub: 'Universe', p: 'पृष्ठ १९४-२०५' },
  { n: 13, title: 'एकाइ १३: सूचना तथा सञ्चार प्रविधि', sub: 'ICT', p: 'पृष्ठ २०६-२२५' },
  { n: 14, title: 'एकाइ १४: परमाणु संरचना र रासायनिक बन्ड', sub: 'Atomic & Bonding', p: 'पृष्ठ २२६-२४६' },
  { n: 15, title: 'एकाइ १५: रासायनिक प्रतिक्रिया', sub: 'Chemical Reactions', p: 'पृष्ठ २४७-२५६' },
  { n: 16, title: 'एकाइ १६: केही ग्यासहरू', sub: 'Some Gases', p: 'पृष्ठ २५७-२७१' },
  { n: 17, title: 'एकाइ १७: धातु र अधातु', sub: 'Metals & Non-metals', p: 'पृष्ठ २७२-२८२' },
  { n: 18, title: 'एकाइ १८: कार्बन र यसका यौगिकहरू', sub: 'Carbon Compounds', p: 'पृष्ठ २८३-२९१' },
  { n: 19, title: 'एकाइ १९: कृषि क्षेत्रमा प्रयोग हुने पदार्थहरू', sub: 'Agriculture', p: 'पृष्ठ २९२-३०६' }
];

const html = `
<div id="unit-list-grade9" class="space-y-1.5 max-h-[72vh] overflow-y-auto pr-1 text-sm font-medium hidden">
${units.map((u, i) => `
  <button id="side-c9-${u.n}" onclick="switchGrade9Unit(${u.n})" class="w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm ${u.n === 1 ? 'bg-cyan-600 text-white font-bold shadow-sm' : 'hover:bg-slate-100 text-slate-700 font-medium'}">
    <div class="truncate mr-2">
      <div class="truncate">${u.title}</div>
      <div class="text-[10px] ${u.n === 1 ? 'text-cyan-100' : 'text-slate-400'}">${u.sub}</div>
    </div>
    <span class="text-[10px] shrink-0 ${u.n === 1 ? 'bg-cyan-700/60 px-2 py-0.5 rounded-full text-white' : 'opacity-75'}">${u.p}</span>
  </button>
`).join('')}
</div>
`;

fs.writeFileSync('scratch/c9_sidebar.html', html);
console.log('Created scratch/c9_sidebar.html');
