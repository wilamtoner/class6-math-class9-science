# -*- coding: utf-8 -*-
"""
Generator for scratch/c9u7_js.js
Class 9 Science Unit 7: Force and Motion (बल र चाल)
"""
import json

output_path = "scratch/c9u7_js.js"

print("Creating " + output_path + " ...")

js_parts = []

# Part 1: Audio Synthesizer & Global State
js_parts.append("""// =========================================================================
// CLASS 9 SCIENCE: UNIT 7 - FORCE AND MOTION (बल र चाल)
// Interactive 3-Mode Physics Lab, Graphs Studio, Newton's Laws & Quiz Engine
// =========================================================================

let activeC9U7Tab = 'concepts';
let activeC9U7LabMode = 'kinematics';

// Mode 1: Kinematics Simulator State
let c9u7U = 0;
let c9u7A = 1.5;
let c9u7T = 30;
let c9u7AnimTimer = null;
let c9u7AnimProgress = 1.0;
let c9u7IsPlayingAnim = false;

// Mode 2: Motion Graphs Studio State
let c9u7ActiveGraph = 'st_graph';
let c9u7ActiveSection = 'all';
let c9u7RaceTimer = null;
let c9u7RaceProgress = 0;
let c9u7IsRacing = false;

// Mode 3: Newton's Laws State
let c9u7ActiveLaw = 1;
let c9u7CoinFlicked = false;
let c9u7BusBraking = false;
let c9u7Mass = 50;
let c9u7Force = 150;
let c9u7RocketFired = false;
let c9u7SpringWeight = 3;

// Tab 2 & 3 Filter States
let c9u7ActiveExFilter = 'all';
let c9u7ActiveTierFilter = 'all';

// Tab 4 Quiz State
let c9u7QuizAnswers = {};

// -------------------------------------------------------------------------
// Web Audio Synthesizer for Unit 7
// -------------------------------------------------------------------------
function playAudioC9U7(type) {
  try {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!AudioContext) return;
    const ctx = new AudioContext();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain);
    gain.connect(ctx.destination);
    const now = ctx.currentTime;

    if (type === 'click') {
      osc.type = 'sine';
      osc.frequency.setValueAtTime(600, now);
      gain.gain.setValueAtTime(0.08, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);
      osc.start(now);
      osc.stop(now + 0.08);
    } else if (type === 'engine') {
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(120, now);
      osc.frequency.exponentialRampToValueAtTime(280, now + 0.35);
      gain.gain.setValueAtTime(0.12, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
      osc.start(now);
      osc.stop(now + 0.35);
    } else if (type === 'brake') {
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(450, now);
      osc.frequency.exponentialRampToValueAtTime(100, now + 0.4);
      gain.gain.setValueAtTime(0.15, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.4);
      osc.start(now);
      osc.stop(now + 0.4);
    } else if (type === 'flick') {
      osc.type = 'sine';
      osc.frequency.setValueAtTime(300, now);
      osc.frequency.exponentialRampToValueAtTime(800, now + 0.12);
      gain.gain.setValueAtTime(0.2, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.12);
      osc.start(now);
      osc.stop(now + 0.12);
    } else if (type === 'launch') {
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(150, now);
      osc.frequency.exponentialRampToValueAtTime(650, now + 0.6);
      gain.gain.setValueAtTime(0.18, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.6);
      osc.start(now);
      osc.stop(now + 0.6);
    } else if (type === 'correct') {
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(523.25, now);
      osc.frequency.setValueAtTime(659.25, now + 0.1);
      osc.frequency.setValueAtTime(783.99, now + 0.2);
      gain.gain.setValueAtTime(0.15, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
      osc.start(now);
      osc.stop(now + 0.35);
    } else if (type === 'wrong') {
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(220, now);
      osc.frequency.setValueAtTime(180, now + 0.12);
      gain.gain.setValueAtTime(0.15, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
      osc.start(now);
      osc.stop(now + 0.3);
    }
  } catch (e) {}
}

// -------------------------------------------------------------------------
// Tab Switcher (Concepts, Exercises, Tiers, Quiz)
// -------------------------------------------------------------------------
function setTabC9U7(tab) {
  activeC9U7Tab = tab;
  playAudioC9U7('click');
  const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
  tabs.forEach(t => {
    const view = document.getElementById(`c9u7-view-${t}`);
    const btn = document.getElementById(`c9u7-tab-${t}`);
    if (view) {
      if (t === tab) view.classList.remove('hidden');
      else view.classList.add('hidden');
    }
    if (btn) {
      if (t === tab) {
        btn.className = "px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer";
      } else {
        btn.className = "px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer";
      }
    }
  });

  if (tab === 'concepts') {
    renderCurrentC9U7Lab();
  } else if (tab === 'exercises') {
    renderC9U7Exercises();
  } else if (tab === 'tiers') {
    renderC9U7Tiers();
  } else if (tab === 'quiz') {
    renderC9U7Quiz();
  }
}

// -------------------------------------------------------------------------
// Lab Modes Switcher (Mode 1, Mode 2, Mode 3)
// -------------------------------------------------------------------------
function setLabModeC9U7(mode) {
  activeC9U7LabMode = mode;
  playAudioC9U7('click');
  const modes = ['kinematics', 'graphs', 'newton_laws'];
  modes.forEach(m => {
    const panel = document.getElementById(`c9u7-lab-mode-${m}`);
    const btn = document.getElementById(`c9u7-btn-mode-${m}`);
    if (panel) {
      if (m === mode) panel.classList.remove('hidden');
      else panel.classList.add('hidden');
    }
    if (btn) {
      if (m === mode) {
        btn.className = "flex-1 py-3 px-4 rounded-2xl bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-black text-xs md:text-sm shadow-md transition cursor-pointer";
      } else {
        btn.className = "flex-1 py-3 px-4 rounded-2xl bg-slate-800 text-slate-400 hover:text-white font-bold text-xs md:text-sm transition cursor-pointer";
      }
    }
  });
  renderCurrentC9U7Lab();
}

function renderCurrentC9U7Lab() {
  if (activeC9U7LabMode === 'kinematics') {
    updateKinematicsSimC9U7();
  } else if (activeC9U7LabMode === 'graphs') {
    renderMotionGraphSVGC9U7();
    updateGraphSectionDetailsC9U7();
  } else if (activeC9U7LabMode === 'newton_laws') {
    renderNewtonDemoSVGC9U7();
  }
}
""")

# Part 2: Mode 1 Kinematics Simulator
js_parts.append("""// =========================================================================
// MODE 1: KINEMATICS SIMULATOR (चाल समीकरण प्रयोगशाला)
// =========================================================================
function updateKinematicsSimC9U7() {
  const sliderU = document.getElementById('c9u7-slider-u');
  const sliderA = document.getElementById('c9u7-slider-a');
  const sliderT = document.getElementById('c9u7-slider-t');

  if (sliderU) c9u7U = parseFloat(sliderU.value);
  if (sliderA) c9u7A = parseFloat(sliderA.value);
  if (sliderT) c9u7T = parseFloat(sliderT.value);

  // Update slider badge labels
  const valU = document.getElementById('c9u7-val-u');
  const valA = document.getElementById('c9u7-val-a');
  const valT = document.getElementById('c9u7-val-t');

  if (valU) valU.textContent = `${c9u7U.toFixed(1)} m/s`;
  if (valA) valA.textContent = `${c9u7A >= 0 ? '+' : ''}${c9u7A.toFixed(1)} m/s²`;
  if (valT) valT.textContent = `${c9u7T.toFixed(0)} s`;

  // Calculate: v = u + at
  let v = c9u7U + c9u7A * c9u7T;
  if (v < 0) v = 0; // cannot reverse beyond stop in this simplified demo

  // Calculate: s = ut + 0.5 * a * t^2
  let s = c9u7U * c9u7T + 0.5 * c9u7A * (c9u7T * c9u7T);
  if (s < 0) s = 0;

  // Calculate: v^2 = u^2 + 2as
  let v2 = (c9u7U * c9u7U) + (2 * c9u7A * s);
  if (v2 < 0) v2 = 0;

  // Average velocity
  let vav = (c9u7U + v) / 2;

  // Update calculation cards
  const calcV = document.getElementById('c9u7-calc-v');
  const calcS = document.getElementById('c9u7-calc-s');
  const calcV2 = document.getElementById('c9u7-calc-v2');
  const calcVav = document.getElementById('c9u7-calc-vav');

  if (calcV) calcV.textContent = `${v.toFixed(1)} m/s`;
  if (calcS) calcS.textContent = `${s.toFixed(1)} m`;
  if (calcV2) calcV2.textContent = `${v2.toFixed(0)} m²/s²`;
  if (calcVav) calcVav.textContent = `${vav.toFixed(1)} m/s`;

  // Step explanation formula
  const stepSol = document.getElementById('c9u7-step-solution');
  if (stepSol) {
    stepSol.textContent = `s = (${c9u7U} × ${c9u7T}) + ½ × (${c9u7A}) × (${c9u7T})² = ${s.toFixed(1)} m`;
  }

  renderTrackSVGC9U7(s, v, c9u7A, c9u7AnimProgress);
}

function applyKinematicsPresetC9U7(preset) {
  playAudioC9U7('click');
  const sliderU = document.getElementById('c9u7-slider-u');
  const sliderA = document.getElementById('c9u7-slider-a');
  const sliderT = document.getElementById('c9u7-slider-t');

  if (preset === 'airplane') {
    // Q5(क): u = 0, a = 1.5, t = 30 -> s = 675 m, v = 45 m/s
    if (sliderU) sliderU.value = 0;
    if (sliderA) sliderA.value = 1.5;
    if (sliderT) sliderT.value = 30;
  } else if (preset === 'bridge') {
    // Q5(ख): u = 0, a = 5 (scaled representation of g for 2s), t = 2 -> s = 19.6 m
    if (sliderU) sliderU.value = 0;
    if (sliderA) sliderA.value = 4.9;
    if (sliderT) sliderT.value = 2;
  } else if (preset === 'car_brake') {
    // Q5(घ): u = 20, a = -3.75, t = 4 -> s = 50 m, v = 5 m/s
    if (sliderU) sliderU.value = 20;
    if (sliderA) sliderA.value = -3.75;
    if (sliderT) sliderT.value = 4;
  }
  c9u7AnimProgress = 1.0;
  updateKinematicsSimC9U7();
}

function playKinematicsAnimationC9U7() {
  if (c9u7IsPlayingAnim) return;
  c9u7IsPlayingAnim = true;
  c9u7AnimProgress = 0;
  playAudioC9U7('engine');

  const btn = document.getElementById('c9u7-btn-anim-play');
  const status = document.getElementById('c9u7-track-status');
  if (btn) btn.innerHTML = "<span>⏳ चलिरहेको छ...</span>";
  if (status) status.textContent = "STATUS: ANIMATING MOTION";

  clearInterval(c9u7AnimTimer);
  const steps = 60;
  let currentStep = 0;

  c9u7AnimTimer = setInterval(() => {
    currentStep++;
    c9u7AnimProgress = currentStep / steps;

    // Fractional time
    const curT = c9u7T * c9u7AnimProgress;
    let curV = c9u7U + c9u7A * curT;
    if (curV < 0) curV = 0;
    let curS = c9u7U * curT + 0.5 * c9u7A * (curT * curT);
    if (curS < 0) curS = 0;

    renderTrackSVGC9U7(curS, curV, c9u7A, c9u7AnimProgress);

    if (currentStep >= steps) {
      clearInterval(c9u7AnimTimer);
      c9u7IsPlayingAnim = false;
      c9u7AnimProgress = 1.0;
      if (btn) btn.innerHTML = "<span>▶ पुनः चलाउनुहोस्</span>";
      if (status) status.textContent = "STATUS: REACHED DESTINATION";
      if (c9u7A < 0) playAudioC9U7('brake');
      else playAudioC9U7('correct');
      updateKinematicsSimC9U7();
    }
  }, 25);
}

function resetKinematicsSimC9U7() {
  clearInterval(c9u7AnimTimer);
  c9u7IsPlayingAnim = false;
  c9u7AnimProgress = 1.0;
  playAudioC9U7('click');

  const btn = document.getElementById('c9u7-btn-anim-play');
  const status = document.getElementById('c9u7-track-status');
  if (btn) btn.innerHTML = "<span>▶ सिमुलेशन चलाउनुहोस्</span>";
  if (status) status.textContent = "STATUS: RESET";

  updateKinematicsSimC9U7();
}

function renderTrackSVGC9U7(s, v, a, progress = 1.0) {
  const container = document.getElementById('c9u7-track-svg-wrap');
  if (!container) return;

  // Max track distance scaled to 700m
  const maxDistance = 700;
  const trackW = 600;
  const trackH = 110;
  const startX = 50;
  const endX = 550;
  const totalTrackPx = endX - startX;

  // Vehicle position
  const clampedS = Math.min(s, maxDistance);
  const vehicleX = startX + (clampedS / maxDistance) * totalTrackPx;

  const isPlane = (c9u7A > 0 && s > 200);

  let vehicleSvg = '';
  if (isPlane) {
    // Airplane SVG
    vehicleSvg = `
      <g transform="translate(${vehicleX - 25}, 38)">
        <!-- Airplane Fuselage -->
        <path d="M0,15 L35,15 L45,10 L50,15 L45,20 L35,15 Z" fill="#38bdf8" stroke="#0284c7" stroke-width="1.5"/>
        <path d="M15,15 L22,2 L27,2 L22,15 Z" fill="#0284c7"/>
        <path d="M15,15 L22,28 L27,28 L22,15 Z" fill="#0284c7"/>
        <circle cx="42" cy="14" r="2.5" fill="#f8fafc"/>
        <text x="25" y="-3" text-anchor="middle" font-size="9" font-family="monospace" fill="#38bdf8" font-weight="bold">${v.toFixed(0)} m/s</text>
      </g>
    `;
  } else {
    // Car SVG
    vehicleSvg = `
      <g transform="translate(${vehicleX - 22}, 46)">
        <!-- Car Body -->
        <rect x="0" y="8" width="44" height="14" rx="4" fill="#3b82f6"/>
        <path d="M8,8 L16,0 L30,0 L36,8 Z" fill="#60a5fa"/>
        <!-- Windows -->
        <rect x="17" y="2" width="11" height="5" rx="1" fill="#e0f2fe"/>
        <!-- Wheels -->
        <circle cx="10" cy="22" r="5" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.5"/>
        <circle cx="34" cy="22" r="5" fill="#0f172a" stroke="#cbd5e1" stroke-width="1.5"/>
        <circle cx="10" cy="22" r="2" fill="#94a3b8"/>
        <circle cx="34" cy="22" r="2" fill="#94a3b8"/>
        <!-- Speed tag -->
        <text x="22" y="-4" text-anchor="middle" font-size="9" font-family="monospace" fill="#60a5fa" font-weight="bold">${v.toFixed(0)} m/s</text>
      </g>
    `;
  }

  container.innerHTML = `
    <svg viewBox="0 0 ${trackW} ${trackH}" class="w-full h-auto max-h-[140px] drop-shadow-md select-none">
      <!-- Sky / Background -->
      <rect x="0" y="0" width="${trackW}" height="${trackH}" rx="16" fill="#020617"/>
      
      <!-- Asphalt Road Track -->
      <rect x="20" y="45" width="${trackW - 40}" height="32" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
      
      <!-- Dashed center lane -->
      <line x1="25" y1="61" x2="${trackW - 25}" y2="61" stroke="#f8fafc" stroke-width="2" stroke-dasharray="12,10" opacity="0.6"/>

      <!-- Distance Metric Ticks -->
      <g font-size="9" font-family="monospace" fill="#94a3b8" text-anchor="middle">
        <line x1="${startX}" y1="80" x2="${startX}" y2="88" stroke="#475569" stroke-width="1.5"/>
        <text x="${startX}" y="98">0m</text>

        <line x1="${startX + totalTrackPx * 0.25}" y1="80" x2="${startX + totalTrackPx * 0.25}" y2="88" stroke="#475569" stroke-width="1.5"/>
        <text x="${startX + totalTrackPx * 0.25}" y="98">175m</text>

        <line x1="${startX + totalTrackPx * 0.5}" y1="80" x2="${startX + totalTrackPx * 0.5}" y2="88" stroke="#475569" stroke-width="1.5"/>
        <text x="${startX + totalTrackPx * 0.5}" y="98">350m</text>

        <line x1="${startX + totalTrackPx * 0.75}" y1="80" x2="${startX + totalTrackPx * 0.75}" y2="88" stroke="#475569" stroke-width="1.5"/>
        <text x="${startX + totalTrackPx * 0.75}" y="98">525m</text>

        <line x1="${endX}" y1="80" x2="${endX}" y2="88" stroke="#475569" stroke-width="1.5"/>
        <text x="${endX}" y="98">700m</text>
      </g>

      <!-- Start and Finish Flags -->
      <g transform="translate(${startX - 4}, 26)">
        <line x1="0" y1="0" x2="0" y2="20" stroke="#94a3b8" stroke-width="1.5"/>
        <polygon points="0,0 10,4 0,8" fill="#10b981"/>
        <text x="-4" y="8" font-size="8" fill="#10b981" font-weight="bold" text-anchor="end">START</text>
      </g>
      <g transform="translate(${endX + 4}, 26)">
        <line x1="0" y1="0" x2="0" y2="20" stroke="#94a3b8" stroke-width="1.5"/>
        <polygon points="0,0 -10,4 0,8" fill="#ef4444"/>
        <text x="5" y="8" font-size="8" fill="#ef4444" font-weight="bold" text-anchor="start">FINISH</text>
      </g>

      <!-- Moving Vehicle -->
      ${vehicleSvg}

      <!-- Current Distance Marker Pointer -->
      <polygon points="${vehicleX},79 ${vehicleX - 4},85 ${vehicleX + 4},85" fill="#38bdf8"/>
    </svg>
  `;
}
""")

# Part 3: Mode 2 Motion Graphs Studio & Hare-Tortoise
js_parts.append("""// =========================================================================
// MODE 2: MOTION GRAPHS STUDIO & HARE-TORTOISE RACE
// =========================================================================
function setGraphTypeC9U7(type) {
  c9u7ActiveGraph = type;
  c9u7ActiveSection = 'all';
  playAudioC9U7('click');

  const btnSt = document.getElementById('c9u7-gbtn-st');
  const btnVt = document.getElementById('c9u7-gbtn-vt');
  const btnRace = document.getElementById('c9u7-gbtn-race');
  const raceCtrl = document.getElementById('c9u7-race-controls');

  if (btnSt) btnSt.className = type === 'st_graph' ? "px-3.5 py-1.5 rounded-xl bg-blue-600/30 border border-blue-500 text-blue-300 font-bold transition text-xs cursor-pointer" : "px-3.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 hover:text-white font-bold transition text-xs cursor-pointer";
  if (btnVt) btnVt.className = type === 'vt_graph' ? "px-3.5 py-1.5 rounded-xl bg-indigo-600/30 border border-indigo-500 text-indigo-300 font-bold transition text-xs cursor-pointer" : "px-3.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 hover:text-white font-bold transition text-xs cursor-pointer";
  if (btnRace) btnRace.className = type === 'hare_tortoise' ? "px-3.5 py-1.5 rounded-xl bg-emerald-600/30 border border-emerald-500 text-emerald-300 font-bold transition text-xs cursor-pointer" : "px-3.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 hover:text-white font-bold transition text-xs cursor-pointer";

  if (raceCtrl) {
    if (type === 'hare_tortoise') raceCtrl.classList.remove('hidden');
    else raceCtrl.classList.add('hidden');
  }

  const badge = document.getElementById('c9u7-graph-title-badge');
  if (badge) {
    if (type === 'st_graph') badge.textContent = "DISPLACEMENT-TIME GRAPH (स्थानान्तरण-समय ग्राफ: अभ्यास प्रश्न ४ घ)";
    else if (type === 'vt_graph') badge.textContent = "VELOCITY-TIME GRAPH (गति-समय ग्राफ: हिसाब प्रश्न ५ ङ)";
    else badge.textContent = "HARE & TORTOISE RACE GRAPH (खरायो र कछुवाको दौड कथा: प्रश्न ४ ङ)";
  }

  renderMotionGraphSVGC9U7();
  updateGraphSectionDetailsC9U7();
}

function selectGraphSectionC9U7(sec) {
  c9u7ActiveSection = sec;
  playAudioC9U7('click');
  renderMotionGraphSVGC9U7();
  updateGraphSectionDetailsC9U7();
}

function updateGraphSectionDetailsC9U7() {
  const secBadge = document.getElementById('c9u7-sec-badge');
  const secTitle = document.getElementById('c9u7-sec-title');
  const secNature = document.getElementById('c9u7-sec-nature');
  const secSlope = document.getElementById('c9u7-sec-slope');
  const secSlopeDesc = document.getElementById('c9u7-sec-slope-desc');
  const secArea = document.getElementById('c9u7-sec-area');
  const secAreaDesc = document.getElementById('c9u7-sec-area-desc');
  const secSummary = document.getElementById('c9u7-sec-summary');
  const secPills = document.getElementById('c9u7-sec-pills');

  if (c9u7ActiveGraph === 'st_graph') {
    // Q4(घ) Data: 0-4s, 4-6s, 6-8s, 8-14s
    const pills = [
      { id: 'all', label: 'समग्र (All)' },
      { id: '0_4', label: '०-४ s (समान गति)' },
      { id: '4_6', label: '४-६ s (स्थिर)' },
      { id: '6_8', label: '६-८ s (समान गति)' },
      { id: '8_14', label: '८-१४ s (फर्केको)' }
    ];

    if (secPills) {
      secPills.innerHTML = pills.map(p => `
        <button onclick="selectGraphSectionC9U7('${p.id}')" class="px-2.5 py-1 rounded-lg text-xs font-mono font-bold transition cursor-pointer ${c9u7ActiveSection === p.id ? 'bg-blue-600 text-white' : 'bg-slate-700 text-slate-300 hover:bg-slate-600'}">
          ${p.label}
        </button>
      `).join('');
    }

    if (c9u7ActiveSection === '0_4') {
      if (secBadge) secBadge.textContent = "खण्ड: ० देखि ४ सेकेन्ड";
      if (secTitle) secTitle.textContent = "समान गतिले अगाडि बढेको अवस्था";
      if (secNature) { secNature.textContent = "समान गति (Uniform Velocity)"; secNature.className = "text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 font-bold border border-emerald-500/30"; }
      if (secSlope) secSlope.textContent = "Slope = (8 - 0) / (4 - 0) = +2.0 m/s";
      if (secSlopeDesc) secSlopeDesc.textContent = "झुकाव धनात्मक र स्थिर छ; वस्तु समान २ m/s गतिले अगाडि बढ्छ।";
      if (secArea) secArea.textContent = "N/A (s-t ग्राफ मुनिको क्षेत्रफल अप्रयुक्त)";
      if (secAreaDesc) secAreaDesc.textContent = "स्थानान्तरण-समय ग्राफमा क्षेत्रफलको कुनै भौतिक अर्थ हुँदैन।";
      if (secSummary) secSummary.textContent = "सुरुको ४ सेकेन्डमा वस्तुले समान गतिले ८ मिटर दूरी पार गर्दछ।";
    } else if (c9u7ActiveSection === '4_6') {
      if (secBadge) secBadge.textContent = "खण्ड: ४ देखि ६ सेकेन्ड";
      if (secTitle) secTitle.textContent = "वस्तु पूर्ण स्थिर अवस्थामा";
      if (secNature) { secNature.textContent = "स्थिर (At Rest)"; secNature.className = "text-xs px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30"; }
      if (secSlope) secSlope.textContent = "Slope = (8 - 8) / (6 - 4) = 0.0 m/s";
      if (secSlopeDesc) secSlopeDesc.textContent = "झुकाव शून्य छ; रेखा समय अक्षसँग समानान्तर तेर्सो छ।";
      if (secArea) secArea.textContent = "N/A";
      if (secAreaDesc) secAreaDesc.textContent = "स-ट ग्राफमा क्षेत्रफल अर्थहीन छ।";
      if (secSummary) secSummary.textContent = "समय बित्दै गयो तर स्थानान्तरण ८ मिटरमै स्थिर रह्यो, अर्थात् वस्तु रोकिएको छ।";
    } else if (c9u7ActiveSection === '8_14') {
      if (secBadge) secBadge.textContent = "खण्ड: ८ देखि १४ सेकेन्ड";
      if (secTitle) secTitle.textContent = "फर्किरहेको चाल (ऋणात्मक झुकाव)";
      if (secNature) { secNature.textContent = "फर्केको चाल (Returning)"; secNature.className = "text-xs px-2.5 py-1 rounded-full bg-rose-500/20 text-rose-300 font-bold border border-rose-500/30"; }
      if (secSlope) secSlope.textContent = "Slope = (0 - 12) / (14 - 8) = -2.0 m/s";
      if (secSlopeDesc) secSlopeDesc.textContent = "झुकाव ऋणात्मक छ; वस्तु सुरुको प्रस्थान बिन्दुतर्फ फर्किरहेको छ।";
      if (secArea) secArea.textContent = "N/A";
      if (secAreaDesc) secAreaDesc.textContent = "स-ट ग्राफमा क्षेत्रफल प्रयोग हुँदैन।";
      if (secSummary) secSummary.textContent = "वस्तु १२ मिटरको उच्चतम बिन्दुबाट फर्केर १४ सेकेन्डमा मूलबिन्दु (० m) मै आइपुग्छ।";
    } else {
      if (secBadge) secBadge.textContent = "समग्र अवलोकन: ० देखि १४ सेकेन्ड";
      if (secTitle) secTitle.textContent = "पाठ्यपुस्तक अभ्यास प्रश्न ४ (घ) को तथ्याङ्क";
      if (secNature) { secNature.textContent = "मिश्रित चाल"; secNature.className = "text-xs px-2.5 py-1 rounded-full bg-blue-500/20 text-blue-300 font-bold border border-blue-500/30"; }
      if (secSlope) secSlope.textContent = "पहिलो ४ सेकेन्डको औसत गति = २.० m/s";
      if (secSlopeDesc) secSlopeDesc.textContent = "स-ट ग्राफको झुकावले गति वा वेग (v = Δs/Δt) दिन्छ।";
      if (secArea) secArea.textContent = "जम्मा समय: १४ सेकेन्ड, अधिकतम स्थानान्तरण: १२ मिटर";
      if (secAreaDesc) secAreaDesc.textContent = "माथिका बटनहरू थिचेर खण्डगत अध्ययन गर्नुहोस्।";
      if (secSummary) secSummary.textContent = "यस ग्राफमा वस्तु अगाडि बढ्छ (०-४s), रोकिन्छ (४-६s), पुनः अगाडि बढ्छ (६-८s) र अन्तमा फर्केर आफ्नै ठाउँमा आउँछ (८-१४s)।";
    }
  } else if (c9u7ActiveGraph === 'vt_graph') {
    // Q5(ङ) Bus Graph: OA (0-6s), AB (6-10s), CD (10-14s), DE (14-18s)
    const pills = [
      { id: 'all', label: 'समग्र (All)' },
      { id: 'oa', label: 'OA (०-६s समान प्रवेग)' },
      { id: 'ab', label: 'AB (६-१०s समान गति)' },
      { id: 'cd', label: 'CD (१०-१४s स्थानान्तरण ८०m)' },
      { id: 'de', label: 'DE (१४-१८s गतिह्रास)' }
    ];

    if (secPills) {
      secPills.innerHTML = pills.map(p => `
        <button onclick="selectGraphSectionC9U7('${p.id}')" class="px-2.5 py-1 rounded-lg text-xs font-mono font-bold transition cursor-pointer ${c9u7ActiveSection === p.id ? 'bg-indigo-600 text-white' : 'bg-slate-700 text-slate-300 hover:bg-slate-600'}">
          ${p.label}
        </button>
      `).join('');
    }

    if (c9u7ActiveSection === 'oa') {
      if (secBadge) secBadge.textContent = "खण्ड OA: ० देखि ६ सेकेन्ड";
      if (secTitle) secTitle.textContent = "समान प्रवेग (Uniform Acceleration)";
      if (secNature) { secNature.textContent = "समान प्रवेग (+3.33 m/s²)"; secNature.className = "text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 font-bold border border-emerald-500/30"; }
      if (secSlope) secSlope.textContent = "Slope = (20 - 0) / (6 - 0) = +3.33 m/s²";
      if (secSlopeDesc) secSlopeDesc.textContent = "झुकावले बसको समान प्रवेग (Uniform acceleration) जनाउँछ।";
      if (secArea) secArea.textContent = "Area = ½ × 6 × 20 = 60 m";
      if (secAreaDesc) secAreaDesc.textContent = "यस खण्डमा बसले ६० मिटर दूरी पार गर्दछ।";
      if (secSummary) secSummary.textContent = "स्थिर अवस्थाबाट सुरु भई बस ६ सेकेन्डमा २० m/s को तीव्र गतिमा पुग्छ।";
    } else if (c9u7ActiveSection === 'cd') {
      if (secBadge) secBadge.textContent = "खण्ड CD: १० देखि १४ सेकेन्ड (प्रश्न ५ ङ)";
      if (secTitle) secTitle.textContent = "समान गति तथा स्थानान्तरण हिसाब";
      if (secNature) { secNature.textContent = "समान गति (प्रवेग = ०)"; secNature.className = "text-xs px-2.5 py-1 rounded-full bg-blue-500/20 text-blue-300 font-bold border border-blue-500/30"; }
      if (secSlope) secSlope.textContent = "Slope = (20 - 20) / (14 - 10) = 0.0 m/s² (प्रवेग शून्य)";
      if (secSlopeDesc) secSlopeDesc.textContent = "तेर्सो रेखा भएकाले प्रवेग शून्य छ; गति २० m/s मा स्थिर छ।";
      if (secArea) secArea.textContent = "Area = 20 m/s × (14 - 10) s = 80 m (उत्तर: ८० मिटर पूर्व)";
      if (secAreaDesc) secAreaDesc.textContent = "आयाताकार भागको क्षेत्रफलले ठीक ८० मिटर स्थानान्तरण दिन्छ।";
      if (secSummary) secSummary.textContent = "पाठ्यपुस्तकको प्रश्न (ई) को उत्तर: बसले C बाट D मा पुग्दा पार गर्ने स्थानान्तरण ८० मिटर हुन्छ।";
    } else if (c9u7ActiveSection === 'de') {
      if (secBadge) secBadge.textContent = "खण्ड DE: १४ देखि १८ सेकेन्ड";
      if (secTitle) secTitle.textContent = "गतिह्रास वा मन्दता (Retardation)";
      if (secNature) { secNature.textContent = "मन्दता (-5.0 m/s²)"; secNature.className = "text-xs px-2.5 py-1 rounded-full bg-rose-500/20 text-rose-300 font-bold border border-rose-500/30"; }
      if (secSlope) secSlope.textContent = "Slope = (0 - 20) / (18 - 14) = -5.0 m/s²";
      if (secSlopeDesc) secSlopeDesc.textContent = "ऋणात्मक झुकावले ब्रेक लगाउँदा उत्पन्न मन्दता जनाउँछ।";
      if (secArea) secArea.textContent = "Area = ½ × 4 × 20 = 40 m";
      if (secAreaDesc) secAreaDesc.textContent = "रोकिनुअघि बसले ४० मिटर दूरी पार गर्दछ।";
      if (secSummary) secSummary.textContent = "बसले ब्रेक लगाई ४ सेकेन्डभित्र २० m/s बाट पूर्ण स्थिर अवस्था (० m/s) मा आउँछ।";
    } else {
      if (secBadge) secBadge.textContent = "समग्र गति-समय ग्राफ (Bus Motion)";
      if (secTitle) secTitle.textContent = "पाठ्यपुस्तक हिसाब प्रश्न ५ (ङ) को बस यात्रा";
      if (secNature) { secNature.textContent = "पूर्ण यात्रा (0-18 s)"; secNature.className = "text-xs px-2.5 py-1 rounded-full bg-indigo-500/20 text-indigo-300 font-bold border border-indigo-500/30"; }
      if (secSlope) secSlope.textContent = "Slope = Acceleration (a = Δv/Δt)";
      if (secSlopeDesc) secSlopeDesc.textContent = "झुकावले प्रवेग र रेखा मुनिको क्षेत्रफलले स्थानान्तरण दिन्छ।";
      if (secArea) secArea.textContent = "कुल क्षेत्रफल = जम्मा पार गरेको दूरी (२६० मिटर)";
      if (secAreaDesc) secAreaDesc.textContent = "Area = Area(OA) + Area(AB) + Area(BC) + Area(CD) + Area(DE)";
      if (secSummary) secSummary.textContent = "कुनै पनि खण्ड (OA, AB, CD, DE) छानेर आधिकारिक समाधान हेर्नुहोस्।";
    }
  } else {
    // Hare & Tortoise Story
    const pills = [
      { id: 'all', label: 'समग्र दौड (Complete Race)' },
      { id: 'hare_sprint', label: 'खरायोको तीव्र दौड (०-४s)' },
      { id: 'hare_sleep', label: 'खरायो सुतेको अवस्था (४-१४s)' },
      { id: 'tortoise_steady', label: 'कछुवाको निरन्तर चाल (०-१६s)' }
    ];

    if (secPills) {
      secPills.innerHTML = pills.map(p => `
        <button onclick="selectGraphSectionC9U7('${p.id}')" class="px-2.5 py-1 rounded-lg text-xs font-mono font-bold transition cursor-pointer ${c9u7ActiveSection === p.id ? 'bg-emerald-600 text-white' : 'bg-slate-700 text-slate-300 hover:bg-slate-600'}">
          ${p.label}
        </button>
      `).join('');
    }

    if (c9u7ActiveSection === 'hare_sleep') {
      if (secBadge) secBadge.textContent = "खरायो रुखमुनि सुतेको अवस्था";
      if (secTitle) secTitle.textContent = "घमन्ड र विश्राम (Slope = 0)";
      if (secNature) { secNature.textContent = "स्थिर (समय बढ्यो, स्थानान्तरण बढेन)"; secNature.className = "text-xs px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30"; }
      if (secSlope) secSlope.textContent = "Slope = 0 m/s (खरायो घोर निद्रामा)";
      if (secSlopeDesc) secSlopeDesc.textContent = "४ सेकेन्डदेखि १४ सेकेन्डसम्म समय बित्छ तर खरायोको दूरी बढ्दैन।";
      if (secArea) secArea.textContent = "कछुवाले खरायोलाई उछिन्छ!";
      if (secAreaDesc) secAreaDesc.textContent = "कछुवा निरन्तर समान गतिमा हिँडिरहन्छ।";
      if (secSummary) secSummary.textContent = "खरायोले कछुवा निकै पछाडि छ भनी रुखको छहारीमा सुत्यो; जसलाई ग्राफको तेर्सो रेखाले देखाउँछ।";
    } else if (c9u7ActiveSection === 'tortoise_steady') {
      if (secBadge) secBadge.textContent = "कछुवाको निरन्तर चाल (Slow & Steady)";
      if (secTitle) secTitle.textContent = "समान गति र धैर्य (Uniform Motion)";
      if (secNature) { secNature.textContent = "कछुवा विजयी! (Wins Race)"; secNature.className = "text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 font-bold border border-emerald-500/30"; }
      if (secSlope) secSlope.textContent = "Slope = +1.0 m/s (स्थिर र धिमा गति)";
      if (secSlopeDesc) secSlopeDesc.textContent = "मूलबिन्दुदेखि अन्तिम बिन्दुसम्म कछुवाको रेखा अविच्छिन्न सिधा छ।";
      if (secArea) secArea.textContent = "१६ सेकेन्डमा १६ मिटर पार!";
      if (secAreaDesc) secAreaDesc.textContent = "कछुवाले खरायोभन्दा २ सेकेन्ड पहिले नै दौड जित्छ।";
      if (secSummary) secSummary.textContent = "कछुवा कतै नरोकिई निरन्तर समान गतिमा अगाडि बढ्छ र दौड जित्न सफल हुन्छ।";
    } else {
      if (secBadge) secBadge.textContent = "खरायो र कछुवाको दौड कथा (Q4 ङ)";
      if (secTitle) secTitle.textContent = "कथाको ग्राफिकल प्रस्तुतीकरण र भौतिक व्याख्या";
      if (secNature) { secNature.textContent = "कछुवा विजयी"; secNature.className = "text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 font-bold border border-emerald-500/30"; }
      if (secSlope) secSlope.textContent = "खरायो: तीव्र ➔ शून्य ➔ तीव्र | कछुवा: एकनास समान";
      if (secSlopeDesc) secSlopeDesc.textContent = "माथिको '▶ दौड सुरु गर्नुहोस्' बटन थिचेर लाइभ दौड हेर्नुहोस्!";
      if (secArea) secArea.textContent = "नैतिक शिक्षा: निरन्तरता र लगनशीलता";
      if (secAreaDesc) secAreaDesc.textContent = "Slow and steady wins the race!";
      if (secSummary) secSummary.textContent = "पाठ्यपुस्तक पृष्ठ १२५ प्रश्न ४ (ङ) मा सोधिएको खरायो र कछुवाको दौडलाई यस ग्राफले शतप्रतिशत स्पष्ट पार्दछ।";
    }
  }
}

function runHareTortoiseRaceC9U7() {
  if (c9u7IsRacing) return;
  c9u7IsRacing = true;
  c9u7RaceProgress = 0;
  playAudioC9U7('launch');

  const btn = document.getElementById('c9u7-btn-race-run');
  if (btn) btn.innerHTML = "<span>🐢 दौड जारी छ...</span>";

  clearInterval(c9u7RaceTimer);
  const totalSteps = 80;
  let cur = 0;

  c9u7RaceTimer = setInterval(() => {
    cur++;
    c9u7RaceProgress = cur / totalSteps;
    renderMotionGraphSVGC9U7();

    if (cur >= totalSteps) {
      clearInterval(c9u7RaceTimer);
      c9u7IsRacing = false;
      c9u7RaceProgress = 1.0;
      if (btn) btn.innerHTML = "<span>▶ पुनः दौड गर्नुहोस्</span>";
      playAudioC9U7('correct');
      selectGraphSectionC9U7('tortoise_steady');
    }
  }, 40);
}

function resetHareTortoiseRaceC9U7() {
  clearInterval(c9u7RaceTimer);
  c9u7IsRacing = false;
  c9u7RaceProgress = 0;
  playAudioC9U7('click');

  const btn = document.getElementById('c9u7-btn-race-run');
  if (btn) btn.innerHTML = "<span>▶ दौड सुरु गर्नुहोस्</span>";
  renderMotionGraphSVGC9U7();
  updateGraphSectionDetailsC9U7();
}

function renderMotionGraphSVGC9U7() {
  const container = document.getElementById('c9u7-motion-graph-svg-wrap');
  if (!container) return;

  const w = 480;
  const h = 260;
  const originX = 50;
  const originY = 220;
  const graphW = 390;
  const graphH = 180;

  if (c9u7ActiveGraph === 'st_graph') {
    // Q4(घ): Table s vs t: (0,0), (2,4), (4,8), (6,8), (8,12), (10,8), (12,4), (14,0)
    const maxT = 14;
    const maxS = 14;
    const toX = t => originX + (t / maxT) * graphW;
    const toY = s => originY - (s / maxS) * graphH;

    const pts = [
      { t: 0, s: 0, label: '(0,0)' },
      { t: 2, s: 4, label: '(2,4)' },
      { t: 4, s: 8, label: '(4,8)' },
      { t: 6, s: 8, label: '(6,8)' },
      { t: 8, s: 12, label: '(8,12)' },
      { t: 10, s: 8, label: '(10,8)' },
      { t: 12, s: 4, label: '(12,4)' },
      { t: 14, s: 0, label: '(14,0)' }
    ];

    const polylinePts = pts.map(p => `${toX(p.t)},${toY(p.s)}`).join(' ');

    let highlightLine = '';
    if (c9u7ActiveSection === '0_4') {
      highlightLine = `<line x1="${toX(0)}" y1="${toY(0)}" x2="${toX(4)}" y2="${toY(8)}" stroke="#38bdf8" stroke-width="5" stroke-linecap="round"/>`;
    } else if (c9u7ActiveSection === '4_6') {
      highlightLine = `<line x1="${toX(4)}" y1="${toY(8)}" x2="${toX(6)}" y2="${toY(8)}" stroke="#fbbf24" stroke-width="5" stroke-linecap="round"/>`;
    } else if (c9u7ActiveSection === '8_14') {
      highlightLine = `<line x1="${toX(8)}" y1="${toY(12)}" x2="${toX(14)}" y2="${toY(0)}" stroke="#f43f5e" stroke-width="5" stroke-linecap="round"/>`;
    }

    container.innerHTML = `
      <svg viewBox="0 0 ${w} ${h}" class="w-full h-auto max-h-[300px] select-none">
        <!-- Axes -->
        <line x1="${originX}" y1="${originY}" x2="${originX + graphW + 20}" y2="${originY}" stroke="#64748b" stroke-width="2"/>
        <line x1="${originX}" y1="${originY}" x2="${originX}" y2="${originY - graphH - 20}" stroke="#64748b" stroke-width="2"/>

        <!-- Grid lines & Ticks -->
        ${[0, 2, 4, 6, 8, 10, 12, 14].map(t => `
          <line x1="${toX(t)}" y1="${originY}" x2="${toX(t)}" y2="${originY - graphH}" stroke="#334155" stroke-width="1" stroke-dasharray="3,3"/>
          <text x="${toX(t)}" y="${originY + 16}" font-size="10" font-family="monospace" fill="#94a3b8" text-anchor="middle">${t}</text>
        `).join('')}

        ${[0, 4, 8, 12].map(s => `
          <line x1="${originX}" y1="${toY(s)}" x2="${originX + graphW}" y2="${toY(s)}" stroke="#334155" stroke-width="1" stroke-dasharray="3,3"/>
          <text x="${originX - 10}" y="${toY(s) + 4}" font-size="10" font-family="monospace" fill="#94a3b8" text-anchor="end">${s}</text>
        `).join('')}

        <!-- Axis Labels -->
        <text x="${originX + graphW + 15}" y="${originY + 4}" font-size="11" font-family="sans-serif" font-weight="bold" fill="#e2e8f0">समय t (s)</text>
        <text x="${originX - 12}" y="${originY - graphH - 10}" font-size="11" font-family="sans-serif" font-weight="bold" fill="#e2e8f0" text-anchor="end">स्थानान्तरण s (m)</text>

        <!-- Base Plot line -->
        <polyline points="${polylinePts}" fill="none" stroke="#60a5fa" stroke-width="3" stroke-linejoin="round"/>
        ${highlightLine}

        <!-- Points -->
        ${pts.map(p => `
          <circle cx="${toX(p.t)}" cy="${toY(p.s)}" r="4.5" fill="#38bdf8" stroke="#0f172a" stroke-width="1.5" class="cursor-pointer hover:r-6"/>
        `).join('')}
      </svg>
    `;
  } else if (c9u7ActiveGraph === 'vt_graph') {
    // Q5(ङ) Bus Graph: OA (0,0)->(6,20), AB (6,20)->(10,20), CD (10,20)->(14,20), DE (14,20)->(18,0)
    const maxT = 18;
    const maxV = 25;
    const toX = t => originX + (t / maxT) * graphW;
    const toY = v => originY - (v / maxV) * graphH;

    let highlightPoly = '';
    if (c9u7ActiveSection === 'cd') {
      highlightPoly = `
        <polygon points="${toX(10)},${originY} ${toX(10)},${toY(20)} ${toX(14)},${toY(20)} ${toX(14)},${originY}" fill="#6366f1" fill-opacity="0.35"/>
        <line x1="${toX(10)}" y1="${toY(20)}" x2="${toX(14)}" y2="${toY(20)}" stroke="#818cf8" stroke-width="5"/>
        <text x="${toX(12)}" y="${toY(10)}" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">Area = 80 m</text>
      `;
    } else if (c9u7ActiveSection === 'oa') {
      highlightPoly = `
        <polygon points="${toX(0)},${originY} ${toX(6)},${toY(20)} ${toX(6)},${originY}" fill="#10b981" fill-opacity="0.35"/>
        <line x1="${toX(0)}" y1="${toY(0)}" x2="${toX(6)}" y2="${toY(20)}" stroke="#34d399" stroke-width="5"/>
      `;
    } else if (c9u7ActiveSection === 'de') {
      highlightPoly = `
        <polygon points="${toX(14)},${originY} ${toX(14)},${toY(20)} ${toX(18)},${originY}" fill="#ef4444" fill-opacity="0.35"/>
        <line x1="${toX(14)}" y1="${toY(20)}" x2="${toX(18)}" y2="${toY(0)}" stroke="#f87171" stroke-width="5"/>
      `;
    }

    container.innerHTML = `
      <svg viewBox="0 0 ${w} ${h}" class="w-full h-auto max-h-[300px] select-none">
        <!-- Axes -->
        <line x1="${originX}" y1="${originY}" x2="${originX + graphW + 20}" y2="${originY}" stroke="#64748b" stroke-width="2"/>
        <line x1="${originX}" y1="${originY}" x2="${originX}" y2="${originY - graphH - 20}" stroke="#64748b" stroke-width="2"/>

        <!-- Ticks -->
        ${[0, 6, 10, 14, 18].map(t => `
          <line x1="${toX(t)}" y1="${originY}" x2="${toX(t)}" y2="${originY - graphH}" stroke="#334155" stroke-width="1" stroke-dasharray="3,3"/>
          <text x="${toX(t)}" y="${originY + 16}" font-size="10" font-family="monospace" fill="#94a3b8" text-anchor="middle">${t}s</text>
        `).join('')}

        ${[0, 10, 20].map(v => `
          <line x1="${originX}" y1="${toY(v)}" x2="${originX + graphW}" y2="${toY(v)}" stroke="#334155" stroke-width="1" stroke-dasharray="3,3"/>
          <text x="${originX - 10}" y="${toY(v) + 4}" font-size="10" font-family="monospace" fill="#94a3b8" text-anchor="end">${v}</text>
        `).join('')}

        <!-- Axis Labels -->
        <text x="${originX + graphW + 15}" y="${originY + 4}" font-size="11" font-family="sans-serif" font-weight="bold" fill="#e2e8f0">समय t (s)</text>
        <text x="${originX - 12}" y="${originY - graphH - 10}" font-size="11" font-family="sans-serif" font-weight="bold" fill="#e2e8f0" text-anchor="end">गति v (m/s)</text>

        <!-- Shaded Area Highlight -->
        ${highlightPoly}

        <!-- Graph Polyline -->
        <polyline points="${toX(0)},${toY(0)} ${toX(6)},${toY(20)} ${toX(10)},${toY(20)} ${toX(14)},${toY(20)} ${toX(18)},${toY(0)}" fill="none" stroke="#818cf8" stroke-width="3" stroke-linejoin="round"/>

        <!-- Node Labels O, A, B, C, D, E -->
        <circle cx="${toX(0)}" cy="${toY(0)}" r="4" fill="#a5b4fc"/>
        <text x="${toX(0)}" y="${toY(0) + 14}" font-size="10" fill="#a5b4fc" font-weight="bold">O</text>

        <circle cx="${toX(6)}" cy="${toY(20)}" r="4" fill="#a5b4fc"/>
        <text x="${toX(6)}" y="${toY(20) - 8}" font-size="10" fill="#a5b4fc" font-weight="bold">A</text>

        <circle cx="${toX(10)}" cy="${toY(20)}" r="4" fill="#a5b4fc"/>
        <text x="${toX(10) - 4}" y="${toY(20) - 8}" font-size="10" fill="#a5b4fc" font-weight="bold">B/C</text>

        <circle cx="${toX(14)}" cy="${toY(20)}" r="4" fill="#a5b4fc"/>
        <text x="${toX(14)}" y="${toY(20) - 8}" font-size="10" fill="#a5b4fc" font-weight="bold">D</text>

        <circle cx="${toX(18)}" cy="${toY(0)}" r="4" fill="#a5b4fc"/>
        <text x="${toX(18)}" y="${toY(0) + 14}" font-size="10" fill="#a5b4fc" font-weight="bold">E</text>
      </svg>
    `;
  } else {
    // Hare & Tortoise Race Graph (Q4 ङ)
    const maxT = 18;
    const maxS = 18;
    const toX = t => originX + (t / maxT) * graphW;
    const toY = s => originY - (s / maxS) * graphH;

    // Tortoise: constant slow velocity: (0,0) to (16,16) -> speed 1.0 m/s
    // Hare: (0,0) -> (4,12) sprint -> (14,12) sleep -> (18,18) sprint
    const curTime = 18 * c9u7RaceProgress;

    // Current positions for animated markers
    let tortT = Math.min(curTime, 16);
    let tortS = tortT * 1.0;

    let hareS = 0;
    if (curTime <= 4) {
      hareS = curTime * 3.0;
    } else if (curTime <= 14) {
      hareS = 12.0; // asleep!
    } else {
      hareS = 12.0 + (curTime - 14) * 1.5;
    }

    container.innerHTML = `
      <svg viewBox="0 0 ${w} ${h}" class="w-full h-auto max-h-[300px] select-none">
        <!-- Axes -->
        <line x1="${originX}" y1="${originY}" x2="${originX + graphW + 20}" y2="${originY}" stroke="#64748b" stroke-width="2"/>
        <line x1="${originX}" y1="${originY}" x2="${originX}" y2="${originY - graphH - 20}" stroke="#64748b" stroke-width="2"/>

        <text x="${originX + graphW + 15}" y="${originY + 4}" font-size="11" font-family="sans-serif" font-weight="bold" fill="#e2e8f0">समय t</text>
        <text x="${originX - 12}" y="${originY - graphH - 10}" font-size="11" font-family="sans-serif" font-weight="bold" fill="#e2e8f0" text-anchor="end">दूरी s</text>

        <!-- Finish line at s = 16 -->
        <line x1="${originX}" y1="${toY(16)}" x2="${originX + graphW}" y2="${toY(16)}" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,4"/>
        <text x="${originX + graphW}" y="${toY(16) - 4}" font-size="9" fill="#ef4444" font-weight="bold" text-anchor="end">🏁 लक्ष्य (FINISH LINE)</text>

        <!-- Tortoise Line (Green, steady) -->
        <line x1="${toX(0)}" y1="${toY(0)}" x2="${toX(16)}" y2="${toY(16)}" stroke="#10b981" stroke-width="3" stroke-dasharray="1,0"/>
        <text x="${toX(16) + 4}" y="${toY(16) + 12}" fill="#10b981" font-size="10" font-weight="bold">🐢 कछुवा (विजेता - 16s)</text>

        <!-- Hare Line (Amber/Rose, sprints then sleeps then late) -->
        <polyline points="${toX(0)},${toY(0)} ${toX(4)},${toY(12)} ${toX(14)},${toY(12)} ${toX(18)},${toY(18)}" fill="none" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>
        <text x="${toX(9)}" y="${toY(12) - 8}" fill="#f59e0b" font-size="10" font-weight="bold" text-anchor="middle">💤 खरायो सुतेको खण्ड (Slope=0)</text>
        <text x="${toX(18)}" y="${toY(18) - 4}" fill="#f59e0b" font-size="10" font-weight="bold">🐇 खरायो (ढिलो)</text>

        <!-- Live Running Markers if racing -->
        ${c9u7RaceProgress > 0 ? `
          <!-- Tortoise marker -->
          <circle cx="${toX(tortT)}" cy="${toY(tortS)}" r="6" fill="#10b981" stroke="#ffffff" stroke-width="2"/>
          <text x="${toX(tortT)}" y="${toY(tortS) - 9}" font-size="12" text-anchor="middle">🐢</text>

          <!-- Hare marker -->
          <circle cx="${toX(curTime)}" cy="${toY(hareS)}" r="6" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
          <text x="${toX(curTime)}" y="${toY(hareS) - 9}" font-size="12" text-anchor="middle">${(curTime > 4 && curTime < 14) ? '💤' : '🐇'}</text>
        ` : ''}
      </svg>
    `;
  }
}
""")

# Part 4: Mode 3 Newton's Laws & Inertia Sandbox
js_parts.append("""// =========================================================================
// MODE 3: NEWTON'S LAWS & INERTIA SANDBOX
// =========================================================================
function setNewtonLawC9U7(lawNum) {
  c9u7ActiveLaw = lawNum;
  playAudioC9U7('click');

  for (let l = 1; l <= 4; l++) {
    const btn = document.getElementById(`c9u7-nbtn-${l}`);
    if (btn) {
      if (l === lawNum) {
        btn.className = "px-3.5 py-1.5 rounded-xl bg-purple-600/30 border border-purple-500 text-purple-300 font-bold transition text-xs cursor-pointer";
      } else {
        btn.className = "px-3.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-slate-400 hover:text-white font-bold transition text-xs cursor-pointer";
      }
    }
  }

  const canvasTitle = document.getElementById('c9u7-newton-canvas-title');
  const statusBadge = document.getElementById('c9u7-newton-status-badge');
  const engTitle = document.getElementById('c9u7-law-engtitle');
  const nepTitle = document.getElementById('c9u7-law-neptitle');
  const stmt = document.getElementById('c9u7-law-statement');
  const exp = document.getElementById('c9u7-law-explanation');
  const formula = document.getElementById('c9u7-law-formula');

  if (lawNum === 1) {
    if (canvasTitle) canvasTitle.textContent = "NEWTON'S FIRST LAW: INERTIA (सिक्का र गिलास इनर्सिया प्रयोग)";
    if (statusBadge) { statusBadge.textContent = "स्थिर इनर्सिया"; statusBadge.className = "px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30"; }
    if (engTitle) engTitle.textContent = "LAW OF INERTIA (FIRST LAW)";
    if (nepTitle) nepTitle.textContent = "चालसम्बन्धी न्युटनको पहिलो नियम";
    if (stmt) stmt.textContent = '"कुनै वस्तुमाथि बाह्य असन्तुलित बलले असर नगरेसम्म, स्थिर अवस्थामा रहेको वस्तु स्थिर अवस्थामै रहन्छ र चाल अवस्थामा रहेको वस्तु सिधा रेखामा समान गतिले निरन्तर चलिरहन्छ।"';
    if (exp) exp.textContent = "कार्डबोर्डलाई तीव्र बलले औँलाले हुत्याउँदा कार्डबोर्ड तुरुन्तै चालमा आउँछ तर सिक्का स्थिर इनर्सियाका कारण स्थिर रहन खोज्दा गुरुत्व बलले गिलासमा सिधै खस्छ।";
    if (formula) formula.textContent = "F_net = 0 ⟹ v = const (Inertia)";
  } else if (lawNum === 2) {
    if (canvasTitle) canvasTitle.textContent = "NEWTON'S SECOND LAW: F = ma & MOMENTUM (बल र संवेग स्यानबक्स)";
    if (statusBadge) { statusBadge.textContent = "बलको परिमाण (F = ma)"; statusBadge.className = "px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30"; }
    if (engTitle) engTitle.textContent = "LAW OF ACCELERATION (SECOND LAW)";
    if (nepTitle) nepTitle.textContent = "चालसम्बन्धी न्युटनको दोस्रो नियम";
    if (stmt) stmt.textContent = '"कुनै वस्तुमा उत्पन्न हुने प्रवेग त्यसमा लगाइएको परिणामात्मक बलसँग समानुपातिक हुन्छ र उक्त वस्तुको पिण्डसँग व्युत्क्रमानुपातिक हुन्छ।"';
    if (exp) exp.textContent = "समान बल लगाउँदा हलुका वस्तु (थोरै पिण्ड) मा धेरै प्रवेग आउँछ, तर भारी वस्तु (धेरै पिण्ड) मा थोरै प्रवेग आउँछ (a = F/m)।";
    if (formula) formula.textContent = "F = ma = Δp/t (Momentum Rate)";
  } else if (lawNum === 3) {
    if (canvasTitle) canvasTitle.textContent = "NEWTON'S THIRD LAW: ACTION & REACTION (रकेट प्रक्षेपण)";
    if (statusBadge) { statusBadge.textContent = "क्रिया र प्रतिक्रिया"; statusBadge.className = "px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30"; }
    if (engTitle) engTitle.textContent = "ACTION & REACTION (THIRD LAW)";
    if (nepTitle) nepTitle.textContent = "चालसम्बन्धी न्युटनको तेस्रो नियम";
    if (stmt) stmt.textContent = '"प्रत्येक क्रियाको बराबर तर विपरीत दिशामा प्रतिक्रिया हुन्छ।" (F_Action = - F_Reaction)';
    if (exp) exp.textContent = "रकेटबाट दहन भएको ग्यास अत्यधिक वेगमा पछाडि निस्कँदा (क्रिया), त्यति नै बराबरको विपरीत प्रतिक्रिया बलले रकेटलाई अन्तरिक्षतर्फ हुत्याउँछ।";
    if (formula) formula.textContent = "F_AB = - F_BA (Recoil & Thrust)";
  } else {
    // Law 4: Elasticity & Plasticity
    if (canvasTitle) canvasTitle.textContent = "ELASTICITY & PLASTICITY: HOOKE'S LAW (स्प्रिङ भार र इलास्टिक सीमा)";
    if (statusBadge) { statusBadge.textContent = "इलास्टिसिटी परीक्षण"; statusBadge.className = "px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30"; }
    if (engTitle) engTitle.textContent = "ELASTICITY & HOOKE'S LAW";
    if (nepTitle) nepTitle.textContent = "इलास्टिसिटी, रिस्टोरिङ बल र इलास्टिक सीमा";
    if (stmt) stmt.textContent = '"इलास्टिक सीमाभित्र कुनै वस्तुमा आउने तन्काइ त्यसमा लगाइएको भार (बल) सँग समानुपातिक हुन्छ।" (F = kx)';
    if (exp) exp.textContent = "इलास्टिक सीमासम्म स्प्रिङले भार हटाउँदा पुरानै आकार लिन्छ, तर सीमा नाघेपछि स्थायी विरूपण (Plasticity) भई स्प्रिङ सधैँका लागि तन्किन्छ।";
    if (formula) formula.textContent = "F = kx (Restoring Force)";
  }

  renderNewtonDemoSVGC9U7();
}

function flickCardC9U7() {
  if (c9u7CoinFlicked) return;
  c9u7CoinFlicked = true;
  playAudioC9U7('flick');
  renderNewtonDemoSVGC9U7();

  setTimeout(() => {
    playAudioC9U7('correct');
  }, 350);
}

function resetCoinDemoC9U7() {
  c9u7CoinFlicked = false;
  playAudioC9U7('click');
  renderNewtonDemoSVGC9U7();
}

function launchRocketC9U7() {
  if (c9u7RocketFired) return;
  c9u7RocketFired = true;
  playAudioC9U7('launch');
  renderNewtonDemoSVGC9U7();

  setTimeout(() => {
    playAudioC9U7('correct');
  }, 600);
}

function resetRocketC9U7() {
  c9u7RocketFired = false;
  playAudioC9U7('click');
  renderNewtonDemoSVGC9U7();
}

function updateSecondLawParamsC9U7(m, f) {
  if (m !== undefined) c9u7Mass = m;
  if (f !== undefined) c9u7Force = f;
  playAudioC9U7('click');
  renderNewtonDemoSVGC9U7();
}

function updateSpringLoadC9U7(weight) {
  c9u7SpringWeight = weight;
  playAudioC9U7('click');
  renderNewtonDemoSVGC9U7();
}

function renderNewtonDemoSVGC9U7() {
  const container = document.getElementById('c9u7-newton-svg-wrap');
  const ctrlBox = document.getElementById('c9u7-newton-controls');
  if (!container) return;

  if (c9u7ActiveLaw === 1) {
    // Law 1: Coin and Glass
    const cardX = c9u7CoinFlicked ? 380 : 200;
    const coinY = c9u7CoinFlicked ? 175 : 85;

    container.innerHTML = `
      <svg viewBox="0 0 460 220" class="w-full h-auto max-h-[220px] select-none">
        <!-- Table surface -->
        <rect x="20" y="195" width="420" height="15" rx="3" fill="#334155"/>

        <!-- Glass Tumbler -->
        <path d="M170,105 L180,195 L240,195 L250,105 Z" fill="#38bdf8" fill-opacity="0.15" stroke="#38bdf8" stroke-width="2"/>
        <ellipse cx="210" cy="105" rx="40" ry="7" fill="#0284c7" fill-opacity="0.2" stroke="#38bdf8" stroke-width="1.5"/>

        <!-- Cardboard Card -->
        <rect x="${cardX - 45}" y="95" width="90" height="10" rx="2" fill="#d97706" stroke="#b45309" stroke-width="1.5">
          ${c9u7CoinFlicked ? '<animate attributeName="x" from="155" to="380" dur="0.25s" fill="freeze"/>' : ''}
        </rect>
        <text x="${cardX}" y="103" font-size="8" fill="#ffffff" font-weight="bold" text-anchor="middle">कार्डबोर्ड</text>

        <!-- Gold Coin -->
        <ellipse cx="210" cy="${coinY}" rx="14" ry="6" fill="#fbbf24" stroke="#d97706" stroke-width="1.5">
          ${c9u7CoinFlicked ? '<animate attributeName="cy" from="85" to="175" dur="0.35s" begin="0.15s" fill="freeze"/>' : ''}
        </ellipse>
        <text x="210" y="${coinY + 3}" font-size="7" fill="#78350f" font-weight="black" text-anchor="middle">सिक्का</text>

        <!-- Motion vectors & Annotation -->
        ${c9u7CoinFlicked ? `
          <path d="M210,100 L210,160" stroke="#10b981" stroke-width="2" stroke-dasharray="3,3"/>
          <polygon points="210,165 207,157 213,157" fill="#10b981"/>
          <text x="215" y="140" font-size="9" fill="#10b981" font-weight="bold">स्थिर इनर्सिया ➔ गिलासमा खस्यो</text>
        ` : `
          <!-- Finger flick indicator -->
          <path d="M120,100 L150,100" stroke="#f43f5e" stroke-width="3" stroke-linecap="round"/>
          <polygon points="155,100 147,96 147,104" fill="#f43f5e"/>
          <text x="135" y="90" font-size="9" fill="#f43f5e" font-weight="bold" text-anchor="middle">औँलाले हुत्याउने</text>
        `}
      </svg>
    `;

    if (ctrlBox) {
      ctrlBox.innerHTML = `
        <div class="flex gap-2">
          <button onclick="flickCardC9U7()" class="px-4 py-2 bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs rounded-xl shadow transition cursor-pointer">
            👉 कार्डबोर्ड हुत्याउनुहोस् (Flick Card)
          </button>
          <button onclick="resetCoinDemoC9U7()" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs rounded-xl transition cursor-pointer">
            ↺ रिसेट
          </button>
        </div>
        <span class="text-xs text-slate-400">सिक्का चालमा नभई आफ्नै स्थिर अवस्थाका कारण सिधै गिलासमा खस्छ।</span>
      `;
    }
  } else if (c9u7ActiveLaw === 2) {
    // Law 2: F = ma Sandbox
    const a = c9u7Force / c9u7Mass;
    const p = c9u7Mass * (a * 2); // momentum after 2s

    container.innerHTML = `
      <svg viewBox="0 0 460 200" class="w-full h-auto max-h-[220px] select-none">
        <!-- Floor -->
        <rect x="20" y="160" width="420" height="12" rx="2" fill="#334155"/>

        <!-- Box (Mass m) -->
        <rect x="180" y="80" width="90" height="80" rx="8" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>
        <text x="225" y="115" font-size="14" font-family="monospace" fill="#ffffff" font-weight="black" text-anchor="middle">${c9u7Mass} kg</text>
        <text x="225" y="135" font-size="10" fill="#bfdbfe" text-anchor="middle">पिण्ड (Mass)</text>

        <!-- Force Arrow (F) -->
        <line x1="80" y1="120" x2="175" y2="120" stroke="#f59e0b" stroke-width="5" stroke-linecap="round"/>
        <polygon points="180,120 168,114 168,126" fill="#f59e0b"/>
        <text x="130" y="108" font-size="12" font-family="monospace" fill="#f59e0b" font-weight="bold" text-anchor="middle">F = ${c9u7Force} N</text>

        <!-- Acceleration Vector (a) -->
        <line x1="275" y1="120" x2="${275 + Math.min(a * 25, 120)}" y2="120" stroke="#10b981" stroke-width="4" stroke-linecap="round"/>
        <polygon points="${275 + Math.min(a * 25, 120) + 5},120 ${275 + Math.min(a * 25, 120) - 6},115 ${275 + Math.min(a * 25, 120) - 6},125" fill="#10b981"/>
        <text x="${275 + Math.min(a * 25, 120) / 2}" y="108" font-size="11" font-family="monospace" fill="#10b981" font-weight="bold" text-anchor="middle">a = ${a.toFixed(2)} m/s²</text>
      </svg>
    `;

    if (ctrlBox) {
      ctrlBox.innerHTML = `
        <div class="w-full grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <div class="flex justify-between text-xs mb-1">
              <span class="text-slate-300">पिण्ड (Mass - m):</span>
              <span class="font-mono text-blue-400 font-bold">${c9u7Mass} kg</span>
            </div>
            <input type="range" min="10" max="100" value="${c9u7Mass}" step="5" oninput="updateSecondLawParamsC9U7(parseFloat(this.value), undefined)" class="w-full accent-blue-500 cursor-pointer">
          </div>
          <div>
            <div class="flex justify-between text-xs mb-1">
              <span class="text-slate-300">बल (Force - F):</span>
              <span class="font-mono text-amber-400 font-bold">${c9u7Force} N</span>
            </div>
            <input type="range" min="10" max="400" value="${c9u7Force}" step="10" oninput="updateSecondLawParamsC9U7(undefined, parseFloat(this.value))" class="w-full accent-amber-500 cursor-pointer">
          </div>
        </div>
      `;
    }
  } else if (c9u7ActiveLaw === 3) {
    // Law 3: Action - Reaction (Rocket Launch)
    const rocketY = c9u7RocketFired ? 20 : 70;

    container.innerHTML = `
      <svg viewBox="0 0 460 220" class="w-full h-auto max-h-[220px] select-none">
        <!-- Launchpad -->
        <rect x="180" y="190" width="100" height="15" rx="3" fill="#475569"/>

        <!-- Rocket Body -->
        <g transform="translate(230, ${rocketY})">
          ${c9u7RocketFired ? '<animateTransform attributeName="transform" type="translate" from="230,70" to="230,20" dur="0.5s" fill="freeze"/>' : ''}
          <!-- Nose cone -->
          <polygon points="0,-45 -14,-15 14,-15" fill="#ef4444"/>
          <!-- Body Cylinder -->
          <rect x="-14" y="-15" width="28" height="60" rx="3" fill="#f8fafc"/>
          <!-- Fins -->
          <polygon points="-14,30 -26,45 -14,45" fill="#ef4444"/>
          <polygon points="14,30 26,45 14,45" fill="#ef4444"/>
          <!-- Windows -->
          <circle cx="0" cy="0" r="5" fill="#0284c7" stroke="#0f172a" stroke-width="1.5"/>

          <!-- Upward Thrust Vector (Reaction) -->
          <line x1="0" y1="-50" x2="0" y2="-75" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>
          <polygon points="0,-80 -4,-72 4,-72" fill="#38bdf8"/>
          <text x="12" y="-62" font-size="9" fill="#38bdf8" font-weight="bold">प्रतिक्रिया बल (Upward Thrust)</text>

          <!-- Flame Thrust (Action) if fired -->
          ${c9u7RocketFired ? `
            <polygon points="-10,45 0,85 10,45" fill="#f59e0b"/>
            <polygon points="-6,45 0,70 6,45" fill="#ef4444"/>
            <line x1="0" y1="90" x2="0" y2="120" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>
            <polygon points="0,125 -4,117 4,117" fill="#f59e0b"/>
            <text x="12" y="110" font-size="9" fill="#f59e0b" font-weight="bold">क्रिया बल (Exhaust Gas Down)</text>
          ` : ''}
        </g>
      </svg>
    `;

    if (ctrlBox) {
      ctrlBox.innerHTML = `
        <div class="flex gap-2">
          <button onclick="launchRocketC9U7()" class="px-4 py-2 bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs rounded-xl shadow transition cursor-pointer">
            🔥 इन्धन बाल्नुहोस् (Ignite & Launch)
          </button>
          <button onclick="resetRocketC9U7()" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs rounded-xl transition cursor-pointer">
            ↺ रिसेट
          </button>
        </div>
        <span class="text-xs text-slate-400">ग्यास तीव्र वेगमा तल निस्कनु (क्रिया) = रकेट माथि उड्नु (प्रतिक्रिया)।</span>
      `;
    }
  } else {
    // Law 4: Elasticity & Hooke's Law
    const isExceeded = c9u7SpringWeight > 7;
    const springLen = 40 + c9u7SpringWeight * 12;

    container.innerHTML = `
      <svg viewBox="0 0 460 220" class="w-full h-auto max-h-[220px] select-none">
        <!-- Ceiling -->
        <rect x="150" y="15" width="160" height="10" rx="2" fill="#475569"/>
        <line x1="230" y1="25" x2="230" y2="40" stroke="#94a3b8" stroke-width="2"/>

        <!-- Spring Coil (F = kx) -->
        <path d="M230,40 Q215,48 230,56 Q245,64 230,72 Q215,80 230,88 Q245,96 230,${40 + springLen}" fill="none" stroke="${isExceeded ? '#ef4444' : '#10b981'}" stroke-width="3" stroke-linecap="round"/>

        <!-- Hanging Hook & Weight -->
        <g transform="translate(230, ${40 + springLen})">
          <circle cx="0" cy="8" r="5" fill="none" stroke="#cbd5e1" stroke-width="2"/>
          <rect x="-20" y="14" width="40" height="30" rx="4" fill="${isExceeded ? '#b91c1c' : '#047857'}" stroke="#f8fafc" stroke-width="1.5"/>
          <text x="0" y="34" font-size="12" font-family="monospace" fill="#ffffff" font-weight="black" text-anchor="middle">${c9u7SpringWeight} kg</text>
        </g>

        <!-- Elastic Limit Line -->
        <line x1="120" y1="130" x2="340" y2="130" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3"/>
        <text x="345" y="133" font-size="9" fill="#ef4444" font-weight="bold">इलास्टिक सीमा (Limit)</text>

        <!-- Status Tag -->
        ${isExceeded ? `
          <rect x="70" y="170" width="320" height="26" rx="8" fill="#ef4444" fill-opacity="0.2" stroke="#ef4444"/>
          <text x="230" y="187" font-size="10" fill="#fca5a5" font-weight="bold" text-anchor="middle">⚠️ इलास्टिक सीमा नाघ्यो! स्थायी विरूपण (Plastic Deformation) भयो!</text>
        ` : `
          <text x="230" y="195" font-size="10" fill="#6ee7b7" font-weight="bold" text-anchor="middle">✓ इलास्टिक सीमाभित्र: भार हटाउँदा स्प्रिङ पुरानै आकारमा फर्कन्छ</text>
        `}
      </svg>
    `;

    if (ctrlBox) {
      ctrlBox.innerHTML = `
        <div class="w-full flex items-center justify-between gap-4">
          <div class="flex-1">
            <div class="flex justify-between text-xs mb-1">
              <span class="text-slate-300">स्प्रिङमा झुन्ड्याइएको भार (Weight):</span>
              <span class="font-mono ${isExceeded ? 'text-rose-400' : 'text-emerald-400'} font-bold">${c9u7SpringWeight} kg (${(c9u7SpringWeight * 9.8).toFixed(1)} N)</span>
            </div>
            <input type="range" min="1" max="10" value="${c9u7SpringWeight}" step="1" oninput="updateSpringLoadC9U7(parseFloat(this.value))" class="w-full accent-emerald-500 cursor-pointer">
          </div>
          <span class="text-[11px] text-slate-400">सीमा: ७ kg भन्दा बढी भएमा स्थायी तन्किन्छ।</span>
        </div>
      `;
    }
  }
}
""")

# Part 5: Tab 2 Exercises Data & Renderer
js_parts.append("""// =========================================================================
// TAB 2: EXERCISE SOLUTIONS RENDERER
// =========================================================================
const C9U7_EXERCISES_DATA = [
  // 1. MCQs
  {
    type: 'mcq',
    id: 'mcq-1',
    q: '१ (क). गति समय रेखाको झुकावले केको मान दिन्छ ?',
    opts: ['(अ) वेग', '(आ) गति', '(इ) प्रवेग (Acceleration)', '(ई) स्थानान्तरण'],
    ans: 2,
    exp: 'गति-समय ग्राफको झुकाव (Slope = Δv/Δt) ले समयसँगै वेग परिवर्तनको दर अर्थात् प्रवेग (Acceleration) को मान दिन्छ।'
  },
  {
    type: 'mcq',
    id: 'mcq-2',
    q: '१ (ख). दिइएको गति समय ग्राफसँग सम्बन्धित स्थानान्तरण समय ग्राफ कुन हो ?',
    opts: ['(अ) तेर्सो सिधा रेखा', '(आ) माथितिर घुमेको वक्र रेखा (Parabolic curve)', '(इ) तलतिर ओर्लिएको सिधा रेखा', '(ई) तलतिर घुमेको वक्र रेखा'],
    ans: 1,
    exp: 'समान प्रवेगमा स्थानान्तरण s = ut + ½at² अनुसार समयको वर्गसँग समानुपातिक (s ∝ t²) हुने हुनाले स्थानान्तरण-समय ग्राफ माथितिर घुमेको वक्र रेखा (पाराबोला) हुन्छ।'
  },
  {
    type: 'mcq',
    id: 'mcq-3',
    q: '१ (ग). गुड्दै गरेको बसबाट ओर्लनु जोखिमपूर्ण हुन्छ । यस भनाइलाई कुन आधारमा पुष्टि गर्न सकिन्छ ?',
    opts: ['(अ) स्थिर इनर्सिया', '(आ) चाल इनर्सिया (Inertia of motion)', '(इ) चालसम्बन्धी दोस्रो नियम', '(ई) चालसम्बन्धी तेस्रो नियम'],
    ans: 1,
    exp: 'गुडिरहेको बसबाट ओर्लँदा जमिन छुनासाथ खुट्टा स्थिर हुन्छ तर शरीरको माथिल्लो भाग चाल इनर्सियाका कारण अगाडि नै हुत्तिने हुँदा लडेर गम्भीर चोट लाग्छ।'
  },
  {
    type: 'mcq',
    id: 'mcq-4',
    q: '१ (घ). क्रिया र प्रतिक्रियाका सन्दर्भमा कुन भनाइ सही हुन्छ ?',
    opts: ['(अ) एकले अर्कोलाई रद्द गर्न सक्छन्', '(आ) दुवै एउटै वस्तुमा लाग्छन्', '(इ) बराबर तर उही दिशामा लाग्छन्', '(ई) दुई फरक फरक वस्तुमा लाग्छन्'],
    ans: 3,
    exp: 'न्युटनको तेस्रो नियम अनुसार क्रिया र प्रतिक्रिया सधैँ दुई भिन्न वस्तुहरूमा लाग्छन्; त्यसैले यिनीहरूले कहिल्यै पनि एकअर्कालाई रद्द (cancel out) गर्न सक्दैनन्।'
  },
  {
    type: 'mcq',
    id: 'mcq-5',
    q: '१ (ङ). इलास्टिसिटीको प्रयोग कुन हो ?',
    opts: ['(अ) माटोलाई आकार दिएर गमलामा रूपान्तरण गर्नु', '(आ) फलामलाई पिटेर पाता बनाउनु', '(इ) मिचेको पिठोलाई रोटीको आकार दिनु', '(ई) ब्याडमिन्टनको र्याकेटले कक हान्नु'],
    ans: 3,
    exp: 'ब्याडमिन्टन र्याकेटको जालीमा उच्च इलास्टिसिटी हुन्छ; कक ठोक्किँदा जाली क्षणभर विरूपित भई रिस्टोरिङ बलले ककलाई तीव्र गतिमा उछिट्टाएर पुनः सुरुको आकारमा फर्कन्छ।'
  },
  {
    type: 'mcq',
    id: 'mcq-6',
    q: '१ (च). सडकमा समान गतिले गुडिरहेका मालबाहक ट्रक र कारमा समान बल लगाउन सक्ने ब्रेकको प्रयोग गरी रोकिएमा तलका मध्ये कुन भनाइ सही हुन्छ ?',
    opts: ['(अ) ट्रकले पार गर्ने दुरी कारले पार गर्ने दुरीभन्दा कम हुन्छ', '(आ) कारले पार गर्ने दुरी ट्रकले पार गर्ने दुरीभन्दा कम हुन्छ', '(इ) दुवैले पार गर्ने दुरी समान हुन्छ', '(ई) दुरी पिण्डसँग सम्बन्धित हुँदैन'],
    ans: 1,
    exp: 'मन्दता a = F/m अनुसार बढी पिण्ड भएको ट्रकमा मन्दता कम उत्पन्न हुन्छ, जसले गर्दा रोकिन लामो दूरी पार गर्नुपर्छ; कम पिण्ड भएको कार थोरै दूरीमै रोकिन्छ।'
  },

  // 2. Differences
  {
    type: 'diff',
    id: 'diff-1',
    title: '२ (क). स्थानान्तरण-समय ग्राफ र गति-समय ग्राफबिच फरक',
    col1: 'स्थानान्तरण-समय ग्राफ (s-t Graph)',
    col2: 'गति-समय ग्राफ (v-t Graph)',
    rows: [
      ['अक्षहरू', 'Y-अक्षमा स्थानान्तरण (s) र X-अक्षमा समय (t) हुन्छ।', 'Y-अक्षमा गति (v) र X-अक्षमा समय (t) हुन्छ।'],
      ['झुकाव (Slope)', 'रेखाको झुकावले वस्तुको गति वा वेग (v = Δs/Δt) दिन्छ।', 'रेखाको झुकावले वस्तुको प्रवेग (a = Δv/Δt) दिन्छ।'],
      ['क्षेत्रफल (Area)', 'रेखा मुनिको क्षेत्रफलको कुनै भौतिक अर्थ हुँदैन।', 'रेखा मुनिको क्षेत्रफलले पार गरेको स्थानान्तरण वा दूरी (s) दिन्छ।'],
      ['तेर्सो रेखा', 'समय अक्षसँग समानान्तर रेखाले वस्तु स्थिर रहेको देखाउँछ।', 'समय अक्षसँग समानान्तर रेखाले वस्तु समान गतिमा रहेको देखाउँछ।']
    ]
  },
  {
    type: 'diff',
    id: 'diff-2',
    title: '२ (ख). स्थिर इनर्सिया र चाल इनर्सियाबिच फरक',
    col1: 'स्थिर इनर्सिया (Inertia of Rest)',
    col2: 'चाल इनर्सिया (Inertia of Motion)',
    rows: [
      ['परिभाषा', 'बाह्य बल नलागेसम्म स्थिर वस्तु स्थिर रहिरहन खोज्ने गुण।', 'बाह्य बल नलागेसम्म चालमा रहेको वस्तु समान गतिले चलिरहन खोज्ने गुण।'],
      ['प्रभाव', 'यसले वस्तुलाई चालमा आउनबाट रोक्ने चेष्टा गर्दछ।', 'यसले गुडिरहेको वस्तुलाई रोकिन वा दिशा बदल्न विरोध गर्दछ।'],
      ['बसमा असर', 'बस अचानक गुड्दा यात्रुहरू पछाडितर्फ हुत्तिन्छन्।', 'गुडिरहेको बस अचानक रोकिँदा यात्रुहरू अगाडितर्फ हुत्तिन्छन्।'],
      ['उदाहरण', 'रुखको हाँगा हल्लाउँदा फलफूल र पातहरू तल झर्नु।', 'साइकलमा प्याडल मार्न छाडे पनि केही परसम्म गुडिरहनु।']
    ]
  },
  {
    type: 'diff',
    id: 'diff-3',
    title: '२ (ग). इलास्टिसिटी र प्लास्टिसिटीबिच फरक',
    col1: 'इलास्टिसिटी (Elasticity)',
    col2: 'प्लास्टिसिटी (Plasticity)',
    rows: [
      ['परिभाषा', 'विरूपक बल हटाउँदा वस्तु पुनः सुरुको वास्तविक आकारमा फर्कने गुण।', 'विरूपक बल हटाउँदा वस्तु सुरुको आकारमा नफर्की विरूपितमै रहने गुण।'],
      ['रिस्टोरिङ बल', 'आन्तरिक रिस्टोरिङ बल (Restoring Force) पूर्ण विकसित हुन्छ।', 'आन्तरिक रिस्टोरिङ बल विकसित हुँदैन।'],
      ['प्रकृति', 'यो अस्थायी (Temporary) परिवर्तन हो।', 'यो स्थायी (Permanent) परिवर्तन हो।'],
      ['उदाहरण', 'रबर ब्यान्ड, स्टिलको स्प्रिङ, ब्याडमिन्टनको जाली।', 'गिलो माटो, मुछिएको पिठो, प्लास्टिकिन (Play-dough)।']
    ]
  },

  // 3. Reasons
  {
    type: 'reason',
    id: 'reason-1',
    q: '३ (क). समान गतिले गुडिरहेका मोटरसाइकल, कार, ट्रक, बस, ट्रेन आदिलाई स्थिर अवस्थामा ल्याउन फरक फरक समय लाग्छ, किन ?',
    ans: 'वस्तुको संवेग (Momentum, p = mv) पिण्डमा निर्भर गर्छ। गति समान भए तापनि ट्रेन र ट्रकको पिण्ड अत्यधिक हुने भएकाले संवेग निकै धेरै हुन्छ, तर मोटरसाइकलको पिण्ड थोरै हुँदा संवेग कम हुन्छ। न्युटनको दोस्रो नियम अनुसार रोक्न लाग्ने समय t = Δp / F हुन्छ। तसर्थ, समान ब्रेक बल लगाउँदा संवेग धेरै भएका ठूला सवारी साधनलाई स्थिर अवस्थामा ल्याउन धेरै समय लाग्छ र कम संवेग भएका साधन छिट्टै रोकिन्छन्।'
  },
  {
    type: 'reason',
    id: 'reason-2',
    q: '३ (ख). रुख हल्लाउँदा पात तथा फल खस्छन्, किन ?',
    ans: 'हाँगा हल्लाउनुअघि हाँगा, पात र फलफूल सबै स्थिर अवस्थामा हुन्छन्। हाँगा हल्लाउँदा हाँगा तुरुन्तै चाल अवस्थामा आउँछ, तर त्यसमा झुन्डिएका फल र पातहरू स्थिर इनर्सिया (Inertia of rest) का कारण आफ्नै पूर्ववत् स्थिर अवस्थामै रहन खोज्छन्। यसले गर्दा फल र हाँगाबीचको डाँठ तन्किएर चुँडिन्छ र गुरुत्व बलका कारण पात तथा फलफूलहरू भुइँमा खस्छन्।'
  },
  {
    type: 'reason',
    id: 'reason-3',
    q: '३ (ग). बस यात्राका क्रममा यात्रुले आफ्नो सिटसँगै भुइँमा राखेको झोला बस चलेको केही समयपछि अगाडिको सिटनजिक पुगेको भेटे, किन ?',
    ans: 'बस गुडिरहेको अवस्थामा भुइँमा रहेको झोला पनि बसकै गतिमा अगाडि बढिरहेको हुन्छ। जब चालकले बाटोको खाल्डाखुल्डी वा मोडमा अचानक ब्रेक लगाउँछ, बसको भुइँ रोकिन्छ। तर भुइँमा रहेको झोला चाल इनर्सिया (Inertia of motion) का कारण आफ्नै पूर्ववत् गतिमा अगाडि नै हुत्तिन्छ। झोला र भुइँबीचको घर्षण कम भएकाले झोला चिप्लिएर अगाडिको सिटनजिक पुगेको हो।'
  },
  {
    type: 'reason',
    id: 'reason-4',
    q: '३ (घ). बन्दुकबाट गोली छोड्दा यसलाई दरिलो आड दिनुपर्छ, किन ?',
    ans: 'न्युटनको तेस्रो नियम अनुसार प्रत्येक क्रियाको बराबर तर विपरीत दिशामा प्रतिक्रिया हुन्छ। बन्दुकबाट गोली छुट्दा बन्दुकले गोलीलाई अगाडितर्फ तीव्र बल (क्रिया) लगाउँछ। त्यसै क्षण गोलीले पनि बन्दुकलाई त्यति नै परिमाणको बलले पछाडितर्फ धकेल्छ (प्रतिक्रिया बल - Recoil)। यदि बन्दुकलाई काँधमा दरिलो आड नदिई खुकुलो राखियो भने बन्दुकको तीव्र झट्काले काँधको हाड भाँच्चिने वा गम्भीर चोट लाग्ने खतरा हुन्छ।'
  },
  {
    type: 'reason',
    id: 'reason-5',
    q: '३ (ङ). दुईओटा समान आकार भएका रबरका बललाई सँगै भुइँमा खसाल्दा एउटा बढी उफ्रिएको पाइयो, किन ?',
    ans: 'रबरको आन्तरिक रासायनिक बनावट र प्रशोधन अनुसार बलहरूको इलास्टिसिटी (Elasticity) फरक-फरक हुन्छ। भुइँमा ठोक्किँदा दुवै बल केही विरूपित हुन्छन्। जुन बलमा इलास्टिसिटी बढी हुन्छ, त्यसले विरूपणको विरोध गर्दै तत्काल तीव्र आन्तरिक रिस्टोरिङ बल उत्पन्न गर्छ र गतिज ऊर्जालाई नगुमाई बललाई माथितिर धकेल्छ। कम इलास्टिसिटी भएको बलमा ऊर्जाको धेरै अंश आन्तरिक घर्षण र तापमा खेर जाने हुँदा त्यो कम उफ्रन्छ।'
  },
  {
    type: 'reason',
    id: 'reason-6',
    q: '३ (च). रबर बेन्डलाई निश्चित सीमाभन्दा बढी तन्काउनु हुँदैन, किन ?',
    ans: 'प्रत्येक इलास्टिक वस्तुको तन्काउन सकिने एउटा निश्चित अधिकतम विरूपक बलको सीमा हुन्छ, जसलाई इलास्टिक सीमा (Elastic Limit) भनिन्छ। यदि रबर बेन्डलाई इलास्टिक सीमाभन्दा बढी तन्काइयो भने यसको इलास्टिक गुण नष्ट भई स्थायी प्लास्टिक विरूपण हुन्छ (रबर लत्रन्छ) वा यसका अणुहरूबीचको आणविक बन्धन चुँडिएर रबर बेन्ड चटक्क फुट्छ।'
  },

  // 4. Structured Questions
  {
    type: 'structured',
    id: 'struct-1',
    q: '४ (क). औसत गति र प्रवेगको परिभाषा लेख्नुहोस् ।',
    ans: '• औसत गति (Average Velocity): वस्तुले पार गरेको जम्मा स्थानान्तरणलाई जम्मा समयले भाग गर्दा आउने मान (v_av = s / t)। SI एकाइ: m/s।\\n• प्रवेग (Acceleration): समयसँगै वस्तुको वेगमा आउने परिवर्तनको दर (a = (v - u) / t)। SI एकाइ: m/s²।'
  },
  {
    type: 'structured',
    id: 'struct-2',
    q: '४ (ख). सिधा रेखीय चालका ३ समीकरणहरूको निगमन गर्नुहोस् ।',
    ans: '१. v = u + at को निगमन: प्रवेगको परिभाषा a = (v - u) / t बाट क्रस-गुणन गर्दा at = v - u ⟹ v = u + at।\\n\\n२. v² = u² + 2as को निगमन: s = ((u + v) / 2) × t र t = (v - u) / a प्रतिस्थापन गर्दा s = ((v + u)(v - u)) / 2a = (v² - u²) / 2a ⟹ 2as = v² - u² ⟹ v² = u² + 2as।\\n\\n३. s = ut + ½at² को निगमन: s = ((u + v) / 2) × t मा v = u + at राख्दा s = ((u + u + at) / 2) × t = ((2u + at) / 2) × t = (u + ½at) × t = ut + ½at²।'
  },
  {
    type: 'structured',
    id: 'struct-3',
    q: '४ (ङ). खरायो र कछुवाको दौड कथा (ग्राफको अवलोकनका आधारमा)',
    ans: 'कछुवा मूलबिन्दुबाट निरन्तर समान गतिमा हिँडिरह्यो (Uniform velocity straight line)। खरायो सुरुमा तीव्र वेगले दौडियो (ठाडो झुकाव), तर कछुवा धेरै पछाडि छ भनी रुखमुनि सुत्यो (तेर्सो रेखा Slope=0 जहाँ समय बढ्यो तर दूरी बढेन)। कछुवा नरोकिई अगाडि बढी फिनिसिङ लाइन पुग्यो। खरायो ब्युँझेर दौडँदा कछुवाले दौड जितिसकेको थियो (Slow and steady wins the race)।'
  },
  {
    type: 'structured',
    id: 'struct-4',
    q: '४ (ट). चालसम्बन्धी न्युटनको दोस्रो नियम लेखी F = ma प्रमाणित गर्नुहोस् ।',
    ans: 'नियम: "कुनै वस्तुमा उत्पन्न हुने प्रवेग लगाइएको बलसँग समानुपातिक (a ∝ F) र पिण्डसँग व्युत्क्रमानुपातिक (a ∝ 1/m) हुन्छ।"\\n\\nप्रमाण: दुवैलाई मिलाउँदा a ∝ F/m ⟹ F ∝ ma ⟹ F = k·ma। SI एकाइमा 1 kg पिण्डमा 1 m/s² प्रवेग उत्पन्न गर्न 1 N बल चाहिन्छ (1 = k × 1 × 1 ⟹ k = 1)। तसर्थ F = ma प्रमाणित भयो।'
  },

  // 5. Numerical Problems
  {
    type: 'numerical',
    id: 'num-1',
    q: '५ (क). हवाईजहाज धावनमार्गमा दक्षिणतर्फ गुड्दाको स्थानान्तरण र गति',
    given: 'सुरुको गति u = 0 m/s, प्रवेग a = 1.5 m/s², समय t = 30 s',
    formula: 's = ut + ½at²,  v = u + at',
    calc: 's = (0 × 30) + ½ × 1.5 × (30)² = 0 + 0.75 × 900 = 675 m (दक्षिण)\\nv = 0 + (1.5 × 30) = 45 m/s (दक्षिण)',
    res: 'स्थानान्तरण = ६७५ m (दक्षिण) र उड्नुपूर्वको गति = ४५ m/s (दक्षिण)'
  },
  {
    type: 'numerical',
    id: 'num-2',
    q: '५ (ख). पुलबाट पानीमा ढुङ्गा खसाल्दा पानीको सतहबाट पुलको उचाइ',
    given: 'सुरुको गति u = 0 m/s, गुरुत्वप्रवेग g = 9.8 m/s², समय t = 2 s',
    formula: 'h = ut + ½gt²',
    calc: 'h = (0 × 2) + ½ × 9.8 × (2)² = 0 + 4.9 × 4 = 19.6 m',
    res: 'पुलको उचाइ = १९.६ m'
  },
  {
    type: 'numerical',
    id: 'num-3',
    q: '५ (ग). सुरज र साइकल ओरालो बाटोमा गुड्दा लागेको परिणामात्मक बल',
    given: 'सुरजको पिण्ड m₁ = 50 kg, साइकल m₂ = 15 kg, कुल पिण्ड m = 65 kg, प्रवेग a = 2 m/s²',
    formula: 'F = ma',
    calc: 'F = 65 kg × 2 m/s² = 130 N',
    res: 'परिणामात्मक बल = १३० N'
  },
  {
    type: 'numerical',
    id: 'num-4',
    q: '५ (घ). कारमा ब्रेक लगाउँदा लागेको परिणामात्मक बल',
    given: 'पिण्ड m = 1500 kg, u = 72 km/h = 20 m/s, v = 18 km/h = 5 m/s, दूरी s = 50 m',
    formula: 'v² = u² + 2as,  F = ma',
    calc: '(5)² = (20)² + 2 × a × 50 ⟹ 25 = 400 + 100a ⟹ 100a = -375 ⟹ a = -3.75 m/s²\\nF = 1500 kg × (-3.75 m/s²) = -5625 N',
    res: 'परिणामात्मक ब्रेक बल = ५६२५ N (गतिको विपरित दिशामा)'
  },
  {
    type: 'numerical',
    id: 'num-5',
    q: '५ (ङ). बसको गति-समय ग्राफ विश्लेषण (खण्ड CD को स्थानान्तरण)',
    given: 'गति v = 20 m/s (समान गति), समय अन्तराल t = 14s - 10s = 4 s',
    formula: 's = v × t (रेखा मुनिको क्षेत्रफल)',
    calc: 's = 20 m/s × 4 s = 80 m (पूर्व तर्फ)',
    res: 'खण्ड CD को प्रवेग = ० m/s² र स्थानान्तरण = ८० m पूर्व'
  },

  // 6. Project Works
  {
    type: 'project',
    id: 'proj-1',
    title: '६ (क). बेलुनबाट चल्ने खेलौना कार निर्माण र न्युटनको दोस्रो नियम प्रदर्शन',
    desc: 'खाली प्लास्टिकको बोतल, बिर्काका पाङ्ग्रा र बेलुन जोडेर खेलौना कार बनाइयो। बेलुनमा धेरै हावा भर्दा (F बढाउँदा) कार तीव्र प्रवेगले गुड्यो र कारभित्र सिक्का थपेर पिण्ड (m) बढाउँदा प्रवेग घट्यो। यसबाट F = ma पूर्ण प्रमाणित भयो।'
  },
  {
    type: 'project',
    id: 'proj-2',
    title: '६ (ख). रबर ब्यान्डको इलास्टिसिटीबाट खेलौना हेलिकप्टर निर्माण',
    desc: 'आइसक्रिमको सिन्का र पेपरक्लिपमा रबर ब्यान्ड जोडी प्लास्टिक प्रोपेलर घुमाएर बटारियो। रबर ब्यान्डको इलास्टिक सम्भाव्य ऊर्जा प्रोपेलरको गतिज ऊर्जामा बदलिएर खेलौना हेलिकप्टर आकाशमा उड्यो।'
  }
];

function filterC9U7Exercises(filter) {
  c9u7ActiveExFilter = filter;
  playAudioC9U7('click');

  const filters = ['all', 'mcq', 'diff', 'reason', 'structured', 'numerical', 'project'];
  filters.forEach(f => {
    const btn = document.getElementById(`c9u7-efilter-${f}`);
    if (btn) {
      if (f === filter) {
        btn.className = "px-4 py-2 rounded-xl text-xs font-bold transition bg-blue-600 text-white cursor-pointer whitespace-nowrap";
      } else {
        btn.className = "px-4 py-2 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap";
      }
    }
  });

  renderC9U7Exercises();
}

function renderC9U7Exercises() {
  const container = document.getElementById('c9u7-exercises-container');
  if (!container) return;

  const filtered = c9u7ActiveExFilter === 'all'
    ? C9U7_EXERCISES_DATA
    : C9U7_EXERCISES_DATA.filter(item => item.type === c9u7ActiveExFilter);

  let html = '';
  filtered.forEach(item => {
    if (item.type === 'mcq') {
      html += `
        <div class="c9u7-ex-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-3">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold px-2.5 py-1 rounded-full bg-blue-100 text-blue-800">
              १. बहुवैकल्पिक प्रश्न (MCQ)
            </span>
            <span class="text-xs font-bold text-emerald-600">✓ आधिकारिक उत्तर</span>
          </div>
          <h4 class="text-sm md:text-base font-bold text-slate-900">${item.q}</h4>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
            ${item.opts.map((opt, idx) => `
              <div class="p-2.5 rounded-xl border text-xs md:text-sm font-medium ${idx === item.ans ? 'bg-emerald-50 border-emerald-400 text-emerald-950 font-bold' : 'bg-slate-50 border-slate-200 text-slate-600'}">
                ${opt}
              </div>
            `).join('')}
          </div>
          <div class="p-3 rounded-2xl bg-blue-50/60 border border-blue-200 text-xs text-blue-950 space-y-1">
            <strong>💡 वैज्ञानिक कारण:</strong>
            <p>${item.exp}</p>
          </div>
        </div>
      `;
    } else if (item.type === 'diff') {
      html += `
        <div class="c9u7-ex-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-4">
          <span class="text-xs font-bold px-2.5 py-1 rounded-full bg-indigo-100 text-indigo-800">
            २. तुलनात्मक फरक (Differences)
          </span>
          <h4 class="text-base font-bold text-slate-900">${item.title}</h4>
          <div class="overflow-x-auto">
            <table class="w-full text-xs md:text-sm border-collapse border border-slate-200 text-left">
              <thead>
                <tr class="bg-slate-100 text-slate-800 font-bold">
                  <th class="border border-slate-200 p-2.5">तुलनाको आधार</th>
                  <th class="border border-slate-200 p-2.5 text-blue-700">${item.col1}</th>
                  <th class="border border-slate-200 p-2.5 text-indigo-700">${item.col2}</th>
                </tr>
              </thead>
              <tbody>
                ${item.rows.map(r => `
                  <tr class="hover:bg-slate-50">
                    <td class="border border-slate-200 p-2.5 font-bold text-slate-700">${r[0]}</td>
                    <td class="border border-slate-200 p-2.5 text-slate-600">${r[1]}</td>
                    <td class="border border-slate-200 p-2.5 text-slate-600">${r[2]}</td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        </div>
      `;
    } else if (item.type === 'reason') {
      html += `
        <div class="c9u7-ex-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-3">
          <span class="text-xs font-bold px-2.5 py-1 rounded-full bg-amber-100 text-amber-800">
            ३. वैज्ञानिक कारण (Give Reason)
          </span>
          <h4 class="text-sm md:text-base font-bold text-slate-900">${item.q}</h4>
          <div class="p-3.5 rounded-2xl bg-amber-50/50 border border-amber-200 text-xs md:text-sm text-slate-800 leading-relaxed">
            <strong>उत्तर:</strong> ${item.ans}
          </div>
        </div>
      `;
    } else if (item.type === 'structured') {
      html += `
        <div class="c9u7-ex-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-3">
          <span class="text-xs font-bold px-2.5 py-1 rounded-full bg-purple-100 text-purple-800">
            ४. विस्तृत प्रश्नोत्तर (Structured Q&A)
          </span>
          <h4 class="text-sm md:text-base font-bold text-slate-900">${item.q}</h4>
          <div class="p-3.5 rounded-2xl bg-purple-50/40 border border-purple-200 text-xs md:text-sm text-slate-800 leading-relaxed whitespace-pre-line">
            ${item.ans}
          </div>
        </div>
      `;
    } else if (item.type === 'numerical') {
      html += `
        <div class="c9u7-ex-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-3">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold px-2.5 py-1 rounded-full bg-emerald-100 text-emerald-800">
              ५. गणितीय समस्या (Numerical Problem)
            </span>
            <span class="text-xs font-bold px-2.5 py-0.5 rounded-full bg-emerald-500 text-white font-mono">
              हल सहित
            </span>
          </div>
          <h4 class="text-sm md:text-base font-bold text-slate-900">${item.q}</h4>
          <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 text-xs md:text-sm text-slate-800 space-y-2">
            <div class="font-mono text-slate-600"><strong>दिइएको छ:</strong> ${item.given}</div>
            <div class="font-mono text-indigo-700"><strong>सूत्र:</strong> ${item.formula}</div>
            <div class="font-mono text-slate-800 whitespace-pre-line bg-white p-2.5 rounded-xl border border-slate-200"><strong>गणना:</strong>\\n${item.calc}</div>
            <div class="p-2 rounded-xl bg-emerald-100 text-emerald-900 font-bold">
              ✓ ${item.res}
            </div>
          </div>
        </div>
      `;
    } else if (item.type === 'project') {
      html += `
        <div class="c9u7-ex-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-3">
          <span class="text-xs font-bold px-2.5 py-1 rounded-full bg-teal-100 text-teal-800">
            ६. परियोजना कार्य (Project Work)
          </span>
          <h4 class="text-base font-bold text-slate-900">${item.title}</h4>
          <p class="text-xs md:text-sm text-slate-700 leading-relaxed bg-teal-50/50 p-3.5 rounded-2xl border border-teal-200">
            ${item.desc}
          </p>
        </div>
      `;
    }
  });

  container.innerHTML = html;
}
""")

# Part 6: Tab 3 16 Tiered Model Questions Data & Renderer
js_parts.append("""// =========================================================================
// TAB 3: 16 TIERED MODEL QUESTIONS (K5, U6, HA5)
// =========================================================================
const C9U7_TIERS_DATA = [
  // 5 Knowledge
  {
    tier: 'knowledge',
    id: 'k-1',
    badge: 'ज्ञानात्मक (K1)',
    q: '१. स्थानान्तरण र वेगको परिभाषा लेखी तिनका SI एकाइ उल्लेख गर्नुहोस् ।',
    ans: '• स्थानान्तरण (Displacement): चालमा रहेको वस्तुको सुरुको बिन्दु र अन्तिम बिन्दुबीचको सबैभन्दा छोटो सिधा दूरीलाई स्थानान्तरण भनिन्छ। SI एकाइ: मिटर (m)।\\n• वेग (Velocity): कुनै निश्चित दिशामा वस्तुले प्रति सेकेन्ड पार गरेको स्थानान्तरणलाई वेग भनिन्छ। SI एकाइ: मिटर प्रति सेकेन्ड (m/s)।'
  },
  {
    tier: 'knowledge',
    id: 'k-2',
    badge: 'ज्ञानात्मक (K2)',
    q: '२. १ न्युटन बल (1 Newton Force) लाई परिभाषित गर्नुहोस् ।',
    ans: '१ किलोग्राम (1 kg) पिण्ड भएको कुनै वस्तुमा बलको दिशामा १ मिटर प्रति सेकेन्ड वर्ग (1 m/s²) को प्रवेग उत्पन्न गराउन आवश्यक पर्ने परिणामात्मक बाह्य बललाई १ न्युटन बल (1 N) भनिन्छ।\\nसूत्र: 1 N = 1 kg × 1 m/s² = 1 kg·m/s²।'
  },
  {
    tier: 'knowledge',
    id: 'k-3',
    badge: 'ज्ञानात्मक (K3)',
    q: '३. संवेग (Linear Momentum) भनेको के हो ? यसको गणितीय सूत्र र SI एकाइ लेख्नुहोस् ।',
    ans: 'कुनै चालमा रहेको वस्तुको पिण्ड र त्यसको वेगको गुणनफलबाट प्राप्त हुने गतिको जम्मा परिमाणलाई संवेग भनिन्छ।\\n• गणितीय सूत्र: p = m × v\\n• SI एकाइ: किलोग्राम मिटर प्रति सेकेन्ड (kg·m/s)।'
  },
  {
    tier: 'knowledge',
    id: 'k-4',
    badge: 'ज्ञानात्मक (K4)',
    q: '४. गति-समय ग्राफको रेखा मुनिको क्षेत्रफलले के जनाउँछ ?',
    ans: 'गति-समय ग्राफ (v-t Graph) को रेखा र समय-अक्षबीचको बन्द क्षेत्रफलले उक्त समयावधिमा वस्तुले पार गरेको जम्मा स्थानान्तरण वा दूरी (s) जनाउँछ। (Area = v × t = Distance s)।'
  },
  {
    tier: 'knowledge',
    id: 'k-5',
    badge: 'ज्ञानात्मक (K5)',
    q: '५. इलास्टिक सीमा (Elastic Limit) भनेको के हो ?',
    ans: 'कुनै इलास्टिक वस्तुमा लगाउन सकिने विरूपक बलको त्यो अधिकतम मान, जसभित्र बल हटाउँदा वस्तु पूर्ण रूपमा आफ्नो सुरुको आकारमा फर्कन सक्छ तर त्योभन्दा बढी बल लगाउँदा वस्तुमा स्थायी विरूपण आउँछ वा चुँडिन्छ, त्यसलाई इलास्टिक सीमा भनिन्छ।'
  },

  // 6 Understanding
  {
    tier: 'understanding',
    id: 'u-1',
    badge: 'बोधात्मक (U1)',
    q: '६. गति-समय ग्राफमा सिधा तेर्सो रेखा र सिधा माथितिर गएको रेखाले जनाउने चालको प्रकृतिबिच तुलना गर्नुहोस् ।',
    ans: '• सिधा तेर्सो रेखा (समय अक्षसँग समानान्तर): झुकाव शून्य (Slope = 0) हुन्छ। यसले वस्तु समान गति (Uniform velocity) मा रहेको र प्रवेग शून्य (a = 0) रहेको जनाउँछ।\\n• सिधा माथितिर गएको रेखा: झुकाव स्थिर र धनात्मक हुन्छ। यसले वस्तु समान प्रवेग (Uniform acceleration) ले गुडिरहेको जनाउँछ।'
  },
  {
    tier: 'understanding',
    id: 'u-2',
    badge: 'बोधात्मक (U2)',
    q: '७. गुडिरहेको बसमा चालकले अचानक ब्रेक लगाउँदा यात्रुहरू अगाडितर्फ किन हुत्तिन्छन् ?',
    ans: 'बस गुडिरहँदा यात्रुको सम्पूर्ण शरीर पनि बसकै गतिमा चाल अवस्थामा हुन्छ। अचानक ब्रेक लगाउँदा बसको सिट र भुइँसँग सम्पर्कमा रहेको शरीरको तल्लो भाग तुरुन्तै स्थिर अवस्थामा आउँछ। तर शरीरको माथिल्लो भाग चाल इनर्सिया (Inertia of motion) का कारण अगाडि नै बढिरहन खोज्ने हुनाले यात्रुहरू अगाडितर्फ हुत्तिन्छन्।'
  },
  {
    tier: 'understanding',
    id: 'u-3',
    badge: 'बोधात्मक (U3)',
    q: '८. क्रिकेट खेलमा फिल्डरले क्याच समात्दा आफ्नो हात पछाडितर्फ किन तान्छ ?',
    ans: 'न्युटनको दोस्रो नियम अनुसार F = Δp / t हुन्छ। हात पछाडि तान्दा बललाई रोकिन लाग्ने समय (t) बढ्छ, जसले गर्दा संवेग परिवर्तनको दर घटेर हत्केलामा बलले लगाउने ठक्कर बल (F) निकै कम हुन्छ र हातमा चोटपटक लाग्नबाट जोगिन्छ।'
  },
  {
    tier: 'understanding',
    id: 'u-4',
    badge: 'बोधात्मक (U4)',
    q: '९. न्युटनको तेस्रो नियम अनुसार क्रिया र प्रतिक्रिया बल बराबर र विपरीत हुन्छन् भने तिनीहरूले एकअर्कालाई किन रद्द गर्दैनन् ?',
    ans: 'कुनै दुई बलहरूले एकअर्कालाई रद्द गर्नका लागि ती बलहरू एउटै वस्तुमा विपरीत दिशाबाट लागेको हुनुपर्छ। तर न्युटनको तेस्रो नियम अनुसार क्रिया पहिलो वस्तुले दोस्रो वस्तुमा र प्रतिक्रिया दोस्रो वस्तुले पहिलो वस्तुमा लगाउँछ। क्रिया र प्रतिक्रिया दुई फरक वस्तुहरूमा लाग्ने हुनाले यिनीहरूले कहिल्यै एकअर्कालाई रद्द गर्न सक्दैनन्।'
  },
  {
    tier: 'understanding',
    id: 'u-5',
    badge: 'बोधात्मक (U5)',
    q: '१०. रबर ब्यान्डलाई तन्काउँदा आकार परिवर्तन हुन्छ तर बल हटाउँदा पुरानै आकारमा फर्कन्छ, किन ?',
    ans: 'रबर उच्च इलास्टिसिटी भएको वस्तु हो। तन्काउँदा यसका अणुहरूबीच विरूपक बलको विपरीत दिशामा तीव्र आन्तरिक रिस्टोरिङ बल (Restoring force) विकसित हुन्छ। जब बाह्य बल हटाइन्छ, यही रिस्टोरिङ बलले अणुहरूलाई पुनः सुरुको न्यूनतम ऊर्जाको अवस्थामा तानेर पुरानै आकारमा फर्काउँछ।'
  },
  {
    tier: 'understanding',
    id: 'u-6',
    badge: 'बोधात्मक (U6)',
    q: '११. पहाडी घुम्तीहरूमा सडकको बाहिरी भागलाई भित्री भागभन्दा केही अग्लो (Banking of Roads) किन बनाइन्छ ?',
    ans: 'तीव्र गतिमा गुडिरहेको गाडी घुम्तीमा मोडिँदा दिशाको इनर्सियाका कारण सिधा अगाडि भीरबाट खस्ने खतरा हुन्छ। सडकको बाहिरी भाग अग्लो बनाउँदा गाडीको तौल र जमिनको प्रतिक्रिया बलको तेर्सो घटकले आवश्यक सेन्ट्रिपेटल बल प्रदान गर्छ, जसले गर्दा गाडी नचिप्लिई सुरक्षित घुम्न सक्छ।'
  },

  // 5 Higher Ability
  {
    tier: 'higher_ability',
    id: 'ha-1',
    badge: 'उच्च दक्षता (HA1)',
    q: '१२. कार स्थिर अवस्थाबाट सुरु भई १०s सम्म २ m/s² प्रवेगले गुड्छ, त्यसपछि २०s समान गतिले र ५s मा रोकिन्छ। जम्मा दूरी कति हुन्छ ?',
    ans: '• खण्ड १ (०-१०s): u = 0, a = 2, t = 10 ⟹ v = 20 m/s, s₁ = ½ × 2 × 100 = 100 m।\\n• खण्ड २ (१०-३०s): v = 20 m/s समान, t = 20s ⟹ s₂ = 20 × 20 = 400 m।\\n• खण्ड ३ (३०-३५s): u = 20, v = 0, t = 5s ⟹ s₃ = ½ × (20 + 0) × 5 = 50 m।\\n• जम्मा दूरी s = १०० + ४०० + ५० = ५५० मिटर (550 m)।'
  },
  {
    tier: 'higher_ability',
    id: 'ha-2',
    badge: 'उच्च दक्षता (HA2)',
    q: '१३. १००० kg को ट्रक ५४ km/h गतिबाट २ सेकेन्डमा रोकिँदा मन्दता बल कति लाग्छ र सिटबेल्ट नबाँधे के हुन्थ्यो ?',
    ans: '• u = 54 km/h = 15 m/s, v = 0, t = 2s ⟹ a = (0 - 15) / 2 = -7.5 m/s²।\\n• मन्दता बल F = ma = 1000 kg × (-7.5 m/s²) = -7500 N (परिमाण ७५०० N)।\\n• सिटबेल्ट नबाँधेको भए चालकको शरीर चाल इनर्सियाका कारण १५ m/s कै वेगले अगाडि हुत्तिएर स्टेरिङ र विन्डसिल्डमा भयानक रूपमा बजारिने थियो।'
  },
  {
    tier: 'higher_ability',
    id: 'ha-3',
    badge: 'उच्च दक्षता (HA3)',
    q: '१४. ४ kg बन्दुकबाट ०.०२ kg (२०g) को गोली ४०० m/s वेगले निस्कँदा बन्दुक पछाडि धकेलिने वेग हिसाब गर्नुहोस् ।',
    ans: 'संवेग संरक्षणको सिद्धान्त अनुसार सुरुको कुल संवेग = अन्तिम कुल संवेग (0 = M·V + m·v)।\\n⟹ 4 × V + 0.02 × 400 = 0 ⟹ 4V + 8 = 0 ⟹ 4V = -8 ⟹ V = -2 m/s।\\nउत्तर: बन्दुक पछाडि धकेलिने वेग २ m/s हो (न्युटनको तेस्रो नियम र संवेग संरक्षण)।'
  },
  {
    tier: 'higher_ability',
    id: 'ha-4',
    badge: 'उच्च दक्षता (HA4)',
    q: '१५. ४४.१ मिटर अग्लो पुलबाट ढुङ्गा खसाल्दा पानीमा ठोक्किन लाग्ने समय र पानी छुँदाको वेग हिसाब गर्नुहोस् ।',
    ans: '• u = 0, h = 44.1 m, g = 9.8 m/s²।\\n• h = ut + ½gt² ⟹ 44.1 = 0 + 4.9t² ⟹ t² = 44.1 / 4.9 = 9 ⟹ t = 3 सेकेन्ड।\\n• अन्तिम वेग v = u + gt = 0 + (9.8 × 3) = २९.४ m/s।'
  },
  {
    tier: 'higher_ability',
    id: 'ha-5',
    badge: 'उच्च दक्षता (HA5)',
    q: '१६. रकेट प्रक्षेपण (Rocket Launch) को कार्यप्रणालीलाई न्युटनको तेस्रो नियम र संवेग संरक्षणका आधारमा व्याख्या गर्नुहोस् ।',
    ans: '१. क्रिया बल: रकेटको इन्जिनमा इन्धन जलेर अत्यधिक ताप र चापको ग्यास नोजलबाट तीव्र वेगमा पछाडि निस्कन्छ।\\n२. प्रतिक्रिया बल: न्युटनको तेस्रो नियम (F_Action = -F_Reaction) अनुसार पछाडि निस्किएको ग्यासले रकेटमा बराबर तर अगाडितर्फ अपवर्ड थ्रस्ट (Upward thrust) दिन्छ।\\n३. संवेग संरक्षण: पछाडि निस्कने ग्यासको संवेग बराबर रकेटले माथितिर संवेग प्राप्त गर्छ, जसले गर्दा रकेट तीव्र प्रवेगका साथ अन्तरिक्षमा उड्छ।'
  }
];

function filterC9U7Tiers(tier) {
  c9u7ActiveTierFilter = tier;
  playAudioC9U7('click');

  const tiers = ['all', 'knowledge', 'understanding', 'higher_ability'];
  tiers.forEach(t => {
    const btn = document.getElementById(`c9u7-tfilter-${t}`);
    if (btn) {
      if (t === tier) {
        btn.className = "px-4 py-2 rounded-xl text-xs font-bold transition bg-blue-600 text-white cursor-pointer whitespace-nowrap";
      } else {
        btn.className = "px-4 py-2 rounded-xl text-xs font-bold transition bg-white text-slate-700 hover:bg-slate-200 cursor-pointer whitespace-nowrap";
      }
    }
  });

  renderC9U7Tiers();
}

function renderC9U7Tiers() {
  const container = document.getElementById('c9u7-tiers-container');
  if (!container) return;

  const filtered = c9u7ActiveTierFilter === 'all'
    ? C9U7_TIERS_DATA
    : C9U7_TIERS_DATA.filter(item => item.tier === c9u7ActiveTierFilter);

  let html = '';
  filtered.forEach(item => {
    let badgeClass = 'bg-blue-100 text-blue-800';
    if (item.tier === 'understanding') badgeClass = 'bg-indigo-100 text-indigo-800';
    if (item.tier === 'higher_ability') badgeClass = 'bg-rose-100 text-rose-800';

    html += `
      <div class="c9u7-tier-card bg-white border border-slate-200 rounded-3xl p-5 shadow-sm space-y-3">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold px-2.5 py-1 rounded-full ${badgeClass}">
            ${item.badge}
          </span>
          <span class="text-xs font-mono text-slate-400">CDC Model Q&A</span>
        </div>
        <h4 class="text-sm md:text-base font-bold text-slate-900">${item.q}</h4>
        <div class="p-3.5 rounded-2xl bg-slate-50 border border-slate-200 text-xs md:text-sm text-slate-800 leading-relaxed whitespace-pre-line">
          ${item.ans}
        </div>
      </div>
    `;
  });

  container.innerHTML = html;
}
""")

# Part 7: Tab 4 Quiz Engine & Initialization
js_parts.append("""// =========================================================================
// TAB 4: QUIZ ENGINE (10 Comprehensive Physics Questions)
// =========================================================================
const C9U7_QUIZ_DATA = [
  {
    q: "१. गति-समय ग्राफको रेखाको झुकाव (Slope = Δv/Δt) ले तलका मध्ये कुन भौतिक राशि दिन्छ ?",
    opts: [
      "चाल (Speed)",
      "दूरी (Distance)",
      "प्रवेग (Acceleration)",
      "संवेग (Momentum)"
    ],
    ans: 2,
    exp: "गति-समय ग्राफको झुकावले समयसँगै वेग परिवर्तनको दर अर्थात् प्रवेग (Acceleration) को मान दिन्छ।"
  },
  {
    q: "२. सिधा रेखीय चालको दोस्रो समीकरण s = ut + ½at² कुन दुई चर राशिका बिचको सम्बन्ध हो ?",
    opts: [
      "वेग र प्रवेग",
      "स्थानान्तरण र समय",
      "बल र संवेग",
      "पिण्ड र इनर्सिया"
    ],
    ans: 1,
    exp: "यस समीकरणले निश्चित प्रवेगमा समय (t) अनुसार वस्तुले पार गर्ने स्थानान्तरण (s) को मान दिन्छ।"
  },
  {
    q: "३. गुडिरहेको बसमा चालकले अचानक तीव्र ब्रेक लगाउँदा सिटमा बसेका यात्रुहरू कुन कारणले अगाडि हुत्तिन्छन् ?",
    opts: [
      "स्थिर इनर्सिया",
      "चाल इनर्सिया (Inertia of Motion)",
      "न्युटनको दोस्रो नियम",
      "इलास्टिक सीमा"
    ],
    ans: 1,
    exp: "बस रोकिँदा पैताला स्थिर हुन्छ तर शरीरको माथिल्लो भाग चाल इनर्सियाका कारण अगाडि नै हुत्तिन्छ।"
  },
  {
    q: "४. न्युटनको चालसम्बन्धी दोस्रो नियम अनुसार १ किलोग्राम पिण्डमा १ m/s² प्रवेग उत्पन्न गर्न कति बल चाहिन्छ ?",
    opts: [
      "०.५ न्युटन",
      "१ न्युटन (1 Newton)",
      "९.८ न्युटन",
      "१० न्युटन"
    ],
    ans: 1,
    exp: "१ न्युटनको परिभाषा नै १ kg पिण्डमा १ m/s² प्रवेग उत्पन्न गराउने बल हो (F = ma = 1 × 1 = 1 N)।"
  },
  {
    q: "५. ५० kg पिण्ड भएको साइकल २ m/s² को प्रवेगले ओरालो गुड्दा त्यसमा लागेको परिणामात्मक बल कति हुन्छ ?",
    opts: [
      "२५ न्युटन",
      "५२ न्युटन",
      "१०० न्युटन (100 N)",
      "१३० न्युटन"
    ],
    ans: 2,
    exp: "F = m × a = 50 kg × 2 m/s² = 100 N परिणामात्मक बल लाग्दछ।"
  },
  {
    q: "६. न्युटनको तेस्रो नियम (F_Action = -F_Reaction) का सन्दर्भमा तलको कुन भनाइ शतप्रतिशत सत्य हो ?",
    opts: [
      "क्रिया र प्रतिक्रियाले एकअर्कालाई सन्तुलित गरी रद्द गर्छन्",
      "क्रिया र प्रतिक्रिया दुई फरक फरक वस्तुहरूमा लाग्छन्",
      "क्रिया जहिले पनि प्रतिक्रियाभन्दा ठूलो हुन्छ",
      "प्रतिक्रिया पहिले लाग्छ र क्रिया पछि लाग्छ"
    ],
    ans: 1,
    exp: "क्रिया पहिलो वस्तुले दोस्रोमा र प्रतिक्रिया दोस्रोले पहिलोमा लगाउँछ; दुई भिन्न वस्तुमा लाग्ने हुँदा यिनीहरू रद्द हुँदैनन्।"
  },
  {
    q: "७. गति-समय ग्राफ मुनिको बन्द क्षेत्रफल (Area under v-t graph) ले केको मान दिन्छ ?",
    opts: [
      "प्रवेग",
      "पार गरेको स्थानान्तरण / दूरी",
      "लागेको बल",
      "गतिह्रास"
    ],
    ans: 1,
    exp: "Area = Velocity × Time = Displacement (s) हुन्छ।"
  },
  {
    q: "८. विरूपक बल हटाउँदा वस्तु पुनः सुरुको आकारमा फर्कने गुणलाई के भनिन्छ ?",
    opts: [
      "प्लास्टिसिटी",
      "इलास्टिसिटी (Elasticity)",
      "इनर्सिया",
      "संवेग"
    ],
    ans: 1,
    exp: "विरूपक बल हटाउँदा आन्तरिक रिस्टोरिङ बलले वस्तुलाई पुरानै आकारमा फर्काउने गुण इलास्टिसिटी हो।"
  },
  {
    q: "९. पानीको सतहबाट १९.६ मिटर अग्लो पुलबाट ढुङ्गा खसाल्दा पानीमा आइपुग्न कति समय लाग्छ (g = 9.8 m/s²) ?",
    opts: [
      "१ सेकेन्ड",
      "२ सेकेन्ड (2 s)",
      "३ सेकेन्ड",
      "४ सेकेन्ड"
    ],
    ans: 1,
    exp: "h = ½gt² ⟹ 19.6 = 4.9t² ⟹ t² = 4 ⟹ t = 2 सेकेन्ड।"
  },
  {
    q: "१०. क्रिकेट खेलाडीले क्याच समात्दा हात पछाडि तान्दा कुन भौतिक प्रभावका कारण हातमा चोट लाग्दैन ?",
    opts: [
      "रोकिने समय बढाई संवेग परिवर्तनको दर र ठक्कर बल घट्छ",
      "बलको पिण्ड घट्छ",
      "गुरुत्व बल शून्य हुन्छ",
      "स्थिर इनर्सिया बढ्छ"
    ],
    ans: 0,
    exp: "F = Δp/t अनुसार रोकिने समय (t) बढाउँदा संवेग परिवर्तनको दर घटेर हत्केलामा लाग्ने बल न्यूनतम हुन्छ।"
  }
];

function renderC9U7Quiz() {
  const container = document.getElementById('c9u7-quiz-container');
  if (!container) return;

  let score = 0;
  let answeredCount = 0;

  let html = '';
  C9U7_QUIZ_DATA.forEach((item, qIdx) => {
    const userAns = c9u7QuizAnswers[qIdx];
    const isAnswered = userAns !== undefined;
    const isCorrect = userAns === item.ans;

    if (isAnswered) {
      answeredCount++;
      if (isCorrect) score++;
    }

    let borderClass = 'border-slate-200';
    if (isAnswered) {
      borderClass = isCorrect ? 'border-emerald-300 bg-emerald-50/20' : 'border-rose-300 bg-rose-50/20';
    }

    html += `
      <div class="bg-white border ${borderClass} rounded-3xl p-5 shadow-sm space-y-3">
        <div class="flex items-center justify-between">
          <span class="text-xs font-bold px-2.5 py-1 rounded-full ${isAnswered ? (isCorrect ? 'bg-emerald-100 text-emerald-800' : 'bg-rose-100 text-rose-800') : 'bg-slate-100 text-slate-700'}">
            प्रश्न ${qIdx + 1} • वस्तुगत
          </span>
          ${isAnswered ? (isCorrect ? '<span class="text-xs text-emerald-600 font-bold">✓ सही उत्तर (+१)</span>' : '<span class="text-xs text-rose-600 font-bold">✗ गलत उत्तर (०)</span>') : '<span class="text-xs text-slate-400">उत्तर छनोट गर्नुहोस्</span>'}
        </div>

        <h4 class="text-sm md:text-base font-bold text-slate-900">${item.q}</h4>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
          ${item.opts.map((opt, optIdx) => {
            let optClass = 'bg-slate-50 border-slate-200 hover:bg-slate-100 text-slate-700';
            if (isAnswered) {
              if (optIdx === item.ans) {
                optClass = 'bg-emerald-100 border-emerald-400 text-emerald-950 font-bold';
              } else if (optIdx === userAns) {
                optClass = 'bg-rose-100 border-rose-400 text-rose-950 font-bold';
              } else {
                optClass = 'bg-slate-50 border-slate-100 text-slate-400 opacity-60';
              }
            }

            return `
              <button onclick="selectC9U7QuizOption(${qIdx}, ${optIdx})" class="p-3 rounded-2xl border text-left text-xs md:text-sm transition cursor-pointer flex items-center gap-2 ${optClass}">
                <span class="w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold ${optIdx === item.ans && isAnswered ? 'bg-emerald-600 text-white' : 'bg-slate-200 text-slate-700'}">
                  ${String.fromCharCode(65 + optIdx)}
                </span>
                <span class="flex-1">${opt}</span>
              </button>
            `;
          }).join('')}
        </div>

        ${isAnswered ? `
          <div class="p-3 rounded-2xl ${isCorrect ? 'bg-emerald-50 border border-emerald-200 text-emerald-900' : 'bg-rose-50 border border-rose-200 text-rose-900'} text-xs space-y-1 mt-2">
            <strong>💡 व्याख्या:</strong>
            <p>${item.exp}</p>
          </div>
        ` : ''}
      </div>
    `;
  });

  container.innerHTML = html;

  const toNepaliNumC9U7 = (n) => {
    const d = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९'];
    return String(n).split('').map(c => d[parseInt(c, 10)] || c).join('');
  };
  const scoreBadge = document.getElementById('c9u7-quiz-score-badge');
  if (scoreBadge) {
    scoreBadge.textContent = `${toNepaliNumC9U7(score)} / १०`;
  }
}

function selectC9U7QuizOption(qIdx, optIdx) {
  if (c9u7QuizAnswers[qIdx] !== undefined) return;
  c9u7QuizAnswers[qIdx] = optIdx;

  const isCorrect = optIdx === C9U7_QUIZ_DATA[qIdx].ans;
  if (isCorrect) playAudioC9U7('correct');
  else playAudioC9U7('wrong');

  renderC9U7Quiz();
}

function resetC9U7Quiz() {
  c9u7QuizAnswers = {};
  playAudioC9U7('click');
  renderC9U7Quiz();
}

// -------------------------------------------------------------------------
// Initialization Entrypoint for Unit 7
// -------------------------------------------------------------------------
function initC9U7() {
  updateKinematicsSimC9U7();
  setGraphTypeC9U7('st_graph');
  setNewtonLawC9U7(1);
  renderC9U7Quiz();
}

// Ensure startup trigger if active
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    if (typeof currentGrade !== 'undefined' && currentGrade === 9 && typeof activeUnit9 !== 'undefined' && activeUnit9 === 7 && typeof initC9U7 === 'function') {
      initC9U7();
    }
  });
}
""")

with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(js_parts) + '\n')

print("Created " + output_path + " successfully!")
