
    function setTab(tabName) {
      ['concepts', 'exercises', 'tiers', 'quiz'].forEach(t => {
        const view = document.getElementById('view-' + t);
        const btn = document.getElementById('tab-' + t);
        if (view) view.classList.add('hidden');
        if (btn) btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap';
      });
      const activeView = document.getElementById('view-' + tabName);
      const activeBtn = document.getElementById('tab-' + tabName);
      if (activeView) activeView.classList.remove('hidden');
      if (activeBtn) activeBtn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap';
      if (window.MathJax && window.MathJax.Hub && activeView) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, activeView]);
      }
    }

    function showExSection(secId) {
      ['ex1_1', 'ex1_2', 'ex_proj', 'ex1_3', 'ex_mix'].forEach(s => {
        const sec = document.getElementById('sec-' + s);
        const btn = document.getElementById('btn-' + s);
        if (sec) sec.classList.add('hidden');
        if (btn) btn.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-slate-100 text-slate-700 hover:bg-slate-200';
      });
      const activeSec = document.getElementById('sec-' + secId);
      const activeBtn = document.getElementById('btn-' + secId);
      if (activeSec) activeSec.classList.remove('hidden');
      if (activeBtn) activeBtn.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-blue-600 text-white shadow-xs';
      if (window.MathJax && window.MathJax.Hub && activeSec) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, activeSec]);
      }
    }

    function checkQuiz(qIdx, selected, correct, exp) {
      const fb = document.getElementById('qfb-' + qIdx);
      fb.classList.remove('hidden', 'bg-green-100', 'text-green-800', 'bg-red-100', 'text-red-800');
      for (let i = 0; i < 4; i++) {
        const b = document.getElementById('qbtn-' + qIdx + '-' + i);
        if (b) {
          b.classList.remove('border-green-500', 'bg-green-50', 'border-red-500', 'bg-red-50');
          if (i === correct) b.classList.add('border-green-500', 'bg-green-50');
        }
      }
      if (selected === correct) {
        fb.classList.add('bg-green-100', 'text-green-800');
        fb.innerHTML = '✓ स्याबास! सही उत्तर। <br><span class=\"font-normal text-xs text-green-700\">' + exp + '</span>';
      } else {
        fb.classList.add('bg-red-100', 'text-red-800');
        fb.innerHTML = '✗ गलत उत्तर। सही उत्तर विकल्प (' + String.fromCharCode(65 + correct) + ') हो।<br><span class=\"font-normal text-xs text-red-700\">' + exp + '</span>';
      }
    }

    // Search filter
    document.getElementById("search-input").addEventListener("input", (e) => {
      const val = e.target.value.toLowerCase();
      const buttons = document.querySelectorAll("#chapter-list button");
      buttons.forEach(b => {
        b.style.display = b.innerText.toLowerCase().includes(val) ? "flex" : "none";
      });
    });
  
    function switchChapter(chNum) {
      try { localStorage.setItem('class6_last_ch', chNum); } catch(e){}
      const b1 = document.getElementById('side-ch-1');
      const b2 = document.getElementById('side-ch-2');
      const b3 = document.getElementById('side-ch-3');
      const b4 = document.getElementById('side-ch-4');
      const b5 = document.getElementById('side-ch-5');
      const b6 = document.getElementById('side-ch-6');
      const b7 = document.getElementById('side-ch-7');
      const b8 = document.getElementById('side-ch-8');
      const b9 = document.getElementById('side-ch-9');
      const b10 = document.getElementById('side-ch-10');
      const b11 = document.getElementById('side-ch-11');
      const b12 = document.getElementById('side-ch-12');
      const b13 = document.getElementById('side-ch-13');
      const b14 = document.getElementById('side-ch-14');
      const b15 = document.getElementById('side-ch-15');
      const b16 = document.getElementById('side-ch-16');
      const b17 = document.getElementById('side-ch-17');
      const b18 = document.getElementById('side-ch-18');
      const b19 = document.getElementById('side-ch-19');
      const b20 = document.getElementById('side-ch-20');
      const v1 = document.getElementById('chapter-view-1');
      const v2 = document.getElementById('chapter-view-2');
      const v3 = document.getElementById('chapter-view-3');
      const v4 = document.getElementById('chapter-view-4');
      const v5 = document.getElementById('chapter-view-5');
      const v6 = document.getElementById('chapter-view-6');
      const v7 = document.getElementById('chapter-view-7');
      const v8 = document.getElementById('chapter-view-8');
      const v9 = document.getElementById('chapter-view-9');
      const v10 = document.getElementById('chapter-view-10');
      const v11 = document.getElementById('chapter-view-11');
      const v12 = document.getElementById('chapter-view-12');
      const v13 = document.getElementById('chapter-view-13');
      const v14 = document.getElementById('chapter-view-14');
      const v15 = document.getElementById('chapter-view-15');
      const v16 = document.getElementById('chapter-view-16');
      const v17 = document.getElementById('chapter-view-17');
      const v18 = document.getElementById('chapter-view-18');
      const v19 = document.getElementById('chapter-view-19');
      const v20 = document.getElementById('chapter-view-20');

      const sideActive = 'w-full text-left px-3.5 py-2.5 rounded-xl transition flex items-center justify-between text-xs md:text-sm bg-blue-600 text-white font-bold shadow-sm';
      const sideInactive = 'w-full text-left px-3.5 py-2 rounded-xl transition flex items-center justify-between text-xs md:text-sm hover:bg-slate-100 text-slate-700 font-medium';

      if (b1) b1.className = (chNum === 1) ? sideActive : sideInactive;
      if (b2) b2.className = (chNum === 2) ? sideActive : sideInactive;
      if (b3) b3.className = (chNum === 3) ? sideActive : sideInactive;
      if (b4) b4.className = (chNum === 4) ? sideActive : sideInactive;
      if (b5) b5.className = (chNum === 5) ? sideActive : sideInactive;
      if (b6) b6.className = (chNum === 6) ? sideActive : sideInactive;
      if (b7) b7.className = (chNum === 7) ? sideActive : sideInactive;
      if (b8) b8.className = (chNum === 8) ? sideActive : sideInactive;
      if (b9) b9.className = (chNum === 9) ? sideActive : sideInactive;
      if (b10) b10.className = (chNum === 10) ? sideActive : sideInactive;
      if (b11) b11.className = (chNum === 11) ? sideActive : sideInactive;
      if (b12) b12.className = (chNum === 12) ? sideActive : sideInactive;
      if (b13) b13.className = (chNum === 13) ? sideActive : sideInactive;
      if (b14) b14.className = (chNum === 14) ? sideActive : sideInactive;
      if (b15) b15.className = (chNum === 15) ? sideActive : sideInactive;
      if (b16) b16.className = (chNum === 16) ? sideActive : sideInactive;
      if (b17) b17.className = (chNum === 17) ? sideActive : sideInactive;
      if (b18) b18.className = (chNum === 18) ? sideActive : sideInactive;
      if (b19) b19.className = (chNum === 19) ? sideActive : sideInactive;
      if (b20) b20.className = (chNum === 20) ? sideActive : sideInactive;

      if (v1) v1.classList.toggle('hidden', chNum !== 1);
      if (v2) v2.classList.toggle('hidden', chNum !== 2);
      if (v3) v3.classList.toggle('hidden', chNum !== 3);
      if (v4) v4.classList.toggle('hidden', chNum !== 4);
      if (v5) v5.classList.toggle('hidden', chNum !== 5);
      if (v6) v6.classList.toggle('hidden', chNum !== 6);
      if (v7) v7.classList.toggle('hidden', chNum !== 7);
      if (v8) v8.classList.toggle('hidden', chNum !== 8);
      if (v9) v9.classList.toggle('hidden', chNum !== 9);
      if (v10) v10.classList.toggle('hidden', chNum !== 10);
      if (v11) v11.classList.toggle('hidden', chNum !== 11);
      if (v12) v12.classList.toggle('hidden', chNum !== 12);
      if (v13) v13.classList.toggle('hidden', chNum !== 13);
      if (v14) v14.classList.toggle('hidden', chNum !== 14);
      if (v15) v15.classList.toggle('hidden', chNum !== 15);
      if (v16) v16.classList.toggle('hidden', chNum !== 16);
      if (v17) v17.classList.toggle('hidden', chNum !== 17);
      if (v18) v18.classList.toggle('hidden', chNum !== 18);
      if (v19) v19.classList.toggle('hidden', chNum !== 19);
      if (v20) v20.classList.toggle('hidden', chNum !== 20);

      if (chNum === 1) {
        setTab('concepts');
        if (window.MathJax && window.MathJax.Hub && v1) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v1]);
      } else if (chNum === 2) {
        setTabCh2('concepts');
        if (window.MathJax && window.MathJax.Hub && v2) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v2]);
      } else if (chNum === 3) {
        setTabCh3('concepts');
        if (window.MathJax && window.MathJax.Hub && v3) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v3]);
      } else if (chNum === 4) {
        setTabCh4('concepts');
        if (window.MathJax && window.MathJax.Hub && v4) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v4]);
      } else if (chNum === 5) {
        setTabCh5('concepts');
        if (window.MathJax && window.MathJax.Hub && v5) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v5]);
      } else if (chNum === 6) {
        setTabCh6('concepts');
        if (window.MathJax && window.MathJax.Hub && v6) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v6]);
      } else if (chNum === 7) {
        setTabCh7('concepts');
        runCh7Calc();
        if (window.MathJax && window.MathJax.Hub && v7) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v7]);
      } else if (chNum === 8) {
        setTabCh8('concepts');
        runCh8Calc();
        if (window.MathJax && window.MathJax.Hub && v8) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v8]);
      } else if (chNum === 9) {
        setTabCh9('concepts');
        runCh9Convert();
        if (window.MathJax && window.MathJax.Hub && v9) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v9]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v9);
        }
      } else if (chNum === 10) {
        setTabCh10('concepts');
        runCh10Calc();
        if (window.MathJax && window.MathJax.Hub && v10) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v10]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v10);
        }
      } else if (chNum === 11) {
        setTabCh11('concepts');
        runCh11Calc();
        if (window.MathJax && window.MathJax.Hub && v11) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v11]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v11);
        }
      } else if (chNum === 12) {
        setTabCh12('concepts');
        runCh12Lab();
        if (window.MathJax && window.MathJax.Hub && v12) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v12]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v12);
        }
      } else if (chNum === 13) {
        setTabCh13('concepts');
        runCh13Lab();
        if (window.MathJax && window.MathJax.Hub && v13) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v13]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v13);
        }
      } else if (chNum === 14) {
        setTabCh14('concepts');
        runCh14Lab();
        if (window.MathJax && window.MathJax.Hub && v14) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v14]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v14);
        }
      } else if (chNum === 15) {
        if (typeof setTabCh15 === 'function') setTabCh15('concepts');
        if (typeof updateTriangleLab === 'function') updateTriangleLab();
        if (typeof setQuadType === 'function') setQuadType('rectangle');
        if (window.MathJax && window.MathJax.Hub && v15) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v15]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v15);
        }
      } else if (chNum === 16) {
        if (typeof setTabCh16 === 'function') setTabCh16('concepts');
        if (typeof updateCircleLab === 'function') updateCircleLab();
        if (window.MathJax && window.MathJax.Hub && v16) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v16]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v16);
        }
      } else if (chNum === 17) {
        if (typeof setTabCh17 === 'function') setTabCh17('concepts');
        if (typeof updatePolyLab === 'function') updatePolyLab();
        if (window.MathJax && window.MathJax.Hub && v17) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v17]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v17);
        }
      } else if (chNum === 18) {
        if (typeof setTabCh18 === 'function') setTabCh18('concepts');
        if (typeof renderCartesianGrid === 'function') renderCartesianGrid();
        if (typeof plotPoint === 'function') plotPoint(3, 4);
        if (window.MathJax && window.MathJax.Hub && v18) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v18]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v18);
        }
      } else if (chNum === 19) {
        if (typeof setTabCh19 === 'function') setTabCh19('concepts');
        if (typeof renderSymmetryShape === 'function') renderSymmetryShape();
        if (typeof renderTessellation === 'function') renderTessellation();
        if (window.MathJax && window.MathJax.Hub && v19) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v19]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v19);
        }
      } else if (chNum === 20) {
        if (typeof setTabCh20 === 'function') setTabCh20('concepts');
        if (typeof renderBarStudio === 'function') renderBarStudio();
        if (window.MathJax && window.MathJax.Hub && v20) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v20]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(v20);
        }
      }
    }

    function setTabCh4(tabName) {
      ['concepts', 'exercises', 'tiers', 'quiz'].forEach(t => {
        const view = document.getElementById('ch4-view-' + t);
        const btn = document.getElementById('ch4-tab-' + t);
        if (view) view.classList.add('hidden');
        if (btn) btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap';
      });
      const activeView = document.getElementById('ch4-view-' + tabName);
      const activeBtn = document.getElementById('ch4-tab-' + tabName);
      if (activeView) activeView.classList.remove('hidden');
      if (activeBtn) activeBtn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap';
      if (window.MathJax && window.MathJax.Hub && activeView) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, activeView]);
      }
    }

    function setExerciseCh4(exId) {
      const allEx = ['ex4_1', 'ex4_2', 'ex4_3', 'ex4_4_1', 'ex4_4_2', 'ex4_5'];
      allEx.forEach(e => {
        const sec = document.getElementById('ch4-sec-' + e);
        const pill = document.getElementById('ch4-pill-' + e);
        if (sec) sec.classList.add('hidden');
        if (pill) pill.className = 'px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap';
      });
      const curSec = document.getElementById('ch4-sec-' + exId);
      const curPill = document.getElementById('ch4-pill-' + exId);
      if (curSec) curSec.classList.remove('hidden');
      if (curPill) curPill.className = 'px-4 py-2 rounded-xl bg-blue-600 text-white shadow-xs whitespace-nowrap';
      if (window.MathJax && window.MathJax.Hub && curSec) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, curSec]);
      }
    }

    const ch4QuizData = [
      { correct: 2, exp: "उचित भिन्नमा अंश हरभन्दा सानो ($4 < 7$) हुन्छ र मान १ भन्दा कम हुन्छ।" },
      { correct: 1, exp: "हरहरूको ल.स. ६ हो: $\\frac{2}{6} + \\frac{1}{6} = \\frac{3}{6} = \\frac{1}{2}$।" },
      { correct: 0, exp: "अंश र हर गुणन गर्दा: $\\frac{3 \\times 10}{5 \\times 9} = \\frac{30}{45} = \\frac{2}{3}$।" },
      { correct: 1, exp: "व्युत्क्रम भिन्नले गुणन गर्दा: $\\frac{4}{7} \\times \\frac{7}{2} = \\frac{4}{2} = 2$।" }
    ];

    function checkQuizCh4(qIdx, selected) {
      const data = ch4QuizData[qIdx];
      const expBox = document.getElementById('ch4-qexp-' + qIdx);
      const badge = document.getElementById('ch4-qbadge-' + qIdx);
      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById('ch4-qbtn-' + qIdx + '-' + i);
        if (btn) {
          if (i === data.correct) {
            btn.className = 'w-full text-left p-2.5 rounded-xl border border-emerald-500 bg-emerald-50 text-emerald-900 font-bold';
          } else if (i === selected) {
            btn.className = 'w-full text-left p-2.5 rounded-xl border border-rose-500 bg-rose-50 text-rose-900';
          } else {
            btn.className = 'w-full text-left p-2.5 rounded-xl border border-slate-200 text-slate-500 opacity-60';
          }
        }
      }
      if (expBox) {
        expBox.classList.remove('hidden');
        if (selected === data.correct) {
          expBox.className = 'p-3 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-900 text-xs';
          expBox.innerHTML = '<strong>✓ सही उत्तर!</strong> ' + data.exp;
          if (badge) {
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-100 text-emerald-800';
            badge.innerText = 'सही (Correct)';
          }
        } else {
          expBox.className = 'p-3 rounded-xl bg-rose-50 border border-rose-200 text-rose-900 text-xs';
          expBox.innerHTML = '<strong>✗ गलत उत्तर!</strong> सही उत्तर विकल्प (' + String.fromCharCode(65 + data.correct) + ') हो। ' + data.exp;
          if (badge) {
            badge.className = 'px-2 py-0.5 rounded text-[10px] font-bold bg-rose-100 text-rose-800';
            badge.innerText = 'गलत (Incorrect)';
          }
        }
        if (window.MathJax && window.MathJax.Hub) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, expBox]);
      }
    }

    function setTabCh3(tabName) {
      ['concepts', 'exercises', 'tiers', 'quiz'].forEach(t => {
        const view = document.getElementById('ch3-view-' + t);
        const btn = document.getElementById('ch3-tab-' + t);
        if (view) view.classList.add('hidden');
        if (btn) btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap';
      });
      const activeView = document.getElementById('ch3-view-' + tabName);
      const activeBtn = document.getElementById('ch3-tab-' + tabName);
      if (activeView) activeView.classList.remove('hidden');
      if (activeBtn) activeBtn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap';
      if (window.MathJax && window.MathJax.Hub && activeView) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, activeView]);
      }
    }

    function checkQuizCh3(qIdx, selected, correct, exp) {
      const fb = document.getElementById('ch3-qfb-' + qIdx);
      fb.classList.remove('hidden', 'bg-green-100', 'text-green-800', 'bg-red-100', 'text-red-800');
      for (let i = 0; i < 4; i++) {
        const b = document.getElementById('ch3-qbtn-' + qIdx + '-' + i);
        if (b) {
          b.classList.remove('border-green-500', 'bg-green-50', 'border-red-500', 'bg-red-50');
          if (i === correct) b.classList.add('border-green-500', 'bg-green-50');
        }
      }
      if (selected === correct) {
        fb.classList.add('bg-green-100', 'text-green-800');
        fb.innerHTML = '✓ स्याबास! सही उत्तर। <br><span class="font-normal text-xs text-green-700">' + exp + '</span>';
      } else {
        fb.classList.add('bg-red-100', 'text-red-800');
        fb.innerHTML = '✗ गलत उत्तर। सही उत्तर विकल्प (' + String.fromCharCode(65 + correct) + ') हो।<br><span class="font-normal text-xs text-red-700">' + exp + '</span>';
      }
    }

    function setTabCh2(tabName) {
      ['concepts', 'exercises', 'tiers', 'quiz'].forEach(t => {
        const view = document.getElementById('ch2-view-' + t);
        const btn = document.getElementById('ch2-tab-' + t);
        if (view) view.classList.add('hidden');
        if (btn) btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap';
      });
      const activeView = document.getElementById('ch2-view-' + tabName);
      const activeBtn = document.getElementById('ch2-tab-' + tabName);
      if (activeView) activeView.classList.remove('hidden');
      if (activeBtn) activeBtn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap';
      if (window.MathJax && window.MathJax.Hub && activeView) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, activeView]);
      }
    }

    function showExSectionCh2(secId) {
      ['ex2_1', 'ex2_2', 'ex2_3', 'ex2_4', 'ex2_5', 'ex2_6', 'ex2_7', 'ex2_8'].forEach(s => {
        const sec = document.getElementById('ch2-sec-' + s);
        const btn = document.getElementById('ch2-btn-' + s);
        if (sec) sec.classList.add('hidden');
        if (btn) btn.className = 'px-3.5 py-1.5 rounded-xl text-xs md:text-sm font-bold bg-slate-100 text-slate-700 hover:bg-slate-200';
      });
      const activeSec = document.getElementById('ch2-sec-' + secId);
      const activeBtn = document.getElementById('ch2-btn-' + secId);
      if (activeSec) activeSec.classList.remove('hidden');
      if (activeBtn) activeBtn.className = 'px-3.5 py-1.5 rounded-xl text-xs md:text-sm font-bold bg-blue-600 text-white shadow-xs';
      if (window.MathJax && window.MathJax.Hub && activeSec) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, activeSec]);
      }
    }

    function checkQuizCh2(qIdx, selected, correct, exp) {
      const fb = document.getElementById('ch2-qfb-' + qIdx);
      fb.classList.remove('hidden', 'bg-green-100', 'text-green-800', 'bg-red-100', 'text-red-800');
      for (let i = 0; i < 4; i++) {
        const b = document.getElementById('ch2-qbtn-' + qIdx + '-' + i);
        if (b) {
          b.classList.remove('border-green-500', 'bg-green-50', 'border-red-500', 'bg-red-50');
          if (i === correct) b.classList.add('border-green-500', 'bg-green-50');
        }
      }
      if (selected === correct) {
        fb.classList.add('bg-green-100', 'text-green-800');
        fb.innerHTML = '✓ स्याबास! सही उत्तर। <br><span class="font-normal text-xs text-green-700">' + exp + '</span>';
      } else {
        fb.classList.add('bg-red-100', 'text-red-800');
        fb.innerHTML = '✗ गलत उत्तर। सही उत्तर विकल्प (' + String.fromCharCode(65 + correct) + ') हो।<br><span class="font-normal text-xs text-red-700">' + exp + '</span>';
      }
    }

    // Check URL parameters for direct deep-linking
    
    function setTabCh5(tabName) {
      ['concepts', 'exercises', 'tiers', 'quiz'].forEach(t => {
        const view = document.getElementById('ch5-view-' + t);
        const btn = document.getElementById('ch5-tab-' + t);
        if (view) view.classList.add('hidden');
        if (btn) btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap';
      });
      const activeView = document.getElementById('ch5-view-' + tabName);
      const activeBtn = document.getElementById('ch5-tab-' + tabName);
      if (activeView) activeView.classList.remove('hidden');
      if (activeBtn) activeBtn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap';
      if (window.MathJax && window.MathJax.Hub && activeView) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, activeView]);
      }
    }

    function setExerciseCh5(exId) {
      const allEx = ['ex5_1', 'ex5_2', 'ex5_3'];
      allEx.forEach(e => {
        const sec = document.getElementById('ch5-sec-' + e);
        const pill = document.getElementById('ch5-pill-' + e);
        if (sec) sec.classList.add('hidden');
        if (pill) pill.className = 'px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap';
      });
      const curSec = document.getElementById('ch5-sec-' + exId);
      const curPill = document.getElementById('ch5-pill-' + exId);
      if (curSec) curSec.classList.remove('hidden');
      if (curPill) curPill.className = 'px-4 py-2 rounded-xl bg-blue-600 text-white shadow-xs whitespace-nowrap';
      if (window.MathJax && window.MathJax.Hub && curSec) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, curSec]);
      }
    }

    const ch5QuizData = [
      { correct: 1, exp: "हरमा १०० (२ वटा शून्य) भएकाले दायाँबाट २ स्थान बायाँ बिन्दु बस्छ: $\\frac{7}{100} = 0.07$।" },
      { correct: 1, exp: "१० ले गुणन गर्दा दशमलव बिन्दु १ स्थान दायाँ सर्दछ: $३.४५ \\times १० = ३४.५$।" },
      { correct: 0, exp: "१०० ले भाग गर्दा दशमलव बिन्दु २ स्थान बायाँ सर्दछ: $२५.४ \\div १०० = ०.२५४$।" },
      { correct: 0, exp: "दशमलव बेवास्ता गरी गुणन गर्दा $५ \\times २ = १०$, कुल २ अङ्क अघि बिन्दु राख्दा $०.१० = ०.१$।" }
    ];

    function checkQuizCh5(qIdx, selected) {
      const data = ch5QuizData[qIdx];
      const expBox = document.getElementById('ch5-qexp-' + qIdx);
      const badge = document.getElementById('ch5-qbadge-' + qIdx);
      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById('ch5-qbtn-' + qIdx + '-' + i);
        if (btn) {
          if (i === data.correct) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-emerald-500 bg-emerald-50 text-emerald-900 font-bold';
          } else if (i === selected) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-rose-500 bg-rose-50 text-rose-900';
          } else {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 text-slate-500';
          }
        }
      }
      if (badge) {
        if (selected === data.correct) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-emerald-100 text-emerald-800';
          badge.textContent = '✓ सही उत्तर';
        } else {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-rose-100 text-rose-800';
          badge.textContent = '✗ गलत उत्तर';
        }
      }
      if (expBox) {
        expBox.classList.remove('hidden');
        if (selected === data.correct) {
          expBox.className = 'p-3 rounded-xl text-xs md:text-sm bg-emerald-50 border border-emerald-200 text-emerald-900';
          expBox.innerHTML = '<strong>✓ उत्कृष्ट! सही उत्तर:</strong> ' + data.exp;
        } else {
          expBox.className = 'p-3 rounded-xl text-xs md:text-sm bg-rose-50 border border-rose-200 text-rose-900';
          expBox.innerHTML = '<strong>✗ गलत उत्तर!</strong> सही विकल्प (' + String.fromCharCode(65 + data.correct) + ') हो। <br>' + data.exp;
        }
        if (window.MathJax && window.MathJax.Hub) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, expBox]);
        }
      }
    }

    function resetQuizCh5() {
      for (let q = 0; q < 4; q++) {
        for (let i = 0; i < 4; i++) {
          const btn = document.getElementById('ch5-qbtn-' + q + '-' + i);
          if (btn) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium';
          }
        }
        const badge = document.getElementById('ch5-qbadge-' + q);
        if (badge) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600';
          badge.textContent = 'हल हुन बाँकी';
        }
        const expBox = document.getElementById('ch5-qexp-' + q);
        if (expBox) {
          expBox.classList.add('hidden');
          expBox.innerHTML = '';
        }
      }
    }


    function setTabCh6(tabName) {
      ['concepts', 'exercises', 'tiers', 'quiz'].forEach(t => {
        const view = document.getElementById('ch6-view-' + t);
        const btn = document.getElementById('ch6-tab-' + t);
        if (view) view.classList.add('hidden');
        if (btn) btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap';
      });
      const activeView = document.getElementById('ch6-view-' + tabName);
      const activeBtn = document.getElementById('ch6-tab-' + tabName);
      if (activeView) activeView.classList.remove('hidden');
      if (activeBtn) activeBtn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap';
      if (window.MathJax && window.MathJax.Hub && activeView) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, activeView]);
      }
    }

    function setExerciseCh6(secId) {
      ['sec1', 'sec2', 'sec3'].forEach(s => {
        const sec = document.getElementById('ch6-sec-' + s);
        const pill = document.getElementById('ch6-pill-' + s);
        if (sec) sec.classList.add('hidden');
        if (pill) pill.className = 'px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap';
      });
      const curSec = document.getElementById('ch6-sec-' + secId);
      const curPill = document.getElementById('ch6-pill-' + secId);
      if (curSec) curSec.classList.remove('hidden');
      if (curPill) curPill.className = 'px-4 py-2 rounded-xl bg-blue-600 text-white shadow-xs whitespace-nowrap';
      if (window.MathJax && window.MathJax.Hub && curSec) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, curSec]);
      }
    }

    function gcd(a, b) {
      return b === 0 ? a : gcd(b, a % b);
    }

    function updateCh6Visualizer(val) {
      val = parseInt(val) || 0;
      val = Math.max(0, Math.min(100, val));
      const badge = document.getElementById('ch6-vis-val-badge');
      const pbar = document.getElementById('ch6-progress-bar');
      const pText = document.getElementById('ch6-vis-pct');
      const dText = document.getElementById('ch6-vis-dec');
      const fText = document.getElementById('ch6-vis-frac');

      if (badge) badge.textContent = val + '%';
      if (pbar) {
        pbar.style.width = val + '%';
        pbar.textContent = val > 5 ? val + '%' : '';
      }
      if (pText) pText.textContent = val + '%';
      if (dText) dText.textContent = (val / 100).toFixed(2);
      if (fText) {
        if (val === 0) {
          fText.textContent = '0/1';
        } else {
          const g = gcd(val, 100);
          fText.textContent = (val / g) + '/' + (100 / g);
        }
      }
    }

    function runCh6Calc1() {
      const q = parseFloat(document.getElementById('calc1-qty').value) || 0;
      const p = parseFloat(document.getElementById('calc1-pct').value) || 0;
      const ans = (q * p) / 100;
      const res = document.getElementById('calc1-res');
      if (res) {
        res.innerHTML = 'उत्तर: <strong>' + q + ' को ' + p + '% = ' + ans + '</strong> (' + q + ' &times; ' + p + '/100 = ' + ans + ')';
      }
    }

    function runCh6Calc2() {
      const n = parseFloat(document.getElementById('calc2-num').value) || 0;
      const d = parseFloat(document.getElementById('calc2-den').value) || 1;
      const pct = (n / d) * 100;
      const dec = n / d;
      const res = document.getElementById('calc2-res');
      if (res) {
        res.innerHTML = 'उत्तर: <strong>' + n + '/' + d + ' = ' + pct.toFixed(2).replace(/\.00$/, '') + '%</strong> (दशमलव: ' + dec.toFixed(4).replace(/0+$/, '').replace(/\.$/, '') + ')';
      }
    }

    const ch6QuizData = [
      { correct: 2, exp: "$\\frac{3}{5} \\times 100\\% = 3 \\times 20\\% = 60\\%$।" },
      { correct: 0, exp: "रु. ८०० को १५% $= 800 \\times \\frac{15}{100} = 8 \\times 15 = \\text{रु. } 120$।" },
      { correct: 1, exp: "१०० ले गुणन गर्दा दशमलव बिन्दु २ स्थान दायाँ सर्दछ: $0.06 \\times 100\\% = 6\\%$।" },
      { correct: 1, exp: "फुटबल मन नपराउने विद्यार्थी $= 500 - 200 = 300$, प्रतिशत $= \\frac{300}{500} \\times 100\\% = 60\\%$।" }
    ];

    function checkQuizCh6(qIdx, selected) {
      const data = ch6QuizData[qIdx];
      const expBox = document.getElementById('ch6-qexp-' + qIdx);
      const badge = document.getElementById('ch6-qbadge-' + qIdx);
      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById('ch6-qbtn-' + qIdx + '-' + i);
        if (btn) {
          if (i === data.correct) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-emerald-500 bg-emerald-50 text-emerald-900 font-bold';
          } else if (i === selected) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-rose-500 bg-rose-50 text-rose-900';
          } else {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 text-slate-500';
          }
        }
      }
      if (badge) {
        if (selected === data.correct) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-emerald-100 text-emerald-800';
          badge.textContent = '✓ सही उत्तर';
        } else {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-rose-100 text-rose-800';
          badge.textContent = '✗ गलत उत्तर';
        }
      }
      if (expBox) {
        expBox.classList.remove('hidden');
        if (selected === data.correct) {
          expBox.className = 'p-3 rounded-xl text-xs md:text-sm bg-emerald-50 border border-emerald-200 text-emerald-900';
          expBox.innerHTML = '<strong>✓ उत्कृष्ट! सही उत्तर:</strong> ' + data.exp;
        } else {
          expBox.className = 'p-3 rounded-xl text-xs md:text-sm bg-rose-50 border border-rose-200 text-rose-900';
          expBox.innerHTML = '<strong>✗ गलत उत्तर!</strong> सही विकल्प (' + String.fromCharCode(65 + data.correct) + ') हो। <br>' + data.exp;
        }
        if (window.MathJax && window.MathJax.Hub) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, expBox]);
        }
      }
    }

    function resetQuizCh6() {
      for (let q = 0; q < 4; q++) {
        for (let i = 0; i < 4; i++) {
          const btn = document.getElementById('ch6-qbtn-' + q + '-' + i);
          if (btn) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium';
          }
        }
        const badge = document.getElementById('ch6-qbadge-' + q);
        if (badge) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600';
          badge.textContent = 'हल हुन बाँकी';
        }
        const expBox = document.getElementById('ch6-qexp-' + q);
        if (expBox) {
          expBox.classList.add('hidden');
          expBox.innerHTML = '';
        }
      }
    }



    
    // Explicit global bindings for interactive handlers
    window.setTabCh6 = setTabCh6;
    window.setExerciseCh6 = setExerciseCh6;
    window.updateCh6Visualizer = updateCh6Visualizer;
    window.runCh6Calc1 = runCh6Calc1;
    window.runCh6Calc2 = runCh6Calc2;
    window.checkQuizCh6 = checkQuizCh6;
    window.resetQuizCh6 = resetQuizCh6;
    window.switchChapter = switchChapter;
    window.setTabCh5 = setTabCh5;
    window.setExerciseCh5 = setExerciseCh5;
    window.checkQuizCh5 = checkQuizCh5;
    window.resetQuizCh5 = resetQuizCh5;

    
    function setTabCh7(tabName) {
      ['concepts', 'exercises', 'tiers', 'quiz'].forEach(t => {
        const view = document.getElementById('ch7-view-' + t);
        const btn = document.getElementById('ch7-tab-' + t);
        if (view) view.classList.add('hidden');
        if (btn) btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
      });
      const activeView = document.getElementById('ch7-view-' + tabName);
      const activeBtn = document.getElementById('ch7-tab-' + tabName);
      if (activeView) activeView.classList.remove('hidden');
      if (activeBtn) activeBtn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
      if (window.MathJax && window.MathJax.Hub && activeView) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, activeView]);
      }
    }

    function setExerciseCh7(secId) {
      ['sec1', 'sec2', 'sec3'].forEach(s => {
        const sec = document.getElementById('ch7-sec-' + s);
        const pill = document.getElementById('ch7-pill-' + s);
        if (sec) sec.classList.add('hidden');
        if (pill) pill.className = 'px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap cursor-pointer';
      });
      const curSec = document.getElementById('ch7-sec-' + secId);
      const curPill = document.getElementById('ch7-pill-' + secId);
      if (curSec) curSec.classList.remove('hidden');
      if (curPill) curPill.className = 'px-4 py-2 rounded-xl bg-blue-600 text-white shadow-xs whitespace-nowrap cursor-pointer';
      if (window.MathJax && window.MathJax.Hub && curSec) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, curSec]);
      }
    }

    function setCh7Preset(cp, exp, sp) {
      const inCp = document.getElementById('ch7-in-cp');
      const inExp = document.getElementById('ch7-in-exp');
      const inSp = document.getElementById('ch7-in-sp');
      if (inCp) inCp.value = cp;
      if (inExp) inExp.value = exp;
      if (inSp) inSp.value = sp;
      runCh7Calc();
    }

    function runCh7Calc() {
      const inCp = document.getElementById('ch7-in-cp');
      const inExp = document.getElementById('ch7-in-exp');
      const inSp = document.getElementById('ch7-in-sp');
      const res = document.getElementById('ch7-calc-res');
      if (!res) return;

      const cp = parseFloat(inCp ? inCp.value : 0) || 0;
      const exp = parseFloat(inExp ? inExp.value : 0) || 0;
      const sp = parseFloat(inSp ? inSp.value : 0) || 0;
      const totalCp = cp + exp;

      if (totalCp <= 0) {
        res.innerHTML = '<div class="text-amber-300 font-bold text-sm">कृपया मान्य खरिद मूल्य प्रविष्ट गर्नुहोस्।</div>';
        return;
      }

      let statusHtml = '';
      if (sp > totalCp) {
        const profit = sp - totalCp;
        const profitPct = (profit / totalCp) * 100;
        statusHtml = `
          <div class="flex flex-wrap items-center justify-between gap-2 border-b border-emerald-400/30 pb-3">
            <span class="px-3 py-1 rounded-xl bg-emerald-500/20 text-emerald-300 font-bold text-xs border border-emerald-400/30">व्यापार स्थिति: नाफा (Profit)</span>
            <span class="text-xs text-blue-200">अवस्था: S.P. (${sp}) > C.P. (${totalCp})</span>
          </div>
          <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-center pt-2">
            <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">जम्मा क्रय मूल्य</span><span class="text-lg font-mono font-bold">रु. ${totalCp}</span></div>
            <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">विक्रय मूल्य</span><span class="text-lg font-mono font-bold">रु. ${sp}</span></div>
            <div class="bg-emerald-500/20 border border-emerald-400/40 p-2.5 rounded-xl"><span class="text-xs text-emerald-200 block">नाफा रकम</span><span class="text-lg font-mono font-bold text-emerald-300">+ रु. ${profit.toFixed(2).replace(/\.00$/, '')}</span></div>
            <div class="bg-emerald-500/20 border border-emerald-400/40 p-2.5 rounded-xl"><span class="text-xs text-emerald-200 block">नाफा प्रतिशत</span><span class="text-lg font-mono font-bold text-emerald-300">+ ${profitPct.toFixed(2).replace(/\.00$/, '')}%</span></div>
          </div>
          <p class="text-xs text-blue-100 bg-white/5 p-2 rounded-lg mt-2">
            <strong>गणना व्याख्या:</strong> नाफा = ${sp} - ${totalCp} = रु. ${profit.toFixed(2).replace(/\.00$/, '')} | नाफा % = (${profit.toFixed(2).replace(/\.00$/, '')} / ${totalCp}) × 100% = ${profitPct.toFixed(2).replace(/\.00$/, '')}%
          </p>
        `;
      } else if (totalCp > sp) {
        const loss = totalCp - sp;
        const lossPct = (loss / totalCp) * 100;
        statusHtml = `
          <div class="flex flex-wrap items-center justify-between gap-2 border-b border-rose-400/30 pb-3">
            <span class="px-3 py-1 rounded-xl bg-rose-500/20 text-rose-300 font-bold text-xs border border-rose-400/30">व्यापार स्थिति: नोक्सान / घाटा (Loss)</span>
            <span class="text-xs text-blue-200">अवस्था: C.P. (${totalCp}) > S.P. (${sp})</span>
          </div>
          <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-center pt-2">
            <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">जम्मा क्रय मूल्य</span><span class="text-lg font-mono font-bold">रु. ${totalCp}</span></div>
            <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">विक्रय मूल्य</span><span class="text-lg font-mono font-bold">रु. ${sp}</span></div>
            <div class="bg-rose-500/20 border border-rose-400/40 p-2.5 rounded-xl"><span class="text-xs text-rose-200 block">नोक्सान रकम</span><span class="text-lg font-mono font-bold text-rose-300">- रु. ${loss.toFixed(2).replace(/\.00$/, '')}</span></div>
            <div class="bg-rose-500/20 border border-rose-400/40 p-2.5 rounded-xl"><span class="text-xs text-rose-200 block">नोक्सान प्रतिशत</span><span class="text-lg font-mono font-bold text-rose-300">- ${lossPct.toFixed(2).replace(/\.00$/, '')}%</span></div>
          </div>
          <p class="text-xs text-blue-100 bg-white/5 p-2 rounded-lg mt-2">
            <strong>गणना व्याख्या:</strong> नोक्सान = ${totalCp} - ${sp} = रु. ${loss.toFixed(2).replace(/\.00$/, '')} | नोक्सान % = (${loss.toFixed(2).replace(/\.00$/, '')} / ${totalCp}) × 100% = ${lossPct.toFixed(2).replace(/\.00$/, '')}%
          </p>
        `;
      } else {
        statusHtml = `
          <div class="flex flex-wrap items-center justify-between gap-2 border-b border-white/20 pb-3">
            <span class="px-3 py-1 rounded-xl bg-slate-500/30 text-slate-200 font-bold text-xs border border-white/20">नाफा पनि छैन, नोक्सान पनि छैन</span>
            <span class="text-xs text-blue-200">C.P. (${totalCp}) = S.P. (${sp})</span>
          </div>
          <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-center pt-2">
            <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">जम्मा क्रय मूल्य</span><span class="text-lg font-mono font-bold">रु. ${totalCp}</span></div>
            <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">विक्रय मूल्य</span><span class="text-lg font-mono font-bold">रु. ${sp}</span></div>
            <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">नाफा/नोक्सान</span><span class="text-lg font-mono font-bold">रु. ०</span></div>
            <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">प्रतिशत</span><span class="text-lg font-mono font-bold">०%</span></div>
          </div>
        `;
      }
      res.innerHTML = statusHtml;
    }

    const ch7QuizData = [
      { correct: 1, exp: "विक्रय मूल्य क्रय मूल्यभन्दा बढी ($S.P. > C.P.$) भएको अवस्थामा नाफा हुन्छ।" },
      { correct: 2, exp: "नाफा $= 575 - 500 = 75$, नाफा प्रतिशत $= \\frac{75}{500} \\times 100\\% = 15\\%$।" },
      { correct: 0, exp: "१०% नोक्सान $= 1200 \\times 10\\% = 120$। विक्रय मूल्य $= 1200 - 120 = \\text{रु. } 1,080$।" },
      { correct: 1, exp: "जम्मा $C.P. = 3000 + 200 = 3200$। नाफा $= 3520 - 3200 = 320$। नाफा % $= \\frac{320}{3200} \\times 100\\% = 10\\%$।" },
      { correct: 1, exp: "१२ गोटाको $S.P. = 12 \\times 25 = 300$। नाफा $= 300 - 240 = \\text{रु. } 60$।" }
    ];

    function checkQuizCh7(qIdx, selected) {
      const data = ch7QuizData[qIdx];
      const expBox = document.getElementById('ch7-qexp-' + qIdx);
      const badge = document.getElementById('ch7-qbadge-' + qIdx);
      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById('ch7-qbtn-' + qIdx + '-' + i);
        if (btn) {
          if (i === data.correct) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-emerald-500 bg-emerald-50 text-emerald-900 font-bold';
          } else if (i === selected) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-rose-500 bg-rose-50 text-rose-900';
          } else {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 text-slate-500';
          }
        }
      }
      if (badge) {
        if (selected === data.correct) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-emerald-100 text-emerald-800';
          badge.textContent = '✓ सही उत्तर';
        } else {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-rose-100 text-rose-800';
          badge.textContent = '✗ गलत उत्तर';
        }
      }
      if (expBox) {
        expBox.classList.remove('hidden');
        if (selected === data.correct) {
          expBox.className = 'p-3 rounded-xl text-xs md:text-sm bg-emerald-50 border border-emerald-200 text-emerald-900';
          expBox.innerHTML = '<strong>✓ उत्कृष्ट! सही उत्तर:</strong> ' + data.exp;
        } else {
          expBox.className = 'p-3 rounded-xl text-xs md:text-sm bg-rose-50 border border-rose-200 text-rose-900';
          expBox.innerHTML = '<strong>✗ गलत उत्तर!</strong> सही विकल्प (' + String.fromCharCode(65 + data.correct) + ') हो। <br>' + data.exp;
        }
        if (window.MathJax && window.MathJax.Hub) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, expBox]);
        }
      }
    }

    function resetQuizCh7() {
      for (let q = 0; q < 5; q++) {
        for (let i = 0; i < 4; i++) {
          const btn = document.getElementById('ch7-qbtn-' + q + '-' + i);
          if (btn) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer';
          }
        }
        const badge = document.getElementById('ch7-qbadge-' + q);
        if (badge) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600';
          badge.textContent = 'हल हुन बाँकी';
        }
        const expBox = document.getElementById('ch7-qexp-' + q);
        if (expBox) {
          expBox.classList.add('hidden');
          expBox.innerHTML = '';
        }
      }
    }

    // Explicit window bindings
    window.setTabCh7 = setTabCh7;
    window.setExerciseCh7 = setExerciseCh7;
    window.setCh7Preset = setCh7Preset;
    window.runCh7Calc = runCh7Calc;
    window.checkQuizCh7 = checkQuizCh7;
    window.resetQuizCh7 = resetQuizCh7;

    
    function setTabCh8(tabName) {
      ['concepts', 'exercises', 'tiers', 'quiz'].forEach(t => {
        const view = document.getElementById('ch8-view-' + t);
        const btn = document.getElementById('ch8-tab-' + t);
        if (view) view.classList.add('hidden');
        if (btn) btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
      });
      const activeView = document.getElementById('ch8-view-' + tabName);
      const activeBtn = document.getElementById('ch8-tab-' + tabName);
      if (activeView) activeView.classList.remove('hidden');
      if (activeBtn) activeBtn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
      if (window.MathJax && window.MathJax.Hub && activeView) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, activeView]);
      }
    }

    function setExerciseCh8(secId) {
      ['sec1', 'sec2', 'sec3'].forEach(s => {
        const sec = document.getElementById('ch8-sec-' + s);
        const pill = document.getElementById('ch8-pill-' + s);
        if (sec) sec.classList.add('hidden');
        if (pill) pill.className = 'px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap cursor-pointer';
      });
      const curSec = document.getElementById('ch8-sec-' + secId);
      const curPill = document.getElementById('ch8-pill-' + secId);
      if (curSec) curSec.classList.remove('hidden');
      if (curPill) curPill.className = 'px-4 py-2 rounded-xl bg-blue-600 text-white shadow-xs whitespace-nowrap cursor-pointer';
      if (window.MathJax && window.MathJax.Hub && curSec) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, curSec]);
      }
    }

    function setCh8Preset(q1, c1, q2) {
      const inQ1 = document.getElementById('ch8-in-q1');
      const inC1 = document.getElementById('ch8-in-c1');
      const inQ2 = document.getElementById('ch8-in-q2');
      if (inQ1) inQ1.value = q1;
      if (inC1) inC1.value = c1;
      if (inQ2) inQ2.value = q2;
      runCh8Calc();
    }

    function runCh8Calc() {
      const inQ1 = document.getElementById('ch8-in-q1');
      const inC1 = document.getElementById('ch8-in-c1');
      const inQ2 = document.getElementById('ch8-in-q2');
      const res = document.getElementById('ch8-calc-res');
      if (!res) return;

      const q1 = parseFloat(inQ1 ? inQ1.value : 0) || 0;
      const c1 = parseFloat(inC1 ? inC1.value : 0) || 0;
      const q2 = parseFloat(inQ2 ? inQ2.value : 0) || 0;

      if (q1 <= 0) {
        res.innerHTML = '<div class="text-amber-300 font-bold text-sm">कृपया सुरुवाती वस्तुको मान्य सङ्ख्या (१ वा सोभन्दा बढी) प्रविष्ट गर्नुहोस्।</div>';
        return;
      }

      const unitCost = c1 / q1;
      const totalCost2 = unitCost * q2;

      const statusHtml = `
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-indigo-400/30 pb-3">
          <span class="px-3 py-1 rounded-xl bg-indigo-500/20 text-indigo-300 font-bold text-xs border border-indigo-400/30">ऐकिक नियम प्रत्यक्ष गणना नतिजा</span>
          <span class="text-xs text-blue-200">१ एकाइको दर = रु. ${unitCost.toFixed(2).replace(/\\.00$/, '')}</span>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-center pt-2">
          <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">सुरुवाती परिमाण (Q₁)</span><span class="text-lg font-mono font-bold">${q1}</span></div>
          <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">सुरुवाती मूल्य (C₁)</span><span class="text-lg font-mono font-bold">रु. ${c1}</span></div>
          <div class="bg-blue-500/20 border border-blue-400/40 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">१ एकाइको मूल्य (दर)</span><span class="text-lg font-mono font-bold text-blue-300">रु. ${unitCost.toFixed(2).replace(/\\.00$/, '')}</span></div>
          <div class="bg-emerald-500/20 border border-emerald-400/40 p-2.5 rounded-xl"><span class="text-xs text-emerald-200 block">माग परिमाण (${q2}) को मूल्य</span><span class="text-lg font-mono font-bold text-emerald-300">रु. ${totalCost2.toFixed(2).replace(/\\.00$/, '')}</span></div>
        </div>
        <p class="text-xs text-blue-100 bg-white/5 p-2.5 rounded-lg mt-2 leading-relaxed">
          <strong>चरणबद्ध समाधान विधि:</strong><br>
          १. भाग क्रिया (१ एकाइको मान निकाल्ने): ${q1} वटाको मूल्य = रु. ${c1} $\\Rightarrow$ १ वटाको मूल्य = $\\frac{${c1}}{${q1}} =$ <strong>रु. ${unitCost.toFixed(2).replace(/\\.00$/, '')}</strong><br>
          २. गुणन क्रिया (${q2} वटाको मान निकाल्ने): ${q2} वटाको मूल्य = ${unitCost.toFixed(2).replace(/\\.00$/, '')} $\\times$ ${q2} = <strong>रु. ${totalCost2.toFixed(2).replace(/\\.00$/, '')}</strong>
        </p>
      `;
      res.innerHTML = statusHtml;
      if (window.MathJax && window.MathJax.Hub) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, res]);
      }
    }

    const ch8QuizData = [
      { correct: 2, exp: "१ ओटाको मूल्य $= \\frac{75}{5} = \\text{रु. } 15$।" },
      { correct: 0, exp: "१ दर्जन $= 12$ ओटा, १ ओटाको $= \\frac{480}{12} = 40$, ८ ओटाको $= 40 \\times 8 = \\text{रु. } 320$।" },
      { correct: 1, exp: "१ ओटा ब्याटको $= \\frac{900}{6} = 150$, ४ ओटाको $= 150 \\times 4 = \\text{रु. } 600$।" },
      { correct: 2, exp: "१ ओटा कुर्सीको $= \\frac{4800}{4} = 1200$, ७ ओटाको $= 1200 \\times 7 = \\text{रु. } 8,400$।" },
      { correct: 1, exp: "ऐकिक नियममा पहिले भाग गरी १ एकाइको मान निकालिन्छ र त्यसपछि गुणन गरी माग गरिएको सङ्ख्याको मान निकालिन्छ।" }
    ];

    function checkQuizCh8(qIdx, selected) {
      const data = ch8QuizData[qIdx];
      const expBox = document.getElementById('ch8-qexp-' + qIdx);
      const badge = document.getElementById('ch8-qbadge-' + qIdx);
      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById('ch8-qbtn-' + qIdx + '-' + i);
        if (btn) {
          if (i === data.correct) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-emerald-500 bg-emerald-50 text-emerald-900 font-bold';
          } else if (i === selected) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-rose-500 bg-rose-50 text-rose-900';
          } else {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 text-slate-500';
          }
        }
      }
      if (badge) {
        if (selected === data.correct) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-emerald-100 text-emerald-800';
          badge.textContent = '✓ सही उत्तर';
        } else {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-rose-100 text-rose-800';
          badge.textContent = '✗ गलत उत्तर';
        }
      }
      if (expBox) {
        expBox.classList.remove('hidden');
        if (selected === data.correct) {
          expBox.className = 'p-3 rounded-xl text-xs md:text-sm bg-emerald-50 border border-emerald-200 text-emerald-900';
          expBox.innerHTML = '<strong>✓ उत्कृष्ट! सही उत्तर:</strong> ' + data.exp;
        } else {
          expBox.className = 'p-3 rounded-xl text-xs md:text-sm bg-rose-50 border border-rose-200 text-rose-900';
          expBox.innerHTML = '<strong>✗ गलत उत्तर!</strong> सही विकल्प (' + String.fromCharCode(65 + data.correct) + ') हो। <br>' + data.exp;
        }
        if (window.MathJax && window.MathJax.Hub) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, expBox]);
        }
      }
    }

    function resetQuizCh8() {
      for (let q = 0; q < 5; q++) {
        for (let i = 0; i < 4; i++) {
          const btn = document.getElementById('ch8-qbtn-' + q + '-' + i);
          if (btn) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer';
          }
        }
        const badge = document.getElementById('ch8-qbadge-' + q);
        if (badge) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600';
          badge.textContent = 'हल हुन बाँकी';
        }
        const expBox = document.getElementById('ch8-qexp-' + q);
        if (expBox) {
          expBox.classList.add('hidden');
          expBox.innerHTML = '';
        }
      }
    }

    // Explicit window bindings
    window.setTabCh8 = setTabCh8;
    window.setExerciseCh8 = setExerciseCh8;
    window.setCh8Preset = setCh8Preset;
    window.runCh8Calc = runCh8Calc;
    window.checkQuizCh8 = checkQuizCh8;
    window.resetQuizCh8 = resetQuizCh8;

    
    // ==========================================
    // OFFLINE SUPPORT & PWA ENGINE
    // ==========================================
    
    // 1. Service Worker Registration (PWA)
    if (typeof navigator !== 'undefined' && 'serviceWorker' in navigator && (window.location.protocol === 'http:' || window.location.protocol === 'https:')) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('./sw.js').then((reg) => {
          console.log('[PWA] Service Worker registered:', reg.scope);
        }).catch((err) => {
          console.log('[PWA] Service Worker registration note:', err);
        });
      });
    }

    // 2. PWA Install Prompt Handler
    let deferredPrompt;
    const pwaInstallBtn = document.getElementById('pwa-install-btn');
    window.addEventListener('beforeinstallprompt', (e) => {
      e.preventDefault();
      deferredPrompt = e;
      if (pwaInstallBtn) pwaInstallBtn.classList.remove('hidden');
    });

    if (pwaInstallBtn) {
      pwaInstallBtn.addEventListener('click', async () => {
        if (deferredPrompt) {
          deferredPrompt.prompt();
          const { outcome } = await deferredPrompt.userChoice;
          if (outcome === 'accepted') {
            pwaInstallBtn.classList.add('hidden');
          }
          deferredPrompt = null;
        } else {
          alert('यो एप इन्स्टल गर्न आफ्नो मोबाइल/ल्यापटप ब्राउजरको तीन थोप्ला मेनुमा गई "Add to Home screen" वा "Install app" रोज्नुहोस्।');
        }
      });
    }

    // 3. Built-in Pure-CSS Offline LaTeX Math Renderer
    function formatLaTeXText(s) {
      s = s.trim();
      let fracRegex = /\\frac\s*\{([^{}]+)\}\s*\{([^{}]+)\}/g;
      while (fracRegex.test(s)) {
        s = s.replace(fracRegex, '<span class="offline-frac"><span class="top">$1</span><span class="bot">$2</span></span>');
      }
      s = s.replace(/\\times/g, " × ")
           .replace(/\\div/g, " ÷ ")
           .replace(/\\pm/g, " ± ")
           .replace(/\\leq/g, " ≤ ")
           .replace(/\\geq/g, " ≥ ")
           .replace(/\\approx/g, " ≈ ")
           .replace(/\\ne/g, " ≠ ")
           .replace(/\\to|\\rightarrow/g, " → ")
           .replace(/\\Rightarrow/g, " ⇒ ")
           .replace(/\\quad/g, " &nbsp; ")
           .replace(/\\circ/g, "°")
           .replace(/\\%/g, "%")
           .replace(/\\text\{([^{}]+)\}/g, '<span style="font-style:normal;">$1</span>')
           .replace(/\^([0-9a-zA-Z]+)/g, "<sup>$1</sup>")
           .replace(/\^\{([^{}]+)\}/g, "<sup>$1</sup>")
           .replace(/_([0-9a-zA-Z]+)/g, "<sub>$1</sub>")
           .replace(/_\{([^{}]+)\}/g, "<sub>$1</sub>")
           .replace(/\\sqrt\{([^{}]+)\}/g, "√($1)");
      return s;
    }

    function renderOfflineMath(container) {
      const root = container || document.body;
      if (!root) return;

      const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null, false);
      const nodes = [];
      let n;
      while ((n = walker.nextNode())) {
        if (n.nodeValue && n.nodeValue.includes('$')) {
          const tag = n.parentNode ? n.parentNode.nodeName.toUpperCase() : '';
          if (tag !== 'SCRIPT' && tag !== 'STYLE' && tag !== 'TEXTAREA') {
            nodes.push(n);
          }
        }
      }

      nodes.forEach((tNode) => {
        const text = tNode.nodeValue;
        if (!text || !text.includes('$')) return;
        const parts = text.split(/(\$\$[\s\S]*?\$\$|\$[^$\n]+?\$)/g);
        if (parts.length <= 1) return;

        const fragment = document.createDocumentFragment();
        parts.forEach((part) => {
          if (part.startsWith('$$') && part.endsWith('$$') && part.length >= 4) {
            const math = part.slice(2, -2);
            const span = document.createElement('span');
            span.className = 'offline-math block my-2 text-center';
            span.innerHTML = formatLaTeXText(math);
            fragment.appendChild(span);
          } else if (part.startsWith('$') && part.endsWith('$') && part.length >= 2) {
            const math = part.slice(1, -1);
            const span = document.createElement('span');
            span.className = 'offline-math';
            span.innerHTML = formatLaTeXText(math);
            fragment.appendChild(span);
          } else if (part.length > 0) {
            fragment.appendChild(document.createTextNode(part));
          }
        });
        if (tNode.parentNode) {
          tNode.parentNode.replaceChild(fragment, tNode);
        }
      });
    }

    // Run offline math engine if MathJax is unavailable after timeout
    let mjLoaded = false;
    if (window.MathJax && window.MathJax.Hub) {
      window.MathJax.Hub.Queue(() => {
        mjLoaded = true;
      });
    }
    setTimeout(() => {
      if (!mjLoaded) {
        console.log('[Offline Math] Activating pure-CSS LaTeX offline math renderer...');
        renderOfflineMath(document.body);
      }
    }, 1200);

    window.renderOfflineMath = renderOfflineMath;

    
    // ==========================================
    // CHAPTER 9: DISTANCE (दूरी) INTERACTIVE LOGIC
    // ==========================================
    function setTabCh9(tab) {
      const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
      tabs.forEach(t => {
        const btn = document.getElementById('ch9-tab-' + t);
        const view = document.getElementById('ch9-view-' + t);
        if (btn && view) {
          if (t === tab) {
            btn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
            view.classList.remove('hidden');
          } else {
            btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
            view.classList.add('hidden');
          }
        }
      });
      if (tab === 'concepts') {
        runCh9Convert();
      }
      if (window.MathJax && window.MathJax.Hub) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub]);
      } else if (window.renderOfflineMath) {
        window.renderOfflineMath(document.getElementById('ch9-view-' + tab));
      }
    }

    function setExerciseCh9(sec) {
      const secs = ['sec1', 'sec2', 'sec3'];
      secs.forEach(s => {
        const btn = document.getElementById('ch9-ex-btn-' + s);
        const view = document.getElementById('ch9-ex-' + s);
        if (btn && view) {
          if (s === sec) {
            btn.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-blue-600 text-white shadow-xs transition cursor-pointer';
            view.classList.remove('hidden');
          } else {
            btn.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold text-slate-600 hover:bg-slate-100 transition cursor-pointer';
            view.classList.add('hidden');
          }
        }
      });
      if (window.MathJax && window.MathJax.Hub) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub]);
      } else if (window.renderOfflineMath) {
        window.renderOfflineMath(document.getElementById('ch9-ex-' + sec));
      }
    }

    function setCh9Preset(val, fromUnit, toUnit) {
      const inVal = document.getElementById('ch9-in-val');
      const inFrom = document.getElementById('ch9-in-from');
      const inTo = document.getElementById('ch9-in-to');
      if (inVal) inVal.value = val;
      if (inFrom) inFrom.value = fromUnit;
      if (inTo) inTo.value = toUnit;
      runCh9Convert();
    }

    function runCh9Convert() {
      const inVal = document.getElementById('ch9-in-val');
      const inFrom = document.getElementById('ch9-in-from');
      const inTo = document.getElementById('ch9-in-to');
      const res = document.getElementById('ch9-calc-res');
      if (!inVal || !inFrom || !inTo || !res) return;

      const val = parseFloat(inVal.value);
      const from = inFrom.value;
      const to = inTo.value;

      if (isNaN(val)) {
        res.innerHTML = '<span class="text-amber-300 text-xs">कृपया संख्यात्मक मान राख्नुहोस्।</span>';
        return;
      }

      // Direct CDC Formula calculation
      let targetVal = 0;
      let formulaStr = "";
      const key = from + "->" + to;

      if (from === to) {
        targetVal = val;
        formulaStr = "उही एकाइ भएकोले कुनै परिवर्तन आवश्यक छैन ($" + val + " " + from + "$)।";
      } else if (key === "m->cm") { targetVal = val * 100; formulaStr = "$" + val + " \\times 100 = " + targetVal + "\\text{ cm}$ (ठूलो $\\to$ सानो = गुणन)"; }
      else if (key === "cm->m") { targetVal = val / 100; formulaStr = "$" + val + " \\div 100 = " + targetVal + "\\text{ m}$ (सानो $\\to$ ठूलो = भाग)"; }
      else if (key === "m->ft") { targetVal = val * 3.28; formulaStr = "$" + val + " \\times 3.28 = " + targetVal.toFixed(3).replace(/\\.?0+$/, '') + "\\text{ ft}$"; }
      else if (key === "ft->m") { targetVal = val / 3.28; formulaStr = "$" + val + " \\div 3.28 = " + targetVal.toFixed(3).replace(/\\.?0+$/, '') + "\\text{ m}$"; }
      else if (key === "m->in") { targetVal = val * 39.37; formulaStr = "$" + val + " \\times 39.37 = " + targetVal.toFixed(2) + "\\text{ in}$"; }
      else if (key === "in->m") { targetVal = val / 39.37; formulaStr = "$" + val + " \\div 39.37 = " + targetVal.toFixed(3).replace(/\\.?0+$/, '') + "\\text{ m}$"; }
      else if (key === "ft->in") { targetVal = val * 12; formulaStr = "$" + val + " \\times 12 = " + targetVal + "\\text{ in}$ (१ फिट = १२ इन्च)"; }
      else if (key === "in->ft") { targetVal = val / 12; formulaStr = "$" + val + " \\div 12 = " + targetVal.toFixed(3).replace(/\\.?0+$/, '') + "\\text{ ft}$"; }
      else if (key === "in->cm") { targetVal = val * 2.54; formulaStr = "$" + val + " \\times 2.54 = " + targetVal.toFixed(2) + "\\text{ cm}$"; }
      else if (key === "cm->in") { targetVal = val / 2.54; formulaStr = "$" + val + " \\div 2.54 = " + targetVal.toFixed(2) + "\\text{ in}$"; }
      else if (key === "ft->cm") { targetVal = val * 30.48; formulaStr = "$" + val + " \\times 30.48 = " + targetVal.toFixed(2) + "\\text{ cm}$"; }
      else if (key === "cm->ft") { targetVal = val / 30.48; formulaStr = "$" + val + " \\div 30.48 = " + targetVal.toFixed(2) + "\\text{ ft}$"; }
      else if (key === "km->m") { targetVal = val * 1000; formulaStr = "$" + val + " \\times 1000 = " + targetVal + "\\text{ m}$"; }
      else if (key === "m->km") { targetVal = val / 1000; formulaStr = "$" + val + " \\div 1000 = " + targetVal + "\\text{ km}$"; }
      else if (key === "cm->mm") { targetVal = val * 10; formulaStr = "$" + val + " \\times 10 = " + targetVal + "\\text{ mm}$"; }
      else if (key === "mm->cm") { targetVal = val / 10; formulaStr = "$" + val + " \\div 10 = " + targetVal + "\\text{ cm}$"; }
      else {
        // Multi-step conversion via base meter
        let base_m = (from === 'm') ? val : (from === 'cm') ? val / 100 : (from === 'mm') ? val / 100 : (from === 'km') ? val * 1000 : (from === 'ft') ? val / 3.28 : (val * 2.54) / 100;
        targetVal = (to === 'm') ? base_m : (to === 'cm') ? base_m * 100 : (to === 'mm') ? base_m * 1000 : (to === 'km') ? base_m / 1000 : (to === 'ft') ? base_m * 3.28 : base_m * 39.37;
        formulaStr = "पहिले आधार एकाइ मिटरमा ($" + base_m.toFixed(3) + "\\text{ m}$) लगेर इच्छित एकाइमा रूपान्तरण गर्दा।";
      }

      // Compute across all other units for rich preview
      let bm = (from === 'm') ? val : (from === 'cm') ? val / 100 : (from === 'mm') ? val / 1000 : (from === 'km') ? val * 1000 : (from === 'ft') ? val / 3.28 : (val * 2.54) / 100;
      let all_m = bm.toFixed(2);
      let all_cm = (bm * 100).toFixed(2);
      let all_ft = (bm * 3.28).toFixed(2);
      let all_in = (bm * 39.37).toFixed(2);

      let statusHtml = `
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-indigo-400/30 pb-3">
          <span class="px-3 py-1 rounded-xl bg-indigo-500/20 text-indigo-300 font-bold text-xs border border-indigo-400/30">दूरी रूपान्तरण प्रत्यक्ष नतिजा</span>
          <span class="text-xs text-blue-200">${val} ${from} $\\rightarrow$ ${to}</span>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-center pt-2">
          <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">सुरुवाती नाप</span><span class="text-lg font-mono font-bold">${val} ${from}</span></div>
          <div class="bg-emerald-500/20 border border-emerald-400/40 p-2.5 rounded-xl"><span class="text-xs text-emerald-200 block">नतिजा (${to})</span><span class="text-lg font-mono font-bold text-emerald-300">${targetVal.toFixed(2).replace(/\\.00$/, '')} ${to}</span></div>
          <div class="bg-blue-500/20 border border-blue-400/40 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">फिट समतुल्य</span><span class="text-lg font-mono font-bold text-blue-300">${all_ft} ft</span></div>
          <div class="bg-purple-500/20 border border-purple-400/40 p-2.5 rounded-xl"><span class="text-xs text-purple-200 block">इन्च समतुल्य</span><span class="text-lg font-mono font-bold text-purple-300">${all_in} in</span></div>
        </div>
        <p class="text-xs text-blue-100 bg-white/5 p-2.5 rounded-lg mt-2 leading-relaxed">
          <strong>चरणबद्ध रूपान्तरण विधि:</strong> ${formulaStr}
        </p>
      `;
      res.innerHTML = statusHtml;
      if (window.MathJax && window.MathJax.Hub) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, res]);
      } else if (window.renderOfflineMath) {
        window.renderOfflineMath(res);
      }
    }

    const ch9QuizData = [
      { correct: 1, exp: "मेट्रिक प्रणाली अनुसार $1\\text{ m} = 100\\text{ cm}$ हुन्छ।" },
      { correct: 0, exp: "$1\\text{ in} = 2.54\\text{ cm}$ हुन्छ।" },
      { correct: 2, exp: "पाठ्यक्रम अनुसार $1\\text{ m} = 3.28\\text{ ft}$ मानिन्छ।" },
      { correct: 1, exp: "१ फिटमा १२ इन्च हुने भएकाले $6\\text{ ft} = 6 \\times 12 = 72\\text{ in}$ हुन्छ।" },
      { correct: 1, exp: "सानो एकाइलाई ठूलो एकाइमा रूपान्तरण गर्दा रूपान्तरण दरले भाग ($\\div$) गर्नुपर्छ।" }
    ];

    function checkQuizCh9(qIdx, selected) {
      const data = ch9QuizData[qIdx];
      const expBox = document.getElementById('ch9-qexp-' + qIdx);
      const badge = document.getElementById('ch9-qbadge-' + qIdx);
      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById('ch9-qbtn-' + qIdx + '-' + i);
        if (btn) {
          if (i === data.correct) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-emerald-500 bg-emerald-50 text-emerald-900 font-bold';
          } else if (i === selected) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-rose-500 bg-rose-50 text-rose-900';
          } else {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 text-slate-500';
          }
        }
      }
      if (badge) {
        if (selected === data.correct) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-emerald-100 text-emerald-800';
          badge.textContent = '✓ सही उत्तर';
        } else {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-rose-100 text-rose-800';
          badge.textContent = '✗ गलत उत्तर';
        }
      }
      if (expBox) {
        expBox.classList.remove('hidden');
        if (selected === data.correct) {
          expBox.className = 'p-3 rounded-xl text-xs md:text-sm bg-emerald-50 border border-emerald-200 text-emerald-900';
          expBox.innerHTML = '<strong>✓ उत्कृष्ट! सही उत्तर:</strong> ' + data.exp;
        } else {
          expBox.className = 'p-3 rounded-xl text-xs md:text-sm bg-rose-50 border border-rose-200 text-rose-900';
          expBox.innerHTML = '<strong>✗ गलत उत्तर!</strong> सही विकल्प (' + String.fromCharCode(65 + data.correct) + ') हो। <br>' + data.exp;
        }
        if (window.MathJax && window.MathJax.Hub) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, expBox]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(expBox);
        }
      }
    }

    function resetQuizCh9() {
      for (let q = 0; q < 5; q++) {
        for (let i = 0; i < 4; i++) {
          const btn = document.getElementById('ch9-qbtn-' + q + '-' + i);
          if (btn) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer';
          }
        }
        const badge = document.getElementById('ch9-qbadge-' + q);
        if (badge) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600';
          badge.textContent = 'हल हुन बाँकी';
        }
        const expBox = document.getElementById('ch9-qexp-' + q);
        if (expBox) {
          expBox.classList.add('hidden');
          expBox.innerHTML = '';
        }
      }
    }

    // Explicit window bindings
    window.setTabCh9 = setTabCh9;
    window.setExerciseCh9 = setExerciseCh9;
    window.setCh9Preset = setCh9Preset;
    window.runCh9Convert = runCh9Convert;
    window.checkQuizCh9 = checkQuizCh9;
    window.resetQuizCh9 = resetQuizCh9;

    
    // ==========================================
    // CHAPTER 10: PERIMETER, AREA, VOLUME LOGIC
    // ==========================================
    let currentCh10Shape = 'rect';

    function setTabCh10(tab) {
      const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
      tabs.forEach(t => {
        const btn = document.getElementById('ch10-tab-' + t);
        const view = document.getElementById('ch10-view-' + t);
        if (btn && view) {
          if (t === tab) {
            btn.className = 'px-5 py-2.5 rounded-xl bg-emerald-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
            view.classList.remove('hidden');
          } else {
            btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
            view.classList.add('hidden');
          }
        }
      });
      if (tab === 'concepts') {
        runCh10Calc();
      }
      if (window.MathJax && window.MathJax.Hub) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub]);
      } else if (window.renderOfflineMath) {
        window.renderOfflineMath(document.getElementById('ch10-view-' + tab));
      }
    }

    function setExerciseCh10(sec) {
      const secs = ['sec1', 'sec2', 'sec3', 'sec4'];
      secs.forEach(s => {
        const btn = document.getElementById('ch10-ex-btn-' + s);
        const view = document.getElementById('ch10-ex-' + s);
        if (btn && view) {
          if (s === sec) {
            btn.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-emerald-600 text-white shadow-xs transition cursor-pointer';
            view.classList.remove('hidden');
          } else {
            btn.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold text-slate-600 hover:bg-slate-100 transition cursor-pointer';
            view.classList.add('hidden');
          }
        }
      });
      if (window.MathJax && window.MathJax.Hub) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub]);
      } else if (window.renderOfflineMath) {
        window.renderOfflineMath(document.getElementById('ch10-ex-' + sec));
      }
    }

    function setCh10Shape(shape) {
      currentCh10Shape = shape;
      ['rect', 'sq', 'cuboid', 'cube'].forEach(s => {
        const b = document.getElementById('ch10-btn-' + s);
        if (b) {
          b.className = (s === (shape === 'square' ? 'sq' : shape)) ? 
            'px-3 py-1.5 rounded-lg bg-emerald-500 text-white transition cursor-pointer' : 
            'px-3 py-1.5 rounded-lg hover:bg-white/10 text-white/80 transition cursor-pointer';
        }
      });

      const boxB = document.getElementById('ch10-box-b');
      const boxH = document.getElementById('ch10-box-h');
      const lblL = document.getElementById('ch10-lbl-l');

      if (shape === 'rect') {
        if (lblL) lblL.textContent = 'लम्बाइ (Length - l):';
        if (boxB) boxB.classList.remove('hidden');
        if (boxH) boxH.classList.add('hidden');
      } else if (shape === 'square') {
        if (lblL) lblL.textContent = 'भुजाको लम्बाइ (Side - l):';
        if (boxB) boxB.classList.add('hidden');
        if (boxH) boxH.classList.add('hidden');
      } else if (shape === 'cuboid') {
        if (lblL) lblL.textContent = 'लम्बाइ (Length - l):';
        if (boxB) boxB.classList.remove('hidden');
        if (boxH) boxH.classList.remove('hidden');
      } else if (shape === 'cube') {
        if (lblL) lblL.textContent = 'किनाराको लम्बाइ (Edge - l):';
        if (boxB) boxB.classList.add('hidden');
        if (boxH) boxH.classList.add('hidden');
      }
      runCh10Calc();
    }

    function setCh10Preset(shape, l, b, h, unit) {
      setCh10Shape(shape);
      const inL = document.getElementById('ch10-in-l');
      const inB = document.getElementById('ch10-in-b');
      const inH = document.getElementById('ch10-in-h');
      const inUnit = document.getElementById('ch10-in-unit');
      if (inL) inL.value = l;
      if (inB) inB.value = b;
      if (inH) inH.value = h;
      if (inUnit) inUnit.value = unit;
      runCh10Calc();
    }

    function runCh10Calc() {
      const inL = document.getElementById('ch10-in-l');
      const inB = document.getElementById('ch10-in-b');
      const inH = document.getElementById('ch10-in-h');
      const inUnit = document.getElementById('ch10-in-unit');
      const res = document.getElementById('ch10-calc-res');
      if (!inL || !inUnit || !res) return;

      const l = parseFloat(inL.value);
      const b = inB ? parseFloat(inB.value) : l;
      const h = inH ? parseFloat(inH.value) : l;
      const unit = inUnit.value;

      if (isNaN(l) || l <= 0) {
        res.innerHTML = '<span class="text-amber-300 text-xs">कृपया मान्य लम्बाइ मान राख्नुहोस्।</span>';
        return;
      }

      let p = 0, a = 0, v = 0, sa = 0, liters = 0;
      let formulaText = "";
      let title = "";

      if (currentCh10Shape === 'rect') {
        if (isNaN(b) || b <= 0) {
          res.innerHTML = '<span class="text-amber-300 text-xs">कृपया मान्य चौडाइ मान राख्नुहोस्।</span>';
          return;
        }
        title = "आयत (Rectangle)";
        p = 2 * (l + b);
        a = l * b;
        formulaText = `• परिमिति: $P = 2(l + b) = 2(${l} + ${b}) = ${p.toFixed(2).replace(/\.00$/, '')}\text{ ${unit}}$<br>` +
                      `• क्षेत्रफल: $A = l \times b = ${l} \times ${b} = ${a.toFixed(2).replace(/\.00$/, '')}\text{ ${unit}}^2$`;
      } else if (currentCh10Shape === 'square') {
        title = "वर्ग (Square)";
        p = 4 * l;
        a = l * l;
        formulaText = `• परिमिति: $P = 4l = 4 \times ${l} = ${p.toFixed(2).replace(/\.00$/, '')}\text{ ${unit}}$<br>` +
                      `• क्षेत्रफल: $A = l^2 = ${l}^2 = ${a.toFixed(2).replace(/\.00$/, '')}\text{ ${unit}}^2$`;
      } else if (currentCh10Shape === 'cuboid') {
        if (isNaN(b) || b <= 0 || isNaN(h) || h <= 0) {
          res.innerHTML = '<span class="text-amber-300 text-xs">कृपया मान्य चौडाइ र उचाइ मान राख्नुहोस्।</span>';
          return;
        }
        title = "षट्मुख (Cuboid)";
        v = l * b * h;
        sa = 2 * (l * b + b * h + l * h);
        if (unit === 'm') liters = v * 1000;
        else if (unit === 'cm') liters = v / 1000;
        else liters = v * 28.317; // ft^3 to liters approx
        formulaText = `• आयतन: $V = l \times b \times h = ${l} \times ${b} \times ${h} = ${v.toFixed(2).replace(/\.00$/, '')}\text{ ${unit}}^3$<br>` +
                      `• कुल सतह क्षेत्रफल: $A = 2(lb + bh + lh) = ${sa.toFixed(2).replace(/\.00$/, '')}\text{ ${unit}}^2$<br>` +
                      `• पानीको क्षमता: <strong>${liters.toFixed(2).replace(/\.00$/, '')} लिटर</strong>`;
      } else if (currentCh10Shape === 'cube') {
        title = "घन (Cube)";
        v = l * l * l;
        sa = 6 * l * l;
        if (unit === 'm') liters = v * 1000;
        else if (unit === 'cm') liters = v / 1000;
        else liters = v * 28.317;
        formulaText = `• आयतन: $V = l^3 = ${l}^3 = ${v.toFixed(2).replace(/\.00$/, '')}\text{ ${unit}}^3$<br>` +
                      `• कुल सतह क्षेत्रफल: $A = 6l^2 = 6 \times ${l}^2 = ${sa.toFixed(2).replace(/\.00$/, '')}\text{ ${unit}}^2$<br>` +
                      `• पानीको क्षमता: <strong>${liters.toFixed(2).replace(/\.00$/, '')} लिटर</strong>`;
      }

      let resCards = '';
      if (currentCh10Shape === 'rect' || currentCh10Shape === 'square') {
        resCards = `
          <div class="bg-emerald-500/20 border border-emerald-400/40 p-2.5 rounded-xl"><span class="text-xs text-emerald-200 block">परिमिति (P)</span><span class="text-lg font-mono font-bold text-emerald-300">${p.toFixed(2).replace(/\.00$/, '')} ${unit}</span></div>
          <div class="bg-teal-500/20 border border-teal-400/40 p-2.5 rounded-xl"><span class="text-xs text-teal-200 block">क्षेत्रफल (A)</span><span class="text-lg font-mono font-bold text-teal-300">${a.toFixed(2).replace(/\.00$/, '')} ${unit}²</span></div>
          <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">लम्बाइ (l)</span><span class="text-lg font-mono font-bold">${l} ${unit}</span></div>
          <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">चौडाइ (b)</span><span class="text-lg font-mono font-bold">${currentCh10Shape === 'square' ? l : b} ${unit}</span></div>
        `;
      } else {
        resCards = `
          <div class="bg-cyan-500/20 border border-cyan-400/40 p-2.5 rounded-xl"><span class="text-xs text-cyan-200 block">आयतन (V)</span><span class="text-lg font-mono font-bold text-cyan-300">${v.toFixed(2).replace(/\.00$/, '')} ${unit}³</span></div>
          <div class="bg-emerald-500/20 border border-emerald-400/40 p-2.5 rounded-xl"><span class="text-xs text-emerald-200 block">पानी क्षमता</span><span class="text-lg font-mono font-bold text-emerald-300">${liters.toFixed(1).replace(/\.0$/, '')} L</span></div>
          <div class="bg-purple-500/20 border border-purple-400/40 p-2.5 rounded-xl"><span class="text-xs text-purple-200 block">सतह क्षेत्रफल</span><span class="text-lg font-mono font-bold text-purple-300">${sa.toFixed(2).replace(/\.00$/, '')} ${unit}²</span></div>
          <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-blue-200 block">नाप (l×b×h)</span><span class="text-sm font-mono font-bold">${l}×${currentCh10Shape==='cube'?l:b}×${currentCh10Shape==='cube'?l:h}</span></div>
        `;
      }

      res.innerHTML = `
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-emerald-400/30 pb-3">
          <span class="px-3 py-1 rounded-xl bg-emerald-500/20 text-emerald-300 font-bold text-xs border border-emerald-400/30">${title} प्रत्यक्ष गणना नतिजा</span>
          <span class="text-xs text-emerald-200">${unit} एकाइमा</span>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-center pt-2">
          ${resCards}
        </div>
        <div class="text-xs text-emerald-100 bg-white/5 p-3 rounded-xl mt-2 leading-relaxed">
          <strong>चरणबद्ध सूत्र तथा हिसाब:</strong><br>
          ${formulaText}
        </div>
      `;

      if (window.MathJax && window.MathJax.Hub) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, res]);
      } else if (window.renderOfflineMath) {
        window.renderOfflineMath(res);
      }
    }

    const ch10QuizData = [
      { correct: 1, exp: "$P = 2(l + b) = 2(8 + 5) = 2 \times 13 = 26\text{ cm}$ हुन्छ।" },
      { correct: 1, exp: "$A = l^2 = 9^2 = 81\text{ cm}^2$ हुन्छ।" },
      { correct: 2, exp: "$V = l \times b \times h = 6 \times 4 \times 3 = 72\text{ m}^3$ हुन्छ।" },
      { correct: 2, exp: "$1\text{ m}^3 = 1,000\text{ L} \implies 2\text{ m}^3 = 2,000\text{ लिटर}$ हुन्छ।" },
      { correct: 2, exp: "व्यास अर्धव्यासको दोब्बर हुने भएकाले $d = 2 \times 14 = 28\text{ cm}$ हुन्छ।" }
    ];

    function checkQuizCh10(qIdx, selected) {
      const data = ch10QuizData[qIdx];
      const expBox = document.getElementById('ch10-qexp-' + qIdx);
      const badge = document.getElementById('ch10-qbadge-' + qIdx);
      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById('ch10-qbtn-' + qIdx + '-' + i);
        if (btn) {
          if (i === data.correct) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-emerald-500 bg-emerald-50 text-emerald-900 font-bold';
          } else if (i === selected) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-rose-500 bg-rose-50 text-rose-900';
          } else {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 text-slate-500';
          }
        }
      }
      if (badge) {
        if (selected === data.correct) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-emerald-100 text-emerald-800';
          badge.textContent = '✓ सही उत्तर';
        } else {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-rose-100 text-rose-800';
          badge.textContent = '✗ गलत उत्तर';
        }
      }
      if (expBox) {
        expBox.classList.remove('hidden');
        if (selected === data.correct) {
          expBox.className = 'p-3 rounded-xl text-xs md:text-sm bg-emerald-50 border border-emerald-200 text-emerald-900';
          expBox.innerHTML = '<strong>✓ उत्कृष्ट! सही उत्तर:</strong> ' + data.exp;
        } else {
          expBox.className = 'p-3 rounded-xl text-xs md:text-sm bg-rose-50 border border-rose-200 text-rose-900';
          expBox.innerHTML = '<strong>✗ गलत उत्तर!</strong> सही विकल्प (' + String.fromCharCode(65 + data.correct) + ') हो। <br>' + data.exp;
        }
        if (window.MathJax && window.MathJax.Hub) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, expBox]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(expBox);
        }
      }
    }

    function resetQuizCh10() {
      for (let q = 0; q < 5; q++) {
        for (let i = 0; i < 4; i++) {
          const btn = document.getElementById('ch10-qbtn-' + q + '-' + i);
          if (btn) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer';
          }
        }
        const badge = document.getElementById('ch10-qbadge-' + q);
        if (badge) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600';
          badge.textContent = 'हल हुन बाँकी';
        }
        const expBox = document.getElementById('ch10-qexp-' + q);
        if (expBox) {
          expBox.classList.add('hidden');
          expBox.innerHTML = '';
        }
      }
    }

    // Explicit window bindings
    window.setTabCh10 = setTabCh10;
    window.setExerciseCh10 = setExerciseCh10;
    window.setCh10Shape = setCh10Shape;
    window.setCh10Preset = setCh10Preset;
    window.runCh10Calc = runCh10Calc;
    window.checkQuizCh10 = checkQuizCh10;
    window.resetQuizCh10 = resetQuizCh10;

    
    // ==========================================
    // CHAPTER 11: INDICES (घाताङ्क) LOGIC
    // ==========================================
    let currentCh11Mode = 'single';

    function setTabCh11(tab) {
      const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
      tabs.forEach(t => {
        const btn = document.getElementById('ch11-tab-' + t);
        const view = document.getElementById('ch11-view-' + t);
        if (btn && view) {
          if (t === tab) {
            btn.className = 'px-5 py-2.5 rounded-xl bg-purple-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
            view.classList.remove('hidden');
          } else {
            btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
            view.classList.add('hidden');
          }
        }
      });
      if (tab === 'concepts') {
        runCh11Calc();
      }
      if (window.MathJax && window.MathJax.Hub) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub]);
      } else if (window.renderOfflineMath) {
        window.renderOfflineMath(document.getElementById('ch11-view-' + tab));
      }
    }

    function setCh11Mode(mode) {
      currentCh11Mode = mode;
      ['single', 'prod', 'quot', 'powpow'].forEach(m => {
        const b = document.getElementById('ch11-btn-' + m);
        if (b) {
          b.className = (m === (mode === 'product' ? 'prod' : mode === 'quotient' ? 'quot' : mode)) ? 
            'px-3 py-1.5 rounded-lg bg-purple-500 text-white transition cursor-pointer' : 
            'px-3 py-1.5 rounded-lg hover:bg-white/10 text-white/80 transition cursor-pointer';
        }
      });

      const boxN = document.getElementById('ch11-box-n');
      const lblM = document.getElementById('ch11-lbl-m');
      const lblN = document.getElementById('ch11-lbl-n');

      if (mode === 'single') {
        if (boxN) boxN.classList.add('hidden');
        if (lblM) lblM.textContent = 'घाताङ्क (Power - n):';
      } else if (mode === 'product') {
        if (boxN) boxN.classList.remove('hidden');
        if (lblM) lblM.textContent = 'पहिलो घात (Power - m):';
        if (lblN) lblN.textContent = 'दोस्रो घात (Power - n):';
      } else if (mode === 'quotient') {
        if (boxN) boxN.classList.remove('hidden');
        if (lblM) lblM.textContent = 'अंशको घात (Numerator Power - m):';
        if (lblN) lblN.textContent = 'हरको घात (Denominator Power - n):';
      } else if (mode === 'powpow') {
        if (boxN) boxN.classList.remove('hidden');
        if (lblM) lblM.textContent = 'भित्री घात (Inner Power - m):';
        if (lblN) lblN.textContent = 'बाहिरी घात (Outer Power - n):';
      }
      runCh11Calc();
    }

    function setCh11Preset(mode, base, m, n) {
      setCh11Mode(mode);
      const inBase = document.getElementById('ch11-in-base');
      const inM = document.getElementById('ch11-in-m');
      const inN = document.getElementById('ch11-in-n');
      if (inBase) inBase.value = base;
      if (inM) inM.value = m;
      if (inN) inN.value = n;
      runCh11Calc();
    }

    function runCh11Calc() {
      const inBase = document.getElementById('ch11-in-base');
      const inM = document.getElementById('ch11-in-m');
      const inN = document.getElementById('ch11-in-n');
      const res = document.getElementById('ch11-calc-res');
      if (!inBase || !inM || !res) return;

      const baseStr = inBase.value.trim() || '2';
      const m = parseInt(inM.value, 10);
      const n = inN ? parseInt(inN.value, 10) : 0;

      if (isNaN(m)) {
        res.innerHTML = '<span class="text-amber-300 text-xs">कृपया मान्य घाताङ्क मान राख्नुहोस्।</span>';
        return;
      }

      const isNumeric = !isNaN(parseFloat(baseStr)) && isFinite(baseStr);
      const numBase = parseFloat(baseStr);

      let title = "";
      let exprTeX = "";
      let stepTeX = "";
      let finalForm = "";
      let finalValStr = "";

      if (currentCh11Mode === 'single') {
        title = `एकल घाताङ्क ($${baseStr}^{${m}}$)`;
        exprTeX = `${baseStr}^{${m}}`;
        if (m === 0) {
          stepTeX = "शून्य घाताङ्क नियम अनुसार कुनै पनि आधार ($a \neq 0$) को घात ० हुँदा मान १ हुन्छ।";
          finalForm = "1";
          finalValStr = "1";
        } else if (m > 0 && m <= 15) {
          let expandedArr = [];
          for (let i = 0; i < m; i++) expandedArr.push(baseStr);
          stepTeX = `विस्तारित रूप: $${expandedArr.join(' \times ')}$`;
          if (isNumeric) {
            let val = Math.pow(numBase, m);
            finalForm = `${baseStr}^{${m}}`;
            finalValStr = val.toLocaleString();
          } else {
            finalForm = `${baseStr}^{${m}}`;
            finalValStr = `${baseStr}^{${m}}`;
          }
        } else {
          stepTeX = `विस्तारित रूप: $${baseStr}$ लाई $${m}$ पटक गुणन गरिएको।`;
          finalForm = `${baseStr}^{${m}}`;
          finalValStr = isNumeric ? Math.pow(numBase, m).toExponential(3) : `${baseStr}^{${m}}`;
        }
      } else if (currentCh11Mode === 'product') {
        title = `गुणनको नियम ($${baseStr}^{${m}} \times ${baseStr}^{${n}}$)`;
        exprTeX = `${baseStr}^{${m}} \times ${baseStr}^{${n}}`;
        const sumPower = m + n;
        stepTeX = `समान आधार भएकाले घातहरू जोडिन्छन्: $${baseStr}^{${m}+${n}} = ${baseStr}^{${sumPower}}$`;
        finalForm = `${baseStr}^{${sumPower}}`;
        if (isNumeric && sumPower >= 0 && sumPower <= 20) {
          finalValStr = Math.pow(numBase, sumPower).toLocaleString();
        } else {
          finalValStr = `${baseStr}^{${sumPower}}`;
        }
      } else if (currentCh11Mode === 'quotient') {
        title = `भागको नियम ($${baseStr}^{${m}} \div ${baseStr}^{${n}}$)`;
        exprTeX = `\frac{${baseStr}^{${m}}}{${baseStr}^{${n}}}`;
        const diffPower = m - n;
        stepTeX = `समान आधार भएकाले घातहरू घटाइन्छन्: $${baseStr}^{${m}-${n}} = ${baseStr}^{${diffPower}}$`;
        finalForm = `${baseStr}^{${diffPower}}`;
        if (diffPower === 0) {
          finalValStr = "1";
        } else if (isNumeric && diffPower > 0 && diffPower <= 20) {
          finalValStr = Math.pow(numBase, diffPower).toLocaleString();
        } else {
          finalValStr = `${baseStr}^{${diffPower}}`;
        }
      } else if (currentCh11Mode === 'powpow') {
        title = `घातको घात नियम ($(${baseStr}^{${m}})^{${n}}$)`;
        exprTeX = `(${baseStr}^{${m}})^{${n}}`;
        const prodPower = m * n;
        stepTeX = `घातमाथि घात भएकाले आपसमा गुणन हुन्छ: $${baseStr}^{${m} \times ${n}} = ${baseStr}^{${prodPower}}$`;
        finalForm = `${baseStr}^{${prodPower}}`;
        if (isNumeric && prodPower >= 0 && prodPower <= 20) {
          finalValStr = Math.pow(numBase, prodPower).toLocaleString();
        } else {
          finalValStr = `${baseStr}^{${prodPower}}`;
        }
      }

      res.innerHTML = `
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-purple-400/30 pb-3">
          <span class="px-3 py-1 rounded-xl bg-purple-500/20 text-purple-300 font-bold text-xs border border-purple-400/30">${title} नतिजा</span>
          <span class="text-xs text-purple-200">आधार: ${baseStr}</span>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-3 text-center pt-2">
          <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-purple-200 block">अभिव्यञ्जन</span><span class="text-base font-mono font-bold">$${exprTeX}$</span></div>
          <div class="bg-purple-500/20 border border-purple-400/40 p-2.5 rounded-xl"><span class="text-xs text-purple-200 block">घाताङ्कीय रूप</span><span class="text-lg font-mono font-bold text-purple-300">$${finalForm}$</span></div>
          <div class="bg-emerald-500/20 border border-emerald-400/40 p-2.5 rounded-xl"><span class="text-xs text-emerald-200 block">संख्यात्मक मान</span><span class="text-lg font-mono font-bold text-emerald-300">${finalValStr}</span></div>
          <div class="bg-white/10 p-2.5 rounded-xl"><span class="text-xs text-purple-200 block">नियम</span><span class="text-xs font-sans font-semibold">${currentCh11Mode === 'single' ? 'परिभाषा' : currentCh11Mode === 'product' ? 'गुणन ($a^{m+n}$)' : currentCh11Mode === 'quotient' ? 'भाग ($a^{m-n}$)' : 'घातको घात ($a^{mn}$)'}</span></div>
        </div>
        <div class="text-xs text-purple-100 bg-white/5 p-3 rounded-xl mt-2 leading-relaxed">
          <strong>चरणबद्ध व्याख्या:</strong><br>
          ${stepTeX}
        </div>
      `;

      if (window.MathJax && window.MathJax.Hub) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, res]);
      } else if (window.renderOfflineMath) {
        window.renderOfflineMath(res);
      }
    }

    const ch11QuizData = [
      { correct: 1, exp: "२ लाई ५ पटक दोहोर्‍याएर गुणन गर्दा $2^5$ हुन्छ।" },
      { correct: 0, exp: "गुणनको नियम अनुसार आधार समान भए घाताङ्क जोडिन्छ: $x^{3+4} = x^7$।" },
      { correct: 2, exp: "शून्यबाहेक जुनसुकै आधारको घात शून्य हुँदा मान सधैँ $1$ हुन्छ: $(15)^0 = 1$।" },
      { correct: 1, exp: "भागको नियम अनुसार आधार समान भए घाताङ्क घटाइन्छ: $a^{8-3} = a^5$।" },
      { correct: 2, exp: "घनको आयतन $V = l^3 = 11^3 = 11 \times 11 \times 11 = 1,331\text{ cm}^3$ हुन्छ।" }
    ];

    function checkQuizCh11(qIdx, selected) {
      const data = ch11QuizData[qIdx];
      const expBox = document.getElementById('ch11-qexp-' + qIdx);
      const badge = document.getElementById('ch11-qbadge-' + qIdx);
      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById('ch11-qbtn-' + qIdx + '-' + i);
        if (btn) {
          if (i === data.correct) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-purple-500 bg-purple-50 text-purple-900 font-bold';
          } else if (i === selected) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-rose-500 bg-rose-50 text-rose-900';
          } else {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 text-slate-500';
          }
        }
      }
      if (badge) {
        if (selected === data.correct) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-emerald-100 text-emerald-800';
          badge.textContent = '✓ सही उत्तर';
        } else {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-rose-100 text-rose-800';
          badge.textContent = '✗ गलत उत्तर';
        }
      }
      if (expBox) {
        expBox.classList.remove('hidden');
        if (selected === data.correct) {
          expBox.className = 'p-3 rounded-xl text-xs md:text-sm bg-purple-50 border border-purple-200 text-purple-900';
          expBox.innerHTML = '<strong>✓ उत्कृष्ट! सही उत्तर:</strong> ' + data.exp;
        } else {
          expBox.className = 'p-3 rounded-xl text-xs md:text-sm bg-rose-50 border border-rose-200 text-rose-900';
          expBox.innerHTML = '<strong>✗ गलत उत्तर!</strong> सही विकल्प (' + String.fromCharCode(65 + data.correct) + ') हो। <br>' + data.exp;
        }
        if (window.MathJax && window.MathJax.Hub) {
          window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, expBox]);
        } else if (window.renderOfflineMath) {
          window.renderOfflineMath(expBox);
        }
      }
    }

    function resetQuizCh11() {
      for (let q = 0; q < 5; q++) {
        for (let i = 0; i < 4; i++) {
          const btn = document.getElementById('ch11-qbtn-' + q + '-' + i);
          if (btn) {
            btn.className = 'w-full text-left p-3 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer';
          }
        }
        const badge = document.getElementById('ch11-qbadge-' + q);
        if (badge) {
          badge.className = 'text-xs font-bold px-2.5 py-0.5 rounded-lg bg-slate-100 text-slate-600';
          badge.textContent = 'हल हुन बाँकी';
        }
        const expBox = document.getElementById('ch11-qexp-' + q);
        if (expBox) {
          expBox.classList.add('hidden');
          expBox.innerHTML = '';
        }
      }
    }

    // Explicit window bindings
    window.setTabCh11 = setTabCh11;
    window.setCh11Mode = setCh11Mode;
    window.setCh11Preset = setCh11Preset;
    window.runCh11Calc = runCh11Calc;
    window.checkQuizCh11 = checkQuizCh11;
    window.resetQuizCh11 = resetQuizCh11;

    // ================= CHAPTER 12 JAVASCRIPT LOGIC =================
    let currentCh12LabMode = 'eval';

    function setTabCh12(tab) {
      const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
      tabs.forEach(t => {
        const btn = document.getElementById('ch12-tab-' + t);
        const view = document.getElementById('ch12-view-' + t);
        if (btn && view) {
          if (t === tab) {
            btn.className = 'px-5 py-2.5 rounded-xl bg-teal-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
            view.classList.remove('hidden');
          } else {
            btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
            view.classList.add('hidden');
          }
        }
      });
      if (tab === 'concepts') {
        runCh12Lab();
      }
      if (window.MathJax && window.MathJax.Hub) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub]);
      } else if (window.renderOfflineMath) {
        window.renderOfflineMath(document.getElementById('ch12-view-' + tab));
      }
    }

    function setExerciseCh12(exId) {
      const allEx = ['ex12_1', 'ex12_2', 'ex12_3', 'project'];
      allEx.forEach(e => {
        const sec = document.getElementById('ch12-sec-' + e);
        const pill = document.getElementById('ch12-pill-' + e);
        if (sec) sec.classList.add('hidden');
        if (pill) pill.className = 'px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap cursor-pointer';
      });
      const curSec = document.getElementById('ch12-sec-' + exId);
      const curPill = document.getElementById('ch12-pill-' + exId);
      if (curSec) curSec.classList.remove('hidden');
      if (curPill) curPill.className = 'px-4 py-2 rounded-xl bg-teal-600 text-white shadow-xs whitespace-nowrap cursor-pointer';
      if (window.MathJax && window.MathJax.Hub && curSec) {
        window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, curSec]);
      } else if (window.renderOfflineMath && curSec) {
        window.renderOfflineMath(curSec);
      }
    }

    function setCh12LabMode(mode) {
      currentCh12LabMode = mode;
      ['eval', 'combine', 'muldiv'].forEach(m => {
        const b = document.getElementById('ch12-lab-btn-' + m);
        const v = document.getElementById('ch12-lab-view-' + m);
        if (b && v) {
          if (m === mode) {
            b.className = 'px-3 py-1.5 rounded-xl text-xs font-bold transition bg-teal-600 text-white shadow-xs cursor-pointer';
            v.classList.remove('hidden');
          } else {
            b.className = 'px-3 py-1.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white transition cursor-pointer';
            v.classList.add('hidden');
          }
        }
      });
      runCh12Lab();
    }

    function setCh12EvalPreset(x, y, z) {
      const exX = document.getElementById('ch12-eval-x');
      const exY = document.getElementById('ch12-eval-y');
      const exZ = document.getElementById('ch12-eval-z');
      if (exX) exX.value = x;
      if (exY) exY.value = y;
      if (exZ) exZ.value = z;
      runCh12Lab();
    }

    function runCh12Lab() {
      if (currentCh12LabMode === 'eval') {
        const expr = document.getElementById('ch12-eval-expr')?.value || '4x2_minus_3xy_plus_2y2';
        const x = parseFloat(document.getElementById('ch12-eval-x')?.value || 3);
        const y = parseFloat(document.getElementById('ch12-eval-y')?.value || -2);
        const z = parseFloat(document.getElementById('ch12-eval-z')?.value || 4);
        const zWrap = document.getElementById('ch12-eval-z-wrap');
        if (zWrap) zWrap.classList.toggle('hidden', expr !== '3x_minus_2y_plus_z');

        const stepsDiv = document.getElementById('ch12-eval-steps');
        const resSpan = document.getElementById('ch12-eval-result');
        let val = 0;
        let html = '';

        if (expr === '2x_plus_3y') {
          val = 2 * x + 3 * y;
          html = `
            <div>• दिइएको अभिव्यञ्जन: <span class="text-teal-300 font-bold">2x + 3y</span></div>
            <div>• मान प्रतिस्थापन गर्दा ($x = ${x}, y = ${y}$):</div>
            <div class="pl-4 text-slate-300">= 2(${x}) + 3(${y})</div>
            <div class="pl-4 text-slate-300">= ${2*x} + (${3*y})</div>
            <div class="pl-4 text-teal-400 font-bold">= ${val}</div>
          `;
        } else if (expr === 'x2_plus_y2') {
          const x2 = x * x;
          const y2 = y * y;
          val = x2 + y2;
          html = `
            <div>• दिइएको अभिव्यञ्जन: <span class="text-teal-300 font-bold">x² + y²</span></div>
            <div>• मान प्रतिस्थापन गर्दा ($x = ${x}, y = ${y}$):</div>
            <div class="pl-4 text-slate-300">= (${x})² + (${y})²</div>
            <div class="pl-4 text-slate-300">= ${x2} + ${y2}</div>
            <div class="pl-4 text-teal-400 font-bold">= ${val}</div>
          `;
        } else if (expr === 'x2_plus_2xy_plus_y2') {
          const x2 = x * x;
          const twoxy = 2 * x * y;
          const y2 = y * y;
          val = x2 + twoxy + y2;
          html = `
            <div>• दिइएको अभिव्यञ्जन: <span class="text-teal-300 font-bold">x² + 2xy + y²</span></div>
            <div>• मान प्रतिस्थापन गर्दा ($x = ${x}, y = ${y}$):</div>
            <div class="pl-4 text-slate-300">= (${x})² + 2(${x})(${y}) + (${y})²</div>
            <div class="pl-4 text-slate-300">= ${x2} + (${twoxy}) + ${y2}</div>
            <div class="pl-4 text-slate-300">= ${x2 + twoxy} + ${y2}</div>
            <div class="pl-4 text-teal-400 font-bold">= ${val}</div>
          `;
        } else if (expr === '4x2_minus_3xy_plus_2y2') {
          const fourX2 = 4 * x * x;
          const threeXY = 3 * x * y;
          const twoY2 = 2 * y * y;
          val = fourX2 - threeXY + twoY2;
          html = `
            <div>• दिइएको अभिव्यञ्जन: <span class="text-teal-300 font-bold">4x² - 3xy + 2y²</span></div>
            <div>• मान प्रतिस्थापन गर्दा ($x = ${x}, y = ${y}$):</div>
            <div class="pl-4 text-slate-300">= 4(${x})² - 3(${x})(${y}) + 2(${y})²</div>
            <div class="pl-4 text-slate-300">= 4(${x*x}) - (${threeXY}) + 2(${y*y})</div>
            <div class="pl-4 text-slate-300">= ${fourX2} - (${threeXY}) + ${twoY2}</div>
            <div class="pl-4 text-slate-300">= ${fourX2 - threeXY} + ${twoY2}</div>
            <div class="pl-4 text-teal-400 font-bold">= ${val}</div>
          `;
        } else if (expr === '3x_minus_2y_plus_z') {
          val = 3 * x - 2 * y + z;
          html = `
            <div>• दिइएको अभिव्यञ्जन: <span class="text-teal-300 font-bold">3x - 2y + z</span></div>
            <div>• मान प्रतिस्थापन गर्दा ($x = ${x}, y = ${y}, z = ${z}$):</div>
            <div class="pl-4 text-slate-300">= 3(${x}) - 2(${y}) + (${z})</div>
            <div class="pl-4 text-slate-300">= ${3*x} - (${2*y}) + ${z}</div>
            <div class="pl-4 text-slate-300">= ${3*x - 2*y} + ${z}</div>
            <div class="pl-4 text-teal-400 font-bold">= ${val}</div>
          `;
        }
        if (stepsDiv) stepsDiv.innerHTML = html;
        if (resSpan) resSpan.textContent = val;

      } else if (currentCh12LabMode === 'combine') {
        const p = document.getElementById('ch12-combine-preset')?.value || '1';
        const stepsDiv = document.getElementById('ch12-combine-steps');
        const resSpan = document.getElementById('ch12-combine-result');
        let html = '';
        let res = '';

        if (p === '1') {
          res = '7x + 3y';
          html = `
            <div>• समस्या: <span class="text-teal-300 font-bold">3x + 5y + 4x - 2y</span></div>
            <div>• चरण १ (सजातीय पदहरूलाई समूहबद्ध गर्ने):</div>
            <div class="pl-4 text-slate-300">= (3x + 4x) + (5y - 2y)</div>
            <div>• चरण २ (गुणाङ्कहरू जोड्ने/घटाउने):</div>
            <div class="pl-4 text-slate-300">= (3 + 4)x + (5 - 2)y</div>
            <div class="pl-4 text-teal-400 font-bold">= 7x + 3y</div>
          `;
        } else if (p === '2') {
          res = 'a + 2b';
          html = `
            <div>• समस्या: <span class="text-teal-300 font-bold">4a + 6a - 9a + 2b</span></div>
            <div>• चरण १ (सजातीय पदहरूलाई समूहबद्ध गर्ने):</div>
            <div class="pl-4 text-slate-300">= (4a + 6a - 9a) + 2b</div>
            <div>• चरण २ (गुणाङ्क सरल गर्ने):</div>
            <div class="pl-4 text-slate-300">= (10a - 9a) + 2b</div>
            <div class="pl-4 text-teal-400 font-bold">= a + 2b</div>
          `;
        } else if (p === '3') {
          res = '5x² + 3xy - y²';
          html = `
            <div>• समस्या: <span class="text-teal-300 font-bold">(2x² - xy + y²) + (3x² + 4xy - 2y²)</span></div>
            <div>• चरण १ (सजातीय पदहरू मिलाउने):</div>
            <div class="pl-4 text-slate-300">= (2x² + 3x²) + (-xy + 4xy) + (y² - 2y²)</div>
            <div>• चरण २ (प्रत्येक समूह सरल गर्ने):</div>
            <div class="pl-4 text-teal-400 font-bold">= 5x² + 3xy - y²</div>
          `;
        } else if (p === '4') {
          res = '4x + 4y + 4z';
          html = `
            <div>• समस्या: <span class="text-teal-300 font-bold">(6x + 7y + 8z) - (2x + 3y + 4z)</span></div>
            <div>• चरण १ (कोष्ठक खोली चिह्न उल्ट्याउने):</div>
            <div class="pl-4 text-slate-300">= 6x + 7y + 8z - 2x - 3y - 4z</div>
            <div>• चरण २ (सजातीय पदहरू घटाउने):</div>
            <div class="pl-4 text-slate-300">= (6x - 2x) + (7y - 3y) + (8z - 4z)</div>
            <div class="pl-4 text-teal-400 font-bold">= 4x + 4y + 4z</div>
          `;
        } else if (p === '5') {
          res = '9x²y + xy²';
          html = `
            <div>• समस्या: <span class="text-teal-300 font-bold">5x²y + 3xy² + 4x²y - 2xy²</span></div>
            <div>• चरण १ (सजातीय पहिचान: x²y र xy² फरक हुन्):</div>
            <div class="pl-4 text-slate-300">= (5x²y + 4x²y) + (3xy² - 2xy²)</div>
            <div>• चरण २ (गुणाङ्क जोड्ने/घटाउने):</div>
            <div class="pl-4 text-teal-400 font-bold">= 9x²y + xy²</div>
          `;
        }
        if (stepsDiv) stepsDiv.innerHTML = html;
        if (resSpan) resSpan.textContent = res;

      } else if (currentCh12LabMode === 'muldiv') {
        const t = document.getElementById('ch12-muldiv-type')?.value || 'm1';
        const stepsDiv = document.getElementById('ch12-muldiv-steps');
        const resSpan = document.getElementById('ch12-muldiv-result');
        let html = '';
        let res = '';

        if (t === 'm1') {
          res = '28x²';
          html = `
            <div>• समस्या: <span class="text-teal-300 font-bold">4x × 7x</span></div>
            <div>• चरण १ (गुणाङ्क र चर छुट्ट्याउने):</div>
            <div class="pl-4 text-slate-300">= (4 × 7) × (x × x)</div>
            <div>• चरण २ (घाताङ्कको नियम प्रयोग: x¹ × x¹ = x¹⁺¹):</div>
            <div class="pl-4 text-teal-400 font-bold">= 28x²</div>
          `;
        } else if (t === 'm2') {
          res = '24pqr';
          html = `
            <div>• समस्या: <span class="text-teal-300 font-bold">2p × 3q × 4r</span></div>
            <div>• चरण १ (सङ्ख्यात्मक गुणाङ्क गुणन): 2 × 3 × 4 = 24</div>
            <div>• चरण २ (विजातीय चरहरू संयोजन): p × q × r = pqr</div>
            <div class="pl-4 text-teal-400 font-bold">= 24pqr</div>
          `;
        } else if (t === 'm3') {
          res = '6x² + 8xy';
          html = `
            <div>• समस्या: <span class="text-teal-300 font-bold">2x(3x + 4y)</span></div>
            <div>• चरण १ (विस्तारीकरण नियम: a(b + c) = ab + ac):</div>
            <div class="pl-4 text-slate-300">= (2x × 3x) + (2x × 4y)</div>
            <div>• चरण २ (प्रत्येक पदको गुणन):</div>
            <div class="pl-4 text-slate-300">= 6x² + 8xy</div>
            <div class="pl-4 text-teal-400 font-bold">= 6x² + 8xy</div>
          `;
        } else if (t === 'd1') {
          res = '5xy';
          html = `
            <div>• समस्या: <span class="text-teal-300 font-bold">20x³y² ÷ 4x²y</span></div>
            <div>• चरण १ (भिन्नको रूपमा लेख्ने): $\\frac{20x^3y^2}{4x^2y}$</div>
            <div>• चरण २ (गुणाङ्क भाग र घाताङ्क घटाउ):</div>
            <div class="pl-4 text-slate-300">= (20 ÷ 4) × x³⁻² × y²⁻¹</div>
            <div class="pl-4 text-teal-400 font-bold">= 5x¹y¹ = 5xy</div>
          `;
        } else if (t === 'd2') {
          res = '4x + 3y';
          html = `
            <div>• समस्या: <span class="text-teal-300 font-bold">(16x² + 12xy) ÷ 4x</span></div>
            <div>• चरण १ (प्रत्येक पदलाई हरले छुट्टाछुट्टै भाग गर्ने):</div>
            <div class="pl-4 text-slate-300">= $\\frac{16x^2}{4x} + \\frac{12xy}{4x}$</div>
            <div>• चरण २ (काट्दा):</div>
            <div class="pl-4 text-slate-300">= 4x + 3y</div>
            <div class="pl-4 text-teal-400 font-bold">= 4x + 3y</div>
          `;
        } else if (t === 'd3') {
          res = '3pqr cm';
          html = `
            <div>• समस्या: <span class="text-teal-300 font-bold">क्षेत्रफल A = 24p⁴q³r² cm², चौडाइ b = 8p³q²r cm</span></div>
            <div>• सूत्र: लम्बाइ $l = \\frac{A}{b}$</div>
            <div class="pl-4 text-slate-300">= $\\frac{24p^4q^3r^2}{8p^3q^2r}$</div>
            <div class="pl-4 text-slate-300">= 3 × p⁴⁻³ × q³⁻² × r²⁻¹</div>
            <div class="pl-4 text-teal-400 font-bold">= 3pqr cm</div>
          `;
        }
        if (stepsDiv) stepsDiv.innerHTML = html;
        if (resSpan) resSpan.textContent = res;
      }
    }

    const quizDataCh12 = [
      {
        correct: 1,
        exp: "पदको अगाडिको सङ्ख्यात्मक मान चिह्न सहित गुणाङ्क हुन्छ। $-7x^2y$ मा गुणाङ्क -७ हो।"
      },
      {
        correct: 2,
        exp: "गुणनमा $ab = ba$ हुने हुनाले $-4ab$ र $7ba$ का चर र घाताङ्क ठ्याक्कै समान छन्, त्यसैले यी सजातीय हुन्।"
      },
      {
        correct: 1,
        exp: "$(-3)^2 + 2(-3) = 9 - 6 = 3$ हुन्छ।"
      },
      {
        correct: 0,
        exp: "$\\\\frac{24}{6} x^{3-1} y^{2-1} = 4x^2y$ हुन्छ।"
      },
      {
        correct: 1,
        exp: "$P = 2(l + b) = 2(2x + 1 + 2x - 1) = 2(4x) = 8x$ हुन्छ।"
      }
    ];

    function checkQuizCh12(qIdx, optIdx) {
      const q = quizDataCh12[qIdx];
      const expDiv = document.getElementById('ch12-qexp-' + qIdx);
      if (!q || !expDiv) return;

      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById(`ch12-qbtn-${qIdx}-${i}`);
        if (!btn) continue;
        btn.classList.remove('bg-green-100', 'border-green-500', 'text-green-800', 'bg-red-100', 'border-red-500', 'text-red-800');
        if (i === q.correct) {
          btn.classList.add('bg-green-100', 'border-green-500', 'text-green-800', 'font-bold');
        } else if (i === optIdx && optIdx !== q.correct) {
          btn.classList.add('bg-red-100', 'border-red-500', 'text-red-800');
        }
      }

      expDiv.classList.remove('hidden', 'bg-green-50', 'text-green-900', 'border-green-200', 'bg-red-50', 'text-red-900', 'border-red-200');
      expDiv.classList.add('border');

      if (optIdx === q.correct) {
        expDiv.classList.add('bg-green-50', 'text-green-900', 'border-green-200');
        expDiv.innerHTML = `<strong>✓ स्याबास! सही उत्तर।</strong><div class="mt-1">${q.exp}</div>`;
      } else {
        expDiv.classList.add('bg-red-50', 'text-red-900', 'border-red-200');
        expDiv.innerHTML = `<strong>✗ गलत उत्तर।</strong> सही विकल्प (${String.fromCharCode(65 + q.correct)}) हो।<div class="mt-1">${q.exp}</div>`;
      }
    }

    function resetQuizCh12() {
      for (let q = 0; q < quizDataCh12.length; q++) {
        for (let i = 0; i < 4; i++) {
          const btn = document.getElementById(`ch12-qbtn-${q}-${i}`);
          if (btn) {
            btn.className = 'p-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 transition font-medium cursor-pointer text-left';
          }
        }
        const expDiv = document.getElementById(`ch12-qexp-${q}`);
        if (expDiv) {
          expDiv.classList.add('hidden');
          expDiv.innerHTML = '';
        }
      }
    }

    window.setTabCh12 = setTabCh12;
    window.setExerciseCh12 = setExerciseCh12;
    window.setCh12LabMode = setCh12LabMode;
    window.setCh12EvalPreset = setCh12EvalPreset;
    window.runCh12Lab = runCh12Lab;
    window.checkQuizCh12 = checkQuizCh12;
    window.resetQuizCh12 = resetQuizCh12;


    
    // ================= CHAPTER 13 JAVASCRIPT LOGIC =================
    let currentCh13LabMode = 'solver';
    let ch13QuizScore = 0;
    const ch13QuizAnswered = {};

    function setTabCh13(tab) {
      const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
      tabs.forEach(t => {
        const btn = document.getElementById('ch13-tab-' + t);
        const view = document.getElementById('ch13-view-' + t);
        if (btn && view) {
          if (t === tab) {
            btn.className = 'px-5 py-2.5 rounded-xl bg-purple-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
            view.classList.remove('hidden');
          } else {
            btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
            view.classList.add('hidden');
          }
        }
      });
      if (tab === 'concepts') {
        setTimeout(runCh13Lab, 50);
      }
      if (window.MathJax && window.MathJax.Hub) {
        const v = document.getElementById('chapter-view-13');
        if (v) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v]);
      }
    }

    function setExerciseCh13(sec) {
      const secs = ['ex13_1', 'ex13_2', 'ex13_3', 'mixed', 'project'];
      secs.forEach(s => {
        const pill = document.getElementById('ch13-pill-' + s);
        const secDiv = document.getElementById('ch13-sec-' + s);
        if (pill && secDiv) {
          if (s === sec) {
            pill.className = 'px-4 py-2 rounded-xl bg-purple-600 text-white shadow-xs whitespace-nowrap cursor-pointer';
            secDiv.classList.remove('hidden');
          } else {
            pill.className = 'px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap cursor-pointer';
            secDiv.classList.add('hidden');
          }
        }
      });
      if (window.MathJax && window.MathJax.Hub) {
        const target = document.getElementById('ch13-sec-' + sec);
        if (target) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, target]);
      }
    }

    function setCh13LabMode(mode) {
      currentCh13LabMode = mode;
      const modes = ['solver', 'ineq', 'graph'];
      modes.forEach(m => {
        const btn = document.getElementById('ch13-lab-btn-' + m);
        const view = document.getElementById('ch13-lab-view-' + m);
        if (btn && view) {
          if (m === mode) {
            btn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold transition bg-indigo-600 text-white shadow-xs cursor-pointer';
            view.classList.remove('hidden');
          } else {
            btn.className = 'px-3 py-1.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white transition cursor-pointer';
            view.classList.add('hidden');
          }
        }
      });
      runCh13Lab();
    }

    function setCh13SolverPreset(a, b, c) {
      const elA = document.getElementById('ch13-eq-a');
      const elB = document.getElementById('ch13-eq-b');
      const elC = document.getElementById('ch13-eq-c');
      if (elA) elA.value = a;
      if (elB) elB.value = b;
      if (elC) elC.value = c;
      runCh13Lab();
    }

    function setCh13IneqTest(k) {
      const el = document.getElementById('ch13-ineq-test');
      if (el) el.value = k;
      runCh13Lab();
    }

    function setCh13GraphPoint(x, y) {
      const elX = document.getElementById('ch13-graph-x');
      const elY = document.getElementById('ch13-graph-y');
      if (elX) elX.value = x;
      if (elY) elY.value = y;
      runCh13Lab();
    }

    function runCh13Lab() {
      if (currentCh13LabMode === 'solver') {
        runCh13Solver();
      } else if (currentCh13LabMode === 'ineq') {
        runCh13Ineq();
      } else if (currentCh13LabMode === 'graph') {
        runCh13Graph();
      }
    }

    function runCh13Solver() {
      const a = parseFloat(document.getElementById('ch13-eq-a')?.value) || 1;
      const b = parseFloat(document.getElementById('ch13-eq-b')?.value) || 0;
      const c = parseFloat(document.getElementById('ch13-eq-c')?.value) || 0;

      const stepsDiv = document.getElementById('ch13-solver-steps');
      const resultDiv = document.getElementById('ch13-solver-result');
      const leftLabel = document.getElementById('ch13-scale-left-label');
      const rightLabel = document.getElementById('ch13-scale-right-label');

      const bSign = b >= 0 ? `+ ${b}` : `- ${Math.abs(b)}`;
      const eqStr = `${a === 1 ? '' : (a === -1 ? '-' : a)}x ${bSign} = ${c}`;

      if (leftLabel) leftLabel.textContent = `${a === 1 ? '' : a}x ${bSign}`;
      if (rightLabel) rightLabel.textContent = `${c}`;

      if (a === 0) {
        if (stepsDiv) stepsDiv.innerHTML = '<div class="text-red-400">गुणाङ्क (a) ० हुन सक्दैन किनकि यो एकपदीय रैखिक समीकरण होइन।</div>';
        if (resultDiv) resultDiv.textContent = 'अपरिभाषित (Undefined)';
        return;
      }

      // Step 1: Subtraction or Addition axiom
      const rhsAfterB = c - b;
      const step1Axiom = b >= 0 ? `दुवै पक्षबाट ${b} घटाउँदा (घटाउ तथ्य):` : `दुवै पक्षमा ${Math.abs(b)} जोड्दा (जोड तथ्य):`;
      const step1Math = `${a}x = ${c} - (${b}) = ${rhsAfterB}`;

      // Step 2: Division axiom
      const xVal = rhsAfterB / a;
      const step2Axiom = `दुवै पक्षलाई ${a} ले भाग गर्दा (भाग तथ्य):`;
      const step2Math = `x = ${rhsAfterB} / ${a} = ${Number.isInteger(xVal) ? xVal : xVal.toFixed(2)}`;

      // Step 3: Verification
      const lhsVal = a * xVal + b;
      const step3Math = `जाँच: LHS = ${a}(${Number.isInteger(xVal) ? xVal : xVal.toFixed(2)}) ${bSign} = ${Number.isInteger(lhsVal) ? lhsVal : lhsVal.toFixed(2)} = RHS (सत्य प्रमाणित)`;

      if (stepsDiv) {
        stepsDiv.innerHTML = `
          <div class="text-indigo-300 font-bold mb-1">दिइएको समीकरण: <span class="text-white">${eqStr}</span></div>
          <div class="p-2 bg-slate-950/60 rounded-lg">
            <span class="text-indigo-400">चरण १:</span> ${step1Axiom}<br>
            <span class="text-white ml-4">${step1Math}</span>
          </div>
          <div class="p-2 bg-slate-950/60 rounded-lg">
            <span class="text-indigo-400">चरण २:</span> ${step2Axiom}<br>
            <span class="text-white ml-4">${step2Math}</span>
          </div>
          <div class="p-2 bg-emerald-950/40 border border-emerald-700/50 rounded-lg text-emerald-300">
            <span class="font-bold">✓ उत्तरको प्रमाणीकरण:</span><br>
            <span class="ml-4 font-mono">${step3Math}</span>
          </div>
        `;
      }

      if (resultDiv) {
        resultDiv.textContent = `x = ${Number.isInteger(xVal) ? xVal : xVal.toFixed(2)}`;
      }
    }

    function runCh13Ineq() {
      const rel = document.getElementById('ch13-ineq-rel')?.value || 'lt';
      const a = parseInt(document.getElementById('ch13-ineq-slider')?.value) || 0;
      const k = parseFloat(document.getElementById('ch13-ineq-test')?.value) || 0;

      const canvas = document.getElementById('ch13-ineq-canvas');
      const verifDiv = document.getElementById('ch13-ineq-verification');

      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width;
      const h = canvas.height;

      ctx.clearRect(0, 0, w, h);

      // Number line parameters
      const cy = 55;
      const minX = -8;
      const maxX = 8;
      const stepPx = (w - 60) / (maxX - minX);
      const getX = (val) => 30 + (val - minX) * stepPx;

      // Draw Main axis
      ctx.strokeStyle = '#94a3b8';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(15, cy);
      ctx.lineTo(w - 15, cy);
      ctx.stroke();

      // Draw Arrows
      ctx.fillStyle = '#94a3b8';
      ctx.beginPath();
      ctx.moveTo(15, cy); ctx.lineTo(25, cy - 5); ctx.lineTo(25, cy + 5); ctx.fill();
      ctx.beginPath();
      ctx.moveTo(w - 15, cy); ctx.lineTo(w - 25, cy - 5); ctx.lineTo(w - 25, cy + 5); ctx.fill();

      // Draw Ticks & Labels
      ctx.font = '11px monospace';
      ctx.textAlign = 'center';
      for (let i = minX; i <= maxX; i++) {
        const px = getX(i);
        ctx.strokeStyle = (i === 0) ? '#6366f1' : '#64748b';
        ctx.lineWidth = (i === 0) ? 2 : 1;
        ctx.beginPath();
        ctx.moveTo(px, cy - 7);
        ctx.lineTo(px, cy + 7);
        ctx.stroke();

        ctx.fillStyle = (i === 0) ? '#c7d2fe' : '#94a3b8';
        ctx.fillText(i.toString(), px, cy + 22);
      }

      // Draw Shaded Region Ray
      const ax = getX(a);
      const isLeft = (rel === 'lt' || rel === 'le');
      const isClosed = (rel === 'le' || rel === 'ge');

      ctx.strokeStyle = '#ec4899';
      ctx.lineWidth = 5;
      ctx.beginPath();
      if (isLeft) {
        ctx.moveTo(ax, cy);
        ctx.lineTo(20, cy);
      } else {
        ctx.moveTo(ax, cy);
        ctx.lineTo(w - 20, cy);
      }
      ctx.stroke();

      // Shaded ray arrow
      ctx.fillStyle = '#ec4899';
      if (isLeft) {
        ctx.beginPath();
        ctx.moveTo(15, cy); ctx.lineTo(28, cy - 6); ctx.lineTo(28, cy + 6); ctx.fill();
      } else {
        ctx.beginPath();
        ctx.moveTo(w - 15, cy); ctx.lineTo(w - 28, cy - 6); ctx.lineTo(w - 28, cy + 6); ctx.fill();
      }

      // Draw boundary circle at a
      ctx.lineWidth = 3;
      ctx.strokeStyle = '#ec4899';
      ctx.fillStyle = isClosed ? '#ec4899' : '#0f172a';
      ctx.beginPath();
      ctx.arc(ax, cy, 6, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      // Draw Test Point k
      if (k >= minX && k <= maxX) {
        const kx = getX(k);
        ctx.fillStyle = '#38bdf8';
        ctx.beginPath();
        ctx.arc(kx, cy - 18, 5, 0, Math.PI * 2);
        ctx.fill();

        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(kx, cy - 13);
        ctx.lineTo(kx, cy - 5);
        ctx.stroke();

        ctx.font = 'bold 10px monospace';
        ctx.fillText(`x=${k}`, kx, cy - 23);
      }

      // Check condition for k
      let isSatisfied = false;
      let relSymbol = '<';
      if (rel === 'lt') { isSatisfied = (k < a); relSymbol = '<'; }
      else if (rel === 'le') { isSatisfied = (k <= a); relSymbol = '≤'; }
      else if (rel === 'gt') { isSatisfied = (k > a); relSymbol = '>'; }
      else if (rel === 'ge') { isSatisfied = (k >= a); relSymbol = '≥'; }

      const circleType = isClosed ? 'भरिएको वृत्त (Solid Circle ●)' : 'खुला वृत्त (Open Circle ○)';
      const statusColor = isSatisfied ? 'text-emerald-400' : 'text-red-400';
      const statusText = isSatisfied ? '✓ साँचो (सन्तुष्ट गर्दछ)' : '✗ झूटो (सन्तुष्ट गर्दैन)';

      if (verifDiv) {
        verifDiv.innerHTML = `
          <div><strong>असमानता:</strong> <span class="text-pink-400 font-bold">x ${relSymbol} ${a}</span> (${circleType})</div>
          <div><strong>परीक्षण मान:</strong> x = ${k} राख्दा: <span class="font-mono">${k} ${relSymbol} ${a}</span></div>
          <div class="font-bold ${statusColor}">नतिजा: ${statusText}</div>
        `;
      }
    }

    function runCh13Graph() {
      const elX = document.getElementById('ch13-graph-x');
      const elY = document.getElementById('ch13-graph-y');
      let x = parseInt(elX?.value) || 0;
      let y = parseInt(elY?.value) || 0;

      // Clamp between -5 and 5
      x = Math.max(-5, Math.min(5, x));
      y = Math.max(-5, Math.min(5, y));
      if (elX) elX.value = x;
      if (elY) elY.value = y;

      const canvas = document.getElementById('ch13-graph-canvas');
      const infoDiv = document.getElementById('ch13-graph-info');

      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width;
      const h = canvas.height;
      const cx = w / 2;
      const cy = h / 2;
      const step = 26; // px per unit

      ctx.clearRect(0, 0, w, h);

      // Grid Lines
      ctx.strokeStyle = '#1e293b';
      ctx.lineWidth = 1;
      for (let i = -5; i <= 5; i++) {
        // vertical
        ctx.beginPath();
        ctx.moveTo(cx + i * step, 0);
        ctx.lineTo(cx + i * step, h);
        ctx.stroke();
        // horizontal
        ctx.beginPath();
        ctx.moveTo(0, cy - i * step);
        ctx.lineTo(w, cy - i * step);
        ctx.stroke();
      }

      // X and Y Axes
      ctx.strokeStyle = '#6366f1';
      ctx.lineWidth = 2;
      // X-axis
      ctx.beginPath();
      ctx.moveTo(0, cy); ctx.lineTo(w, cy); ctx.stroke();
      // Y-axis
      ctx.beginPath();
      ctx.moveTo(cx, 0); ctx.lineTo(cx, h); ctx.stroke();

      // Axis Arrowheads
      ctx.fillStyle = '#6366f1';
      ctx.beginPath(); ctx.moveTo(w, cy); ctx.lineTo(w - 8, cy - 4); ctx.lineTo(w - 8, cy + 4); ctx.fill();
      ctx.beginPath(); ctx.moveTo(cx, 0); ctx.lineTo(cx - 4, 8); ctx.lineTo(cx + 4, 8); ctx.fill();

      // Ticks & Labels
      ctx.font = '10px monospace';
      ctx.textAlign = 'center';
      for (let i = -5; i <= 5; i++) {
        if (i !== 0) {
          // X labels
          ctx.fillStyle = '#94a3b8';
          ctx.fillText(i.toString(), cx + i * step, cy + 13);
          // Y labels
          ctx.fillText(i.toString(), cx - 12, cy - i * step + 3);
        }
      }
      ctx.fillStyle = '#c7d2fe';
      ctx.fillText('O', cx - 9, cy + 12);
      ctx.fillText('X', w - 8, cy - 6);
      ctx.fillText('Y', cx + 12, 12);

      // Quadrant labels
      ctx.fillStyle = '#334155';
      ctx.font = 'bold 12px sans-serif';
      ctx.fillText('Q1 (+,+)', cx + 2.5 * step, cy - 3.5 * step);
      ctx.fillText('Q2 (-,+)', cx - 2.5 * step, cy - 3.5 * step);
      ctx.fillText('Q3 (-,-)', cx - 2.5 * step, cy + 3.8 * step);
      ctx.fillText('Q4 (+,-)', cx + 2.5 * step, cy + 3.8 * step);

      // Plot point P(x, y)
      const px = cx + x * step;
      const py = cy - y * step;

      // Dashed guide lines
      ctx.strokeStyle = '#ec4899';
      ctx.lineWidth = 1.5;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(px, cy);
      ctx.lineTo(px, py);
      ctx.lineTo(cx, py);
      ctx.stroke();
      ctx.setLineDash([]);

      // Point circle
      ctx.fillStyle = '#a855f7';
      ctx.beginPath();
      ctx.arc(px, py, 6, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 2;
      ctx.stroke();

      // Point label
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 11px monospace';
      ctx.fillText(`P(${x}, ${y})`, px, py - 10);

      // Quadrant / Axis calculation
      let loc = '';
      if (x === 0 && y === 0) loc = 'उद्गम बिन्दु (Origin)';
      else if (x === 0) loc = 'Y-अक्षमा (On Y-axis)';
      else if (y === 0) loc = 'X-अक्षमा (On X-axis)';
      else if (x > 0 && y > 0) loc = 'पहिलो चतुर्थांश (First Quadrant — Q1)';
      else if (x < 0 && y > 0) loc = 'दोस्रो चतुर्थांश (Second Quadrant — Q2)';
      else if (x < 0 && y < 0) loc = 'तेस्रो चतुर्थांश (Third Quadrant — Q3)';
      else if (x > 0 && y < 0) loc = 'चौथो चतुर्थांश (Fourth Quadrant — Q4)';

      if (infoDiv) {
        infoDiv.innerHTML = `
          <div><strong>बिन्दु:</strong> <span class="text-purple-400 font-bold">P(${x}, ${y})</span></div>
          <div><strong>भुज (Abscissa, x):</strong> ${x} | <strong>कोटि (Ordinate, y):</strong> ${y}</div>
          <div><strong>स्थान:</strong> <span class="text-indigo-300 font-semibold">${loc}</span></div>
          <div class="text-[11px] text-slate-400">X-अक्षबाट लम्ब दूरी = ${Math.abs(y)} एकाइ | Y-अक्षबाट लम्ब दूरी = ${Math.abs(x)} एकाइ</div>
        `;
      }

      // Attach click listener once
      if (!canvas._clickAttached) {
        canvas._clickAttached = true;
        canvas.addEventListener('click', (e) => {
          const rect = canvas.getBoundingClientRect();
          const scaleX = canvas.width / rect.width;
          const scaleY = canvas.height / rect.height;
          const clickX = (e.clientX - rect.left) * scaleX;
          const clickY = (e.clientY - rect.top) * scaleY;
          const newX = Math.round((clickX - cx) / step);
          const newY = Math.round((cy - clickY) / step);
          setCh13GraphPoint(newX, newY);
        });
      }
    }

    const ch13QuizData = [
      { correct: 1, exp: 'खुला वाक्य (Open sentence) मा अज्ञात चर (variable) हुन्छ, जसको मान नतोकिएसम्म साँचो वा झूटो भन्न सकिँदैन।' },
      { correct: 1, exp: 'समीकरण x - 7 = 15 मा दुवैतर्फ ७ जोड्दा x = 15 + 7 = 22 प्राप्त हुन्छ (जोड तथ्य)।' },
      { correct: 2, exp: '4x = 24 मा x को गुणाङ्क ४ हटाउन दुवैतर्फ ४ ले भाग गरिन्छ (भाग तथ्य)।' },
      { correct: 0, exp: 'y + 8 = 13 ⇒ y = 13 - 8 = 5 मा मात्र यो खुला वाक्य साँचो हुन्छ।' },
      { correct: 1, exp: 'कुनै दुई वास्तविक सङ्ख्या बीच a < b, a = b, वा a > b मध्ये केवल एक अवस्था सत्य हुने नियम ट्राइकोटोमी नियम हो।' },
      { correct: 1, exp: 'ऋणात्मक सङ्ख्यामा सङ्ख्या रेखाको बायाँतर्फ पर्ने सङ्ख्या सानो हुन्छ। त्यसैले -5 < -2 सत्य हो।' },
      { correct: 1, exp: 'x ऋणात्मक (-) र y धनात्मक (+) हुने बिन्दु दोस्रो चतुर्थांश (Second Quadrant) मा पर्दछ।' },
      { correct: 1, exp: 'X-अक्ष र Y-अक्ष काटिने उद्गम बिन्दु (Origin) को निर्देशाङ्क सधैँ (0, 0) हुन्छ।' },
      { correct: 1, exp: 'कुनै सङ्ख्याको ३ गुणा (3x) मा ५ जोड्दा (+ 5) १७ हुन्छ (= 17) ⇒ 3x + 5 = 17।' },
      { correct: 1, exp: 'समीकरण: x + 15 = 40 ⇒ x = 40 - 15 = 25 (सुरुमा रु. २५ थियो)।' }
    ];

    function checkQuizCh13(qIdx, optIdx) {
      if (ch13QuizAnswered[qIdx]) return;
      ch13QuizAnswered[qIdx] = true;

      const q = ch13QuizData[qIdx];
      const buttons = document.querySelectorAll('.ch13-opt-' + qIdx);
      const expDiv = document.getElementById('ch13-qexp-' + qIdx);
      const badge = document.getElementById('ch13-qbadge-' + qIdx);

      const isCorrect = (optIdx === q.correct);

      buttons.forEach((btn, idx) => {
        btn.classList.remove('hover:bg-purple-50');
        if (idx === q.correct) {
          btn.className += ' bg-emerald-50 border-emerald-500 text-emerald-800 font-bold';
        } else if (idx === optIdx && !isCorrect) {
          btn.className += ' bg-red-50 border-red-500 text-red-800 line-through';
        } else {
          btn.className += ' opacity-50';
        }
      });

      if (badge) {
        if (isCorrect) {
          badge.className = 'text-xs font-bold px-2 py-0.5 rounded-lg bg-emerald-100 text-emerald-800';
          badge.textContent = '✓ सही';
          ch13QuizScore++;
        } else {
          badge.className = 'text-xs font-bold px-2 py-0.5 rounded-lg bg-red-100 text-red-800';
          badge.textContent = '✗ गलत';
        }
      }

      const scoreEl = document.getElementById('ch13-quiz-score');
      if (scoreEl) scoreEl.textContent = ch13QuizScore.toString();

      if (expDiv) {
        expDiv.classList.remove('hidden');
        expDiv.innerHTML = `<strong>व्याख्या:</strong> ${q.exp}`;
      }
    }

    function resetQuizCh13() {
      ch13QuizScore = 0;
      for (const k in ch13QuizAnswered) delete ch13QuizAnswered[k];

      const scoreEl = document.getElementById('ch13-quiz-score');
      if (scoreEl) scoreEl.textContent = '0';

      for (let i = 0; i < ch13QuizData.length; i++) {
        const buttons = document.querySelectorAll('.ch13-opt-' + i);
        buttons.forEach(btn => {
          btn.className = 'ch13-opt-' + i + ' p-3 rounded-xl border border-slate-200 hover:bg-purple-50 text-left transition font-medium cursor-pointer';
        });
        const badge = document.getElementById('ch13-qbadge-' + i);
        if (badge) {
          badge.className = 'text-xs font-bold px-2 py-0.5 rounded-lg bg-slate-100 text-slate-600';
          badge.textContent = 'अपेक्षित';
        }
        const expDiv = document.getElementById('ch13-qexp-' + i);
        if (expDiv) {
          expDiv.classList.add('hidden');
          expDiv.innerHTML = '';
        }
      }
    }

    window.setTabCh13 = setTabCh13;
    window.setExerciseCh13 = setExerciseCh13;
    window.setCh13LabMode = setCh13LabMode;
    window.setCh13SolverPreset = setCh13SolverPreset;
    window.setCh13IneqTest = setCh13IneqTest;
    window.setCh13GraphPoint = setCh13GraphPoint;
    window.runCh13Lab = runCh13Lab;
    window.checkQuizCh13 = checkQuizCh13;
    window.resetQuizCh13 = resetQuizCh13;



    // ================= CHAPTER 14 JAVASCRIPT LOGIC =================
    let currentCh14LabMode = 'protractor';
    let currentCh14Angle = 60;
    let ch14ConstructStep = 1;
    let ch14QuizScore = 0;
    const ch14QuizAnswered = {};

    function setTabCh14(tab) {
      const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
      tabs.forEach(t => {
        const btn = document.getElementById('ch14-tab-' + t);
        const view = document.getElementById('ch14-view-' + t);
        if (btn && view) {
          if (t === tab) {
            btn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
            view.classList.remove('hidden');
          } else {
            btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
            view.classList.add('hidden');
          }
        }
      });
      if (tab === 'concepts') {
        setTimeout(runCh14Lab, 50);
      }
      if (window.MathJax && window.MathJax.Hub) {
        const v = document.getElementById('chapter-view-14');
        if (v) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, v]);
      }
    }

    function setExerciseCh14(sec) {
      const secs = ['ex14_1', 'ex14_2', 'ex14_3', 'ex14_4', 'ex14_5', 'project'];
      secs.forEach(s => {
        const pill = document.getElementById('ch14-pill-' + s);
        const secDiv = document.getElementById('ch14-sec-' + s);
        if (pill && secDiv) {
          if (s === sec) {
            pill.className = 'px-4 py-2 rounded-xl bg-blue-600 text-white shadow-xs whitespace-nowrap cursor-pointer';
            secDiv.classList.remove('hidden');
          } else {
            pill.className = 'px-4 py-2 rounded-xl text-slate-600 hover:bg-slate-100 whitespace-nowrap cursor-pointer';
            secDiv.classList.add('hidden');
          }
        }
      });
      if (window.MathJax && window.MathJax.Hub) {
        const target = document.getElementById('ch14-sec-' + sec);
        if (target) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, target]);
      }
    }

    function setCh14LabMode(mode) {
      currentCh14LabMode = mode;
      const modes = ['protractor', 'pairs', 'construct'];
      modes.forEach(m => {
        const btn = document.getElementById('ch14-lab-btn-' + m);
        const view = document.getElementById('ch14-lab-view-' + m);
        if (btn && view) {
          if (m === mode) {
            btn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold transition bg-blue-600 text-white shadow-xs cursor-pointer';
            view.classList.remove('hidden');
          } else {
            btn.className = 'px-3 py-1.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white transition cursor-pointer';
            view.classList.add('hidden');
          }
        }
      });
      runCh14Lab();
    }

    function setCh14Angle(deg) {
      currentCh14Angle = parseInt(deg) || 0;
      const slider = document.getElementById('ch14-deg-slider');
      const valLabel = document.getElementById('ch14-deg-val');
      const liveMath = document.getElementById('ch14-live-math-deg');

      if (slider) slider.value = currentCh14Angle;
      if (valLabel) valLabel.textContent = currentCh14Angle + '°';
      if (liveMath) liveMath.textContent = currentCh14Angle + '°';

      // Type Badge
      const badge = document.getElementById('ch14-angle-type-badge');
      if (badge) {
        if (currentCh14Angle === 0) {
          badge.textContent = 'शून्य कोण (Zero Angle)';
          badge.className = 'font-bold px-2 py-0.5 rounded-md bg-slate-800 text-slate-300 border border-slate-700';
        } else if (currentCh14Angle < 90) {
          badge.textContent = 'न्यून कोण (Acute Angle)';
          badge.className = 'font-bold px-2 py-0.5 rounded-md bg-cyan-900/80 text-cyan-300 border border-cyan-700/50';
        } else if (currentCh14Angle === 90) {
          badge.textContent = 'समकोण (Right Angle — ९०°)';
          badge.className = 'font-bold px-2 py-0.5 rounded-md bg-emerald-900/80 text-emerald-300 border border-emerald-700/50';
        } else if (currentCh14Angle < 180) {
          badge.textContent = 'अधिक कोण (Obtuse Angle)';
          badge.className = 'font-bold px-2 py-0.5 rounded-md bg-amber-900/80 text-amber-300 border border-amber-700/50';
        } else if (currentCh14Angle === 180) {
          badge.textContent = 'सरल कोण (Straight Angle — १८०°)';
          badge.className = 'font-bold px-2 py-0.5 rounded-md bg-purple-900/80 text-purple-300 border border-purple-700/50';
        } else if (currentCh14Angle < 360) {
          badge.textContent = 'बृहत् कोण (Reflex Angle)';
          badge.className = 'font-bold px-2 py-0.5 rounded-md bg-pink-900/80 text-pink-300 border border-pink-700/50';
        } else {
          badge.textContent = 'पूर्ण परिभ्रमण कोण (Complete Turn — ३६०°)';
          badge.className = 'font-bold px-2 py-0.5 rounded-md bg-indigo-900/80 text-indigo-300 border border-indigo-700/50';
        }
      }

      // Calculations
      const compEl = document.getElementById('ch14-angle-comp');
      const suppEl = document.getElementById('ch14-angle-supp');
      const reflEl = document.getElementById('ch14-angle-refl');

      if (compEl) compEl.textContent = (currentCh14Angle <= 90) ? (90 - currentCh14Angle) + '°' : 'लागू हुँदैन (> ९०°)';
      if (suppEl) suppEl.textContent = (currentCh14Angle <= 180) ? (180 - currentCh14Angle) + '°' : 'लागू हुँदैन (> १८०°)';
      if (reflEl) reflEl.textContent = (360 - currentCh14Angle) + '°';

      drawCh14Protractor();
    }

    function runCh14Lab() {
      if (currentCh14LabMode === 'protractor') {
        drawCh14Protractor();
      } else if (currentCh14LabMode === 'pairs') {
        drawCh14Pairs();
      } else if (currentCh14LabMode === 'construct') {
        drawCh14Construct();
      }
    }

    function drawCh14Protractor() {
      const canvas = document.getElementById('ch14-protractor-canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width;
      const h = canvas.height;
      const ox = w / 2;
      const oy = h - 45;
      const r = 125;

      ctx.clearRect(0, 0, w, h);

      // Draw Protractor Background Body
      ctx.fillStyle = 'rgba(30, 41, 59, 0.7)';
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(ox, oy, r, Math.PI, 0, false);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();

      // Inner Semicircle Ring
      ctx.strokeStyle = '#1e293b';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.arc(ox, oy, r - 30, Math.PI, 0, false);
      ctx.stroke();

      // Degree Ticks & Labels
      ctx.font = '9px monospace';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';

      for (let d = 0; d <= 180; d += 5) {
        const rad = Math.PI - (d * Math.PI / 180);
        const isTen = (d % 10 === 0);
        const tickLen = isTen ? 14 : 7;
        const x1 = ox + Math.cos(rad) * r;
        const y1 = oy - Math.sin(rad) * r;
        const x2 = ox + Math.cos(rad) * (r - tickLen);
        const y2 = oy - Math.sin(rad) * (r - tickLen);

        ctx.strokeStyle = isTen ? '#7dd3fc' : '#475569';
        ctx.lineWidth = isTen ? 1.5 : 1;
        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y2);
        ctx.stroke();

        if (d % 30 === 0) {
          const tx = ox + Math.cos(rad) * (r - 20);
          const ty = oy - Math.sin(rad) * (r - 20);
          ctx.fillStyle = '#bae6fd';
          ctx.fillText(d.toString(), tx, ty);
        }
      }

      // Base Arm OA (Horizontal Right)
      ctx.strokeStyle = '#94a3b8';
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(ox, oy);
      ctx.lineTo(ox + r + 15, oy);
      ctx.stroke();

      // Arrow on Base Arm
      ctx.fillStyle = '#94a3b8';
      ctx.beginPath();
      ctx.moveTo(ox + r + 20, oy);
      ctx.lineTo(ox + r + 12, oy - 4);
      ctx.lineTo(ox + r + 12, oy + 4);
      ctx.fill();

      // Rotating Arm OB at angle theta
      const thetaRad = currentCh14Angle * Math.PI / 180;
      const bx = ox + Math.cos(thetaRad) * (r + 15);
      const by = oy - Math.sin(thetaRad) * (r + 15);

      // Shaded Angle Sector Arc
      ctx.fillStyle = 'rgba(6, 182, 212, 0.25)';
      ctx.beginPath();
      ctx.moveTo(ox, oy);
      ctx.arc(ox, oy, 45, 0, -thetaRad, true);
      ctx.closePath();
      ctx.fill();

      ctx.strokeStyle = '#06b6d4';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(ox, oy, 45, 0, -thetaRad, true);
      ctx.stroke();

      // Rotating Arm Line
      ctx.strokeStyle = '#38bdf8';
      ctx.lineWidth = 3.5;
      ctx.beginPath();
      ctx.moveTo(ox, oy);
      ctx.lineTo(bx, by);
      ctx.stroke();

      // Arrow on Rotating Arm
      const arrowLen = 10;
      const arrowAngle = 0.35;
      ctx.fillStyle = '#38bdf8';
      ctx.beginPath();
      ctx.moveTo(bx, by);
      ctx.lineTo(bx - arrowLen * Math.cos(thetaRad - arrowAngle), by + arrowLen * Math.sin(thetaRad - arrowAngle));
      ctx.lineTo(bx - arrowLen * Math.cos(thetaRad + arrowAngle), by + arrowLen * Math.sin(thetaRad + arrowAngle));
      ctx.fill();

      // Center Pivot Eyelet
      ctx.fillStyle = '#f59e0b';
      ctx.beginPath();
      ctx.arc(ox, oy, 5, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 1.5;
      ctx.stroke();

      // Labels
      ctx.font = 'bold 11px monospace';
      ctx.fillStyle = '#ffffff';
      ctx.fillText('O', ox - 12, oy + 12);
      ctx.fillText('A', ox + r + 25, oy + 4);
      ctx.fillText('B', bx + 10 * Math.cos(thetaRad), by - 10 * Math.sin(thetaRad));

      // Attach Click / Drag Listener Once
      if (!canvas._clickAttached) {
        canvas._clickAttached = true;
        const handleAngleEvent = (e) => {
          const rect = canvas.getBoundingClientRect();
          const scaleX = canvas.width / rect.width;
          const scaleY = canvas.height / rect.height;
          const clickX = (e.clientX - rect.left) * scaleX;
          const clickY = (e.clientY - rect.top) * scaleY;
          const dx = clickX - ox;
          const dy = oy - clickY;
          let deg = Math.round(Math.atan2(dy, dx) * 180 / Math.PI);
          if (deg < 0) deg = 360 + deg;
          setCh14Angle(deg);
        };
        canvas.addEventListener('mousedown', (e) => {
          canvas._isDragging = true;
          handleAngleEvent(e);
        });
        window.addEventListener('mousemove', (e) => {
          if (canvas._isDragging) handleAngleEvent(e);
        });
        window.addEventListener('mouseup', () => {
          canvas._isDragging = false;
        });
      }
    }

    function drawCh14Pairs() {
      const mode = document.getElementById('ch14-pairs-mode')?.value || 'linear';
      const slider = document.getElementById('ch14-pair-slider');
      const aValLabel = document.getElementById('ch14-pair-a-val');
      const expDiv = document.getElementById('ch14-pair-explanation');
      const mathCard = document.getElementById('ch14-pair-math-card');
      const canvas = document.getElementById('ch14-pairs-canvas');

      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width;
      const h = canvas.height;
      const cx = w / 2;
      const cy = h / 2 + 30;

      let a = parseInt(slider?.value) || 70;
      if (mode === 'comp' && a > 80) a = 80;
      if (slider) slider.max = (mode === 'comp') ? '80' : '170';
      if (slider) slider.min = (mode === 'comp') ? '10' : '10';
      if (slider) slider.value = a;
      if (aValLabel) aValLabel.textContent = a + '°';

      ctx.clearRect(0, 0, w, h);

      if (mode === 'linear') {
        const b = 180 - a;
        const radA = a * Math.PI / 180;
        const r = 90;

        // Baseline AOB
        ctx.strokeStyle = '#94a3b8';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(35, cy);
        ctx.lineTo(w - 35, cy);
        ctx.stroke();

        // Arm OC
        const ocX = cx + Math.cos(radA) * r;
        const ocY = cy - Math.sin(radA) * r;
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 3.5;
        ctx.beginPath();
        ctx.moveTo(cx, cy);
        ctx.lineTo(ocX, ocY);
        ctx.stroke();

        // Arc A (from right horizontal 0 to radA)
        ctx.strokeStyle = '#06b6d4';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.arc(cx, cy, 35, 0, -radA, true);
        ctx.stroke();

        // Arc B (from radA to PI)
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.arc(cx, cy, 45, -radA, -Math.PI, true);
        ctx.stroke();

        // Center dot
        ctx.fillStyle = '#ffffff';
        ctx.beginPath(); ctx.arc(cx, cy, 4, 0, Math.PI * 2); ctx.fill();

        // Labels
        ctx.font = 'bold 11px monospace';
        ctx.fillStyle = '#06b6d4';
        ctx.fillText(`a = ${a}°`, cx + 45, cy - 15);
        ctx.fillStyle = '#f59e0b';
        ctx.fillText(`b = ${b}°`, cx - 65, cy - 20);
        ctx.fillStyle = '#ffffff';
        ctx.fillText('A', 25, cy + 5);
        ctx.fillText('B', w - 25, cy + 5);
        ctx.fillText('C', ocX, ocY - 10);
        ctx.fillText('O', cx - 5, cy + 18);

        if (expDiv) {
          expDiv.innerHTML = `
            <div><strong>सम्बन्ध:</strong> रेखीय जोडाका कोणहरू (Linear Pair)</div>
            <div><strong>तथ्य:</strong> सीधा रेखामा बन्ने दुई आसन्न कोणहरूको योगफल १८०° हुन्छ।</div>
            <div class="text-cyan-400">समीकरण: a + b = 180° ⇒ b = 180° - ${a}° = ${b}°</div>
          `;
        }
        if (mathCard) {
          mathCard.innerHTML = `रेखीय जोडा: ${a}° + ${b}° = 180° (सरल कोण)`;
        }

      } else if (mode === 'comp') {
        const b = 90 - a;
        const radA = a * Math.PI / 180;
        const r = 90;

        // Horizontal OA & Vertical OB (Right angle)
        ctx.strokeStyle = '#94a3b8';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(cx, cy); ctx.lineTo(cx + r + 20, cy); ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(cx, cy); ctx.lineTo(cx, cy - r - 20); ctx.stroke();

        // 90 deg corner box
        ctx.strokeStyle = '#475569';
        ctx.lineWidth = 1.5;
        ctx.strokeRect(cx, cy - 15, 15, 15);

        // Ray OC
        const ocX = cx + Math.cos(radA) * r;
        const ocY = cy - Math.sin(radA) * r;
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 3.5;
        ctx.beginPath();
        ctx.moveTo(cx, cy); ctx.lineTo(ocX, ocY); ctx.stroke();

        // Arcs
        ctx.strokeStyle = '#06b6d4';
        ctx.lineWidth = 2;
        ctx.beginPath(); ctx.arc(cx, cy, 32, 0, -radA, true); ctx.stroke();
        ctx.strokeStyle = '#ec4899';
        ctx.lineWidth = 2;
        ctx.beginPath(); ctx.arc(cx, cy, 45, -radA, -Math.PI / 2, true); ctx.stroke();

        // Labels
        ctx.font = 'bold 11px monospace';
        ctx.fillStyle = '#06b6d4'; ctx.fillText(`a = ${a}°`, cx + 45, cy - 12);
        ctx.fillStyle = '#ec4899'; ctx.fillText(`b = ${b}°`, cx + 18, cy - 55);
        ctx.fillStyle = '#ffffff'; ctx.fillText('O', cx - 12, cy + 12);
        ctx.fillText('A', cx + r + 25, cy + 4); ctx.fillText('B', cx - 4, cy - r - 25);
        ctx.fillText('C', ocX + 5, ocY - 5);

        if (expDiv) {
          expDiv.innerHTML = `
            <div><strong>सम्बन्ध:</strong> पूरक कोणहरू (Complementary Angles)</div>
            <div><strong>तथ्य:</strong> दुई कोणहरूको योगफल ९०° भए तिनीहरू पूरक कोण हुन्।</div>
            <div class="text-cyan-400">समीकरण: a + b = 90° ⇒ b = 90° - ${a}° = ${b}°</div>
          `;
        }
        if (mathCard) {
          mathCard.innerHTML = `पूरक कोण: ${a}° + ${b}° = 90° (समकोण)`;
        }

      } else if (mode === 'vert') {
        const radA = a * Math.PI / 180;
        const b = 180 - a;
        const r = 85;

        // Line 1: Horizontal line
        ctx.strokeStyle = '#94a3b8';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(cx - r - 20, cy); ctx.lineTo(cx + r + 20, cy); ctx.stroke();

        // Line 2: Intersecting line at angle radA
        const dx = Math.cos(radA) * (r + 20);
        const dy = Math.sin(radA) * (r + 20);
        ctx.strokeStyle = '#38bdf8';
        ctx.lineWidth = 2.5;
        ctx.beginPath();
        ctx.moveTo(cx - dx, cy + dy); ctx.lineTo(cx + dx, cy - dy); ctx.stroke();

        // Opposite Arcs (Angle 1 and Angle 3)
        ctx.strokeStyle = '#06b6d4';
        ctx.lineWidth = 2.5;
        ctx.beginPath(); ctx.arc(cx, cy, 28, 0, -radA, true); ctx.stroke();
        ctx.beginPath(); ctx.arc(cx, cy, 28, -Math.PI, -Math.PI - radA, true); ctx.stroke();

        // Opposite Arcs (Angle 2 and Angle 4)
        ctx.strokeStyle = '#f59e0b';
        ctx.lineWidth = 2;
        ctx.beginPath(); ctx.arc(cx, cy, 38, -radA, -Math.PI, true); ctx.stroke();
        ctx.beginPath(); ctx.arc(cx, cy, 38, -Math.PI - radA, -Math.PI * 2, true); ctx.stroke();

        ctx.font = 'bold 11px monospace';
        ctx.fillStyle = '#06b6d4';
        ctx.fillText(`∠1=${a}°`, cx + 35, cy - 12);
        ctx.fillText(`∠3=${a}°`, cx - 65, cy + 15);
        ctx.fillStyle = '#f59e0b';
        ctx.fillText(`∠2=${b}°`, cx - 25, cy - 42);
        ctx.fillText(`∠4=${b}°`, cx + 15, cy + 42);

        if (expDiv) {
          expDiv.innerHTML = `
            <div><strong>सम्बन्ध:</strong> शीर्षाभिमुख कोणहरू (Vertically Opposite)</div>
            <div><strong>तथ्य:</strong> आपसमा काटिएका दुई रेखाका आमने-सामनेका कोण सधैँ बराबर हुन्छन्।</div>
            <div class="text-cyan-400">∠1 = ∠3 = ${a}° तथा ∠2 = ∠4 = ${b}°</div>
          `;
        }
        if (mathCard) {
          mathCard.innerHTML = `शीर्षाभिमुख बराबर: ∠1 = ∠3 = ${a}° | ∠2 = ∠4 = ${b}°`;
        }
      }
    }

    const ch14ConstructData = {
      bisector_line: [
        { desc: '१. रुलरको सहायताले तोकिएको नापको सीधा रेखाखण्ड AB खिच्ने।', summary: 'चरण १: रेखाखण्ड AB को निर्माण' },
        { desc: '२. कम्पासको सियो बिन्दु A मा राखी AB को आधाभन्दा बढी (more than half) अर्धव्यास लिई रेखाखण्डको माथि र तल दुईवटा चापहरू खिच्ने।', summary: 'चरण २: बिन्दु A बाट माथि र तल चाप' },
        { desc: '३. सोही अर्धव्यास नबदली कम्पासको सियो बिन्दु B मा राखी पहिलेका चापहरूलाई काट्ने गरी क्रमशः बिन्दु P र Q मा चाप खिच्ने।', summary: 'चरण ३: बिन्दु B बाट चाप काटी P र Q प्राप्त' },
        { desc: '४. रुलरको सहायताले बिन्दु P र Q लाई सीधा रेखाले जोड्ने। यो रेखा PQ नै रेखाखण्ड AB को अभीष्ट लम्बाधर्क (Perpendicular Bisector) हो (AO = OB र ∠AOP = ९०°)।', summary: 'चरण ४: लम्बाधर्क PQ पूर्ण भयो' }
      ],
      angle_60: [
        { desc: '१. रुलरले सीधा किरण OA खिच्ने।', summary: 'चरण १: आधार किरण OA' },
        { desc: '२. बिन्दु O मा कम्पास राखी उपयुक्त अर्धव्यास लिई किरण OA लाई बिन्दु B मा काट्ने गरी आधार चाप खिच्ने।', summary: 'चरण २: O बाट आधार चाप' },
        { desc: '३. सोही अर्धव्यास लिएर सियो बिन्दु B मा राखी उक्त चापलाई काट्दा बिन्दु C प्राप्त हुन्छ।', summary: 'चरण ३: B बाट चाप काट्दा ६०° बिन्दु C' },
        { desc: '४. शीर्षबिन्दु O र C लाई रुलरले सीधा जोड्दा ∠AOC = ६०° (समबाहु त्रिभुजको कोण) तयार हुन्छ।', summary: 'चरण ४: ∠AOC = ६०° सम्पन्न' }
      ],
      angle_90: [
        { desc: '१. आधार किरण OA खिची O बाट आधार चाप खिच्ने (बिन्दु B मा काट्छ)।', summary: 'चरण १: आधार किरण र चाप' },
        { desc: '२. सोही नापले B बाट पहिलो कटाइ C (६०°) र C बाट दोस्रो कटाइ D (१२०°) प्राप्त गर्ने।', summary: 'चरण २: ६०° र १२०° का बिन्दुहरू' },
        { desc: '३. बिन्दु C र D बाट बराबर अर्धव्यास लिई माथिल्लो भागमा चापहरू काटी प्रतिच्छेदन बिन्दु E बनाउने।', summary: 'चरण ३: ६०° र १२०° को अर्धक' },
        { desc: '४. O र E लाई रुलरले जोड्दा ठ्याक्कै ९०° को समकोण (Right Angle, OE ⊥ OA) प्राप्त हुन्छ।', summary: 'चरण ४: ∠AOE = ९०° सम्पन्न' }
      ],
      angle_45: [
        { desc: '१. पहिले ९०° को समकोण ∠AOE रचना गर्ने।', summary: 'चरण १: ९०° को समकोण' },
        { desc: '२. आधार भुजाको बिन्दु B र ९०° को भुजाको बिन्दु F बाट समान अर्धव्यास लिने।', summary: 'चरण २: B र F बाट चाप' },
        { desc: '३. दुवै बिन्दुबाट भित्री भागमा चाप काटी काटिएको बिन्दुलाई G नाम दिने।', summary: 'चरण ३: ९०° को अर्धक बिन्दु G' },
        { desc: '४. O र G जोड्दा किरण OG ले ९०° लाई आधा गरी ∠AOG = ४५° बनाउँछ।', summary: 'चरण ४: ∠AOG = ४५° सम्पन्न' }
      ],
      angle_30: [
        { desc: '१. पहिले ६०° को कोण ∠AOC रचना गर्ने।', summary: 'चरण १: ६०° को कोण' },
        { desc: '२. आधार बिन्दु B र ६०° को बिन्दु C बाट समान अर्धव्यास लिने।', summary: 'चरण २: B र C बाट चाप' },
        { desc: '३. दुवै बिन्दुबाट भित्री भागमा चाप काटी प्रतिच्छेदन बिन्दु H बनाउने।', summary: 'चरण ३: ६०° को अर्धक बिन्दु H' },
        { desc: '४. O र H जोड्दा किरण OH ले ६०° लाई आधा गरी ∠AOH = ३०° बनाउँछ।', summary: 'चरण ४: ∠AOH = ३०° सम्पन्न' }
      ],
      angle_bisector: [
        { desc: '१. दिइएको कुनै पनि कोण ∠AOB को शीर्षबिन्दु O मा कम्पास राख्ने।', summary: 'चरण १: शीर्षबिन्दु O मा कम्पास' },
        { desc: '२. उपयुक्त अर्धव्यास लिई भुजा OA लाई P मा र OB लाई Q मा काट्ने गरी चाप खिच्ने।', summary: 'चरण २: भुजाहरूमा P र Q बिन्दु' },
        { desc: '३. बिन्दु P र Q बाट समान अर्धव्यास लिई कोणको भित्र चाप काटी बिन्दु R बनाउने।', summary: 'चरण ३: P र Q बाट चाप काट्ने' },
        { desc: '४. O र R लाई जोड्दा किरण OR ले दिइएको कोणलाई दुई बराबर भागमा बाँड्दछ (∠AOR = ∠BOR)।', summary: 'चरण ४: कोणको अर्धक OR पूर्ण भयो' }
      ]
    };

    function resetCh14Construct() {
      ch14ConstructStep = 1;
    }

    function prevCh14Step() {
      if (ch14ConstructStep > 1) {
        ch14ConstructStep--;
        runCh14Lab();
      }
    }

    function nextCh14Step() {
      const type = document.getElementById('ch14-construct-type')?.value || 'bisector_line';
      const steps = ch14ConstructData[type] || [];
      if (ch14ConstructStep < steps.length) {
        ch14ConstructStep++;
        runCh14Lab();
      }
    }

    function drawCh14Construct() {
      const type = document.getElementById('ch14-construct-type')?.value || 'bisector_line';
      const steps = ch14ConstructData[type] || [];
      const counter = document.getElementById('ch14-step-counter');
      const descDiv = document.getElementById('ch14-construct-desc');
      const sumDiv = document.getElementById('ch14-construct-summary');
      const canvas = document.getElementById('ch14-construct-canvas');

      if (counter) counter.textContent = `${ch14ConstructStep} / ${steps.length}`;
      const curData = steps[ch14ConstructStep - 1];
      if (descDiv && curData) descDiv.textContent = curData.desc;
      if (sumDiv && curData) sumDiv.textContent = curData.summary;

      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width;
      const h = canvas.height;
      const cx = w / 2;
      const cy = h / 2 + 30;

      ctx.clearRect(0, 0, w, h);

      if (type === 'bisector_line') {
        const ax = cx - 90, bx = cx + 90, ay = cy;
        // Step 1: Base line AB
        ctx.strokeStyle = '#94a3b8'; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(ax, ay); ctx.lineTo(bx, ay); ctx.stroke();
        ctx.fillStyle = '#ffffff';
        ctx.beginPath(); ctx.arc(ax, ay, 4, 0, Math.PI * 2); ctx.fill();
        ctx.beginPath(); ctx.arc(bx, ay, 4, 0, Math.PI * 2); ctx.fill();
        ctx.font = 'bold 11px monospace';
        ctx.fillText('A', ax - 14, ay + 4); ctx.fillText('B', bx + 6, ay + 4);

        if (ch14ConstructStep >= 2) {
          // Arcs from A
          ctx.strokeStyle = '#06b6d4'; ctx.lineWidth = 1.5; ctx.setLineDash([3, 3]);
          ctx.beginPath(); ctx.arc(ax, ay, 110, -Math.PI/3, -Math.PI/6); ctx.stroke();
          ctx.beginPath(); ctx.arc(ax, ay, 110, Math.PI/6, Math.PI/3); ctx.stroke();
          ctx.setLineDash([]);
        }
        if (ch14ConstructStep >= 3) {
          // Arcs from B
          ctx.strokeStyle = '#ec4899'; ctx.lineWidth = 1.5; ctx.setLineDash([3, 3]);
          ctx.beginPath(); ctx.arc(bx, ay, 110, -Math.PI*5/6, -Math.PI*2/3); ctx.stroke();
          ctx.beginPath(); ctx.arc(bx, ay, 110, Math.PI*2/3, Math.PI*5/6); ctx.stroke();
          ctx.setLineDash([]);
          // Intersection points P & Q
          ctx.fillStyle = '#f59e0b';
          ctx.beginPath(); ctx.arc(cx, cy - 65, 4, 0, Math.PI * 2); ctx.fill();
          ctx.beginPath(); ctx.arc(cx, cy + 65, 4, 0, Math.PI * 2); ctx.fill();
          ctx.fillText('P', cx + 6, cy - 65); ctx.fillText('Q', cx + 6, cy + 68);
        }
        if (ch14ConstructStep >= 4) {
          // Bisector Line PQ
          ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 3;
          ctx.beginPath(); ctx.moveTo(cx, cy - 85); ctx.lineTo(cx, cy + 85); ctx.stroke();
          // Right angle box
          ctx.strokeStyle = '#f59e0b'; ctx.lineWidth = 1.5;
          ctx.strokeRect(cx, cy - 12, 12, 12);
          ctx.fillStyle = '#ffffff'; ctx.fillText('O', cx - 14, cy + 16);
        }
      } else {
        // Angle constructions (60, 90, 45, 30, bisector)
        const ox = 70, oy = cy + 20;
        const r = 90;
        // Step 1: Base Ray OA
        ctx.strokeStyle = '#94a3b8'; ctx.lineWidth = 3;
        ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(ox + 200, oy); ctx.stroke();
        ctx.fillStyle = '#ffffff'; ctx.beginPath(); ctx.arc(ox, oy, 4, 0, Math.PI*2); ctx.fill();
        ctx.font = 'bold 11px monospace';
        ctx.fillText('O', ox - 14, oy + 4); ctx.fillText('A', ox + 210, oy + 4);

        if (ch14ConstructStep >= 2) {
          // Base Arc from O
          ctx.strokeStyle = '#475569'; ctx.lineWidth = 1.5; ctx.setLineDash([3, 3]);
          ctx.beginPath(); ctx.arc(ox, oy, r, -Math.PI*2/3, 0); ctx.stroke();
          ctx.setLineDash([]);
          ctx.fillStyle = '#38bdf8'; ctx.beginPath(); ctx.arc(ox + r, oy, 3.5, 0, Math.PI*2); ctx.fill();
          ctx.fillText('B', ox + r - 3, oy + 14);
        }

        if (type === 'angle_60') {
          if (ch14ConstructStep >= 3) {
            const rad60 = Math.PI / 3;
            const cx60 = ox + Math.cos(rad60) * r;
            const cy60 = oy - Math.sin(rad60) * r;
            ctx.fillStyle = '#f59e0b'; ctx.beginPath(); ctx.arc(cx60, cy60, 4, 0, Math.PI*2); ctx.fill();
            ctx.fillText('C (60°)', cx60 + 6, cy60 - 4);
          }
          if (ch14ConstructStep >= 4) {
            const rad60 = Math.PI / 3;
            const armX = ox + Math.cos(rad60) * 160;
            const armY = oy - Math.sin(rad60) * 160;
            ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 3;
            ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(armX, armY); ctx.stroke();
            ctx.strokeStyle = '#06b6d4'; ctx.lineWidth = 2;
            ctx.beginPath(); ctx.arc(ox, oy, 35, 0, -rad60, true); ctx.stroke();
            ctx.fillStyle = '#06b6d4'; ctx.fillText('60°', ox + 42, oy - 15);
          }
        } else {
          // Generic angle arm for other types
          let targetDeg = 90;
          if (type === 'angle_45') targetDeg = 45;
          if (type === 'angle_30') targetDeg = 30;
          if (type === 'angle_bisector') targetDeg = 50;

          const rad = targetDeg * Math.PI / 180;
          if (ch14ConstructStep >= 3) {
            const px = ox + Math.cos(rad) * r;
            const py = oy - Math.sin(rad) * r;
            ctx.fillStyle = '#f59e0b'; ctx.beginPath(); ctx.arc(px, py, 4, 0, Math.PI*2); ctx.fill();
          }
          if (ch14ConstructStep >= 4) {
            const armX = ox + Math.cos(rad) * 160;
            const armY = oy - Math.sin(rad) * 160;
            ctx.strokeStyle = '#38bdf8'; ctx.lineWidth = 3;
            ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(armX, armY); ctx.stroke();
            ctx.strokeStyle = '#06b6d4'; ctx.lineWidth = 2;
            ctx.beginPath(); ctx.arc(ox, oy, 35, 0, -rad, true); ctx.stroke();
            ctx.fillStyle = '#06b6d4'; ctx.fillText(`${targetDeg}°`, ox + 42, oy - 15);
          }
        }
      }
    }

    const ch14QuizData = [
      { correct: 2, exp: 'दुईवटा निश्चित अन्तिम बिन्दुहरू भएको रेखाको परिमित भाग रेखाखण्ड (Line Segment) हो।' },
      { correct: 1, exp: 'आपसमा काटिँदा ठीक ९०° को समकोण बनाउने रेखाहरू लम्ब रेखाहरू (Perpendicular lines) हुन्।' },
      { correct: 2, exp: '९०° भन्दा ठूलो र १८०° भन्दा सानो कोणलाई अधिक कोण (Obtuse Angle) भनिन्छ।' },
      { correct: 0, exp: 'पूरक कोणहरूको योगफल ९०° हुन्छ: ९०° - ४०° = ५०°।' },
      { correct: 1, exp: 'सम्पूरक कोणहरूको योगफल १८०° हुन्छ: १८०° - ७०° = ११०°।' },
      { correct: 1, exp: '३:०० बजे घडीका दुई सुई बीच ३ घण्टाको अन्तर हुन्छ: ३ × ३०° = ९०° (समकोण)।' },
      { correct: 1, exp: 'आपसमा काटिएका सीधा रेखाका विपरीत आमने-सामनेका कोणहरूलाई शीर्षाभिमुख कोण भनिन्छ।' },
      { correct: 1, exp: '६०° र १२०° को अर्धकले ठीक ९०° को कोण बनाउँछ: (६०° + १२०°) / २ = ९०°।' },
      { correct: 1, exp: 'लम्बाधर्क खिच्दा चापहरू आपसमा काटिन रेखाखण्डको आधाभन्दा बढी (more than half) अर्धव्यास लिनुपर्छ।' },
      { correct: 1, exp: 'रेखीय जोडाका कोणहरूको योगफल १८०° हुन्छ: x + ६५° = १८०° ⇒ x = १८०° - ६५° = ११५°।' }
    ];

    function checkQuizCh14(qIdx, optIdx) {
      if (ch14QuizAnswered[qIdx]) return;
      ch14QuizAnswered[qIdx] = true;

      const q = ch14QuizData[qIdx];
      const buttons = document.querySelectorAll('.ch14-opt-' + qIdx);
      const expDiv = document.getElementById('ch14-qexp-' + qIdx);
      const badge = document.getElementById('ch14-qbadge-' + qIdx);

      const isCorrect = (optIdx === q.correct);

      buttons.forEach((btn, idx) => {
        btn.classList.remove('hover:bg-blue-50');
        if (idx === q.correct) {
          btn.className += ' bg-emerald-50 border-emerald-500 text-emerald-800 font-bold';
        } else if (idx === optIdx && !isCorrect) {
          btn.className += ' bg-red-50 border-red-500 text-red-800 line-through';
        } else {
          btn.className += ' opacity-50';
        }
      });

      if (badge) {
        if (isCorrect) {
          badge.className = 'text-xs font-bold px-2 py-0.5 rounded-lg bg-emerald-100 text-emerald-800';
          badge.textContent = '✓ सही';
          ch14QuizScore++;
        } else {
          badge.className = 'text-xs font-bold px-2 py-0.5 rounded-lg bg-red-100 text-red-800';
          badge.textContent = '✗ गलत';
        }
      }

      const scoreEl = document.getElementById('ch14-quiz-score');
      if (scoreEl) scoreEl.textContent = ch14QuizScore.toString();

      if (expDiv) {
        expDiv.classList.remove('hidden');
        expDiv.innerHTML = `<strong>व्याख्या:</strong> ${q.exp}`;
      }
    }

    function resetQuizCh14() {
      ch14QuizScore = 0;
      for (const k in ch14QuizAnswered) delete ch14QuizAnswered[k];

      const scoreEl = document.getElementById('ch14-quiz-score');
      if (scoreEl) scoreEl.textContent = '0';

      for (let i = 0; i < ch14QuizData.length; i++) {
        const buttons = document.querySelectorAll('.ch14-opt-' + i);
        buttons.forEach(btn => {
          btn.className = 'ch14-opt-' + i + ' p-3 rounded-xl border border-slate-200 hover:bg-blue-50 text-left transition font-medium cursor-pointer';
        });
        const badge = document.getElementById('ch14-qbadge-' + i);
        if (badge) {
          badge.className = 'text-xs font-bold px-2 py-0.5 rounded-lg bg-slate-100 text-slate-600';
          badge.textContent = 'अपेक्षित';
        }
        const expDiv = document.getElementById('ch14-qexp-' + i);
        if (expDiv) {
          expDiv.classList.add('hidden');
          expDiv.innerHTML = '';
        }
      }
    }

    window.setTabCh14 = setTabCh14;
    window.setExerciseCh14 = setExerciseCh14;
    window.setCh14LabMode = setCh14LabMode;
    window.setCh14Angle = setCh14Angle;
    window.prevCh14Step = prevCh14Step;
    window.nextCh14Step = nextCh14Step;
    window.resetCh14Construct = resetCh14Construct;
    window.runCh14Lab = runCh14Lab;
    window.checkQuizCh14 = checkQuizCh14;
    window.resetQuizCh14 = resetQuizCh14;




// ==================== CHAPTER 15 INTERACTIVE ENGINE ====================

// --- Tab Switcher ---
function setTabCh15(tab) {
  const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
  tabs.forEach(t => {
    const btn = document.getElementById('ch15-tab-' + t);
    const view = document.getElementById('ch15-view-' + t);
    if (btn && view) {
      if (t === tab) {
        btn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
        view.classList.remove('hidden');
      } else {
        btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
        view.classList.add('hidden');
      }
    }
  });

  if (tab === 'quiz') {
    renderCh15Quiz();
  }

  // Render MathJax / KaTeX if available
  try {
    if (window.renderMathInElement) {
      renderMathInElement(document.getElementById('chapter-view-15'), {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false }
        ],
        throwOnError: false
      });
    }
  } catch (e) {}
}

// --- Lab Mode Switcher ---
function switchCh15Lab(mode) {
  const triLab = document.getElementById('ch15-sublab-triangle');
  const quadLab = document.getElementById('ch15-sublab-quad');
  const btnTri = document.getElementById('btn-lab-triangle');
  const btnQuad = document.getElementById('btn-lab-quad');

  if (mode === 'triangle') {
    if (triLab) triLab.classList.remove('hidden');
    if (quadLab) quadLab.classList.add('hidden');
    if (btnTri) btnTri.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-blue-600 text-white shadow-sm transition cursor-pointer';
    if (btnQuad) btnQuad.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold text-slate-300 hover:text-white hover:bg-slate-700 transition cursor-pointer';
  } else {
    if (triLab) triLab.classList.add('hidden');
    if (quadLab) quadLab.classList.remove('hidden');
    if (btnQuad) btnQuad.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-purple-600 text-white shadow-sm transition cursor-pointer';
    if (btnTri) btnTri.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold text-slate-300 hover:text-white hover:bg-slate-700 transition cursor-pointer';
  }
}

// --- DYNAMIC TRIANGLE LAB ---
const triState = {
  Ax: 200,
  Ay: 60,
  Bx: 80,
  By: 240,
  Cx: 320,
  Cy: 240
};

function updateTriangleLab() {
  const poly = document.getElementById('tri-polygon');
  const nodeA = document.getElementById('node-A');
  const textA = document.getElementById('text-A');
  const labelA = document.getElementById('label-side-a');
  const labelB = document.getElementById('label-side-b');
  const labelC = document.getElementById('label-side-c');

  if (!poly || !nodeA) return;

  const Ax = triState.Ax;
  const Ay = triState.Ay;
  const Bx = triState.Bx;
  const By = triState.By;
  const Cx = triState.Cx;
  const Cy = triState.Cy;

  // Update polygon & node
  poly.setAttribute('points', `${Ax},${Ay} ${Bx},${By} ${Cx},${Cy}`);
  nodeA.setAttribute('cx', Ax);
  nodeA.setAttribute('cy', Ay);
  textA.setAttribute('x', Ax);
  textA.setAttribute('y', Ay - 12);

  // Side lengths (Euclidean distance, scaled: 10px = 1 cm)
  const a = Math.hypot(Cx - Bx, Cy - By) / 10;
  const b = Math.hypot(Ax - Cx, Ay - Cy) / 10;
  const c = Math.hypot(Ax - Bx, Ay - By) / 10;

  // Labels position at midpoints
  if (labelC) {
    labelC.setAttribute('x', (Ax + Bx) / 2 - 15);
    labelC.setAttribute('y', (Ay + By) / 2);
    labelC.textContent = `c=${c.toFixed(1)}`;
  }
  if (labelB) {
    labelB.setAttribute('x', (Ax + Cx) / 2 + 15);
    labelB.setAttribute('y', (Ay + Cy) / 2);
    labelB.textContent = `b=${b.toFixed(1)}`;
  }
  if (labelA) {
    labelA.setAttribute('x', (Bx + Cx) / 2);
    labelA.setAttribute('y', By + 22);
    labelA.textContent = `a=${a.toFixed(1)}`;
  }

  // Calculate angles via Law of Cosines
  // cos A = (b^2 + c^2 - a^2) / (2bc)
  function getAngleDeg(opp, adj1, adj2) {
    const cosVal = Math.max(-1, Math.min(1, (adj1 * adj1 + adj2 * adj2 - opp * opp) / (2 * adj1 * adj2)));
    return (Math.acos(cosVal) * 180) / Math.PI;
  }

  const angA = getAngleDeg(a, b, c);
  const angB = getAngleDeg(b, a, c);
  const angC = Math.max(0, 180 - (angA + angB));

  // Display angles in UI
  const elA = document.getElementById('val-ang-A');
  const elB = document.getElementById('val-ang-B');
  const elC = document.getElementById('val-ang-C');
  const elSum = document.getElementById('val-ang-sum');
  if (elA) elA.textContent = `${Math.round(angA)}°`;
  if (elB) elB.textContent = `${Math.round(angB)}°`;
  if (elC) elC.textContent = `${Math.round(angC)}°`;
  if (elSum) elSum.textContent = `180°`;

  // Draw angle arcs
  drawAngleArc('arc-A', Ax, Ay, Bx, By, Cx, Cy, 25);
  drawAngleArc('arc-B', Bx, By, Cx, Cy, Ax, Ay, 25);
  drawAngleArc('arc-C', Cx, Cy, Ax, Ay, Bx, By, 25);

  // Statistics & Classification
  const elStatA = document.getElementById('stat-side-a');
  const elStatB = document.getElementById('stat-side-b');
  const elStatC = document.getElementById('stat-side-c');
  const elSideType = document.getElementById('stat-side-type');
  const elAngType = document.getElementById('stat-angle-type');
  const elBadge = document.getElementById('tri-type-badge');

  if (elStatA) elStatA.textContent = `${a.toFixed(1)} cm`;
  if (elStatB) elStatB.textContent = `${b.toFixed(1)} cm`;
  if (elStatC) elStatC.textContent = `${c.toFixed(1)} cm`;

  // Side classification
  let sideType = 'विषमबाहु (Scalene)';
  const diffAB = Math.abs(c - b);
  const diffBC = Math.abs(a - b);
  const diffCA = Math.abs(a - c);
  if (diffAB < 0.6 && diffBC < 0.6 && diffCA < 0.6) {
    sideType = 'समबाहु (Equilateral)';
  } else if (diffAB < 0.6 || diffBC < 0.6 || diffCA < 0.6) {
    sideType = 'समद्विबाहु (Isosceles)';
  }
  if (elSideType) elSideType.textContent = sideType;

  // Angle classification
  let angType = 'न्यूनकोणी त्रिभुज (Acute)';
  const maxAng = Math.max(angA, angB, angC);
  if (Math.abs(maxAng - 90) <= 2) {
    angType = 'समकोणी त्रिभुज (Right-angled)';
  } else if (maxAng > 92) {
    angType = 'अधिककोणी त्रिभुज (Obtuse-angled)';
  }
  if (elAngType) elAngType.textContent = angType;
  if (elBadge) elBadge.textContent = `${sideType} | ${angType}`;
}

function drawAngleArc(arcId, vx, vy, p1x, p1y, p2x, p2y, r) {
  const arc = document.getElementById(arcId);
  if (!arc) return;
  const a1 = Math.atan2(p1y - vy, p1x - vx);
  const a2 = Math.atan2(p2y - vy, p2x - vx);
  let start = a1;
  let end = a2;
  let diff = end - start;
  while (diff < 0) diff += 2 * Math.PI;
  while (diff > 2 * Math.PI) diff -= 2 * Math.PI;
  if (diff > Math.PI) {
    start = a2;
    end = a1;
    diff = 2 * Math.PI - diff;
  }
  const x1 = vx + r * Math.cos(start);
  const y1 = vy + r * Math.sin(start);
  const x2 = vx + r * Math.cos(end);
  const y2 = vy + r * Math.sin(end);
  const largeArc = diff > Math.PI ? 1 : 0;
  arc.setAttribute('d', `M ${vx} ${vy} L ${x1} ${y1} A ${r} ${r} 0 ${largeArc} 1 ${x2} ${y2} Z`);
}

function onTriSliderChange() {
  const sx = document.getElementById('slider-tri-x');
  const sy = document.getElementById('slider-tri-y');
  const lx = document.getElementById('slider-x-val');
  const ly = document.getElementById('slider-y-val');
  if (sx && sy) {
    triState.Ax = parseInt(sx.value);
    triState.Ay = parseInt(sy.value);
    if (lx) lx.textContent = `${triState.Ax} px`;
    if (ly) ly.textContent = `${triState.Ay} px`;
    updateTriangleLab();
  }
}

function setTriPreset(preset) {
  const sx = document.getElementById('slider-tri-x');
  const sy = document.getElementById('slider-tri-y');
  const lx = document.getElementById('slider-x-val');
  const ly = document.getElementById('slider-y-val');

  if (preset === 'equilateral') {
    // Equilateral: base 240, height = 240 * sqrt(3)/2 = 207.8 -> y = 240 - 208 = 32
    triState.Ax = 200;
    triState.Ay = 32;
  } else if (preset === 'isosceles') {
    triState.Ax = 200;
    triState.Ay = 90;
  } else if (preset === 'right') {
    triState.Ax = 80;
    triState.Ay = 60;
  } else if (preset === 'obtuse') {
    triState.Ax = 280;
    triState.Ay = 175;
  } else if (preset === 'acute_scalene') {
    triState.Ax = 160;
    triState.Ay = 60;
  }

  if (sx) sx.value = triState.Ax;
  if (sy) sy.value = triState.Ay;
  if (lx) lx.textContent = `${triState.Ax} px`;
  if (ly) ly.textContent = `${triState.Ay} px`;
  updateTriangleLab();
}

// --- DYNAMIC QUADRILATERAL LAB ---
const quadConfigs = {
  rectangle: {
    title: 'आयतका प्रमाणित ज्यामितीय गुणहरू',
    badge: 'आयत (Rectangle)',
    points: '80,80 320,80 320,220 80,220',
    diag1: { x1: 80, y1: 80, x2: 320, y2: 220 },
    diag2: { x1: 320, y1: 80, x2: 80, y2: 220 },
    nodes: [
      { id: 'qnode-A', cx: 80, cy: 80 },
      { id: 'qnode-B', cx: 320, cy: 80 },
      { id: 'qnode-C', cx: 320, cy: 220 },
      { id: 'qnode-D', cx: 80, cy: 220 }
    ],
    labels: [
      { id: 'qtext-A', x: 65, y: 75 },
      { id: 'qtext-B', x: 335, y: 75 },
      { id: 'qtext-C', x: 335, y: 240 },
      { id: 'qtext-D', x: 65, y: 240 },
      { id: 'qlabel-AB', x: 200, y: 70, text: 'AB = 6 cm' },
      { id: 'qlabel-CD', x: 200, y: 240, text: 'CD = 6 cm' },
      { id: 'qlabel-AD', x: 50, y: 155, text: 'AD = 3.5 cm' },
      { id: 'qlabel-BC', x: 350, y: 155, text: 'BC = 3.5 cm' }
    ],
    angles: { A: '90°', B: '90°', C: '90°', D: '90°', sum: '360°' },
    squaresVisible: true,
    sqPaths: {
      A: 'M 80 100 L 100 100 L 100 80',
      B: 'M 300 80 L 300 100 L 320 100',
      C: 'M 320 200 L 300 200 L 300 220',
      D: 'M 100 220 L 100 200 L 80 200'
    },
    props: [
      '✓ सम्मुख भुजाहरू बराबर र समानान्तर (AB = CD, AD = BC)',
      '✓ चारवटै कोणहरू ९०° (समकोण) छन्',
      '✓ दुवै विकर्णहरू (AC = BD) लम्बाइमा बराबर छन्',
      '✓ विकर्णहरू परस्पर समद्विभाजित हुन्छन्'
    ]
  },
  square: {
    title: 'वर्गका प्रमाणित ज्यामितीय गुणहरू',
    badge: 'वर्ग (Square)',
    points: '120,70 280,70 280,230 120,230',
    diag1: { x1: 120, y1: 70, x2: 280, y2: 230 },
    diag2: { x1: 280, y1: 70, x2: 120, y2: 230 },
    nodes: [
      { id: 'qnode-A', cx: 120, cy: 70 },
      { id: 'qnode-B', cx: 280, cy: 70 },
      { id: 'qnode-C', cx: 280, cy: 230 },
      { id: 'qnode-D', cx: 120, cy: 230 }
    ],
    labels: [
      { id: 'qtext-A', x: 105, y: 65 },
      { id: 'qtext-B', x: 295, y: 65 },
      { id: 'qtext-C', x: 295, y: 245 },
      { id: 'qtext-D', x: 105, y: 245 },
      { id: 'qlabel-AB', x: 200, y: 60, text: 'AB = 4 cm' },
      { id: 'qlabel-CD', x: 200, y: 250, text: 'CD = 4 cm' },
      { id: 'qlabel-AD', x: 90, y: 155, text: 'AD = 4 cm' },
      { id: 'qlabel-BC', x: 310, y: 155, text: 'BC = 4 cm' }
    ],
    angles: { A: '90°', B: '90°', C: '90°', D: '90°', sum: '360°' },
    squaresVisible: true,
    sqPaths: {
      A: 'M 120 90 L 140 90 L 140 70',
      B: 'M 260 70 L 260 90 L 280 90',
      C: 'M 280 210 L 260 210 L 260 230',
      D: 'M 140 230 L 140 210 L 120 210'
    },
    props: [
      '✓ चारवटै भुजाहरू समान लम्बाइका छन् (AB = BC = CD = DA)',
      '✓ चारवटै कोणहरू ठीक ९०° का समकोण छन्',
      '✓ दुवै विकर्णहरू बराबर छन् (AC = BD)',
      '✓ विकर्णहरू परस्पर ९०° मा समद्विभाजित हुन्छन्'
    ]
  },
  parallelogram: {
    title: 'समानान्तर चतुर्भुजका प्रमाणित गुणहरू',
    badge: 'समानान्तर चतुर्भुज (Parallelogram)',
    points: '120,80 340,80 280,220 60,220',
    diag1: { x1: 120, y1: 80, x2: 280, y2: 220 },
    diag2: { x1: 340, y1: 80, x2: 60, y2: 220 },
    nodes: [
      { id: 'qnode-A', cx: 120, cy: 80 },
      { id: 'qnode-B', cx: 340, cy: 80 },
      { id: 'qnode-C', cx: 280, cy: 220 },
      { id: 'qnode-D', cx: 60, cy: 220 }
    ],
    labels: [
      { id: 'qtext-A', x: 110, y: 70 },
      { id: 'qtext-B', x: 355, y: 80 },
      { id: 'qtext-C', x: 295, y: 235 },
      { id: 'qtext-D', x: 45, y: 230 },
      { id: 'qlabel-AB', x: 230, y: 70, text: 'AB = 6 cm' },
      { id: 'qlabel-CD', x: 170, y: 240, text: 'CD = 6 cm' },
      { id: 'qlabel-AD', x: 70, y: 145, text: 'AD = 4 cm' },
      { id: 'qlabel-BC', x: 330, y: 155, text: 'BC = 4 cm' }
    ],
    angles: { A: '115°', B: '65°', C: '115°', D: '65°', sum: '360°' },
    squaresVisible: false,
    sqPaths: {},
    props: [
      '✓ सम्मुख भुजाहरू समानान्तर र बराबर छन् (AB ∥ CD, AD ∥ BC)',
      '✓ सम्मुख कोणहरू बराबर छन् (∠A = ∠C = 115°, ∠B = ∠D = 65°)',
      '✓ क्रमागत भित्री कोणहरूको योग १८०° हुन्छ (115° + 65° = 180°)',
      '✓ विकर्णहरूले एक-अर्कालाई समद्विभाजित गर्दछन्'
    ]
  },
  rhombus: {
    title: 'समबाहु चतुर्भुजका प्रमाणित गुणहरू',
    badge: 'समबाहु चतुर्भुज (Rhombus)',
    points: '200,60 310,150 200,240 90,150',
    diag1: { x1: 200, y1: 60, x2: 200, y2: 240 },
    diag2: { x1: 90, y1: 150, x2: 310, y2: 150 },
    nodes: [
      { id: 'qnode-A', cx: 200, cy: 60 },
      { id: 'qnode-B', cx: 310, cy: 150 },
      { id: 'qnode-C', cx: 200, cy: 240 },
      { id: 'qnode-D', cx: 90, cy: 150 }
    ],
    labels: [
      { id: 'qtext-A', x: 200, y: 48 },
      { id: 'qtext-B', x: 325, y: 155 },
      { id: 'qtext-C', x: 200, y: 258 },
      { id: 'qtext-D', x: 75, y: 155 },
      { id: 'qlabel-AB', x: 265, y: 100, text: 'AB = 4.5 cm' },
      { id: 'qlabel-CD', x: 135, y: 200, text: 'CD = 4.5 cm' },
      { id: 'qlabel-AD', x: 135, y: 100, text: 'AD = 4.5 cm' },
      { id: 'qlabel-BC', x: 265, y: 200, text: 'BC = 4.5 cm' }
    ],
    angles: { A: '78°', B: '102°', C: '78°', D: '102°', sum: '360°' },
    squaresVisible: false,
    sqPaths: {},
    props: [
      '✓ चारवटै भुजाहरू समान लम्बाइका छन् (AB = BC = CD = DA)',
      '✓ सम्मुख भुजाहरू समानान्तर छन् (AB ∥ CD, AD ∥ BC)',
      '✓ सम्मुख कोणहरू बराबर छन् (∠A = ∠C, ∠B = ∠D)',
      '✓ विकर्णहरू परस्पर ९०° मा लम्ब भई समद्विभाजित हुन्छन्'
    ]
  },
  trapezium: {
    title: 'समलम्ब चतुर्भुजका प्रमाणित गुणहरू',
    badge: 'समलम्ब चतुर्भुज (Trapezium)',
    points: '120,80 280,80 340,220 60,220',
    diag1: { x1: 120, y1: 80, x2: 340, y2: 220 },
    diag2: { x1: 280, y1: 80, x2: 60, y2: 220 },
    nodes: [
      { id: 'qnode-A', cx: 120, cy: 80 },
      { id: 'qnode-B', cx: 280, cy: 80 },
      { id: 'qnode-C', cx: 340, cy: 220 },
      { id: 'qnode-D', cx: 60, cy: 220 }
    ],
    labels: [
      { id: 'qtext-A', x: 110, y: 70 },
      { id: 'qtext-B', x: 290, y: 70 },
      { id: 'qtext-C', x: 355, y: 235 },
      { id: 'qtext-D', x: 45, y: 235 },
      { id: 'qlabel-AB', x: 200, y: 70, text: 'AB = 4 cm (∥)' },
      { id: 'qlabel-CD', x: 200, y: 240, text: 'DC = 7 cm (∥)' },
      { id: 'qlabel-AD', x: 75, y: 150, text: 'AD = 4.2 cm' },
      { id: 'qlabel-BC', x: 325, y: 150, text: 'BC = 4.2 cm' }
    ],
    angles: { A: '113°', B: '113°', C: '67°', D: '67°', sum: '360°' },
    squaresVisible: false,
    sqPaths: {},
    props: [
      '✓ केवल एक जोडा सम्मुख भुजाहरू मात्र समानान्तर छन् (AB ∥ DC)',
      '✓ असमानान्तर भुजाहरू (AD र BC) बराबर भए समद्विबाहु समलम्ब हुन्छ',
      '✓ समानान्तर भुजाबीचको लम्ब दूरी सधैँ स्थिर रहन्छ',
      '✓ चारवटै कोणहरूको कुल योग सधैँ ३६०° हुन्छ'
    ]
  }
};

function setQuadType(type) {
  const conf = quadConfigs[type];
  if (!conf) return;

  const poly = document.getElementById('quad-polygon');
  const d1 = document.getElementById('quad-diag-1');
  const d2 = document.getElementById('quad-diag-2');
  const title = document.getElementById('quad-prop-title');
  const badge = document.getElementById('quad-type-badge');
  const propList = document.getElementById('quad-prop-list');

  if (poly) poly.setAttribute('points', conf.points);
  if (d1) {
    d1.setAttribute('x1', conf.diag1.x1);
    d1.setAttribute('y1', conf.diag1.y1);
    d1.setAttribute('x2', conf.diag1.x2);
    d1.setAttribute('y2', conf.diag1.y2);
  }
  if (d2) {
    d2.setAttribute('x1', conf.diag2.x1);
    d2.setAttribute('y1', conf.diag2.y1);
    d2.setAttribute('x2', conf.diag2.x2);
    d2.setAttribute('y2', conf.diag2.y2);
  }

  conf.nodes.forEach(n => {
    const el = document.getElementById(n.id);
    if (el) {
      el.setAttribute('cx', n.cx);
      el.setAttribute('cy', n.cy);
    }
  });

  conf.labels.forEach(l => {
    const el = document.getElementById(l.id);
    if (el) {
      el.setAttribute('x', l.x);
      el.setAttribute('y', l.y);
      if (l.text) el.textContent = l.text;
    }
  });

  // Angles readout
  const qA = document.getElementById('qval-ang-A');
  const qB = document.getElementById('qval-ang-B');
  const qC = document.getElementById('qval-ang-C');
  const qD = document.getElementById('qval-ang-D');
  const qSum = document.getElementById('qval-ang-sum');
  if (qA) qA.textContent = conf.angles.A;
  if (qB) qB.textContent = conf.angles.B;
  if (qC) qC.textContent = conf.angles.C;
  if (qD) qD.textContent = conf.angles.D;
  if (qSum) qSum.textContent = conf.angles.sum;

  // Right angle markers
  const sqA = document.getElementById('quad-sq-A');
  const sqB = document.getElementById('quad-sq-B');
  const sqC = document.getElementById('quad-sq-C');
  const sqD = document.getElementById('quad-sq-D');
  if (conf.squaresVisible) {
    if (sqA) { sqA.style.display = 'block'; sqA.setAttribute('d', conf.sqPaths.A); }
    if (sqB) { sqB.style.display = 'block'; sqB.setAttribute('d', conf.sqPaths.B); }
    if (sqC) { sqC.style.display = 'block'; sqC.setAttribute('d', conf.sqPaths.C); }
    if (sqD) { sqD.style.display = 'block'; sqD.setAttribute('d', conf.sqPaths.D); }
  } else {
    if (sqA) sqA.style.display = 'none';
    if (sqB) sqB.style.display = 'none';
    if (sqC) sqC.style.display = 'none';
    if (sqD) sqD.style.display = 'none';
  }

  if (title) title.textContent = conf.title;
  if (badge) badge.textContent = conf.badge;

  if (propList) {
    propList.innerHTML = conf.props
      .map(p => `<div class="flex items-center gap-2 text-emerald-400">${p}</div>`)
      .join('');
  }
}

// --- CHAPTER 15 QUIZ ENGINE ---
const ch15QuizData = [
  {
    q: '१. समबाहु त्रिभुज (Equilateral Triangle) का प्रत्येक कोणको नाप कति हुन्छ ?',
    opts: ['४५°', '६०°', '९०°', '१२०°'],
    ans: 1,
    exp: 'समबाहु त्रिभुजका तीनवटै भुजाहरू र तीनवटै कोणहरू बराबर हुन्छन्: १८०° ÷ ३ = ६०° ।'
  },
  {
    q: '२. त्रिभुजका तीनवटै भित्री कोणहरूको योगफल सधैँ कति डिग्री हुन्छ ?',
    opts: ['९०°', '१८०°', '२७०°', '३६०°'],
    ans: 1,
    exp: 'ज्यामितिको आधारभूत साध्य अनुसार जुनसुकै त्रिभुजका तीन भित्री कोणको योग १८०° (२ समकोण) हुन्छ ।'
  },
  {
    q: '३. कुनै एउटा कोण ९०° भन्दा ठूलो भएको त्रिभुजलाई के भनिन्छ ?',
    opts: ['न्यूनकोणी', 'समकोणी', 'अधिककोणी', 'समबाहु'],
    ans: 2,
    exp: 'एउटा कोण ९०° भन्दा बढी (अधिककोण) भएको त्रिभुज अधिककोणी त्रिभुज हो ।'
  },
  {
    q: '४. कुनै दुईवटा भुजाहरू मात्र बराबर भएको त्रिभुज कुन हो ?',
    opts: ['समबाहु', 'समद्विबाहु', 'विषमबाहु', 'अधिककोणी'],
    ans: 1,
    exp: 'दुई भुजा बराबर भएको त्रिभुजलाई समद्विबाहु त्रिभुज (Isosceles Triangle) भनिन्छ ।'
  },
  {
    q: '५. चतुर्भुजका चारवटै भित्री कोणहरूको योगफल कति डिग्री हुन्छ ?',
    opts: ['१८०°', '२७०°', '३६०°', '५४०°'],
    ans: 2,
    exp: 'चतुर्भुजमा २ वटा त्रिभुज बन्ने भएकाले कुल कोण योगफल १८०° × २ = ३६०° हुन्छ ।'
  },
  {
    q: '६. चारवटै भुजा बराबर र चारवटै कोण ९०° भएको चतुर्भुजलाई के भनिन्छ ?',
    opts: ['आयत', 'समानान्तर चतुर्भुज', 'वर्ग', 'समलम्ब चतुर्भुज'],
    ans: 2,
    exp: 'चारै भुजा बराबर र चारै कोण ९०° भएको चतुर्भुज वर्ग (Square) हो ।'
  },
  {
    q: '७. केवल एक जोडा सम्मुख भुजाहरू मात्र समानान्तर भएको चतुर्भुज कुन हो ?',
    opts: ['समलम्ब चतुर्भुज (Trapezium)', 'आयत', 'समबाहु चतुर्भुज', 'समानान्तर चतुर्भुज'],
    ans: 0,
    exp: 'जुन चतुर्भुजका केवल १ जोडा सम्मुख भुजाहरू समानान्तर हुन्छन्, त्यसलाई समलम्ब चतुर्भुज भनिन्छ ।'
  },
  {
    q: '८. एउटा समद्विबाहु त्रिभुजको शीर्षकोण ४०° छ भने त्यसका समान आधारकोणहरू कति-कति हुन्छन् ?',
    opts: ['४०° र ४०°', '५०° र ५०°', '७०° र ७०°', '८०° र ८०°'],
    ans: 2,
    exp: '१८०° - ४०° = १४०° । दुई आधारकोण बराबर हुने भएकाले १४०° ÷ २ = ७०° र ७०° हुन्छ ।'
  },
  {
    q: '९. त्रिभुजको बाहिरी कोण ११०° र एउटा अनासन्न भित्री कोण ५०° छ भने अर्को भित्री कोण कति हुन्छ ?',
    opts: ['५०°', '६०°', '७०°', '११०°'],
    ans: 1,
    exp: 'बाहिरी कोण साध्य अनुसार: ११०° - ५०° = ६०° ।'
  },
  {
    q: '१०. समानान्तर चतुर्भुजको एउटा कोण ८०° छ भने त्यसको सम्मुख कोणको नाप कति हुन्छ ?',
    opts: ['८०°', '१००°', '९०°', '१६०°'],
    ans: 0,
    exp: 'समानान्तर चतुर्भुजका सम्मुख कोणहरू सधैँ लम्बाइ र नापमा बराबर हुन्छन्: सम्मुख कोण = ८०° ।'
  }
];

let ch15QuizAnswers = {};

function renderCh15Quiz() {
  const container = document.getElementById('ch15-quiz-container');
  if (!container) return;

  container.innerHTML = ch15QuizData
    .map((item, qIdx) => {
      const isAnswered = ch15QuizAnswers.hasOwnProperty(qIdx);
      const selected = ch15QuizAnswers[qIdx];
      const isCorrect = isAnswered && selected === item.ans;

      const optsHtml = item.opts
        .map((opt, optIdx) => {
          let btnClass = 'p-3 rounded-xl border text-xs md:text-sm text-left transition font-semibold ';
          if (!isAnswered) {
            btnClass += 'bg-slate-50 hover:bg-blue-50 border-slate-200 text-slate-700 cursor-pointer';
          } else {
            if (optIdx === item.ans) {
              btnClass += 'bg-emerald-100 border-emerald-500 text-emerald-900 font-bold';
            } else if (optIdx === selected) {
              btnClass += 'bg-rose-100 border-rose-500 text-rose-900 font-bold';
            } else {
              btnClass += 'bg-slate-50 border-slate-200 text-slate-400 opacity-60';
            }
          }

          return `
            <button onclick="handleCh15QuizAnswer(${qIdx}, ${optIdx})" class="${btnClass}">
              ${opt}
            </button>
          `;
        })
        .join('');

      let feedbackHtml = '';
      if (isAnswered) {
        feedbackHtml = `
          <div class="mt-2.5 p-3 rounded-xl text-xs ${isCorrect ? 'bg-emerald-50 border border-emerald-200 text-emerald-900' : 'bg-rose-50 border border-rose-200 text-rose-900'}">
            <span class="font-bold">${isCorrect ? '✓ सही उत्तर!' : '✗ गलत उत्तर!'}</span> ${item.exp}
          </div>
        `;
      }

      return `
        <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
          <div class="font-bold text-slate-800 text-sm md:text-base">${item.q}</div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
            ${optsHtml}
          </div>
          ${feedbackHtml}
        </div>
      `;
    })
    .join('');

  updateCh15QuizScore();
}

function handleCh15QuizAnswer(qIdx, optIdx) {
  if (ch15QuizAnswers.hasOwnProperty(qIdx)) return;
  ch15QuizAnswers[qIdx] = optIdx;
  renderCh15Quiz();
}

function updateCh15QuizScore() {
  let score = 0;
  Object.keys(ch15QuizAnswers).forEach(qIdx => {
    if (ch15QuizAnswers[qIdx] === ch15QuizData[qIdx].ans) {
      score++;
    }
  });
  const el = document.getElementById('ch15-quiz-score');
  if (el) el.textContent = score;
}

function resetCh15Quiz() {
  ch15QuizAnswers = {};
  renderCh15Quiz();
}

// Initialize when view loads
document.addEventListener('DOMContentLoaded', () => {
  updateTriangleLab();
  setQuadType('rectangle');
});


    // Expose Chapter 15 globals
    window.setTabCh15 = setTabCh15;
    window.switchCh15Lab = switchCh15Lab;
    window.setTriPreset = setTriPreset;
    window.onTriSliderChange = onTriSliderChange;
    window.setQuadType = setQuadType;
    window.handleCh15QuizAnswer = handleCh15QuizAnswer;
    window.resetCh15Quiz = resetCh15Quiz;
    window.updateTriangleLab = updateTriangleLab;


// ==================== CHAPTER 16 INTERACTIVE ENGINE ====================

// --- Tab Switcher ---
function setTabCh16(tab) {
  const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
  tabs.forEach(t => {
    const btn = document.getElementById('ch16-tab-' + t);
    const view = document.getElementById('ch16-view-' + t);
    if (btn && view) {
      if (t === tab) {
        btn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
        view.classList.remove('hidden');
      } else {
        btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
        view.classList.add('hidden');
      }
    }
  });

  if (tab === 'quiz') {
    renderCh16Quiz();
  }

  // Render MathJax / KaTeX if available
  try {
    if (window.renderMathInElement) {
      renderMathInElement(document.getElementById('chapter-view-16'), {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false }
        ],
        throwOnError: false
      });
    }
  } catch (e) {}
}

// --- Lab Mode Switcher ---
function switchCh16Lab(mode) {
  const circLab = document.getElementById('ch16-sublab-circle');
  const wheelLab = document.getElementById('ch16-sublab-wheel');
  const btnCirc = document.getElementById('btn-lab-circle');
  const btnWheel = document.getElementById('btn-lab-wheel');

  if (mode === 'circle') {
    if (circLab) circLab.classList.remove('hidden');
    if (wheelLab) wheelLab.classList.add('hidden');
    if (btnCirc) btnCirc.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-blue-600 text-white shadow-sm transition cursor-pointer';
    if (btnWheel) btnWheel.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold text-slate-300 hover:text-white hover:bg-slate-700 transition cursor-pointer';
  } else {
    if (circLab) circLab.classList.add('hidden');
    if (wheelLab) wheelLab.classList.remove('hidden');
    if (btnWheel) btnWheel.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-cyan-600 text-white shadow-sm transition cursor-pointer';
    if (btnCirc) btnCirc.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold text-slate-300 hover:text-white hover:bg-slate-700 transition cursor-pointer';
    onWheelChange();
  }
}

// --- DYNAMIC CIRCLE LAB ---
let circleCurrentRadius = 7.0; // in cm
let circleCurrentPart = 'radius';

const circlePartDetails = {
  centre: {
    title: 'केन्द्रबिन्दु (Centre - O)',
    badge: 'केन्द्रबिन्दु (Centre)',
    desc: 'वृत्तको ठीक बीचमा रहने निश्चित स्थिर बिन्दुलाई केन्द्रबिन्दु भनिन्छ । परिधिका सबै बिन्दुहरू यसबाट सधैँ समान दूरीमा रहन्छन् ।',
    formula: 'केन्द्रबिन्दु O बाट परिधिसम्मको दूरी = अर्धव्यास (r)',
    color: '#f43f5e'
  },
  radius: {
    title: 'अर्धव्यास (Radius - r)',
    badge: 'अर्धव्यास (Radius)',
    desc: 'वृत्तको केन्द्रबिन्दु O बाट परिधिको कुनै पनि बिन्दुसम्म जोड्ने सीधा रेखाखण्डलाई अर्धव्यास भनिन्छ । यो व्यासको आधा हुन्छ ।',
    formula: 'अर्धव्यास r = d ÷ २',
    color: '#10b981'
  },
  diameter: {
    title: 'व्यास (Diameter - d)',
    badge: 'व्यास (Diameter)',
    desc: 'केन्द्रबिन्दु O भएर जाने र दुवै छेउ परिधिमा छुने सीधा रेखाखण्ड व्यास हो । यो वृत्तको सबैभन्दा लामो जीवा हो र अर्धव्यासको दोब्बर हुन्छ ।',
    formula: 'व्यास d = २ × r',
    color: '#f59e0b'
  },
  chord: {
    title: 'जीवा (Chord - EF)',
    badge: 'जीवा (Chord)',
    desc: 'वृत्तको परिधिका कुनै दुई बिन्दुहरूलाई जोड्ने सीधा रेखाखण्डलाई जीवा भनिन्छ । व्यास केन्द्रबिन्दु भएर जाने सबैभन्दा ठूलो जीवा हो ।',
    formula: 'जीवाको लम्बाइ सधैँ व्यासभन्दा सानो वा बराबर हुन्छ (Chord ≤ d)',
    color: '#ec4899'
  },
  sector: {
    title: 'क्षेत्रक (Sector - AOB)',
    badge: 'क्षेत्रक (Sector)',
    desc: 'वृत्तका दुईवटा अर्धव्यासहरू (OA र OB) र तिनीहरूबीचको परिधिको चापले घेरिएको भित्री समतलीय भागलाई क्षेत्रक भनिन्छ (पिज्जाको टुक्रा जस्तो) ।',
    formula: 'क्षेत्रक = दुई अर्धव्यास + १ चाप बीचको क्षेत्र',
    color: '#f43f5e'
  },
  semicircle: {
    title: 'अर्धवृत्त (Semi-circle)',
    badge: 'अर्धवृत्त (Semi-circle)',
    desc: 'व्यासले वृत्तलाई दुई बराबर भागमा विभाजन गर्दा बन्ने आधा वृत्तलाई अर्धवृत्त भनिन्छ । एउटा वृत्तमा २ वटा अर्धवृत्तहरू हुन्छन् ।',
    formula: 'अर्धवृत्तको कोण = १८०°, परिधिको आधा = πr',
    color: '#10b981'
  },
  arc: {
    title: 'चाप (Arc - AB)',
    badge: 'चाप (Arc)',
    desc: 'वृत्तको बाहिरी परिधिको कुनै एउटा परिमित खण्ड वा टुक्रालाई चाप भनिन्छ । सानो भागलाई लघुचाप र ठूलो भागलाई वृहत् चाप भनिन्छ ।',
    formula: 'चाप = परिधिको एक टुक्रा (भाग)',
    color: '#a855f7'
  },
  circumference: {
    title: 'परिधि (Circumference - C)',
    badge: 'परिधि (Circumference)',
    desc: 'वृत्तको वरिपरिको कुल घेरा वा वक्ररेखाको लम्बाइलाई परिधि भनिन्छ ।',
    formula: 'परिधि C = २πr = πd (जहाँ π ≈ २२/७)',
    color: '#38bdf8'
  }
};

function updateCircleLab() {
  const r = circleCurrentRadius;
  // Visual scaling: 7 cm = 120 SVG units -> scale = 120 / 7 ≈ 17.14
  const scale = 17.14;
  const svgR = Math.round(r * scale);
  const cx = 200, cy = 200;

  // Update SVG elements
  const boundary = document.getElementById('circ-boundary');
  if (boundary) boundary.setAttribute('r', svgR);

  // Measurements
  const diam = r * 2;
  const circum = 2 * (22 / 7) * r;
  const area = (22 / 7) * r * r;

  // Live values in UI
  const elR = document.getElementById('live-r-val');
  const elD = document.getElementById('live-d-val');
  const elC = document.getElementById('live-c-val');
  const elA = document.getElementById('live-a-val');
  const sliderLabel = document.getElementById('slider-r-label');
  const measLabel = document.getElementById('circ-meas-label');

  if (elR) elR.textContent = `${r.toFixed(1)} cm`;
  if (elD) elD.textContent = `${diam.toFixed(1)} cm`;
  if (elC) elC.textContent = `${circum.toFixed(1)} cm`;
  if (elA) elA.textContent = `${area.toFixed(1)} cm²`;
  if (sliderLabel) sliderLabel.textContent = `${r.toFixed(1)} cm`;

  // Radius Line OA
  const radLine = document.getElementById('circ-radius-line');
  const nodeA = document.getElementById('circ-node-A');
  const textA = document.getElementById('circ-text-A');
  if (radLine) {
    radLine.setAttribute('x1', cx);
    radLine.setAttribute('y1', cy);
    radLine.setAttribute('x2', cx + svgR);
    radLine.setAttribute('y2', cy);
  }
  if (nodeA) {
    nodeA.setAttribute('cx', cx + svgR);
    nodeA.setAttribute('cy', cy);
  }
  if (textA) {
    textA.setAttribute('x', cx + svgR + 12);
    textA.setAttribute('y', cy + 5);
  }
  if (measLabel) {
    measLabel.setAttribute('x', cx + svgR / 2);
    measLabel.setAttribute('y', cy - 10);
    measLabel.textContent = `r = ${r.toFixed(1)} cm`;
  }

  // Diameter Line CD
  const diamLine = document.getElementById('circ-diam-line');
  const nodeC = document.getElementById('circ-node-C');
  const textC = document.getElementById('circ-text-C');
  const textD = document.getElementById('circ-text-D');
  if (diamLine) {
    diamLine.setAttribute('x1', cx - svgR);
    diamLine.setAttribute('y1', cy);
    diamLine.setAttribute('x2', cx + svgR);
    diamLine.setAttribute('y2', cy);
  }
  if (nodeC) {
    nodeC.setAttribute('cx', cx - svgR);
    nodeC.setAttribute('cy', cy);
  }
  if (textC) {
    textC.setAttribute('x', cx - svgR - 15);
    textC.setAttribute('y', cy + 5);
  }
  if (textD) {
    textD.setAttribute('x', cx + svgR + 12);
    textD.setAttribute('y', cy + 5);
  }

  // Radius OB (for sector, 60 deg angle)
  // angle 60 deg: x = cx + r*cos(-60) = cx + r*0.5, y = cy + r*sin(-60) = cy - r*0.866
  const obX = Math.round(cx + svgR * 0.5);
  const obY = Math.round(cy - svgR * 0.866);
  const radOB = document.getElementById('circ-radius-ob');
  const nodeB = document.getElementById('circ-node-B');
  const textB = document.getElementById('circ-text-B');
  if (radOB) {
    radOB.setAttribute('x1', cx);
    radOB.setAttribute('y1', cy);
    radOB.setAttribute('x2', obX);
    radOB.setAttribute('y2', obY);
  }
  if (nodeB) {
    nodeB.setAttribute('cx', obX);
    nodeB.setAttribute('cy', obY);
  }
  if (textB) {
    textB.setAttribute('x', obX + 10);
    textB.setAttribute('y', obY - 5);
  }

  // Sector Path (from OA to OB)
  const sector = document.getElementById('circ-sector');
  if (sector) {
    sector.setAttribute('d', `M ${cx} ${cy} L ${cx + svgR} ${cy} A ${svgR} ${svgR} 0 0 0 ${obX} ${obY} Z`);
  }

  // Arc Path (from OA to OB)
  const arcPath = document.getElementById('circ-arc-path');
  if (arcPath) {
    arcPath.setAttribute('d', `M ${cx + svgR} ${cy} A ${svgR} ${svgR} 0 0 0 ${obX} ${obY}`);
  }

  // Semicircle Path (from -svgR to +svgR)
  const semi = document.getElementById('circ-semicircle');
  if (semi) {
    semi.setAttribute('d', `M ${cx - svgR} ${cy} A ${svgR} ${svgR} 0 0 1 ${cx + svgR} ${cy} Z`);
  }

  // Chord EF (horizontal chord at cy + svgR*0.6)
  const chordLine = document.getElementById('circ-chord-line');
  const nodeE = document.getElementById('circ-node-E');
  const textE = document.getElementById('circ-text-E');
  const nodeF = document.getElementById('circ-node-F');
  const textF = document.getElementById('circ-text-F');
  const chordY = cy + Math.round(svgR * 0.6);
  const chordHalfW = Math.round(Math.sqrt(svgR * svgR - (chordY - cy) * (chordY - cy)));
  if (chordLine) {
    chordLine.setAttribute('x1', cx - chordHalfW);
    chordLine.setAttribute('y1', chordY);
    chordLine.setAttribute('x2', cx + chordHalfW);
    chordLine.setAttribute('y2', chordY);
  }
  if (nodeE) {
    nodeE.setAttribute('cx', cx - chordHalfW);
    nodeE.setAttribute('cy', chordY);
  }
  if (textE) {
    textE.setAttribute('x', cx - chordHalfW - 15);
    textE.setAttribute('y', chordY + 10);
  }
  if (nodeF) {
    nodeF.setAttribute('cx', cx + chordHalfW);
    nodeF.setAttribute('cy', chordY);
  }
  if (textF) {
    textF.setAttribute('x', cx + chordHalfW + 12);
    textF.setAttribute('y', chordY + 10);
  }

  // Update info card formula
  const infoFormula = document.getElementById('part-info-formula');
  if (infoFormula) {
    if (circleCurrentPart === 'radius') {
      infoFormula.textContent = `अर्धव्यास r = ${r.toFixed(1)} cm ⟹ व्यास d = ${diam.toFixed(1)} cm`;
    } else if (circleCurrentPart === 'diameter') {
      infoFormula.textContent = `व्यास d = ${diam.toFixed(1)} cm ⟹ अर्धव्यास r = ${r.toFixed(1)} cm`;
    } else if (circleCurrentPart === 'circumference') {
      infoFormula.textContent = `परिधि C = २ × (२२/७) × ${r.toFixed(1)} = ${circum.toFixed(1)} cm`;
    }
  }
}

function highlightCirclePart(part) {
  circleCurrentPart = part;
  const conf = circlePartDetails[part];
  if (!conf) return;

  // Update badge and info card
  const badge = document.getElementById('circle-part-badge');
  const title = document.getElementById('part-info-title');
  const desc = document.getElementById('part-info-desc');
  if (badge) badge.textContent = conf.badge;
  if (title) title.textContent = conf.title;
  if (desc) desc.textContent = conf.desc;

  // Update button highlights
  const parts = ['centre', 'radius', 'diameter', 'chord', 'sector', 'semicircle', 'arc', 'circumference'];
  parts.forEach(p => {
    const btn = document.getElementById('pbtn-' + p);
    if (btn) {
      if (p === part) {
        btn.className = 'p-2 rounded-xl bg-blue-600 text-white transition text-left font-semibold border border-blue-500 shadow-sm';
      } else {
        btn.className = 'p-2 rounded-xl bg-slate-800 hover:bg-slate-700 transition text-left font-semibold border border-slate-700 text-slate-300';
      }
    }
  });

  // Toggle visibility of SVG elements
  const elBoundary = document.getElementById('circ-boundary');
  const elDiam = document.getElementById('circ-diam-line');
  const elRad = document.getElementById('circ-radius-line');
  const elRadOB = document.getElementById('circ-radius-ob');
  const elChord = document.getElementById('circ-chord-line');
  const elSector = document.getElementById('circ-sector');
  const elSemi = document.getElementById('circ-semicircle');
  const elArc = document.getElementById('circ-arc-path');
  const nodeB = document.getElementById('circ-node-B');
  const textB = document.getElementById('circ-text-B');
  const nodeC = document.getElementById('circ-node-C');
  const textC = document.getElementById('circ-text-C');
  const textD = document.getElementById('circ-text-D');
  const nodeE = document.getElementById('circ-node-E');
  const textE = document.getElementById('circ-text-E');
  const nodeF = document.getElementById('circ-node-F');
  const textF = document.getElementById('circ-text-F');
  const measLabel = document.getElementById('circ-meas-label');

  // Reset styles
  if (elDiam) elDiam.style.display = 'none';
  if (elRad) elRad.style.display = 'none';
  if (elRadOB) elRadOB.style.display = 'none';
  if (elChord) elChord.style.display = 'none';
  if (elSector) elSector.style.display = 'none';
  if (elSemi) elSemi.style.display = 'none';
  if (elArc) elArc.style.display = 'none';
  if (nodeB) nodeB.style.display = 'none';
  if (textB) textB.style.display = 'none';
  if (nodeC) nodeC.style.display = 'none';
  if (textC) textC.style.display = 'none';
  if (textD) textD.style.display = 'none';
  if (nodeE) nodeE.style.display = 'none';
  if (textE) textE.style.display = 'none';
  if (nodeF) nodeF.style.display = 'none';
  if (textF) textF.style.display = 'none';

  if (part === 'centre') {
    if (elBoundary) elBoundary.setAttribute('stroke', '#38bdf8');
  } else if (part === 'radius') {
    if (elRad) elRad.style.display = 'block';
  } else if (part === 'diameter') {
    if (elDiam) elDiam.style.display = 'block';
    if (nodeC) nodeC.style.display = 'block';
    if (textC) textC.style.display = 'block';
    if (textD) textD.style.display = 'block';
  } else if (part === 'chord') {
    if (elChord) elChord.style.display = 'block';
    if (nodeE) nodeE.style.display = 'block';
    if (textE) textE.style.display = 'block';
    if (nodeF) nodeF.style.display = 'block';
    if (textF) textF.style.display = 'block';
  } else if (part === 'sector') {
    if (elSector) elSector.style.display = 'block';
    if (elRad) elRad.style.display = 'block';
    if (elRadOB) elRadOB.style.display = 'block';
    if (nodeB) nodeB.style.display = 'block';
    if (textB) textB.style.display = 'block';
  } else if (part === 'semicircle') {
    if (elSemi) elSemi.style.display = 'block';
    if (elDiam) elDiam.style.display = 'block';
  } else if (part === 'arc') {
    if (elArc) elArc.style.display = 'block';
    if (nodeB) nodeB.style.display = 'block';
    if (textB) textB.style.display = 'block';
  } else if (part === 'circumference') {
    if (elBoundary) elBoundary.setAttribute('stroke', '#ec4899');
  }

  updateCircleLab();
}

function onCircleRadiusSliderChange() {
  const slider = document.getElementById('slider-circle-r');
  if (slider) {
    circleCurrentRadius = parseFloat(slider.value);
    updateCircleLab();
  }
}

function setCircleRadiusPreset(r) {
  circleCurrentRadius = r;
  const slider = document.getElementById('slider-circle-r');
  if (slider) slider.value = r;
  updateCircleLab();
}

// --- SUB-LAB 2: WHEEL ROTATION LAB ---
function onWheelChange() {
  const sel = document.getElementById('wheel-radius-select');
  const inp = document.getElementById('wheel-rot-input');
  if (!sel || !inp) return;

  const r = parseFloat(sel.value);
  const n = Math.max(1, parseInt(inp.value) || 1);

  // Circumference
  const c = Math.round(2 * (22 / 7) * r);
  const totalDistCm = n * c;
  const totalDistM = (totalDistCm / 100).toFixed(2);

  const statC = document.getElementById('wheel-stat-c');
  const statCm = document.getElementById('wheel-stat-dist-cm');
  const statM = document.getElementById('wheel-stat-dist-m');
  const calcTotal = document.getElementById('wheel-calc-total');
  const badge = document.getElementById('wheel-rot-badge');
  const distLabel = document.getElementById('wheel-dist-label');

  if (statC) statC.textContent = `${c} cm`;
  if (statCm) statCm.textContent = `${totalDistCm} cm`;
  if (statM) statM.textContent = `${totalDistM} m`;
  if (calcTotal) calcTotal.textContent = `${totalDistCm} cm (${totalDistM} m)`;
  if (badge) badge.textContent = `${n} फन्को (${n} Rotation${n > 1 ? 's' : ''})`;
  if (distLabel) distLabel.textContent = `दूरी = ${totalDistCm} cm`;
}

function setWheelRotations(n) {
  const inp = document.getElementById('wheel-rot-input');
  if (inp) {
    inp.value = n;
    onWheelChange();
  }
}

// --- CHAPTER 16 QUIZ DATA & ENGINE ---
const ch16QuizData = [
  {
    q: '१. वृत्तको सबैभन्दा लामो जीवा कुन हो ?',
    opts: ['अर्धव्यास', 'व्यास', 'चाप', 'स्पर्शरेखा'],
    ans: 1,
    exp: 'केन्द्रबिन्दु भएर जाने जीवा नै वृत्तको सबैभन्दा लामो जीवा हो, जसलाई व्यास (Diameter) भनिन्छ ।'
  },
  {
    q: '२. एउटा वृत्तमा कतिवटा केन्द्रबिन्दु हुन्छन् ?',
    opts: ['१ वटा', '२ वटा', '४ वटा', 'अनगिन्ती'],
    ans: 0,
    exp: 'वृत्तको ठीक बीचमा एउटा मात्र निश्चित केन्द्रबिन्दु हुन्छ ।'
  },
  {
    q: '३. व्यास (d) र अर्धव्यास (r) बीचको सम्बन्ध कुन सही हो ?',
    opts: ['d = r', 'd = 2r', 'r = 2d', 'd = r ÷ 2'],
    ans: 1,
    exp: 'व्यास अर्धव्यासको ठ्याक्कै दोब्बर हुन्छ: d = 2r वा r = d/2 ।'
  },
  {
    q: '४. वृत्तका दुई अर्धव्यास र चापले घेरिएको भागलाई के भनिन्छ ?',
    opts: ['जीवा', 'वृत्तखण्ड', 'क्षेत्रक (Sector)', 'अर्धवृत्त'],
    ans: 2,
    exp: 'दुईवटा अर्धव्यासहरू र तिनीहरूबीचको चापले घेरिएको भित्री क्षेत्रलाई क्षेत्रक भनिन्छ ।'
  },
  {
    q: '५. वृत्तको वरिपरिको कुल घेरा वा वक्ररेखाको लम्बाइलाई के भनिन्छ ?',
    opts: ['व्यास', 'अर्धव्यास', 'परिधि (Circumference)', 'चाप'],
    ans: 2,
    exp: 'वृत्तको वरिपरिको घेराको लम्बाइ परिधि (Circumference) हो ।'
  },
  {
    q: '६. अर्धव्यास ७ से.मी. भएको वृत्तको परिधि कति हुन्छ ? (π = २२/७)',
    opts: ['२२ से.मी.', '४४ से.मी.', '८८ से.मी.', '१५४ से.मी.'],
    ans: 1,
    exp: 'C = 2πr = 2 × (22/7) × 7 = 44 cm हुन्छ ।'
  },
  {
    q: '७. व्यास १४ से.मी. भएको वृत्तको अर्धव्यास कति हुन्छ ?',
    opts: ['७ से.मी.', '१४ से.मी.', '२८ से.मी.', '४४ से.मी.'],
    ans: 0,
    exp: 'अर्धव्यास r = d ÷ 2 = 14 ÷ 2 = 7 cm हुन्छ ।'
  },
  {
    q: '८. वृत्तको परिधि र त्यसको व्यासको अनुपातलाई के भनिन्छ ?',
    opts: ['क्षेत्रफल', 'π (पाइ)', 'अर्धव्यास', 'जीवा'],
    ans: 1,
    exp: 'परिधि र व्यासको अनुपात स्थिर सङ्ख्या π (पाइ ≈ २२/७) हुन्छ ।'
  },
  {
    q: '९. एउटा व्यासले वृत्तलाई कतिवटा अर्धवृत्तमा विभाजन गर्दछ ?',
    opts: ['१ वटा', '२ वटा', '३ वटा', '४ वटा'],
    ans: 1,
    exp: 'व्यासले वृत्तलाई ठ्याक्कै दुई बराबर भाग (अर्धवृत्तहरू) मा विभाजन गर्दछ ।'
  },
  {
    q: '१०. साइकलको पाङ्ग्रा १ फन्को घुम्दा पार गर्ने दूरी कुन नापसँग बराबर हुन्छ ?',
    opts: ['व्यास', 'अर्धव्यास', 'पाङ्ग्राको परिधि', 'पाङ्ग्राको क्षेत्रफल'],
    ans: 2,
    exp: 'पाङ्ग्रा १ पटक पूरा घुम्दा त्यसको बाहिरी घेरा अर्थात् परिधि (2πr) बराबर दूरी पार गर्दछ ।'
  }
];

let ch16QuizAnswers = {};

function renderCh16Quiz() {
  const container = document.getElementById('ch16-quiz-container');
  if (!container) return;

  container.innerHTML = ch16QuizData
    .map((item, qIdx) => {
      const isAnswered = ch16QuizAnswers.hasOwnProperty(qIdx);
      const selected = ch16QuizAnswers[qIdx];
      const isCorrect = isAnswered && selected === item.ans;

      const optsHtml = item.opts
        .map((opt, optIdx) => {
          let btnClass = 'p-3 rounded-xl border text-xs md:text-sm text-left transition font-semibold ';
          if (!isAnswered) {
            btnClass += 'bg-slate-50 hover:bg-blue-50 border-slate-200 text-slate-700 cursor-pointer';
          } else {
            if (optIdx === item.ans) {
              btnClass += 'bg-emerald-100 border-emerald-500 text-emerald-900 font-bold';
            } else if (optIdx === selected) {
              btnClass += 'bg-rose-100 border-rose-500 text-rose-900 font-bold';
            } else {
              btnClass += 'bg-slate-50 border-slate-200 text-slate-400 opacity-60';
            }
          }

          return `
            <button onclick="handleCh16QuizAnswer(${qIdx}, ${optIdx})" class="${btnClass}">
              ${opt}
            </button>
          `;
        })
        .join('');

      let feedbackHtml = '';
      if (isAnswered) {
        feedbackHtml = `
          <div class="mt-2.5 p-3 rounded-xl text-xs ${isCorrect ? 'bg-emerald-50 border border-emerald-200 text-emerald-900' : 'bg-rose-50 border border-rose-200 text-rose-900'}">
            <span class="font-bold">${isCorrect ? '✓ सही उत्तर!' : '✗ गलत उत्तर!'}</span> ${item.exp}
          </div>
        `;
      }

      return `
        <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
          <div class="font-bold text-slate-800 text-sm md:text-base">${item.q}</div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
            ${optsHtml}
          </div>
          ${feedbackHtml}
        </div>
      `;
    })
    .join('');

  updateCh16QuizScore();
}

function handleCh16QuizAnswer(qIdx, optIdx) {
  if (ch16QuizAnswers.hasOwnProperty(qIdx)) return;
  ch16QuizAnswers[qIdx] = optIdx;
  renderCh16Quiz();
}

function updateCh16QuizScore() {
  let score = 0;
  Object.keys(ch16QuizAnswers).forEach(qIdx => {
    if (ch16QuizAnswers[qIdx] === ch16QuizData[qIdx].ans) {
      score++;
    }
  });
  const el = document.getElementById('ch16-quiz-score');
  if (el) el.textContent = score;
}

function resetCh16Quiz() {
  ch16QuizAnswers = {};
  renderCh16Quiz();
}

// Initialise Chapter 16 when DOM loads
document.addEventListener('DOMContentLoaded', () => {
  updateCircleLab();
});


    // Expose Chapter 16 globals
    window.setTabCh16 = setTabCh16;
    window.switchCh16Lab = switchCh16Lab;
    window.updateCircleLab = updateCircleLab;
    window.highlightCirclePart = highlightCirclePart;
    window.onCircleRadiusSliderChange = onCircleRadiusSliderChange;
    window.setCircleRadiusPreset = setCircleRadiusPreset;
    window.onWheelChange = onWheelChange;
    window.setWheelRotations = setWheelRotations;
    window.renderCh16Quiz = renderCh16Quiz;
    window.handleCh16QuizAnswer = handleCh16QuizAnswer;
    window.resetCh16Quiz = resetCh16Quiz;

// ==================== CHAPTER 17 INTERACTIVE ENGINE ====================

// --- Tab Switcher ---
function setTabCh17(tab) {
  const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
  tabs.forEach(t => {
    const btn = document.getElementById('ch17-tab-' + t);
    const view = document.getElementById('ch17-view-' + t);
    if (btn && view) {
      if (t === tab) {
        btn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
        view.classList.remove('hidden');
      } else {
        btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
        view.classList.add('hidden');
      }
    }
  });

  if (tab === 'quiz') {
    renderCh17Quiz();
  }

  try {
    if (window.renderMathInElement) {
      renderMathInElement(document.getElementById('chapter-view-17'), {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false }
        ],
        throwOnError: false
      });
    }
  } catch (e) {}
}

// --- Lab Mode Switcher ---
function switchCh17Lab(mode) {
  const polyLab = document.getElementById('ch17-sublab-poly');
  const curvedLab = document.getElementById('ch17-sublab-curved');
  const netLab = document.getElementById('ch17-sublab-net');
  const btnPoly = document.getElementById('btn-lab-poly');
  const btnCurved = document.getElementById('btn-lab-curved');
  const btnNet = document.getElementById('btn-lab-net');

  const activeCls = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-blue-600 text-white shadow-sm transition cursor-pointer';
  const inactiveCls = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold text-slate-300 hover:text-white hover:bg-slate-700 transition cursor-pointer';

  if (mode === 'poly') {
    if (polyLab) polyLab.classList.remove('hidden');
    if (curvedLab) curvedLab.classList.add('hidden');
    if (netLab) netLab.classList.add('hidden');
    if (btnPoly) btnPoly.className = activeCls;
    if (btnCurved) btnCurved.className = inactiveCls;
    if (btnNet) btnNet.className = inactiveCls;
    updatePolyLab();
  } else if (mode === 'curved') {
    if (polyLab) polyLab.classList.add('hidden');
    if (curvedLab) curvedLab.classList.remove('hidden');
    if (netLab) netLab.classList.add('hidden');
    if (btnCurved) btnCurved.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-cyan-600 text-white shadow-sm transition cursor-pointer';
    if (btnPoly) btnPoly.className = inactiveCls;
    if (btnNet) btnNet.className = inactiveCls;
    updateCurvedLab();
  } else if (mode === 'net') {
    if (polyLab) polyLab.classList.add('hidden');
    if (curvedLab) curvedLab.classList.add('hidden');
    if (netLab) netLab.classList.remove('hidden');
    if (btnNet) btnNet.className = 'px-4 py-2 rounded-xl text-xs md:text-sm font-bold bg-purple-600 text-white shadow-sm transition cursor-pointer';
    if (btnPoly) btnPoly.className = inactiveCls;
    if (btnCurved) btnCurved.className = inactiveCls;
    updateNetLab();
  }
}

// --- SUB-LAB 1: POLYHEDRA & EULER EXPLORER STATE ---
let currentPolyShape = 'cube';
let currentPolyHighlight = 'all';

const polyShapeData = {
  cube: {
    title: 'घन (Cube)',
    F: 6,
    V: 8,
    E: 12,
    desc: 'घनमा ६ वटा बराबर वर्गहरू, १२ वटा बराबर सिधा किनारा र ८ वटा शीर्षबिन्दु हुन्छन् । यसका तीनवटै आयामहरू बराबर हुन्छन् (l = b = h) ।'
  },
  cuboid: {
    title: 'षड्मुखा (Cuboid)',
    F: 6,
    V: 8,
    E: 12,
    desc: 'षड्मुखामा ६ वटा आयताकार सतहहरू (३ जोडी समानान्तर आयतहरू), १२ वटा किनारा र ८ वटा शीर्षबिन्दु हुन्छन् ।'
  },
  prism: {
    title: 'त्रिकोणात्मक प्रिज्मा (Triangular Prism)',
    F: 5,
    V: 6,
    E: 9,
    desc: 'प्रिज्मामा २ वटा त्रिभुजाकार आधार र ३ वटा आयताकार सतहहरू गरी जम्मा ५ सतह, ९ किनारा र ६ शीर्षबिन्दु हुन्छन् ।'
  },
  pyramid: {
    title: 'वर्गाकार पिरामिड (Square Pyramid)',
    F: 5,
    V: 5,
    E: 8,
    desc: 'पिरामिडमा १ वटा वर्गाकार आधार र ४ वटा त्रिभुजाकार छड्के सतहहरू हुन्छन् । जम्मा ५ सतह, ८ किनारा र ५ शीर्षबिन्दु हुन्छन् ।'
  },
  tetra: {
    title: 'टेट्राहेड्रन / त्रिभुजाकार पिरामिड',
    F: 4,
    V: 4,
    E: 6,
    desc: 'टेट्राहेड्रनमा ४ वटा त्रिभुजाकार सतहहरू, ६ वटा किनारा र ४ वटा शीर्षबिन्दु हुन्छन् । यो सबैभन्दा सरल बहुफलक हो ।'
  }
};

function setPolyShape(shape) {
  currentPolyShape = shape;
  ['cube', 'cuboid', 'prism', 'pyramid', 'tetra'].forEach(s => {
    const btn = document.getElementById('btn-shape-' + s);
    if (btn) {
      if (s === shape) {
        btn.className = 'px-3 py-2 rounded-xl bg-blue-600 text-white font-bold text-xs shadow-sm transition cursor-pointer';
      } else {
        btn.className = 'px-3 py-2 rounded-xl bg-slate-700 hover:bg-slate-600 text-slate-200 font-bold text-xs transition cursor-pointer';
      }
    }
  });

  updatePolyLab();
}

function setPolyHighlight(mode) {
  currentPolyHighlight = mode;
  ['all', 'faces', 'edges', 'vertices'].forEach(m => {
    const btn = document.getElementById('btn-high-' + m);
    if (btn) {
      if (m === mode) {
        btn.className = 'px-3 py-2 rounded-xl bg-indigo-600 text-white font-bold text-xs transition cursor-pointer';
      } else {
        btn.className = 'px-3 py-2 rounded-xl bg-slate-700 hover:bg-slate-600 text-slate-200 font-bold text-xs transition cursor-pointer';
      }
    }
  });

  updatePolyLab();
}

function updatePolyLab() {
  const data = polyShapeData[currentPolyShape] || polyShapeData.cube;

  // Update counters
  const fEl = document.getElementById('live-f-val');
  const vEl = document.getElementById('live-v-val');
  const eEl = document.getElementById('live-e-val');
  const eulerEl = document.getElementById('live-euler-val');
  const badgeEl = document.getElementById('poly-part-badge');
  const titleEl = document.getElementById('poly-shape-title');
  const descEl = document.getElementById('poly-desc-box');
  const calcEl = document.getElementById('poly-euler-calc');

  if (fEl) fEl.textContent = data.F;
  if (vEl) vEl.textContent = data.V;
  if (eEl) eEl.textContent = data.E;
  if (eulerEl) eulerEl.textContent = (data.F + data.V - data.E) + ' ✓';
  if (badgeEl) badgeEl.textContent = data.title;
  if (titleEl) titleEl.textContent = data.title;
  if (descEl) descEl.textContent = data.desc;
  if (calcEl) calcEl.textContent = `F + V - E = ${data.F} + ${data.V} - ${data.E} = 2`;

  // Sync inputs
  const inF = document.getElementById('calc-f-input');
  const inV = document.getElementById('calc-v-input');
  const inE = document.getElementById('calc-e-input');
  if (inF) inF.value = data.F;
  if (inV) inV.value = data.V;
  if (inE) inE.value = data.E;
  const solverRes = document.getElementById('calc-solver-result');
  if (solverRes) {
    solverRes.textContent = `E = F + V - 2 = ${data.F} + ${data.V} - 2 = ${data.E}`;
  }

  // Render 3D SVG
  renderPolySvg(currentPolyShape, currentPolyHighlight);
}

function renderPolySvg(shape, highlight) {
  const container = document.getElementById('poly-svg-shapes');
  if (!container) return;

  const showFaces = highlight === 'all' || highlight === 'faces';
  const showEdges = highlight === 'all' || highlight === 'edges';
  const showVerts = highlight === 'all' || highlight === 'vertices';

  const faceFill = showFaces ? 'rgba(99, 102, 241, 0.35)' : 'rgba(99, 102, 241, 0.12)';
  const faceStroke = showFaces ? '#818cf8' : 'rgba(129, 140, 248, 0.4)';
  const edgeColor = showEdges ? '#f59e0b' : '#38bdf8';
  const edgeWidth = showEdges ? 3.5 : 2;
  const vertFill = showVerts ? '#f43f5e' : '#3b82f6';
  const vertR = showVerts ? 6.5 : 4.5;

  let html = '';

  if (shape === 'cube' || shape === 'cuboid') {
    const isCube = shape === 'cube';
    const w = isCube ? 140 : 170;
    const h = isCube ? 140 : 110;
    const dx = 50;
    const dy = isCube ? 50 : 40;
    const ox = isCube ? 110 : 90;
    const oy = isCube ? 280 : 270;

    const A = { x: ox + dx, y: oy - h - dy, name: 'A' };
    const B = { x: ox + w + dx, y: oy - h - dy, name: 'B' };
    const C = { x: ox + w, y: oy - h, name: 'C' };
    const D = { x: ox, y: oy - h, name: 'D' };
    const E = { x: ox + dx, y: oy - dy, name: 'E' };
    const F = { x: ox + w + dx, y: oy - dy, name: 'F' };
    const G = { x: ox + w, y: oy, name: 'G' };
    const H = { x: ox, y: oy, name: 'H' };

    // Dashed back edges
    html += `
      <line x1="${E.x}" y1="${E.y}" x2="${A.x}" y2="${A.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
      <line x1="${E.x}" y1="${E.y}" x2="${F.x}" y2="${F.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
      <line x1="${H.x}" y1="${H.y}" x2="${E.x}" y2="${E.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
    `;

    // Shaded Faces
    html += `
      <!-- Top Face ABCD -->
      <polygon points="${A.x},${A.y} ${B.x},${B.y} ${C.x},${C.y} ${D.x},${D.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
      <!-- Right Face BCGF -->
      <polygon points="${B.x},${B.y} ${C.x},${C.y} ${G.x},${G.y} ${F.x},${F.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
      <!-- Front Face DCGH -->
      <polygon points="${D.x},${D.y} ${C.x},${C.y} ${G.x},${G.y} ${H.x},${H.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
    `;

    // Visible Edges
    const edges = [
      [A, B], [B, C], [C, D], [D, A],
      [B, F], [C, G], [D, H],
      [F, G], [G, H]
    ];
    edges.forEach(([p1, p2]) => {
      html += `<line x1="${p1.x}" y1="${p1.y}" x2="${p2.x}" y2="${p2.y}" stroke="${edgeColor}" stroke-width="${edgeWidth}" stroke-linecap="round" />`;
    });

    // Vertices
    const verts = [A, B, C, D, E, F, G, H];
    verts.forEach(p => {
      const isBack = p === E;
      const fill = isBack ? '#94a3b8' : vertFill;
      html += `
        <circle cx="${p.x}" cy="${p.y}" r="${vertR}" fill="${fill}" stroke="#ffffff" stroke-width="1.5" />
        <text x="${p.x + 8}" y="${p.y - 4}" fill="#f8fafc" font-size="12" font-weight="bold">${p.name}</text>
      `;
    });
  } else if (shape === 'prism') {
    // Triangular Prism
    const A = { x: 90, y: 110, name: 'A' };
    const B = { x: 190, y: 190, name: 'B' };
    const C = { x: 50, y: 220, name: 'C' };

    const D = { x: 260, y: 110, name: 'D' };
    const E = { x: 360, y: 190, name: 'E' };
    const F = { x: 220, y: 220, name: 'F' };

    // Back dashed edge
    html += `<line x1="${A.x}" y1="${A.y}" x2="${D.x}" y2="${D.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />`;

    // Faces
    html += `
      <!-- Front Triangle ABC -->
      <polygon points="${A.x},${A.y} ${B.x},${B.y} ${C.x},${C.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
      <!-- Back Triangle DEF -->
      <polygon points="${D.x},${D.y} ${E.x},${E.y} ${F.x},${F.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
      <!-- Lateral Face ABED -->
      <polygon points="${A.x},${A.y} ${B.x},${B.y} ${E.x},${E.y} ${D.x},${D.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
      <!-- Lateral Face BCFE -->
      <polygon points="${B.x},${B.y} ${C.x},${C.y} ${F.x},${F.y} ${E.x},${E.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
    `;

    // Edges
    const edges = [
      [A, B], [B, C], [C, A],
      [D, E], [E, F], [F, D],
      [B, E], [C, F]
    ];
    edges.forEach(([p1, p2]) => {
      html += `<line x1="${p1.x}" y1="${p1.y}" x2="${p2.x}" y2="${p2.y}" stroke="${edgeColor}" stroke-width="${edgeWidth}" stroke-linecap="round" />`;
    });

    // Vertices
    [A, B, C, D, E, F].forEach(p => {
      html += `
        <circle cx="${p.x}" cy="${p.y}" r="${vertR}" fill="${vertFill}" stroke="#ffffff" stroke-width="1.5" />
        <text x="${p.x + 8}" y="${p.y - 4}" fill="#f8fafc" font-size="12" font-weight="bold">${p.name}</text>
      `;
    });
  } else if (shape === 'pyramid') {
    // Square Pyramid
    const Apex = { x: 200, y: 70, name: 'V' };
    const A = { x: 120, y: 220, name: 'A' };
    const B = { x: 280, y: 220, name: 'B' };
    const C = { x: 330, y: 270, name: 'C' };
    const D = { x: 70, y: 270, name: 'D' };

    // Dashed back lines
    html += `
      <line x1="${A.x}" y1="${A.y}" x2="${Apex.x}" y2="${Apex.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
      <line x1="${A.x}" y1="${A.y}" x2="${B.x}" y2="${B.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
      <line x1="${D.x}" y1="${D.y}" x2="${A.x}" y2="${A.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
    `;

    // Faces
    html += `
      <polygon points="${Apex.x},${Apex.y} ${B.x},${B.y} ${C.x},${C.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
      <polygon points="${Apex.x},${Apex.y} ${D.x},${D.y} ${C.x},${C.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
    `;

    // Edges
    const edges = [
      [Apex, B], [Apex, C], [Apex, D],
      [B, C], [C, D]
    ];
    edges.forEach(([p1, p2]) => {
      html += `<line x1="${p1.x}" y1="${p1.y}" x2="${p2.x}" y2="${p2.y}" stroke="${edgeColor}" stroke-width="${edgeWidth}" stroke-linecap="round" />`;
    });

    [Apex, A, B, C, D].forEach(p => {
      const isBack = p === A;
      const fill = isBack ? '#94a3b8' : vertFill;
      html += `
        <circle cx="${p.x}" cy="${p.y}" r="${vertR}" fill="${fill}" stroke="#ffffff" stroke-width="1.5" />
        <text x="${p.x + 8}" y="${p.y - 4}" fill="#f8fafc" font-size="12" font-weight="bold">${p.name}</text>
      `;
    });
  } else if (shape === 'tetra') {
    // Tetrahedron (Triangular Pyramid)
    const Apex = { x: 200, y: 70, name: 'V' };
    const A = { x: 170, y: 220, name: 'A' };
    const B = { x: 310, y: 250, name: 'B' };
    const C = { x: 90, y: 260, name: 'C' };

    // Dashed back edge
    html += `
      <line x1="${A.x}" y1="${A.y}" x2="${Apex.x}" y2="${Apex.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
      <line x1="${C.x}" y1="${C.y}" x2="${A.x}" y2="${A.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
      <line x1="${A.x}" y1="${A.y}" x2="${B.x}" y2="${B.y}" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
    `;

    // Front Faces
    html += `
      <polygon points="${Apex.x},${Apex.y} ${B.x},${B.y} ${C.x},${C.y}" fill="${faceFill}" stroke="${faceStroke}" stroke-width="1.5" />
    `;

    // Edges
    const edges = [
      [Apex, B], [Apex, C],
      [C, B]
    ];
    edges.forEach(([p1, p2]) => {
      html += `<line x1="${p1.x}" y1="${p1.y}" x2="${p2.x}" y2="${p2.y}" stroke="${edgeColor}" stroke-width="${edgeWidth}" stroke-linecap="round" />`;
    });

    [Apex, A, B, C].forEach(p => {
      const isBack = p === A;
      const fill = isBack ? '#94a3b8' : vertFill;
      html += `
        <circle cx="${p.x}" cy="${p.y}" r="${vertR}" fill="${fill}" stroke="#ffffff" stroke-width="1.5" />
        <text x="${p.x + 8}" y="${p.y - 4}" fill="#f8fafc" font-size="12" font-weight="bold">${p.name}</text>
      `;
    });
  }

  container.innerHTML = html;
}

function solveEulerUnknown(changed) {
  const fIn = document.getElementById('calc-f-input');
  const vIn = document.getElementById('calc-v-input');
  const eIn = document.getElementById('calc-e-input');
  const resEl = document.getElementById('calc-solver-result');
  if (!fIn || !vIn || !eIn || !resEl) return;

  let F = parseInt(fIn.value) || 0;
  let V = parseInt(vIn.value) || 0;
  let E = parseInt(eIn.value) || 0;

  if (changed === 'E') {
    // If user changed E, solve for V or check formula
    V = 2 + E - F;
    vIn.value = V;
    resEl.textContent = `कुना V = 2 + E - F = 2 + ${E} - ${F} = ${V}`;
  } else {
    // Calculate E
    E = F + V - 2;
    eIn.value = E;
    resEl.textContent = `किनारा E = F + V - 2 = ${F} + ${V} - 2 = ${E}`;
  }
}

// --- SUB-LAB 2: CURVED SOLIDS EXPLORER STATE ---
let currentCurvedShape = 'cylinder';

const curvedShapeData = {
  cylinder: {
    title: 'बेलना (Cylinder)',
    surfaces: '२ समतल (वृत्ताकार आधार) + १ वक्र सतह',
    vertices: '०',
    desc: 'बेलनामा माथि र तल २ ओटा बराबर वृत्ताकार समतलीय आधारहरू हुन्छन् र वरिपरि एउटा वक्र सतह हुन्छ । यसमा २ ओटा घुमाउरा किनारा हुन्छन् तर कुनै कुना हुँदैन ($V=0$) ।'
  },
  cone: {
    title: 'सोली (Cone)',
    surfaces: '१ समतलीय वृत्ताकार आधार + १ वक्र सतह',
    vertices: '१ (शीर्षबिन्दु / Apex)',
    desc: 'सोलीमा तल १ वटा समतलीय वृत्ताकार आधार र वरिपरि घुमेको वक्र सतह हुन्छ । यसको माथिल्लो टुप्पोमा ठ्याक्कै १ वटा शीर्षबिन्दु (Vertex) हुन्छ र १ घुमाउरो किनारा हुन्छ ।'
  },
  sphere: {
    title: 'गोला (Sphere)',
    surfaces: '१ पूर्ण वक्र सतह (समतल सतह शून्य)',
    vertices: '०',
    desc: 'गोला केन्द्रबिन्दुबाट सतहका सबै बिन्दुहरू बराबर दूरीमा भएको पूर्ण वक्र ठोस वस्तु हो । यसमा कुनै समतल सतह, किनारा वा शीर्षबिन्दु हुँदैन ।'
  }
};

function setCurvedShape(shape) {
  currentCurvedShape = shape;
  ['cyl', 'cone', 'sph'].forEach(s => {
    const btn = document.getElementById('btn-curved-' + s);
    const map = { cyl: 'cylinder', cone: 'cone', sph: 'sphere' };
    if (btn) {
      if (map[s] === shape) {
        btn.className = 'px-3 py-2 rounded-xl bg-cyan-600 text-white font-bold text-xs shadow-sm transition cursor-pointer';
      } else {
        btn.className = 'px-3 py-2 rounded-xl bg-slate-700 hover:bg-slate-600 text-slate-200 font-bold text-xs transition cursor-pointer';
      }
    }
  });

  updateCurvedLab();
}

function updateCurvedLab() {
  const data = curvedShapeData[currentCurvedShape] || curvedShapeData.cylinder;

  const badgeEl = document.getElementById('curved-part-badge');
  const surEl = document.getElementById('curved-surface-types');
  const vEl = document.getElementById('curved-v-count');
  const descEl = document.getElementById('curved-desc-box');

  if (badgeEl) badgeEl.textContent = data.title;
  if (surEl) surEl.textContent = data.surfaces;
  if (vEl) vEl.textContent = data.vertices;
  if (descEl) descEl.textContent = data.desc;

  renderCurvedSvg(currentCurvedShape);
}

function renderCurvedSvg(shape) {
  const container = document.getElementById('curved-svg-shapes');
  if (!container) return;

  let html = '';

  if (shape === 'cylinder') {
    // Cylinder SVG
    html = `
      <!-- Lower Base Dashed Back Arc -->
      <path d="M 120 280 A 80 30 0 0 1 280 280" fill="none" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
      <!-- Lower Base Visible Front Arc -->
      <path d="M 120 280 A 80 30 0 0 0 280 280" fill="none" stroke="#38bdf8" stroke-width="3" />
      
      <!-- Body Shading -->
      <path d="M 120 120 L 120 280 A 80 30 0 0 0 280 280 L 280 120 Z" fill="rgba(56, 189, 248, 0.15)" stroke="none" />
      
      <!-- Side Generators -->
      <line x1="120" y1="120" x2="120" y2="280" stroke="#38bdf8" stroke-width="3" />
      <line x1="280" y1="120" x2="280" y2="280" stroke="#38bdf8" stroke-width="3" />
      
      <!-- Top Elliptical Flat Face -->
      <ellipse cx="200" cy="120" rx="80" ry="30" fill="rgba(56, 189, 248, 0.35)" stroke="#38bdf8" stroke-width="3" />
      
      <!-- Center and Radius in Top Base -->
      <circle cx="200" cy="120" r="4" fill="#f43f5e" />
      <line x1="200" y1="120" x2="280" y2="120" stroke="#f43f5e" stroke-width="2" />
      <text x="235" y="112" fill="#f43f5e" font-size="11" font-weight="bold">r</text>
      
      <!-- Height Dimension Arrow -->
      <line x1="90" y1="120" x2="90" y2="280" stroke="#eab308" stroke-width="1.5" />
      <polygon points="90,115 86,125 94,125" fill="#eab308" />
      <polygon points="90,285 86,275 94,275" fill="#eab308" />
      <text x="75" y="205" fill="#eab308" font-size="12" font-weight="bold">h</text>
    `;
  } else if (shape === 'cone') {
    // Cone SVG
    html = `
      <!-- Base Dashed Back Arc -->
      <path d="M 110 280 A 90 32 0 0 1 290 280" fill="none" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
      <!-- Base Visible Front Arc -->
      <path d="M 110 280 A 90 32 0 0 0 290 280" fill="none" stroke="#f59e0b" stroke-width="3" />
      
      <!-- Cone Curved Body Fill -->
      <path d="M 200 80 L 110 280 A 90 32 0 0 0 290 280 Z" fill="rgba(245, 158, 11, 0.2)" stroke="none" />
      
      <!-- Slant Sides -->
      <line x1="200" y1="80" x2="110" y2="280" stroke="#f59e0b" stroke-width="3" />
      <line x1="200" y1="80" x2="290" y2="280" stroke="#f59e0b" stroke-width="3" />
      
      <!-- Apex Vertex -->
      <circle cx="200" cy="80" r="6" fill="#f43f5e" stroke="#ffffff" stroke-width="2" />
      <text x="212" y="78" fill="#f43f5e" font-size="13" font-weight="extrabold">शीर्षबिन्दु (Vertex)</text>
      
      <!-- Base Radius -->
      <circle cx="200" cy="280" r="4" fill="#38bdf8" />
      <line x1="200" y1="280" x2="290" y2="280" stroke="#38bdf8" stroke-width="2" />
      <text x="245" y="272" fill="#38bdf8" font-size="11" font-weight="bold">r</text>
    `;
  } else if (shape === 'sphere') {
    // Sphere SVG
    html = `
      <!-- Sphere Outer Boundary Circle -->
      <circle cx="200" cy="200" r="100" fill="rgba(168, 85, 247, 0.2)" stroke="#a855f7" stroke-width="3.5" />
      
      <!-- Equatorial Ellipse (Dashed back) -->
      <path d="M 100 200 A 100 35 0 0 1 300 200" fill="none" stroke="#64748b" stroke-width="2" stroke-dasharray="4,4" />
      <!-- Equatorial Ellipse (Front) -->
      <path d="M 100 200 A 100 35 0 0 0 300 200" fill="none" stroke="#c084fc" stroke-width="2.5" />
      
      <!-- Polar Meridian Ellipse (Vertical) -->
      <ellipse cx="200" cy="200" rx="35" ry="100" fill="none" stroke="#a855f7" stroke-width="1.5" stroke-dasharray="2,2" />
      
      <!-- Centre O -->
      <circle cx="200" cy="200" r="5" fill="#f43f5e" stroke="#ffffff" stroke-width="1.5" />
      <text x="185" y="195" fill="#ffffff" font-size="12" font-weight="bold">O</text>
      
      <!-- Radius Line -->
      <line x1="200" y1="200" x2="300" y2="200" stroke="#f43f5e" stroke-width="2.5" />
      <text x="245" y="190" fill="#f43f5e" font-size="12" font-weight="bold">r</text>
    `;
  }

  container.innerHTML = html;
}

// --- SUB-LAB 3: 3D NET / UNPOLDING LAB STATE ---
let currentNetShape = 'cube';

const netShapeData = {
  cube: {
    title: 'घनको नेट (Cube Net)',
    desc: '६ वटा बराबर वर्गहरू मिलेर बनेको क्रस (Cross / T) ढाँचा । यसलाई पट्याउँदा ठ्याक्कै घन बन्दछ ।',
    faces: 6,
    tip: '💡 <strong>घनको नेट:</strong> ६ वटा वर्गहरूलाई विभिन्न ११ प्रकारका वैध ढाँचामा फैलाउन सकिन्छ । ती सबैबाट पट्याएर घन बनाउन सकिन्छ ।'
  },
  cuboid: {
    title: 'षड्मुखाको नेट (Cuboid Net)',
    desc: '६ वटा आयताकार सतहहरू (३ जोडी फरक आयतहरू) मिलेर बनेको ढाँचा ।',
    faces: 6,
    tip: '💡 <strong>षड्मुखाको नेट:</strong> विपरीत आयताकार सतहहरू एकअर्काको सिधा समानान्तर हुने गरी पट्याइन्छ ।'
  },
  cylinder: {
    title: 'बेलनाको नेट (Cylinder Net)',
    desc: '१ वटा लामो आयत (वक्र सतह खोल्दा) र २ वटा बराबर वृत्तहरू (माथिल्लो र तल्लो आधार) ।',
    faces: 3,
    tip: '💡 <strong>बेलनाको वक्र सतह:</strong> आयतको लम्बाइ ठ्याक्कै वृत्तको परिधि ($2\\pi r$) बराबर हुन्छ र चौडाइ बेलनाको उचाइ ($h$) बराबर हुन्छ ।'
  },
  cone: {
    title: 'सोलीको नेट (Cone Net)',
    desc: '१ वटा वृत्तखण्ड वा क्षेत्रक (वक्र सतह खोल्दा) र १ वटा वृत्ताकार समतल आधार ।',
    faces: 2,
    tip: '💡 <strong>सोलीको जाली:</strong> क्षेत्रकको चापको लम्बाइ आधार वृत्तको परिधि बराबर हुन्छ ।'
  }
};

function setNetShape(shape) {
  currentNetShape = shape;
  ['cube', 'cuboid', 'cylinder', 'cone'].forEach(s => {
    const btn = document.getElementById('btn-net-' + s);
    if (btn) {
      if (s === shape) {
        btn.className = 'px-3 py-2 rounded-xl bg-purple-600 text-white font-bold text-xs shadow-sm transition cursor-pointer';
      } else {
        btn.className = 'px-3 py-2 rounded-xl bg-slate-700 hover:bg-slate-600 text-slate-200 font-bold text-xs transition cursor-pointer';
      }
    }
  });

  updateNetLab();
}

function updateNetLab() {
  const data = netShapeData[currentNetShape] || netShapeData.cube;

  const badgeEl = document.getElementById('net-part-badge');
  const descEl = document.getElementById('net-desc-summary');
  const fEl = document.getElementById('net-faces-count');
  const tipEl = document.getElementById('net-tip-box');

  if (badgeEl) badgeEl.textContent = data.title;
  if (descEl) descEl.textContent = data.desc;
  if (fEl) fEl.textContent = data.faces;
  if (tipEl) tipEl.innerHTML = data.tip;

  renderNetSvg(currentNetShape);
}

function renderNetSvg(shape) {
  const container = document.getElementById('net-svg-shapes');
  if (!container) return;

  let html = '';

  if (shape === 'cube') {
    // Cross-shaped Cube Net (4 in row, 1 top, 1 bottom)
    const s = 50;
    const ox = 75;
    const oy = 100;
    const squares = [
      { x: ox + s, y: oy, label: '१' },      // Top
      { x: ox, y: oy + s, label: '२' },      // Left
      { x: ox + s, y: oy + s, label: '३' },  // Middle
      { x: ox + 2 * s, y: oy + s, label: '४' }, // Right
      { x: ox + 3 * s, y: oy + s, label: '५' }, // Far Right
      { x: ox + s, y: oy + 2 * s, label: '६' }  // Bottom
    ];

    squares.forEach(sq => {
      html += `
        <rect x="${sq.x}" y="${sq.y}" width="${s}" height="${s}" fill="rgba(168, 85, 247, 0.3)" stroke="#c084fc" stroke-width="2" rx="2" />
        <text x="${sq.x + s/2}" y="${sq.y + s/2 + 5}" fill="#ffffff" font-size="14" font-weight="bold" text-anchor="middle">${sq.label}</text>
      `;
    });
  } else if (shape === 'cuboid') {
    // Cuboid Net
    const ox = 70;
    const oy = 90;
    const l = 60;
    const b = 45;
    const h = 50;

    // 6 Rectangles
    html = `
      <!-- Top -->
      <rect x="${ox + b}" y="${oy}" width="${l}" height="${b}" fill="rgba(99, 102, 241, 0.3)" stroke="#818cf8" stroke-width="2" />
      <text x="${ox + b + l/2}" y="${oy + b/2 + 4}" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">माथि</text>
      
      <!-- Side Left -->
      <rect x="${ox}" y="${oy + b}" width="${b}" height="${h}" fill="rgba(99, 102, 241, 0.25)" stroke="#818cf8" stroke-width="2" />
      <text x="${ox + b/2}" y="${oy + b + h/2 + 4}" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">बायाँ</text>
      
      <!-- Front -->
      <rect x="${ox + b}" y="${oy + b}" width="${l}" height="${h}" fill="rgba(99, 102, 241, 0.35)" stroke="#818cf8" stroke-width="2" />
      <text x="${ox + b + l/2}" y="${oy + b + h/2 + 4}" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">अगाडि</text>
      
      <!-- Side Right -->
      <rect x="${ox + b + l}" y="${oy + b}" width="${b}" height="${h}" fill="rgba(99, 102, 241, 0.25)" stroke="#818cf8" stroke-width="2" />
      <text x="${ox + b + l + b/2}" y="${oy + b + h/2 + 4}" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">दायाँ</text>
      
      <!-- Back -->
      <rect x="${ox + 2*b + l}" y="${oy + b}" width="${l}" height="${h}" fill="rgba(99, 102, 241, 0.35)" stroke="#818cf8" stroke-width="2" />
      <text x="${ox + 2*b + 3*l/2}" y="${oy + b + h/2 + 4}" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">पछाडि</text>
      
      <!-- Bottom -->
      <rect x="${ox + b}" y="${oy + b + h}" width="${l}" height="${b}" fill="rgba(99, 102, 241, 0.3)" stroke="#818cf8" stroke-width="2" />
      <text x="${ox + b + l/2}" y="${oy + b + h + b/2 + 4}" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">तल</text>
    `;
  } else if (shape === 'cylinder') {
    // Cylinder Net (1 Rectangle + 2 Circles)
    html = `
      <!-- Top Circle -->
      <circle cx="200" cy="90" r="35" fill="rgba(56, 189, 248, 0.3)" stroke="#38bdf8" stroke-width="2" />
      <text x="200" y="94" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">माथिल्लो वृत्त</text>
      
      <!-- Lateral Rectangle -->
      <rect x="90" y="135" width="220" height="90" fill="rgba(56, 189, 248, 0.2)" stroke="#38bdf8" stroke-width="2" rx="3" />
      <text x="200" y="175" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">वक्र सतह (Rectangle: 2πr × h)</text>
      <text x="200" y="195" fill="#94a3b8" font-size="10" text-anchor="middle">लम्बाइ = परिधि (2πr), चौडाइ = उचाइ (h)</text>
      
      <!-- Bottom Circle -->
      <circle cx="200" cy="270" r="35" fill="rgba(56, 189, 248, 0.3)" stroke="#38bdf8" stroke-width="2" />
      <text x="200" y="274" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">तल्लो वृत्त</text>
    `;
  } else if (shape === 'cone') {
    // Cone Net (1 Sector + 1 Circle)
    html = `
      <!-- Sector (Curved Surface) -->
      <path d="M 200 80 L 110 220 A 160 160 0 0 0 290 220 Z" fill="rgba(245, 158, 11, 0.25)" stroke="#f59e0b" stroke-width="2.5" />
      <text x="200" y="160" fill="#f59e0b" font-size="12" font-weight="bold" text-anchor="middle">वक्र सतह (Sector)</text>
      
      <!-- Base Circle -->
      <circle cx="200" cy="280" r="40" fill="rgba(245, 158, 11, 0.35)" stroke="#f59e0b" stroke-width="2" />
      <text x="200" y="284" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">वृत्ताकार आधार</text>
    `;
  }

  container.innerHTML = html;
}

// ==================== CHAPTER 17 QUIZ ENGINE ====================
const ch17QuizData = [
  {
    q: '१. ६ वटा बराबर वर्गाकार सतहहरू मिलेर बनेको ठोस वस्तु कुन हो ?',
    opts: ['षड्मुखा (Cuboid)', 'घन (Cube)', 'बेलना (Cylinder)', 'पिरामिड'],
    ans: 1,
    exp: 'छओटा बराबर वर्गाकार समतलीय सतहहरू मिलेर बनेको बन्द ठोस वस्तुलाई घन (Cube) भनिन्छ ।'
  },
  {
    q: '२. बहुफलकमा सतह (F), शीर्षबिन्दु (V) र किनारा (E) बीचको यूलरको सही सूत्र कुन हो ?',
    opts: ['V + E + F = 2', 'V - E + F = 2', 'F - V + E = 2', 'E - V - F = 2'],
    ans: 1,
    exp: 'यूलरको सूत्र अनुसार V - E + F = 2 वा F + V = E + 2 हुन्छ ।'
  },
  {
    q: '३. एउटा षड्मुखा (Cuboid) मा कतिवटा किनाराहरू (Edges) हुन्छन् ?',
    opts: ['६ ओटा', '८ ओटा', '१० ओटा', '१२ ओटा'],
    ans: 3,
    exp: 'षड्मुखामा ४ लम्बाइ, ४ चौडाइ र ४ उचाइ गरी जम्मा १२ ओटा किनाराहरू हुन्छन् ।'
  },
  {
    q: '४. कुनै ठोस वस्तुमा सतह F = 5 र शीर्षबिन्दु V = 6 भए किनारा E को मान कति हुन्छ ?',
    opts: ['७ ओटा', '८ ओटा', '९ ओटा', '११ ओटा'],
    ans: 2,
    exp: 'यूलर सूत्र अनुसार: E = F + V - 2 = 5 + 6 - 2 = 9 ओटा किनारा हुन्छन् (यो त्रिकोणात्मक प्रिज्मा हो) ।'
  },
  {
    q: '५. तलका मध्ये कुन ठोस वस्तुमा ठ्याक्कै एउटा मात्र शीर्षबिन्दु (Vertex) हुन्छ ?',
    opts: ['बेलना (Cylinder)', 'सोली (Cone)', 'गोला (Sphere)', 'घन (Cube)'],
    ans: 1,
    exp: 'सोली (Cone) मा तल १ वृत्ताकार आधार र माथिल्लो टुप्पोमा ठ्याक्कै १ वटा शीर्षबिन्दु हुन्छ ।'
  },
  {
    q: '६. बेलना (Cylinder) मा कतिवटा समतलीय र कतिवटा वक्र सतह हुन्छन् ?',
    opts: ['२ समतलीय र १ वक्र सतह', '१ समतलीय र २ वक्र सतह', '३ समतलीय सतह', '१ वक्र सतह मात्र'],
    ans: 0,
    exp: 'बेलनामा माथि र तल २ ओटा समतलीय वृत्ताकार सतह र १ वटा वक्र सतह गरी जम्मा ३ सतह हुन्छन् ।'
  },
  {
    q: '७. फुटबल, गुच्चा र सुन्तला कुन ठोस ज्यामितीय आकृतिका उदाहरण हुन् ?',
    opts: ['बेलना (Cylinder)', 'सोली (Cone)', 'गोला (Sphere)', 'पिरामिड'],
    ans: 2,
    exp: 'फुटबल र गुच्चा पूर्ण रूपमा गोलाकार वक्र सतह भएकाले यी गोला (Sphere) का उदाहरण हुन् ।'
  },
  {
    q: '८. एउटा षड्मुखाको लम्बाइ, चौडाइ र उचाइ तीनवटै बराबर भएमा उक्त आकृति के बन्दछ ?',
    opts: ['बेलना', 'सोली', 'घन (Cube)', 'प्रिज्मा'],
    ans: 2,
    exp: 'जब षड्मुखामा l = b = h हुन्छ, सबै ६ सतहहरू वर्ग बन्दछन् र त्यो आकृति घन बन्दछ ।'
  },
  {
    q: '९. वर्गाकार आधार भएको पिरामिड (Square Pyramid) मा जम्मा कतिवटा सतहहरू हुन्छन् ?',
    opts: ['४ ओटा', '५ ओटा', '६ ओटा', '८ ओटा'],
    ans: 1,
    exp: 'वर्गाकार पिरामिडमा १ वटा वर्गाकार आधार र ४ वटा त्रिभुजाकार सतह गरी जम्मा ५ ओटा सतह हुन्छन् ।'
  },
  {
    q: '१०. तलका मध्ये कुन ठोस वस्तुमा कुनै पनि कुना (शीर्षबिन्दु) र समतलीय सतह हुँदैन ?',
    opts: ['घन', 'षड्मुखा', 'बेलना', 'गोला (Sphere)'],
    ans: 3,
    exp: 'गोला (Sphere) मा एउटा मात्र पूर्ण वक्र सतह हुन्छ; यसमा कुनै समतल सतह, किनारा वा शीर्षबिन्दु हुँदैन ।'
  }
];

let ch17QuizAnswers = {};

function renderCh17Quiz() {
  const container = document.getElementById('ch17-quiz-container');
  if (!container) return;

  container.innerHTML = ch17QuizData
    .map((item, qIdx) => {
      const isAnswered = ch17QuizAnswers.hasOwnProperty(qIdx);
      const selAns = ch17QuizAnswers[qIdx];
      const isCorrect = isAnswered && selAns === item.ans;

      const optsHtml = item.opts
        .map((opt, optIdx) => {
          let btnClass = 'p-3 rounded-xl border text-left text-xs md:text-sm transition cursor-pointer ';
          if (!isAnswered) {
            btnClass += 'bg-slate-50 border-slate-200 hover:bg-blue-50 hover:border-blue-300 text-slate-800';
          } else {
            if (optIdx === item.ans) {
              btnClass += 'bg-emerald-100 border-emerald-500 text-emerald-900 font-bold';
            } else if (optIdx === selAns) {
              btnClass += 'bg-rose-100 border-rose-500 text-rose-900 font-bold';
            } else {
              btnClass += 'bg-slate-50 border-slate-200 text-slate-400 opacity-60';
            }
          }

          return `
            <button onclick="handleCh17QuizAnswer(${qIdx}, ${optIdx})" class="${btnClass}">
              ${opt}
            </button>
          `;
        })
        .join('');

      let feedbackHtml = '';
      if (isAnswered) {
        feedbackHtml = `
          <div class="mt-2.5 p-3 rounded-xl text-xs ${isCorrect ? 'bg-emerald-50 border border-emerald-200 text-emerald-900' : 'bg-rose-50 border border-rose-200 text-rose-900'}">
            <span class="font-bold">${isCorrect ? '✓ सही उत्तर!' : '✗ गलत उत्तर!'}</span> ${item.exp}
          </div>
        `;
      }

      return `
        <div class="p-5 bg-white rounded-2xl border border-slate-200 shadow-sm space-y-3">
          <div class="font-bold text-slate-800 text-sm md:text-base">${item.q}</div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
            ${optsHtml}
          </div>
          ${feedbackHtml}
        </div>
      `;
    })
    .join('');

  updateCh17QuizScore();
}

function handleCh17QuizAnswer(qIdx, optIdx) {
  if (ch17QuizAnswers.hasOwnProperty(qIdx)) return;
  ch17QuizAnswers[qIdx] = optIdx;
  renderCh17Quiz();
}

function updateCh17QuizScore() {
  let score = 0;
  Object.keys(ch17QuizAnswers).forEach(qIdx => {
    if (ch17QuizAnswers[qIdx] === ch17QuizData[qIdx].ans) {
      score++;
    }
  });
  const el = document.getElementById('ch17-quiz-score');
  if (el) el.textContent = score;
}

function resetCh17Quiz() {
  ch17QuizAnswers = {};
  renderCh17Quiz();
}

// Initialise Chapter 17 Lab on load
document.addEventListener('DOMContentLoaded', () => {
  updatePolyLab();
});

    // Expose Chapter 17 globals
    window.setTabCh17 = setTabCh17;
    window.switchCh17Lab = switchCh17Lab;
    window.setPolyShape = setPolyShape;
    window.setPolyHighlight = setPolyHighlight;
    window.updatePolyLab = updatePolyLab;
    window.solveEulerUnknown = solveEulerUnknown;
    window.setCurvedShape = setCurvedShape;
    window.updateCurvedLab = updateCurvedLab;
    window.setNetShape = setNetShape;
    window.updateNetLab = updateNetLab;
    window.renderCh17Quiz = renderCh17Quiz;
    window.handleCh17QuizAnswer = handleCh17QuizAnswer;
    window.resetCh17Quiz = resetCh17Quiz;




// ==================== CHAPTER 18 INTERACTIVE ENGINE ====================

// --- Tab Switcher ---
function setTabCh18(tab) {
  const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
  tabs.forEach(t => {
    const btn = document.getElementById('ch18-tab-' + t);
    const view = document.getElementById('ch18-view-' + t);
    if (btn && view) {
      if (t === tab) {
        btn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
        view.classList.remove('hidden');
      } else {
        btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
        view.classList.add('hidden');
      }
    }
  });

  if (tab === 'quiz') {
    renderCh18Quiz();
  }

  try {
    if (window.renderMathInElement) {
      renderMathInElement(document.getElementById('chapter-view-18'), {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false }
        ],
        throwOnError: false
      });
    }
  } catch (e) {}
}

// --- Lab Mode Switcher ---
let currentCh18LabMode = 'plot'; // 'plot', 'shapes', 'quads'
let currentActivePoint = { x: 3, y: 4, name: 'P' };
let currentActiveShape = 'square';
let activeHighlightedQuad = 1;

function switchCh18Lab(mode) {
  currentCh18LabMode = mode;
  ['plot', 'shapes', 'quads'].forEach(m => {
    const btn = document.getElementById('ch18-lab-tab-' + m);
    const panel = document.getElementById('ch18-panel-' + m);
    if (btn && panel) {
      if (m === mode) {
        btn.className = 'px-4 py-2 rounded-xl bg-blue-600 text-white font-bold text-xs shadow-sm transition cursor-pointer';
        panel.classList.remove('hidden');
      } else {
        btn.className = 'px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs transition cursor-pointer';
        panel.classList.add('hidden');
      }
    }
  });

  const hintEl = document.getElementById('ch18-grid-hint');
  if (hintEl) {
    if (mode === 'plot') {
      hintEl.textContent = 'ग्राफमा जहाँसुकै क्लिक गरी बिन्दु अङ्कन गर्नुहोस्';
    } else if (mode === 'shapes') {
      hintEl.textContent = 'आकृति छनोट गरी शीर्षबिन्दु र क्षेत्रफल अवलोकन गर्नुहोस्';
    } else if (mode === 'quads') {
      hintEl.textContent = 'चतुर्थांशहरू क्लिक गरी विशेषता र चिह्नहरू हेर्नुहोस्';
    }
  }

  renderCartesianGrid();
  if (mode === 'plot') {
    plotPoint(currentActivePoint.x, currentActivePoint.y);
  } else if (mode === 'shapes') {
    loadShapePreset(currentActiveShape);
  } else if (mode === 'quads') {
    highlightQuadrant(activeHighlightedQuad);
  }
}

// --- Grid Renderer ---
function renderCartesianGrid() {
  const gridG = document.getElementById('cartesian-grid-lines');
  if (!gridG) return;

  let html = '';
  // Grid lines: step 20 from -200 to 200
  for (let i = -10; i <= 10; i++) {
    const pos = i * 20;
    const isMain = i % 5 === 0;
    const stroke = isMain ? 'rgba(255, 255, 255, 0.35)' : 'rgba(255, 255, 255, 0.12)';
    const strokeW = isMain ? 1.4 : 0.8;

    // Vertical line (x = pos)
    html += `<line x1="${pos}" y1="-210" x2="${pos}" y2="210" stroke="${stroke}" stroke-width="${strokeW}" />`;
    // Horizontal line (y = pos)
    html += `<line x1="-210" y1="${pos}" x2="210" y2="${pos}" stroke="${stroke}" stroke-width="${strokeW}" />`;

    // Numeric Ticks (except 0 which is at origin)
    if (i !== 0 && (i % 2 === 0 || i === -10 || i === 10)) {
      // X-axis numbers (y = 12)
      html += `<text x="${pos}" y="12" fill="#cbd5e1" font-size="8" text-anchor="middle" font-family="monospace">${i}</text>`;
      // Y-axis numbers (x = -8, SVG y is -i*20)
      html += `<text x="-8" y="${-pos + 3}" fill="#cbd5e1" font-size="8" text-anchor="end" font-family="monospace">${i}</text>`;
    }
  }

  gridG.innerHTML = html;
}

// --- Grid Click Handler ---
function handleCartesianGridClick(evt) {
  if (currentCh18LabMode !== 'plot') return;

  const svg = document.getElementById('svg-cartesian-grid');
  if (!svg) return;

  const pt = svg.createSVGPoint();
  pt.x = evt.clientX;
  pt.y = evt.clientY;
  const svgP = pt.matrixTransform(svg.getScreenCTM().inverse());

  // Scale: 1 unit = 20 svg units
  let mathX = Math.round(svgP.x / 20);
  let mathY = Math.round(-svgP.y / 20);

  // Clamp to [-10, 10]
  mathX = Math.max(-10, Math.min(10, mathX));
  mathY = Math.max(-10, Math.min(10, mathY));

  plotPoint(mathX, mathY);
}

function plotFromInput() {
  const inX = document.getElementById('ch18-input-x');
  const inY = document.getElementById('ch18-input-y');
  if (!inX || !inY) return;

  const x = parseInt(inX.value, 10) || 0;
  const y = parseInt(inY.value, 10) || 0;
  plotPoint(x, y);
}

function resetCh18Plot() {
  plotPoint(0, 0);
}

// --- Point Plotter Logic ---
function plotPoint(x, y) {
  currentActivePoint = { x, y, name: 'P' };

  // Update inputs
  const inX = document.getElementById('ch18-input-x');
  const inY = document.getElementById('ch18-input-y');
  if (inX) inX.value = x;
  if (inY) inY.value = y;

  // Clear shapes and shading
  const shapeG = document.getElementById('cartesian-shapes-layer');
  if (shapeG) shapeG.innerHTML = '';
  const quadG = document.getElementById('cartesian-quad-shading');
  if (quadG) quadG.innerHTML = '';

  // Determine Quadrant / Position
  let quadText = '';
  let signText = '';
  let xDesc = '';
  let yDesc = '';
  let walkDesc = '';

  if (x > 0 && y > 0) {
    quadText = 'पहिलो चतुर्थांश (First Quadrant - Q₁)';
    signText = '(+, +)';
    xDesc = `दायाँ ${x} एकाइ`;
    yDesc = `माथि ${y} एकाइ`;
    walkDesc = `उद्गम बिन्दु O(0, 0) बाट X-अक्षमा ${x} एकाइ दायाँ जानुहोस्, अनि त्यहीँबाट सीधा माथि ${y} एकाइ जानुहोस्।`;
  } else if (x < 0 && y > 0) {
    quadText = 'दोस्रो चतुर्थांश (Second Quadrant - Q₂)';
    signText = '(-, +)';
    xDesc = `बायाँ ${Math.abs(x)} एकाइ`;
    yDesc = `माथि ${y} एकाइ`;
    walkDesc = `उद्गम बिन्दु O(0, 0) बाट X-अक्षमा ${Math.abs(x)} एकाइ बायाँ जानुहोस्, अनि त्यहीँबाट सीधा माथि ${y} एकाइ जानुहोस्।`;
  } else if (x < 0 && y < 0) {
    quadText = 'तेस्रो चतुर्थांश (Third Quadrant - Q₃)';
    signText = '(-, -)';
    xDesc = `बायाँ ${Math.abs(x)} एकाइ`;
    yDesc = `तल ${Math.abs(y)} एकाइ`;
    walkDesc = `उद्गम बिन्दु O(0, 0) बाट X-अक्षमा ${Math.abs(x)} एकाइ बायाँ जानुहोस्, अनि त्यहीँबाट सीधा तल ${Math.abs(y)} एकाइ जानुहोस्।`;
  } else if (x > 0 && y < 0) {
    quadText = 'चौथो चतुर्थांश (Fourth Quadrant - Q₄)';
    signText = '(+, -)';
    xDesc = `दायाँ ${x} एकाइ`;
    yDesc = `तल ${Math.abs(y)} एकाइ`;
    walkDesc = `उद्गम बिन्दु O(0, 0) बाट X-अक्षमा ${x} एकाइ दायाँ जानुहोस्, अनि त्यहीँबाट सीधा तल ${Math.abs(y)} एकाइ जानुहोस्।`;
  } else if (x === 0 && y === 0) {
    quadText = 'उद्गम बिन्दु (Origin - O)';
    signText = '(0, 0)';
    xDesc = 'शून्य दूरी';
    yDesc = 'शून्य दूरी';
    walkDesc = 'यो केन्द्रबिन्दु हो, यहाँ कुनै दिशा हिँड्नु पर्दैन।';
  } else if (y === 0) {
    quadText = x > 0 ? 'धनात्मक X-अक्षमा (+X Axis)' : 'ऋणात्मक X-अक्षमा (-X Axis)';
    signText = `(${x > 0 ? '+' : '-'}, 0)`;
    xDesc = x > 0 ? `दायाँ ${x} एकाइ` : `बायाँ ${Math.abs(x)} एकाइ`;
    yDesc = 'अक्षमै (ठाडो दूरी शून्य)';
    walkDesc = `उद्गम बिन्दु O(0, 0) बाट X-अक्षमा ${Math.abs(x)} एकाइ ${x > 0 ? 'दायाँ' : 'बायाँ'} जानुहोस्। माथि वा तल जानु पर्दैन।`;
  } else if (x === 0) {
    quadText = y > 0 ? 'धनात्मक Y-अक्षमा (+Y Axis)' : 'ऋणात्मक Y-अक्षमा (-Y Axis)';
    signText = `(0, ${y > 0 ? '+' : '-'})`;
    xDesc = 'अक्षमै (तेर्सो दूरी शून्य)';
    yDesc = y > 0 ? `माथि ${y} एकाइ` : `तल ${Math.abs(y)} एकाइ`;
    walkDesc = `उद्गम बिन्दु O(0, 0) बाट Y-अक्षमा सीधा ${Math.abs(y)} एकाइ ${y > 0 ? 'माथि' : 'तल'} जानुहोस्। दायाँ वा बायाँ जानु पर्दैन।`;
  }

  // Update DOM Inspector
  const badgeEl = document.getElementById('ch18-coord-badge');
  const inspName = document.getElementById('insp-point-name');
  const inspX = document.getElementById('insp-x-val');
  const inspXDesc = document.getElementById('insp-x-desc');
  const inspY = document.getElementById('insp-y-val');
  const inspYDesc = document.getElementById('insp-y-desc');
  const inspQuad = document.getElementById('insp-quad-val');
  const inspSign = document.getElementById('insp-sign-val');
  const inspDist = document.getElementById('insp-dist-val');
  const inspWalk = document.getElementById('insp-walk-desc');

  const dist = Math.sqrt(x * x + y * y).toFixed(2);
  const pointStr = `P(${x}, ${y})`;

  if (badgeEl) badgeEl.textContent = `${pointStr} — ${quadText}`;
  if (inspName) inspName.textContent = pointStr;
  if (inspX) inspX.textContent = (x > 0 ? '+' : '') + x;
  if (inspXDesc) inspXDesc.textContent = xDesc;
  if (inspY) inspY.textContent = (y > 0 ? '+' : '') + y;
  if (inspYDesc) inspYDesc.textContent = yDesc;
  if (inspQuad) inspQuad.textContent = quadText;
  if (inspSign) inspSign.textContent = signText;
  if (inspDist) inspDist.textContent = dist + ' एकाइ';
  if (inspWalk) inspWalk.textContent = walkDesc;

  // Render SVG Elements
  const ptG = document.getElementById('cartesian-points-layer');
  if (!ptG) return;

  const svgX = x * 20;
  const svgY = -y * 20;

  let html = '';

  // Guidelines from Origin if not at origin
  if (x !== 0 || y !== 0) {
    // Horizontal segment along X: (0, 0) to (svgX, 0)
    html += `<line x1="0" y1="0" x2="${svgX}" y2="0" stroke="#3b82f6" stroke-width="2" stroke-dasharray="3,3" />`;
    // Vertical segment: (svgX, 0) to (svgX, svgY)
    html += `<line x1="${svgX}" y1="0" x2="${svgX}" y2="${svgY}" stroke="#10b981" stroke-width="2" stroke-dasharray="3,3" />`;
    // Corner turn indicator
    html += `<circle cx="${svgX}" cy="0" r="3" fill="#3b82f6" />`;
  }

  // Active glowing target
  html += `
    <circle cx="${svgX}" cy="${svgY}" r="12" fill="rgba(245, 158, 11, 0.25)" class="animate-pulse" />
    <circle cx="${svgX}" cy="${svgY}" r="5.5" fill="#f59e0b" stroke="#ffffff" stroke-width="2" />
  `;

  // Label positioning: avoid colliding with axes
  const labelX = svgX >= 0 ? svgX + 8 : svgX - 8;
  const textAnchor = svgX >= 0 ? 'start' : 'end';
  const labelY = svgY >= 0 ? svgY + 16 : svgY - 8;

  html += `
    <rect x="${textAnchor === 'start' ? labelX - 2 : labelX - 58}" y="${labelY - 12}" width="60" height="18" rx="4" fill="rgba(15, 23, 42, 0.85)" stroke="#f59e0b" stroke-width="1" />
    <text x="${textAnchor === 'start' ? labelX + 4 : labelX - 4}" y="${labelY + 1}" fill="#fef08a" font-size="11" font-weight="bold" font-family="monospace" text-anchor="${textAnchor}">
      ${pointStr}
    </text>
  `;

  ptG.innerHTML = html;
}

// --- Shape Builder Logic ---
const shapePresets = {
  square: {
    title: 'वर्ग (Square) — प्रश्न ४ (क)',
    vertices: [
      { x: 4, y: 4, name: 'A' },
      { x: -4, y: 4, name: 'B' },
      { x: -4, y: -4, name: 'C' },
      { x: 4, y: -4, name: 'D' }
    ],
    side: '८ एकाइ',
    area: '६४ वर्ग एकाइ',
    calc: 'क्षेत्रफल = l² = 8 × 8 = 64 वर्ग एकाइ (६४ ओटा वर्गाकार कोठाहरू)'
  },
  triangle: {
    title: 'समद्विबाहु त्रिभुज — प्रश्न ४ (ख)',
    vertices: [
      { x: 0, y: 6, name: 'P' },
      { x: -6, y: 0, name: 'Q' },
      { x: 6, y: 0, name: 'R' }
    ],
    side: 'आधार: १२ एकाइ, उचाइ: ६ एकाइ',
    area: '३६ वर्ग एकाइ',
    calc: 'क्षेत्रफल = ½ × आधार × उचाइ = ½ × 12 × 6 = 36 वर्ग एकाइ'
  },
  parallelogram: {
    title: 'समानान्तर चतुर्भुज — प्रश्न ४ (घ)',
    vertices: [
      { x: 8, y: 9, name: 'A' },
      { x: 4, y: 9, name: 'B' },
      { x: 2, y: 2, name: 'C' },
      { x: 6, y: 2, name: 'D' }
    ],
    side: 'आधार: ४ एकाइ, उचाइ: ७ एकाइ',
    area: '२८ वर्ग एकाइ',
    calc: 'क्षेत्रफल = आधार × उचाइ = 4 × 7 = 28 वर्ग एकाइ'
  },
  rectangle: {
    title: 'आयत (Rectangle) — प्रश्न ४ (ङ)',
    vertices: [
      { x: 0, y: 9, name: 'A' },
      { x: 5, y: 9, name: 'B' },
      { x: 5, y: -2, name: 'C' },
      { x: 0, y: -2, name: 'D' }
    ],
    side: 'लम्बाइ: ११ एकाइ, चौडाइ: ५ एकाइ',
    area: '५५ वर्ग एकाइ',
    calc: 'क्षेत्रफल = l × b = 11 × 5 = 55 वर्ग एकाइ'
  }
};

function loadShapePreset(presetKey) {
  currentActiveShape = presetKey;
  const data = shapePresets[presetKey] || shapePresets.square;

  // Clear points layer and quad shading
  const ptG = document.getElementById('cartesian-points-layer');
  if (ptG) ptG.innerHTML = '';
  const quadG = document.getElementById('cartesian-quad-shading');
  if (quadG) quadG.innerHTML = '';

  // Button styles
  ['square', 'triangle', 'parallelogram', 'rectangle'].forEach(k => {
    const btn = document.getElementById('btn-preset-' + k);
    if (btn) {
      if (k === presetKey) {
        btn.className = 'p-2.5 bg-blue-600 text-white rounded-xl text-xs font-bold transition cursor-pointer text-left shadow-sm';
      } else {
        btn.className = 'p-2.5 bg-slate-700 hover:bg-slate-600 text-slate-200 rounded-xl text-xs font-bold transition cursor-pointer text-left';
      }
    }
  });

  // Update Inspector Card
  const nameEl = document.getElementById('shape-name-badge');
  const vertEl = document.getElementById('shape-vertices-list');
  const sideEl = document.getElementById('shape-side-val');
  const areaEl = document.getElementById('shape-area-val');
  const calcEl = document.getElementById('shape-calc-desc');
  const badgeEl = document.getElementById('ch18-coord-badge');

  if (nameEl) nameEl.textContent = data.title;
  if (vertEl) {
    vertEl.textContent = data.vertices.map(v => `${v.name}(${v.x}, ${v.y})`).join(', ');
  }
  if (sideEl) sideEl.textContent = data.side;
  if (areaEl) areaEl.textContent = data.area;
  if (calcEl) calcEl.textContent = data.calc;
  if (badgeEl) badgeEl.textContent = `${data.title} — क्षेत्रफल: ${data.area}`;

  // Render on SVG
  const shapeG = document.getElementById('cartesian-shapes-layer');
  if (!shapeG) return;

  const pointsAttr = data.vertices.map(v => `${v.x * 20},${-v.y * 20}`).join(' ');

  let html = `
    <!-- Filled polygon -->
    <polygon points="${pointsAttr}" fill="rgba(56, 189, 248, 0.25)" stroke="#38bdf8" stroke-width="2.5" />
  `;

  // Draw vertices and text
  data.vertices.forEach(v => {
    const sx = v.x * 20;
    const sy = -v.y * 20;
    const lx = sx >= 0 ? sx + 7 : sx - 7;
    const ly = sy >= 0 ? sy + 14 : sy - 6;
    const anchor = sx >= 0 ? 'start' : 'end';

    html += `
      <circle cx="${sx}" cy="${sy}" r="5" fill="#f43f5e" stroke="#ffffff" stroke-width="1.5" />
      <text x="${lx}" y="${ly}" fill="#ffffff" font-size="10" font-weight="bold" font-family="monospace" text-anchor="${anchor}">
        ${v.name}(${v.x}, ${v.y})
      </text>
    `;
  });

  shapeG.innerHTML = html;
}

// --- Quadrant Explorer Logic ---
const quadData = {
  1: {
    title: 'पहिलो चतुर्थांश (First Quadrant - Q₁)',
    signs: '(+, +)',
    desc: 'उद्गम बिन्दु O बाट दायाँतर्फ र माथितर्फ पर्ने सम्पूर्ण क्षेत्र। यहाँ भुज (x > 0) र कोटि (y > 0) दुवै धनात्मक हुन्छन्।',
    eg: 'नमुना बिन्दुहरू: A(3, 5), B(6, 2), C(1, 8), D(4, 4)',
    box: { x: 0, y: -200, w: 200, h: 200 }
  },
  2: {
    title: 'दोस्रो चतुर्थांश (Second Quadrant - Q₂)',
    signs: '(-, +)',
    desc: 'उद्गम बिन्दु O बाट बायाँतर्फ र माथितर्फ पर्ने सम्पूर्ण क्षेत्र। यहाँ भुज ऋणात्मक (x < 0) र कोटि धनात्मक (y > 0) हुन्छ।',
    eg: 'नमुना बिन्दुहरू: P(-4, 5), Q(-7, 2), R(-2, 8), S(-5, 6)',
    box: { x: -200, y: -200, w: 200, h: 200 }
  },
  3: {
    title: 'तेस्रो चतुर्थांश (Third Quadrant - Q₃)',
    signs: '(-, -)',
    desc: 'उद्गम बिन्दु O बाट बायाँतर्फ र तलतर्फ पर्ने सम्पूर्ण क्षेत्र। यहाँ भुज (x < 0) र कोटि (y < 0) दुवै ऋणात्मक हुन्छन्।',
    eg: 'नमुना बिन्दुहरू: M(-3, -6), N(-7, -2), K(-5, -4), L(-8, -8)',
    box: { x: -200, y: 0, w: 200, h: 200 }
  },
  4: {
    title: 'चौथो चतुर्थांश (Fourth Quadrant - Q₄)',
    signs: '(+, -)',
    desc: 'उद्गम बिन्दु O बाट दायाँतर्फ र तलतर्फ पर्ने सम्पूर्ण क्षेत्र। यहाँ भुज धनात्मक (x > 0) र कोटि ऋणात्मक (y < 0) हुन्छ।',
    eg: 'नमुना बिन्दुहरू: X(5, -3), Y(7, -6), Z(2, -8), W(4, -5)',
    box: { x: 0, y: 0, w: 200, h: 200 }
  }
};

function highlightQuadrant(q) {
  activeHighlightedQuad = q;
  const data = quadData[q] || quadData[1];

  // Button styles
  [1, 2, 3, 4].forEach(i => {
    const btn = document.getElementById('btn-quad-' + i);
    if (btn) {
      if (i === q) {
        btn.className = 'p-3 bg-blue-600 text-white rounded-xl text-xs font-bold transition cursor-pointer text-left shadow-sm';
      } else {
        btn.className = 'p-3 bg-slate-700 hover:bg-slate-600 text-slate-200 rounded-xl text-xs font-bold transition cursor-pointer text-left';
      }
    }
  });

  // Update text
  const titleEl = document.getElementById('quad-info-title');
  const descEl = document.getElementById('quad-info-desc');
  const egEl = document.getElementById('quad-info-eg');
  const badgeEl = document.getElementById('ch18-coord-badge');

  if (titleEl) titleEl.textContent = `${data.title} ${data.signs}`;
  if (descEl) descEl.textContent = data.desc;
  if (egEl) egEl.textContent = data.eg;
  if (badgeEl) badgeEl.textContent = `${data.title} — चिह्न: ${data.signs}`;

  // Clear shapes and points
  const shapeG = document.getElementById('cartesian-shapes-layer');
  if (shapeG) shapeG.innerHTML = '';
  const ptG = document.getElementById('cartesian-points-layer');
  if (ptG) ptG.innerHTML = '';

  // Render Quadrant Shading
  const quadG = document.getElementById('cartesian-quad-shading');
  if (!quadG) return;

  const b = data.box;
  quadG.innerHTML = `
    <rect x="${b.x}" y="${b.y}" width="${b.w}" height="${b.h}" fill="rgba(129, 140, 248, 0.25)" stroke="#818cf8" stroke-width="2" stroke-dasharray="4,4" />
    <text x="${b.x + b.w / 2}" y="${b.y + b.h / 2}" fill="#818cf8" font-size="28" font-weight="black" text-anchor="middle" dominant-baseline="middle" opacity="0.4">
      Q${q}
    </text>
  `;
}

// ==================== QUIZ ENGINE ====================
const ch18QuizQuestions = [
  {
    id: 1,
    question: "समतलमा X-अक्ष र Y-अक्ष परस्पर काटिने बिन्दुलाई के भनिन्छ र यसको निर्देशाङ्क कति हुन्छ ?",
    options: [
      "उद्गम बिन्दु (Origin), (0, 0)",
      "शीर्षबिन्दु, (1, 1)",
      "चतुर्थांश केन्द्र, (0, 1)",
      "मध्यबिन्दु, (-1, -1)"
    ],
    correct: 0,
    explanation: "X र Y अक्ष आपसमा ९०° मा काटिने केन्द्रलाई उद्गम बिन्दु (Origin) भनिन्छ र यसको निर्देशाङ्क O(0, 0) हुन्छ।"
  },
  {
    id: 2,
    question: "बिन्दु P(-5, 4) कुन चतुर्थांशमा पर्दछ ?",
    options: [
      "पहिलो चतुर्थांश (Q₁)",
      "दोस्रो चतुर्थांश (Q₂)",
      "तेस्रो चतुर्थांश (Q₃)",
      "चौथो चतुर्थांश (Q₄)"
    ],
    correct: 1,
    explanation: "भुज ऋणात्मक (x = -5) र कोटि धनात्मक (y = 4) भएको बिन्दु दोस्रो चतुर्थांश (-, +) मा पर्दछ।"
  },
  {
    id: 3,
    question: "X-अक्षमा पर्ने कुनै पनि बिन्दुको रूप कस्तो हुन्छ ?",
    options: [
      "(0, y)",
      "(x, 0)",
      "(x, y)",
      "(0, 0)"
    ],
    correct: 1,
    explanation: "X-अक्षमा पर्ने जुनसुकै बिन्दुको कोटि (y-मान) सधैँ शून्य (0) हुने भएकाले यसको स्वरूप (x, 0) हुन्छ।"
  },
  {
    id: 4,
    question: "बिन्दु A(3, -6) मा भुज (Abscissa) को मान कति हो ?",
    options: [
      "-6",
      "3",
      "-3",
      "6"
    ],
    correct: 1,
    explanation: "निर्देशाङ्क जोडी (x, y) मा पहिलो मान भुज (x-coordinate) हुन्छ। त्यसैले भुज = 3 हो।"
  },
  {
    id: 5,
    question: "कुन चतुर्थांशमा भुज (x) र कोटि (y) दुवै ऋणात्मक (Negative) हुन्छन् ?",
    options: [
      "पहिलो चतुर्थांश (Q₁)",
      "दोस्रो चतुर्थांश (Q₂)",
      "तेस्रो चतुर्थांश (Q₃)",
      "चौथो चतुर्थांश (Q₄)"
    ],
    correct: 2,
    explanation: "तेस्रो चतुर्थांश (Q₃) मा उद्गमबाट बायाँ र तल पर्ने भएकाले दुवै ऋणात्मक (-, -) हुन्छन्।"
  },
  {
    id: 6,
    question: "बिन्दु (0, -8) कार्तेसियन समतलको कुन स्थानमा पर्दछ ?",
    options: [
      "तेस्रो चतुर्थांशमा",
      "धनात्मक X-अक्षमा",
      "ऋणात्मक Y-अक्षमा",
      "चौथो चतुर्थांशमा"
    ],
    correct: 2,
    explanation: "x = 0 भएकाले यो Y-अक्षमा पर्छ र y = -8 ऋणात्मक भएकाले ऋणात्मक Y-अक्षमा पर्छ।"
  },
  {
    id: 7,
    question: "बिन्दु M(2, 5) र N(2, -3) बीचको ठाडो दूरी कति हुन्छ ?",
    options: [
      "२ एकाइ",
      "८ एकाइ",
      "५ एकाइ",
      "१० एकाइ"
    ],
    correct: 1,
    explanation: "x-मान समान (2) भएकाले ठाडो दूरी = y₁ - y₂ = 5 - (-3) = 5 + 3 = 8 एकाइ हुन्छ।"
  },
  {
    id: 8,
    question: "बिन्दुहरू (4, 4), (-4, 4), (-4, -4) र (4, -4) जोड्दा बन्ने वर्गको क्षेत्रफल कति हुन्छ ?",
    options: [
      "१६ वर्ग एकाइ",
      "३२ वर्ग एकाइ",
      "६४ वर्ग एकाइ",
      "१२८ वर्ग एकाइ"
    ],
    correct: 2,
    explanation: "वर्गको प्रत्येक भुजाको लम्बाइ = 4 - (-4) = 8 एकाइ हो। क्षेत्रफल = l² = 8 × 8 = 64 वर्ग एकाइ।"
  },
  {
    id: 9,
    question: "बिन्दु (3, 5) र (5, 3) बारे कुन भनाइ सत्य हो ?",
    options: [
      "दुवै एउटै बिन्दु हुन्",
      "दुवै फरक-फरक बिन्दु हुन्",
      "दुवै X-अक्षमा पर्छन्",
      "दुवै Y-अक्षमा पर्छन्"
    ],
    correct: 1,
    explanation: "निर्देशाङ्क क्रमित जोडी (Ordered pair) हो। (3, 5) मा x=3, y=5 छ भने (5, 3) मा x=5, y=3 छ, त्यसैले दुवै फरक बिन्दु हुन्।"
  },
  {
    id: 10,
    question: "उद्गम बिन्दु O(0, 0) बाट ६ एकाइ बायाँ र ४ एकाइ माथि पर्ने बिन्दुको निर्देशाङ्क कुन हो ?",
    options: [
      "(6, 4)",
      "(-6, 4)",
      "(6, -4)",
      "(-6, -4)"
    ],
    correct: 1,
    explanation: "बायाँ ६ एकाइ भन्नाले x = -6 र माथि ४ एकाइ भन्नाले y = 4, तसर्थ निर्देशाङ्क (-6, 4) हुन्छ।"
  }
];

let ch18UserAnswers = {};

function renderCh18Quiz() {
  const container = document.getElementById('ch18-quiz-container');
  if (!container) return;

  let html = '';
  ch18QuizQuestions.forEach((q, idx) => {
    const answered = ch18UserAnswers.hasOwnProperty(q.id);
    const selectedOpt = ch18UserAnswers[q.id];

    html += `
      <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm space-y-3">
        <div class="flex items-start gap-3">
          <span class="w-7 h-7 rounded-xl bg-blue-100 text-blue-800 flex items-center justify-center font-bold text-xs shrink-0 mt-0.5">
            ${idx + 1}
          </span>
          <h4 class="font-bold text-slate-900 text-sm leading-relaxed">${q.question}</h4>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-2.5 pt-1">
    `;

    q.options.forEach((opt, oIdx) => {
      let optClass = 'p-3 rounded-xl border text-xs font-semibold transition cursor-pointer text-left flex items-center justify-between ';

      if (!answered) {
        optClass += 'bg-slate-50 hover:bg-blue-50/60 border-slate-200 text-slate-700';
      } else {
        if (oIdx === q.correct) {
          optClass += 'bg-emerald-50 border-emerald-400 text-emerald-800 font-bold';
        } else if (oIdx === selectedOpt) {
          optClass += 'bg-rose-50 border-rose-400 text-rose-800 font-bold';
        } else {
          optClass += 'bg-slate-50 border-slate-200 text-slate-400 opacity-60';
        }
      }

      html += `
        <button onclick="handleCh18QuizAnswer(${q.id}, ${oIdx})" ${answered ? 'disabled' : ''} class="${optClass}">
          <span>${opt}</span>
          ${answered && oIdx === q.correct ? '<span class="text-emerald-600 font-bold text-sm">✓</span>' : ''}
          ${answered && oIdx === selectedOpt && oIdx !== q.correct ? '<span class="text-rose-600 font-bold text-sm">✗</span>' : ''}
        </button>
      `;
    });

    html += '</div>';

    if (answered) {
      const isCorrect = selectedOpt === q.correct;
      html += `
        <div class="mt-2.5 p-3 rounded-xl text-xs ${isCorrect ? 'bg-emerald-50 text-emerald-900 border border-emerald-200' : 'bg-rose-50 text-rose-900 border border-rose-200'}">
          <span class="font-bold block mb-0.5">${isCorrect ? '✓ सही उत्तर !' : '✗ गलत उत्तर !'}</span>
          <p class="text-[11px] leading-relaxed">${q.explanation}</p>
        </div>
      `;
    }

    html += '</div>';
  });

  container.innerHTML = html;
  updateCh18QuizScore();
}

function handleCh18QuizAnswer(qId, optIdx) {
  if (ch18UserAnswers.hasOwnProperty(qId)) return;
  ch18UserAnswers[qId] = optIdx;
  renderCh18Quiz();
}

function updateCh18QuizScore() {
  let score = 0;
  ch18QuizQuestions.forEach(q => {
    if (ch18UserAnswers[q.id] === q.correct) {
      score++;
    }
  });

  const scoreEl = document.getElementById('ch18-quiz-score');
  if (scoreEl) {
    scoreEl.textContent = `${score} / ${ch18QuizQuestions.length}`;
  }
}

function resetCh18Quiz() {
  ch18UserAnswers = {};
  renderCh18Quiz();
}

// Expose to window for global access
window.setTabCh18 = setTabCh18;
window.switchCh18Lab = switchCh18Lab;
window.renderCartesianGrid = renderCartesianGrid;
window.handleCartesianGridClick = handleCartesianGridClick;
window.plotFromInput = plotFromInput;
window.resetCh18Plot = resetCh18Plot;
window.plotPoint = plotPoint;
window.loadShapePreset = loadShapePreset;
window.highlightQuadrant = highlightQuadrant;
window.renderCh18Quiz = renderCh18Quiz;
window.handleCh18QuizAnswer = handleCh18QuizAnswer;
window.resetCh18Quiz = resetCh18Quiz;

                // ================= CHAPTER 19: SYMMETRY & TESSELLATION JAVASCRIPT ENGINE =================

// 1. Tab Navigation
function setTabCh19(tabName) {
  ['concepts', 'exercises', 'tiers', 'quiz'].forEach(t => {
    const view = document.getElementById('ch19-view-' + t);
    const btn = document.getElementById('ch19-tab-' + t);
    if (view) view.classList.add('hidden');
    if (btn) btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
  });
  const activeView = document.getElementById('ch19-view-' + tabName);
  const activeBtn = document.getElementById('ch19-tab-' + tabName);
  if (activeView) activeView.classList.remove('hidden');
  if (activeBtn) activeBtn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';

  if (tabName === 'concepts') {
    renderSymmetryShape();
  } else if (tabName === 'quiz') {
    renderCh19Quiz();
  }

  if (window.MathJax && window.MathJax.Hub && activeView) {
    window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, activeView]);
  } else if (window.renderOfflineMath) {
    window.renderOfflineMath(activeView);
  }
}

// 2. Exercise Sub-section Filter
function filterCh19Exercises(sec) {
  const allSecs = ['ex19_1', 'ex19_2', 'unit5_mixed'];
  const btns = {
    'all': document.getElementById('btn-sub-all'),
    'ex19_1': document.getElementById('btn-sub-ex19_1'),
    'ex19_2': document.getElementById('btn-sub-ex19_2'),
    'unit5_mixed': document.getElementById('btn-sub-mixed')
  };

  Object.keys(btns).forEach(k => {
    if (btns[k]) {
      btns[k].className = (k === sec) 
        ? 'ch19-sub-btn px-4 py-2 rounded-xl text-xs font-bold bg-blue-600 text-white shadow-sm transition'
        : 'ch19-sub-btn px-4 py-2 rounded-xl text-xs font-bold bg-white text-slate-700 hover:bg-slate-200 transition';
    }
  });

  allSecs.forEach(s => {
    const el = document.getElementById('sec-ch19-' + s);
    if (el) {
      el.classList.toggle('hidden', sec !== 'all' && sec !== s);
    }
  });
}

// 3. Interactive Lab Mode Switcher
function switchCh19Lab(mode) {
  const modes = ['symmetry', 'tessellation', 'mirror'];
  modes.forEach(m => {
    const el = document.getElementById('ch19-lab-mode-' + m);
    const btn = document.getElementById('ch19-lab-btn-' + m);
    if (el) el.classList.toggle('hidden', m !== mode);
    if (btn) {
      btn.className = (m === mode)
        ? 'px-4 py-2 rounded-xl text-xs font-bold bg-blue-600 text-white shadow-md transition'
        : 'px-4 py-2 rounded-xl text-xs font-bold text-slate-300 hover:text-white transition';
    }
  });

  if (mode === 'symmetry') {
    renderSymmetryShape();
  } else if (mode === 'tessellation') {
    renderTessellation();
  } else if (mode === 'mirror') {
    initMirrorGrid();
  }
}

// ================= MODE 1: SYMMETRY EXPLORER =================
let currentSymShape = 'equilateral';
let showAllSymLines = true;

const symShapeData = {
  equilateral: {
    name: 'समबाहु त्रिभुज (Equilateral Triangle)',
    badge: '३ वटा अक्ष',
    desc: 'यसका तीनवटै भुजाहरू बराबर हुन्छन्। प्रत्येक शीर्षबिन्दुबाट विपरीत भुजाको मध्यबिन्दुमा खिचेको रेखाले त्रिभुजलाई दुई समान भागमा विभाजन गर्छ।',
    vert: '१ वटा (ठाडो)',
    diag: '२ वटा (छड्के)',
    rot: '३ (१२०°)',
    tip: '💡 नियमित बहुभुज (Regular Polygon) का जतिवटा भुजा हुन्छन्, त्यति नै वटा सममिति रेखा हुन्छन्!',
    lines: 3,
    render: function(gShape, gLines) {
      // Triangle path
      const p1 = [200, 50], p2 = [70, 275], p3 = [330, 275];
      gShape.innerHTML = `<polygon points="${p1[0]},${p1[1]} ${p2[0]},${p2[1]} ${p3[0]},${p3[1]}" fill="rgba(59, 130, 246, 0.25)" stroke="#38bdf8" stroke-width="3" stroke-linejoin="round"/>`;
      if (showAllSymLines) {
        gLines.innerHTML = `
          <!-- Line 1: Top to base midpoint -->
          <line x1="200" y1="20" x2="200" y2="305" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
          <!-- Line 2: P2 to opposite mid (265, 162.5) -->
          <line x1="45" y1="290" x2="285" y2="145" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
          <!-- Line 3: P3 to opposite mid (135, 162.5) -->
          <line x1="355" y1="290" x2="115" y2="145" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
          <!-- Center point -->
          <circle cx="200" cy="200" r="4" fill="#fbbf24"/>
        `;
      }
    }
  },
  isosceles: {
    name: 'समद्विबाहु त्रिभुज (Isosceles Triangle)',
    badge: '१ वटा अक्ष',
    desc: 'दुई बराबर भुजाहरूको साझा शीर्षबिन्दुबाट आधारको मध्यबिन्दु जोड्ने लम्ब रेखा नै यसको एकमात्र सममिति अक्ष हो।',
    vert: '१ वटा (ठाडो)',
    diag: '० वटा',
    rot: '१ (३६०°)',
    tip: '💡 केवल दुई भुजा बराबर भएकाले अन्य शीर्षबिन्दुबाट खिचेका रेखाहरूले सममिति दिँदैनन्।',
    lines: 1,
    render: function(gShape, gLines) {
      const p1 = [200, 45], p2 = [100, 280], p3 = [300, 280];
      gShape.innerHTML = `<polygon points="${p1[0]},${p1[1]} ${p2[0]},${p2[1]} ${p3[0]},${p3[1]}" fill="rgba(14, 165, 233, 0.25)" stroke="#38bdf8" stroke-width="3" stroke-linejoin="round"/>`;
      if (showAllSymLines) {
        gLines.innerHTML = `
          <line x1="200" y1="20" x2="200" y2="310" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
        `;
      }
    }
  },
  scalene: {
    name: 'विषमबाहु त्रिभुज (Scalene Triangle)',
    badge: '० वटा (कुनै छैन)',
    desc: 'कुनै पनि भुजा वा कोण बराबर हुँदैनन्। यसलाई कुनै पनि रेखाबाट दोब्य्राउँदा दुवै भागहरू खप्टिँदैनन्।',
    vert: '० वटा',
    diag: '० वटा',
    rot: '१ (३६०°)',
    tip: '💡 विषमबाहु त्रिभुजमा रेखीय सममिति रेखा हुँदैन!',
    lines: 0,
    render: function(gShape, gLines) {
      const p1 = [160, 55], p2 = [60, 275], p3 = [340, 240];
      gShape.innerHTML = `<polygon points="${p1[0]},${p1[1]} ${p2[0]},${p2[1]} ${p3[0]},${p3[1]}" fill="rgba(244, 63, 94, 0.2)" stroke="#fb7185" stroke-width="3" stroke-linejoin="round"/>`;
      gLines.innerHTML = `
        <text x="200" y="170" fill="#f43f5e" font-size="14" font-weight="bold" text-anchor="middle">❌ कुनै सममिति रेखा छैन</text>
      `;
    }
  },
  square: {
    name: 'वर्ग (Square)',
    badge: '४ वटा अक्ष',
    desc: 'वर्गका चारवटै भुजा र चारवटै कोण बराबर हुन्छन्। विपरीत भुजाका मध्यबिन्दु जोड्ने २ रेखा र २ वटा विकर्ण गरी जम्मा ४ वटा सममिति अक्ष हुन्छन्।',
    vert: '१ ठाडो + १ तेर्सो (२ अक्षीय)',
    diag: '२ वटा (विकर्ण)',
    rot: '४ (९०°)',
    tip: '💡 वर्गमा अक्षीय र विकर्ण दुवै गरी कुल ४ वटा सममिति रेखा हुन्छन्!',
    lines: 4,
    render: function(gShape, gLines) {
      gShape.innerHTML = `<rect x="90" y="60" width="220" height="220" rx="4" fill="rgba(16, 185, 129, 0.25)" stroke="#34d399" stroke-width="3"/>`;
      if (showAllSymLines) {
        gLines.innerHTML = `
          <!-- Vertical -->
          <line x1="200" y1="30" x2="200" y2="310" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
          <!-- Horizontal -->
          <line x1="60" y1="170" x2="340" y2="170" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
          <!-- Diagonal 1 -->
          <line x1="70" y1="40" x2="330" y2="300" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
          <!-- Diagonal 2 -->
          <line x1="70" y1="300" x2="330" y2="40" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
        `;
      }
    }
  },
  rectangle: {
    name: 'आयत (Rectangle)',
    badge: '२ वटा अक्ष',
    desc: 'विपरीत भुजाहरूका मध्यबिन्दु जोड्ने १ ठाडो र १ तेर्सो रेखा मात्र सममिति रेखा हुन्। विकर्णबाट पट्याउँदा कुनाहरू बाहिर निस्कने हुँदा विकर्ण सममिति रेखा बन्दैन!',
    vert: '१ ठाडो + १ तेर्सो',
    diag: '० वटा (विकर्ण सममिति होइन)',
    rot: '२ (१८०°)',
    tip: '⚠️ ध्यान दिनुहोस्: आयतलाई विकर्णबाट पट्याउँदा कुनाहरू ठ्याक्कै खप्टिँदैनन्!',
    lines: 2,
    render: function(gShape, gLines) {
      gShape.innerHTML = `<rect x="60" y="85" width="280" height="170" rx="4" fill="rgba(168, 85, 247, 0.25)" stroke="#c084fc" stroke-width="3"/>`;
      if (showAllSymLines) {
        gLines.innerHTML = `
          <!-- Vertical -->
          <line x1="200" y1="45" x2="200" y2="295" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
          <!-- Horizontal -->
          <line x1="30" y1="170" x2="370" y2="170" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
          <!-- Failed Diagonal indicator -->
          <line x1="60" y1="85" x2="340" y2="255" stroke="rgba(244, 63, 94, 0.3)" stroke-width="1.5" stroke-dasharray="3,3"/>
          <text x="300" y="110" fill="#fb7185" font-size="10">विकर्ण ≠ अक्ष</text>
        `;
      }
    }
  },
  rhombus: {
    name: 'समचतुर्भुज (Rhombus)',
    badge: '२ वटा अक्ष',
    desc: 'समचतुर्भुजका चारवटै भुजाहरू बराबर हुन्छन्। यसका दुईवटा विकर्णहरू नै यसका २ वटा सममिति रेखा हुन्। भुजाहरूका मध्यबिन्दु जोड्ने रेखा सममिति हुँदैन।',
    vert: '१ वटा (ठाडो विकर्ण)',
    diag: '१ वटा (तेर्सो विकर्ण)',
    rot: '२ (१८०°)',
    tip: '💡 समचतुर्भुजमा विकर्णहरू सममिति रेखा हुन्छन् तर मध्यबिन्दु जोड्ने रेखा हुँदैनन् (आयतको उल्टो)!',
    lines: 2,
    render: function(gShape, gLines) {
      gShape.innerHTML = `<polygon points="200,45 330,170 200,295 70,170" fill="rgba(245, 158, 11, 0.25)" stroke="#fbbf24" stroke-width="3"/>`;
      if (showAllSymLines) {
        gLines.innerHTML = `
          <!-- Vertical diagonal -->
          <line x1="200" y1="20" x2="200" y2="320" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
          <!-- Horizontal diagonal -->
          <line x1="45" y1="170" x2="355" y2="170" stroke="#f43f5e" stroke-width="2.5" stroke-dasharray="6,4"/>
        `;
      }
    }
  },
  hexagon: {
    name: 'नियमित षट्कोण (Regular Hexagon)',
    badge: '६ वटा अक्ष',
    desc: 'यसका ६ वटा बराबर भुजाहरू हुन्छन्। ३ वटा विपरीत शीर्षबिन्दु जोड्ने विकर्णहरू र ३ वटा विपरीत भुजाका मध्यबिन्दु जोड्ने लम्ब रेखाहरू गरी कुल ६ वटा अक्ष हुन्छन्।',
    vert: '३ विकर्ण',
    diag: '३ मध्यबिन्दु लम्ब',
    rot: '६ (६०°)',
    tip: '💡 नियमित षट्कोणले मौरीको घारजस्तै बिना कुनै खाली ठाउँ टेसेलेसन बनाउँछ!',
    lines: 6,
    render: function(gShape, gLines) {
      const cx = 200, cy = 170, r = 115;
      let pts = [];
      for (let i = 0; i < 6; i++) {
        let ang = (i * 60 - 30) * Math.PI / 180;
        pts.push(`${cx + r * Math.cos(ang)},${cy + r * Math.sin(ang)}`);
      }
      gShape.innerHTML = `<polygon points="${pts.join(' ')}" fill="rgba(99, 102, 241, 0.25)" stroke="#818cf8" stroke-width="3"/>`;
      if (showAllSymLines) {
        let linesHtml = '';
        for (let i = 0; i < 6; i++) {
          let ang = (i * 30) * Math.PI / 180;
          let x1 = cx - 145 * Math.cos(ang), y1 = cy - 145 * Math.sin(ang);
          let x2 = cx + 145 * Math.cos(ang), y2 = cy + 145 * Math.sin(ang);
          linesHtml += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#f43f5e" stroke-width="2" stroke-dasharray="6,4"/>`;
        }
        gLines.innerHTML = linesHtml;
      }
    }
  },
  circle: {
    name: 'वृत्त (Circle)',
    badge: 'अनन्त (∞) अक्ष',
    desc: 'केन्द्रबिन्दु भएर जाने जुनसुकै सीधा रेखा (व्यास) ले वृत्तलाई दुई बराबर अर्धवृत्तमा बाँड्दछ। त्यसैले वृत्तमा अनन्त सममिति रेखाहरू हुन्छन्।',
    vert: 'अनन्त (ठाडो)',
    diag: 'अनन्त (छड्के)',
    rot: 'अनन्त (कुनै पनि कोण)',
    tip: '💡 वृत्त संसारको सबैभन्दा पूर्ण सममितीय २D ज्यामितीय आकृति हो!',
    lines: 999,
    render: function(gShape, gLines) {
      gShape.innerHTML = `<circle cx="200" cy="170" r="110" fill="rgba(20, 184, 166, 0.25)" stroke="#2dd4bf" stroke-width="3"/>`;
      if (showAllSymLines) {
        let linesHtml = '';
        for (let i = 0; i < 8; i++) {
          let ang = (i * 22.5) * Math.PI / 180;
          let x1 = 200 - 135 * Math.cos(ang), y1 = 170 - 135 * Math.sin(ang);
          let x2 = 200 + 135 * Math.cos(ang), y2 = 170 + 135 * Math.sin(ang);
          linesHtml += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#f43f5e" stroke-width="1.8" stroke-dasharray="5,4" opacity="0.85"/>`;
        }
        linesHtml += `<circle cx="200" cy="170" r="5" fill="#fbbf24"/>`;
        gLines.innerHTML = linesHtml;
      }
    }
  }
};

function selectSymmetryShape(key) {
  currentSymShape = key;
  document.querySelectorAll('.sym-shape-btn').forEach(b => {
    b.className = 'sym-shape-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-700 text-slate-200 hover:bg-slate-600 transition';
  });
  const btn = document.getElementById('btn-sym-' + key);
  if (btn) btn.className = 'sym-shape-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-blue-600 text-white transition';
  renderSymmetryShape();
}

function toggleSymmetryLine() {
  showAllSymLines = !showAllSymLines;
  renderSymmetryShape();
}

function renderSymmetryShape() {
  const gShape = document.getElementById('sym-shape-container');
  const gLines = document.getElementById('sym-lines-container');
  if (!gShape || !gLines) return;
  gShape.innerHTML = '';
  gLines.innerHTML = '';

  const data = symShapeData[currentSymShape] || symShapeData['equilateral'];
  data.render(gShape, gLines);

  const tEl = document.getElementById('sym-info-title');
  const bEl = document.getElementById('sym-info-badge');
  const dEl = document.getElementById('sym-info-desc');
  const vEl = document.getElementById('sym-val-vert');
  const dgEl = document.getElementById('sym-val-diag');
  const rEl = document.getElementById('sym-val-rot');
  const tipEl = document.getElementById('sym-info-tip');

  if (tEl) tEl.textContent = data.name;
  if (bEl) bEl.textContent = data.badge;
  if (dEl) dEl.textContent = data.desc;
  if (vEl) vEl.textContent = data.vert;
  if (dgEl) dgEl.textContent = data.diag;
  if (rEl) rEl.textContent = data.rot;
  if (tipEl) tipEl.innerHTML = `<span>💡</span><span>${data.tip.replace('💡 ', '')}</span>`;

  if (window.MathJax && window.MathJax.Hub) {
    const card = document.getElementById('sym-info-card');
    if (card) window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, card]);
  }
}

// ================= MODE 2: TESSELLATION STUDIO =================
let currentTessShape = 'square';

const tessThemes = {
  emerald: { bg1: '#047857', bg2: '#059669', bg3: '#10b981', stroke: '#a7f3d0' },
  cyber:   { bg1: '#1d4ed8', bg2: '#2563eb', bg3: '#3b82f6', stroke: '#93c5fd' },
  warm:    { bg1: '#b45309', bg2: '#d97706', bg3: '#f59e0b', stroke: '#fde68a' },
  duo:     { bg1: '#0f172a', bg2: '#334155', bg3: '#64748b', stroke: '#e2e8f0' }
};

function selectTessShape(key) {
  currentTessShape = key;
  document.querySelectorAll('.tess-btn').forEach(b => {
    b.className = 'tess-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-700 text-slate-200 hover:bg-slate-600 transition';
  });
  const btn = document.getElementById('btn-tess-' + key);
  if (btn) {
    if (key === 'pentagon') {
      btn.className = 'tess-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-rose-600 text-white transition';
    } else {
      btn.className = 'tess-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-teal-600 text-white transition';
    }
  }
  renderTessellation();
}

function renderTessellation() {
  const gTiles = document.getElementById('tess-tiles-group');
  const gOverlay = document.getElementById('tess-overlay-group');
  if (!gTiles || !gOverlay) return;
  gTiles.innerHTML = '';
  gOverlay.innerHTML = '';

  const themeKey = (document.getElementById('ch19-tess-theme') || {}).value || 'emerald';
  const theme = tessThemes[themeKey] || tessThemes['emerald'];

  const tTitle = document.getElementById('tess-info-title');
  const tBadge = document.getElementById('tess-status-badge');
  const tDesc = document.getElementById('tess-info-desc');
  const tAngle = document.getElementById('tess-angle-each');
  const tCount = document.getElementById('tess-tile-count');
  const tSum = document.getElementById('tess-angle-sum');
  const tReason = document.getElementById('tess-reason-box');

  if (currentTessShape === 'square') {
    if (tTitle) tTitle.textContent = 'वर्गाकार टेसेलेसन (Square Tiling)';
    if (tBadge) {
      tBadge.textContent = 'सफल टेसेलेसन ✓';
      tBadge.className = 'px-2.5 py-0.5 rounded-full text-xs font-black bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
    }
    if (tDesc) tDesc.textContent = 'वर्गका चारवटै कोणहरू ९०° हुन्छन्। एउटा साझा शीर्षबिन्दुमा ४ वटा वर्गहरू जोडिँदा कोणहरूको कुल योग ठ्याक्कै ३६०° हुन्छ।';
    if (tAngle) tAngle.textContent = '९०°';
    if (tCount) tCount.textContent = '४ वटा';
    if (tSum) tSum.textContent = '४ × ९०° = ३६०°';
    if (tReason) tReason.textContent = 'कुनै खाली ठाउँ नछाडी र नखप्टाई सम्पूर्ण समतल सतह पूर्ण रूपमा ढाकिएको छ।';

    // Render 7x5 square grid
    const size = 50;
    let tilesHtml = '';
    for (let r = 0; r < 7; r++) {
      for (let c = 0; c < 9; c++) {
        let x = c * size - 15;
        let y = r * size - 5;
        let col = ((r + c) % 2 === 0) ? theme.bg1 : theme.bg2;
        tilesHtml += `<rect x="${x}" y="${y}" width="${size}" height="${size}" fill="${col}" stroke="${theme.stroke}" stroke-width="1.5"/>`;
      }
    }
    gTiles.innerHTML = tilesHtml;

    // Highlight one shared vertex
    gOverlay.innerHTML = `
      <circle cx="185" cy="145" r="7" fill="#f43f5e"/>
      <circle cx="185" cy="145" r="14" fill="none" stroke="#f43f5e" stroke-width="2" stroke-dasharray="3,3"/>
      <text x="185" y="125" fill="#f43f5e" font-size="11" font-weight="bold" text-anchor="middle">साझा शीर्षबिन्दु (३६०°)</text>
    `;

  } else if (currentTessShape === 'triangle') {
    if (tTitle) tTitle.textContent = 'समबाहु त्रिभुजाकार टेसेलेसन (Equilateral Triangle Tiling)';
    if (tBadge) {
      tBadge.textContent = 'सफल टेसेलेसन ✓';
      tBadge.className = 'px-2.5 py-0.5 rounded-full text-xs font-black bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
    }
    if (tDesc) tDesc.textContent = 'समबाहु त्रिभुजको प्रत्येक भित्री कोण ६०° हुन्छ। साझा शीर्षबिन्दुमा ६ वटा त्रिभुजहरू मिल्दा ६ × ६०° = ३६०° भई सतह भरिन्छ।';
    if (tAngle) tAngle.textContent = '६०°';
    if (tCount) tCount.textContent = '६ वटा';
    if (tSum) tSum.textContent = '६ × ६०° = ३६०°';
    if (tReason) tReason.textContent = 'सुल्टो र उल्टो त्रिभुजहरू पालैपालो जोडेर आकर्षक नियमित टेसेलेसन बन्दछ।';

    const s = 60, h = s * Math.sqrt(3) / 2;
    let tilesHtml = '';
    for (let row = -1; row < 7; row++) {
      let y0 = row * h;
      let y1 = (row + 1) * h;
      for (let col = -1; col < 9; col++) {
        let x0 = col * s + (row % 2) * (s / 2);
        let x1 = x0 + s;
        let xMid = x0 + s / 2;
        // Upward triangle
        let col1 = ((row + col) % 3 === 0) ? theme.bg1 : ((row + col) % 3 === 1) ? theme.bg2 : theme.bg3;
        tilesHtml += `<polygon points="${x0},${y1} ${x1},${y1} ${xMid},${y0}" fill="${col1}" stroke="${theme.stroke}" stroke-width="1.2"/>`;
        // Downward triangle
        let col2 = ((row + col + 1) % 3 === 0) ? theme.bg1 : theme.bg2;
        tilesHtml += `<polygon points="${x0},${y1} ${xMid},${y0} ${x0 - s/2},${y0}" fill="${col2}" stroke="${theme.stroke}" stroke-width="1.2"/>`;
      }
    }
    gTiles.innerHTML = tilesHtml;

    // Highlight shared vertex with 6 triangles
    gOverlay.innerHTML = `
      <circle cx="210" cy="156" r="6" fill="#fbbf24"/>
      <text x="210" y="140" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">६ वटा त्रिभुजको भेट (३६०°)</text>
    `;

  } else if (currentTessShape === 'hexagon') {
    if (tTitle) tTitle.textContent = 'नियमित षट्कोणीय टेसेलेसन (Honeycomb Hexagon)';
    if (tBadge) {
      tBadge.textContent = 'सफल टेसेलेसन ✓';
      tBadge.className = 'px-2.5 py-0.5 rounded-full text-xs font-black bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
    }
    if (tDesc) tDesc.textContent = 'नियमित षट्कोणको प्रत्येक भित्री कोण १२०° हुन्छ। साझा शीर्षबिन्दुमा ३ वटा षट्कोण मिल्दा ३ × १२०° = ३६०° पुग्छ। मौरीको घार यसको प्राकृतिक उदाहरण हो।';
    if (tAngle) tAngle.textContent = '१२०°';
    if (tCount) tCount.textContent = '३ वटा';
    if (tSum) tSum.textContent = '३ × १२०° = ३६०°';
    if (tReason) tReason.textContent = 'न्यूनतम परिधिमा अधिकतम क्षेत्रफल घेर्ने भएकाले प्रकृतिमा मौरीले यही ढाँचा प्रयोग गर्छ।';

    const r = 38;
    const w = Math.sqrt(3) * r;
    const h = 2 * r * 0.75;
    let tilesHtml = '';
    for (let row = -1; row < 7; row++) {
      for (let col = -1; col < 8; col++) {
        let cx = col * w + ((row % 2) * (w / 2));
        let cy = row * h;
        let pts = [];
        for (let i = 0; i < 6; i++) {
          let ang = (i * 60 + 30) * Math.PI / 180;
          pts.push(`${cx + r * Math.cos(ang)},${cy + r * Math.sin(ang)}`);
        }
        let colShade = ((row + col) % 3 === 0) ? theme.bg1 : ((row + col) % 3 === 1) ? theme.bg2 : theme.bg3;
        tilesHtml += `<polygon points="${pts.join(' ')}" fill="${colShade}" stroke="${theme.stroke}" stroke-width="1.8"/>`;
      }
    }
    gTiles.innerHTML = tilesHtml;

    // Highlight shared vertex of 3 hexagons
    gOverlay.innerHTML = `
      <circle cx="214" cy="142" r="6" fill="#f43f5e"/>
      <text x="214" y="125" fill="#f43f5e" font-size="11" font-weight="bold" text-anchor="middle">३ वटा षट्कोण (३ × १२०° = ३६०°)</text>
    `;

  } else if (currentTessShape === 'brick') {
    if (tTitle) tTitle.textContent = 'आयताकार इँटाको टेसेलेसन (Brick Running Bond)';
    if (tBadge) {
      tBadge.textContent = 'व्यावहारिक टेसेलेसन ✓';
      tBadge.className = 'px-2.5 py-0.5 rounded-full text-xs font-black bg-blue-500/20 text-blue-300 border border-blue-500/30';
    }
    if (tDesc) tDesc.textContent = 'घरको पर्खाल लगाउँदा आयताकार इँटाहरूलाई आधा-आधा खप्टाएर (Running bond) बिछ्याइन्छ। यसले पर्खाललाई बलियो बनाउँछ र खाली ठाउँ छोड्दैन।';
    if (tAngle) tAngle.textContent = '९०°';
    if (tCount) tCount.textContent = '४ वा ३ वटा';
    if (tSum) tSum.textContent = '२ × ९०° + १८०° = ३६०°';
    if (tReason) tReason.textContent = 'इँटाको पर्खाल निर्माणमा प्रयोग हुने विश्वप्रसिद्ध इन्जिनियरिङ टेसेलेसन।';

    const bw = 70, bh = 32;
    let tilesHtml = '';
    for (let r = 0; r < 11; r++) {
      let offset = (r % 2 === 0) ? 0 : -bw / 2;
      for (let c = -1; c < 8; c++) {
        let x = c * bw + offset;
        let y = r * bh;
        let col = ((r + c) % 2 === 0) ? '#b45309' : '#d97706';
        tilesHtml += `<rect x="${x}" y="${y}" width="${bw}" height="${bh}" fill="${col}" stroke="#fde68a" stroke-width="1.5"/>`;
      }
    }
    gTiles.innerHTML = tilesHtml;

  } else if (currentTessShape === 'pentagon') {
    if (tTitle) tTitle.textContent = 'नियमित पञ्चकोण (Regular Pentagon Test)';
    if (tBadge) {
      tBadge.textContent = 'टेसेलेसन असम्भव ❌';
      tBadge.className = 'px-2.5 py-0.5 rounded-full text-xs font-black bg-rose-500/20 text-rose-300 border border-rose-500/30';
    }
    if (tDesc) tDesc.textContent = 'नियमित पञ्चकोणको भित्री कोण १०८° हुन्छ। ३ वटा जोड्दा ३२४° मात्र हुन्छ (३६° खाली ठाउँ बाँकी रहन्छ)। ४ वटा जोड्दा ४३२° भई खप्टिन्छ!';
    if (tAngle) tAngle.textContent = '१०८°';
    if (tCount) tCount.textContent = '३ वटा जोड्दा';
    if (tSum) tSum.textContent = '३ × १०८° = ३२४° (< ३६०°)';
    if (tReason) tReason.textContent = '३६०° लाई १०८° ले भाग गर्दा ३.३३ आउँछ (पूर्ण सङ्ख्या नहुने)। तसर्थ पञ्चकोणले टेसेलेसन बनाउन सक्दैन!';

    // Render 3 regular pentagons meeting at center with a visible gap
    const cx = 210, cy = 175, r = 75;
    let tilesHtml = '';
    const angles = [0, 108, 216];
    angles.forEach((startDeg, idx) => {
      let pts = [];
      for (let i = 0; i < 5; i++) {
        let a = (startDeg + i * 72 - 54) * Math.PI / 180;
        pts.push(`${cx + r * Math.cos(a)},${cy + r * Math.sin(a)}`);
      }
      tilesHtml += `<polygon points="${pts.join(' ')}" fill="rgba(244, 63, 94, 0.4)" stroke="#fb7185" stroke-width="2.5"/>`;
    });

    // Render GAP sector
    tilesHtml += `
      <!-- Gap arc -->
      <path d="M 210 175 L 285 175 A 75 75 0 0 1 270 235 Z" fill="rgba(251, 191, 36, 0.4)" stroke="#f59e0b" stroke-width="2"/>
    `;
    gTiles.innerHTML = tilesHtml;

    gOverlay.innerHTML = `
      <circle cx="210" cy="175" r="7" fill="#f43f5e"/>
      <text x="210" y="80" fill="#fb7185" font-size="13" font-weight="black" text-anchor="middle">❌ खाली ठाउँ (३६° Gap)</text>
      <text x="210" y="98" fill="#cbd5e1" font-size="11" text-anchor="middle">३ वटा पञ्चकोण = ३२४° (३६०° पुगेन)</text>
    `;
  }
}

// ================= MODE 3: MIRROR REFLECTION GRID =================
const GRID_ROWS = 8;
const GRID_COLS = 8; // 0..3 Left, 4..7 Right
let mirrorGridState = []; // 8x8 boolean

function initMirrorGrid() {
  loadMirrorPreset('rocket');
}

function clearMirrorGrid() {
  mirrorGridState = Array(GRID_ROWS).fill(null).map(() => Array(GRID_COLS).fill(false));
  renderMirrorGridDom();
  setMirrorFeedback('ग्रिड खाली गरियो। नयाँ आकृति कोर्नुहोस् वा नमुना छान्नुहोस्।', 'text-slate-300');
}

function loadMirrorPreset(name) {
  mirrorGridState = Array(GRID_ROWS).fill(null).map(() => Array(GRID_COLS).fill(false));

  if (name === 'rocket') {
    // Left side rocket
    mirrorGridState[0][3] = true;
    mirrorGridState[1][3] = true;
    mirrorGridState[2][3] = true; mirrorGridState[2][2] = true;
    mirrorGridState[3][3] = true; mirrorGridState[3][2] = true;
    mirrorGridState[4][3] = true; mirrorGridState[4][2] = true;
    mirrorGridState[5][3] = true; mirrorGridState[5][2] = true; mirrorGridState[5][1] = true;
    mirrorGridState[6][3] = true; mirrorGridState[6][2] = true; mirrorGridState[6][0] = true;
    mirrorGridState[7][3] = true; mirrorGridState[7][1] = true;
  } else if (name === 'heart') {
    mirrorGridState[1][2] = true; mirrorGridState[1][1] = true;
    mirrorGridState[2][3] = true; mirrorGridState[2][2] = true; mirrorGridState[2][1] = true; mirrorGridState[2][0] = true;
    mirrorGridState[3][3] = true; mirrorGridState[3][2] = true; mirrorGridState[3][1] = true; mirrorGridState[3][0] = true;
    mirrorGridState[4][3] = true; mirrorGridState[4][2] = true; mirrorGridState[4][1] = true;
    mirrorGridState[5][3] = true; mirrorGridState[5][2] = true;
    mirrorGridState[6][3] = true;
  } else if (name === 'tree') {
    mirrorGridState[0][3] = true;
    mirrorGridState[1][3] = true; mirrorGridState[1][2] = true;
    mirrorGridState[2][3] = true; mirrorGridState[2][2] = true;
    mirrorGridState[3][3] = true; mirrorGridState[3][2] = true; mirrorGridState[3][1] = true;
    mirrorGridState[4][3] = true; mirrorGridState[4][2] = true; mirrorGridState[4][1] = true; mirrorGridState[4][0] = true;
    mirrorGridState[5][3] = true; mirrorGridState[5][2] = true;
    mirrorGridState[6][3] = true;
    mirrorGridState[7][3] = true;
  } else if (name === 'arrow') {
    mirrorGridState[1][3] = true;
    mirrorGridState[2][3] = true; mirrorGridState[2][2] = true;
    mirrorGridState[3][3] = true; mirrorGridState[3][2] = true; mirrorGridState[3][1] = true; mirrorGridState[3][0] = true;
    mirrorGridState[4][3] = true; mirrorGridState[4][2] = true; mirrorGridState[4][1] = true; mirrorGridState[4][0] = true;
    mirrorGridState[5][3] = true; mirrorGridState[5][2] = true;
    mirrorGridState[6][3] = true;
  }

  renderMirrorGridDom();
  setMirrorFeedback('बायाँ भाग तयार छ। दायाँतर्फ क्लिक गरी ऐना प्रतिबिम्ब पूरा गर्नुहोस्!', 'text-cyan-300');
}

function renderMirrorGridDom() {
  const container = document.getElementById('ch19-mirror-grid');
  if (!container) return;
  container.innerHTML = '';
  container.style.display = 'grid';
  container.style.gridTemplateColumns = `repeat(${GRID_COLS}, 32px)`;
  container.style.gap = '4px';
  container.style.width = 'fit-content';

  for (let r = 0; r < GRID_ROWS; r++) {
    for (let c = 0; c < GRID_COLS; c++) {
      const cell = document.createElement('button');
      cell.className = 'w-8 h-8 rounded text-xs font-bold transition flex items-center justify-center cursor-pointer ';
      
      const isLeft = c < 4;
      const isFilled = mirrorGridState[r][c];

      // Mirror line border indicator between col 3 and col 4
      if (c === 3) {
        cell.classList.add('border-r-2', 'border-rose-500');
      } else {
        cell.classList.add('border', 'border-slate-800');
      }

      if (isLeft) {
        cell.className += isFilled ? 'bg-blue-600 text-white' : 'bg-slate-900/60 hover:bg-slate-800 text-transparent';
        cell.onclick = () => toggleGridTile(r, c);
      } else {
        cell.className += isFilled ? 'bg-emerald-500 text-white shadow' : 'bg-slate-900/80 hover:bg-slate-700 text-transparent';
        cell.onclick = () => toggleGridTile(r, c);
      }

      container.appendChild(cell);
    }
  }
}

function toggleGridTile(r, c) {
  mirrorGridState[r][c] = !mirrorGridState[r][c];
  renderMirrorGridDom();
}

function autoCompleteMirror() {
  for (let r = 0; r < GRID_ROWS; r++) {
    for (let c = 0; c < 4; c++) {
      const mirrorCol = 7 - c;
      mirrorGridState[r][mirrorCol] = mirrorGridState[r][c];
    }
  }
  renderMirrorGridDom();
  setMirrorFeedback('✨ ऐना प्रतिबिम्ब स्वतः पूरा भयो! दुवै भाग दुरुस्त सममितीय छन्।', 'text-emerald-400');
}

function checkMirrorSymmetry() {
  let errors = 0;
  for (let r = 0; r < GRID_ROWS; r++) {
    for (let c = 0; c < 4; c++) {
      const mirrorCol = 7 - c;
      if (mirrorGridState[r][c] !== mirrorGridState[r][mirrorCol]) {
        errors++;
      }
    }
  }

  if (errors === 0) {
    setMirrorFeedback('🎉 उत्कृष्ट! तपाईंको चित्र पूर्ण रूपमा सममितीय छ (Symmetric Match)!', 'text-emerald-400 font-extrabold text-sm');
  } else {
    setMirrorFeedback(`⚠️ अझै ${errors} ठाउँमा मिलेको छैन। डट रेखाबाट दायाँ र बायाँको दूरी पुनः गन्नुहोस्!`, 'text-amber-400 font-bold');
  }
}

function setMirrorFeedback(msg, colorClass) {
  const fb = document.getElementById('mirror-feedback');
  if (fb) {
    fb.textContent = msg;
    fb.className = `mt-3 text-xs font-bold ${colorClass} min-h-[20px] text-center transition`;
  }
}

// ================= 4. SELF-ASSESSMENT QUIZ ENGINE =================
const ch19QuizQuestions = [
  {
    id: 'q1',
    question: 'समबाहु त्रिभुज (Equilateral Triangle) मा कतिवटा सममिति रेखा हुन्छन्?',
    options: ['१ वटा', '२ वटा', '३ वटा', '४ वटा'],
    correct: 2,
    explanation: 'समबाहु त्रिभुजका तीनवटै भुजाहरू बराबर हुने भएकाले यसका प्रत्येक शीर्षबिन्दुबाट विपरीत भुजाको मध्यबिन्दुमा ३ वटा सममिति रेखा खिच्न सकिन्छ।'
  },
  {
    id: 'q2',
    question: 'तलका मध्ये कुन अङ्ग्रेजी क्यापिटल अक्षरमा ठाडो र तेर्सो दुवै सममिति रेखा हुन्छ?',
    options: ['अक्षर A', 'अक्षर M', 'अक्षर H', 'अक्षर E'],
    correct: 2,
    explanation: 'अक्षर H लाई ठाडो र तेर्सो दुवै रेखाबाट पट्याउँदा दुरुस्त खप्टिन्छ। अक्षर A र M मा ठाडो मात्र र E मा तेर्सो मात्र हुन्छ।'
  },
  {
    id: 'q3',
    question: 'आयत (Rectangle) मा कतिवटा सममिति रेखा हुन्छन्?',
    options: ['४ वटा', '२ वटा', '१ वटा', 'शून्य (हुँदैन)'],
    correct: 1,
    explanation: 'आयतका विपरीत भुजाहरूका मध्यबिन्दु जोड्ने १ ठाडो र १ तेर्सो गरी २ वटा मात्र अक्ष हुन्छन्। विकर्णबाट पट्याउँदा कुनाहरू नखप्टिने भएकाले विकर्ण सममिति रेखा हुँदैन।'
  },
  {
    id: 'q4',
    question: 'टेसेलेसन हुनका लागि साझा शीर्षबिन्दु (Vertex) मा बन्ने कोणहरूको योगफल कति हुनुपर्दछ?',
    options: ['१८०°', '२७०°', '३६०°', '५४०°'],
    correct: 2,
    explanation: 'समतल सतहलाई बिना खाली ठाउँ र नखप्टाई पूर्ण रूपमा ढाक्न शीर्षबिन्दु वरिपरिका भित्री कोणहरूको योग ठ्याक्कै ३६०° हुनुपर्छ।'
  },
  {
    id: 'q5',
    question: 'तलका मध्ये कुन नियमित बहुभुजले एक्लै नियमित टेसेलेसन बनाउन सक्दैन?',
    options: ['समबाहु त्रिभुज', 'वर्ग', 'नियमित पञ्चकोण', 'नियमित षट्कोण'],
    correct: 2,
    explanation: 'नियमित पञ्चकोणको प्रत्येक भित्री कोण १०८° हुन्छ र ३६०° लाई १०८° ले निःशेष भाग जाँदैन (३.३३ आउँछ)। त्यसैले पञ्चकोणले टेसेलेसन बनाउन सक्दैन।'
  },
  {
    id: 'q6',
    question: 'नियमित षट्कोणको प्रत्येक भित्री कोण १२०° हुन्छ। यसको टेसेलेसनमा एउटा शीर्षबिन्दुमा कतिवटा षट्कोण भेटिन्छन्?',
    options: ['२ वटा', '३ वटा', '४ वटा', '६ वटा'],
    correct: 1,
    explanation: '३ × १२०° = ३६०° हुने भएकाले प्रत्येक साझा शीर्षबिन्दुमा ३ वटा नियमित षट्कोणहरू आपसमा जोडिन्छन्।'
  },
  {
    id: 'q7',
    question: 'वृत्त (Circle) मा कतिवटा सममिति रेखाहरू हुन्छन्?',
    options: ['४ वटा', '३६० वटा', '१ वटा', 'अनन्त (Infinite)'],
    correct: 3,
    explanation: 'केन्द्रबिन्दु भएर जाने जुनसुकै सीधा रेखा (व्यास) ले वृत्तलाई दुई दुरुस्त आधा भागमा बाँड्ने भएकाले वृत्तमा अनन्त सममिति रेखाहरू हुन्छन्।'
  },
  {
    id: 'q8',
    question: 'नियमित अष्टकोण (१३५°) र वर्ग (९०°) मिलेर भुइँमा टेसेलेसन बन्दा साझा शीर्षबिन्दुमा कोणहरूको योग कति हुन्छ?',
    options: ['३६०° (२ अष्टकोण + १ वर्ग)', '२७०°', '४००°', '३००°'],
    correct: 0,
    explanation: 'दुईवटा अष्टकोण (२ × १३५° = २७०°) र एउटा वर्ग (९०°) जोड्दा कुल २७०° + ९०° = ३६०° पुग्ने भएकाले यिनीहरूले अर्ध-नियमित टेसेलेसन बनाउँछन्।'
  },
  {
    id: 'q9',
    question: 'कुन चतुर्भुजमा रेखीय सममिति रेखा हुँदैन (० वटा हुन्छ)?',
    options: ['वर्ग', 'आयत', 'समचतुर्भुज', 'साधारण समानान्तर चतुर्भुज'],
    correct: 3,
    explanation: 'साधारण समानान्तर चतुर्भुज (Parallelogram) लाई कुनै पनि ठाडो, तेर्सो वा विकर्ण रेखाबाट दोब्य्राउँदा भुजाहरू ठ्याक्कै खप्टिँदैनन्। त्यसैले यसमा रेखीय सममिति हुँदैन।'
  },
  {
    id: 'q10',
    question: 'कुनै पनि n-भुजा भएको नियमित बहुभुजमा सममिति रेखाको सङ्ख्या कति हुन्छ?',
    options: ['n - २', 'n वटा', '२n वटा', 'n / २'],
    correct: 1,
    explanation: 'नियमित बहुभुज (जस्तै समबाहु त्रिभुजमा ३, वर्गमा ४, पञ्चकोणमा ५, षट्कोणमा ६) मा सममिति रेखाको सङ्ख्या भुजाहरूको सङ्ख्या n बराबर हुन्छ।'
  }
];

let ch19UserAnswers = {};

function renderCh19Quiz() {
  const container = document.getElementById('ch19-quiz-container');
  if (!container) return;
  container.innerHTML = '';

  ch19QuizQuestions.forEach((q, idx) => {
    const answered = ch19UserAnswers.hasOwnProperty(q.id);
    const selectedOpt = ch19UserAnswers[q.id];

    const card = document.createElement('div');
    card.className = 'bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-3';

    let optionsHtml = '';
    q.options.forEach((opt, oIdx) => {
      let optClass = 'w-full text-left p-3 rounded-xl border text-xs md:text-sm font-semibold transition flex items-center justify-between ';
      if (!answered) {
        optClass += 'border-slate-200 hover:bg-slate-50 text-slate-700 cursor-pointer';
      } else {
        if (oIdx === q.correct) {
          optClass += 'border-emerald-500 bg-emerald-50 text-emerald-900 font-bold';
        } else if (oIdx === selectedOpt) {
          optClass += 'border-rose-500 bg-rose-50 text-rose-900 font-bold';
        } else {
          optClass += 'border-slate-200 text-slate-400 opacity-60';
        }
      }

      optionsHtml += `
        <button onclick="handleCh19QuizAnswer('${q.id}', ${oIdx})" ${answered ? 'disabled' : ''} class="${optClass}">
          <span>${String.fromCharCode(65 + oIdx)}. ${opt}</span>
          ${answered && oIdx === q.correct ? '<span class="text-emerald-600 font-black">✓ सही</span>' : ''}
          ${answered && oIdx === selectedOpt && oIdx !== q.correct ? '<span class="text-rose-600 font-black">✗ गलत</span>' : ''}
        </button>
      `;
    });

    let explanationHtml = '';
    if (answered) {
      explanationHtml = `
        <div class="mt-3 p-3 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-600 space-y-1">
          <strong class="text-slate-800">💡 व्याख्या:</strong> ${q.explanation}
        </div>
      `;
    }

    card.innerHTML = `
      <div class="flex items-center justify-between border-b border-slate-100 pb-2">
        <span class="text-xs font-bold text-blue-600">प्रश्न ${idx + 1} / ${ch19QuizQuestions.length}</span>
        <span class="text-[11px] font-mono text-slate-400">१ अङ्क</span>
      </div>
      <p class="font-extrabold text-sm md:text-base text-slate-800">${q.question}</p>
      <div class="space-y-2 pt-1">
        ${optionsHtml}
      </div>
      ${explanationHtml}
    `;

    container.appendChild(card);
  });
}

function handleCh19QuizAnswer(qId, optIdx) {
  if (ch19UserAnswers.hasOwnProperty(qId)) return;
  ch19UserAnswers[qId] = optIdx;

  // Calculate score
  let score = 0;
  ch19QuizQuestions.forEach(q => {
    if (ch19UserAnswers[q.id] === q.correct) {
      score++;
    }
  });

  const scoreEl = document.getElementById('ch19-quiz-score');
  if (scoreEl) {
    scoreEl.textContent = `${score} / ${ch19QuizQuestions.length}`;
  }

  renderCh19Quiz();
}

function resetCh19Quiz() {
  ch19UserAnswers = {};
  const scoreEl = document.getElementById('ch19-quiz-score');
  if (scoreEl) {
    scoreEl.textContent = `० / ${ch19QuizQuestions.length}`;
  }
  renderCh19Quiz();
}

// Expose to window for global access
window.setTabCh19 = setTabCh19;
window.filterCh19Exercises = filterCh19Exercises;
window.switchCh19Lab = switchCh19Lab;
window.selectSymmetryShape = selectSymmetryShape;
window.toggleSymmetryLine = toggleSymmetryLine;
window.renderSymmetryShape = renderSymmetryShape;
window.selectTessShape = selectTessShape;
window.renderTessellation = renderTessellation;
window.toggleGridTile = toggleGridTile;
window.clearMirrorGrid = clearMirrorGrid;
window.loadMirrorPreset = loadMirrorPreset;
window.autoCompleteMirror = autoCompleteMirror;
window.checkMirrorSymmetry = checkMirrorSymmetry;
window.initMirrorGrid = initMirrorGrid;
window.renderCh19Quiz = renderCh19Quiz;
window.handleCh19QuizAnswer = handleCh19QuizAnswer;
window.resetCh19Quiz = resetCh19Quiz;


    // ================= CHAPTER 20: STATISTICS JAVASCRIPT ENGINE =================

// 1. Tab Navigation
function setTabCh20(tabName) {
  ['concepts', 'exercises', 'tiers', 'quiz'].forEach(t => {
    const view = document.getElementById('ch20-view-' + t);
    const btn = document.getElementById('ch20-tab-' + t);
    if (view) view.classList.add('hidden');
    if (btn) btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
  });
  const activeView = document.getElementById('ch20-view-' + tabName);
  const activeBtn = document.getElementById('ch20-tab-' + tabName);
  if (activeView) activeView.classList.remove('hidden');
  if (activeBtn) activeBtn.className = 'px-5 py-2.5 rounded-xl bg-blue-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';

  if (tabName === 'concepts') {
    renderBarStudio();
  } else if (tabName === 'quiz') {
    renderCh20Quiz();
  }

  if (window.MathJax && window.MathJax.Hub && activeView) {
    window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub, activeView]);
  } else if (window.renderOfflineMath) {
    window.renderOfflineMath(activeView);
  }
}

// 2. Exercise Sub-section Filter
function filterCh20Exercises(sec) {
  const allSecs = ['ex20_1', 'ex20_2', 'unit6_mixed'];
  const btns = {
    'all': document.getElementById('btn-sub20-all'),
    'ex20_1': document.getElementById('btn-sub20-ex20_1'),
    'ex20_2': document.getElementById('btn-sub20-ex20_2'),
    'unit6_mixed': document.getElementById('btn-sub20-mixed')
  };

  Object.keys(btns).forEach(k => {
    if (btns[k]) {
      btns[k].className = (k === sec) 
        ? 'ch20-sub-btn px-4 py-2 rounded-xl text-xs font-bold bg-blue-600 text-white shadow-sm transition'
        : 'ch20-sub-btn px-4 py-2 rounded-xl text-xs font-bold bg-white text-slate-700 hover:bg-slate-200 transition';
    }
  });

  allSecs.forEach(s => {
    const el = document.getElementById('sec-ch20-' + s);
    if (el) {
      el.classList.toggle('hidden', sec !== 'all' && sec !== s);
    }
  });
}

// 3. Interactive Lab Mode Switcher
function switchCh20Lab(mode) {
  const modes = ['barStudio', 'tallyLab', 'readerLab'];
  modes.forEach(m => {
    const el = document.getElementById('ch20-lab-mode-' + m);
    const btn = document.getElementById('ch20-lab-btn-' + m);
    if (el) el.classList.toggle('hidden', m !== mode);
    if (btn) {
      btn.className = (m === mode)
        ? 'px-4 py-2 rounded-xl text-xs font-bold bg-blue-600 text-white shadow-md transition'
        : 'px-4 py-2 rounded-xl text-xs font-bold text-slate-300 hover:text-white transition';
    }
  });

  if (mode === 'barStudio') {
    renderBarStudio();
  } else if (mode === 'tallyLab') {
    initTallyLab();
  } else if (mode === 'readerLab') {
    initReaderLab();
  }
}

// ================= MODE 1: DYNAMIC BAR CHART STUDIO =================
let currentBarPreset = 'absent';

const barDatasets = {
  absent: {
    title: 'हप्ताका ६ दिनमा अनुपस्थित विद्यार्थी सङ्ख्या सम्बन्धी साधारण स्तम्भ चित्र',
    xAxisLabel: 'दिनहरू (Days)',
    yAxisLabel: 'विद्यार्थी सङ्ख्या',
    scaleText: 'Y-अक्ष: १ से.मि. = ५ जना',
    data: [
      { label: 'आइतबार', val: 5 },
      { label: 'सोमबार', val: 10 },
      { label: 'मङ्गलबार', val: 25 },
      { label: 'बुधबार', val: 10 },
      { label: 'बिहीबार', val: 5 },
      { label: 'शुक्रबार', val: 5 }
    ]
  },
  subjects: {
    title: 'सौरभको पहिलो त्रैमासिक परीक्षा प्राप्ताङ्क सम्बन्धी स्तम्भ चित्र',
    xAxisLabel: 'विषयहरू (Subjects)',
    yAxisLabel: 'प्राप्ताङ्क (अङ्क)',
    scaleText: 'Y-अक्ष: १ से.मि. = १० अङ्क',
    data: [
      { label: 'नेपाली', val: 65 },
      { label: 'गणित', val: 90 },
      { label: 'अङ्ग्रेजी', val: 75 },
      { label: 'विज्ञान', val: 80 },
      { label: 'सामाजिक', val: 55 }
    ]
  },
  population: {
    title: 'सहरको ६ वर्षको जनसङ्ख्या (लाखमा) स्तम्भ चित्र',
    xAxisLabel: 'वर्ष (वि.सं.)',
    yAxisLabel: 'जनसङ्ख्या (लाखमा)',
    scaleText: 'Y-अक्ष: १ से.मि. = १० लाख',
    data: [
      { label: '२०७०', val: 35 },
      { label: '२०७१', val: 40 },
      { label: '२०७२', val: 50 },
      { label: '२०७३', val: 65 },
      { label: '२०७४', val: 90 },
      { label: '२०७५', val: 100 }
    ]
  },
  expenses: {
    title: 'परिवारको वार्षिक खर्च (रू. हजारमा) सम्बन्धी स्तम्भ चित्र',
    xAxisLabel: 'खर्च शीर्षकहरू',
    yAxisLabel: 'रकम (रू. हजारमा)',
    scaleText: 'Y-अक्ष: १ से.मि. = १० हजार',
    data: [
      { label: 'खाना', val: 50 },
      { label: 'कपडा', val: 15 },
      { label: 'स्वास्थ्य', val: 15 },
      { label: 'शिक्षा', val: 20 },
      { label: 'घरभाडा', val: 30 },
      { label: 'अन्य', val: 15 }
    ]
  },
  animals: {
    title: 'पशु फार्ममा भएका पशुहरूको सङ्ख्या सम्बन्धी स्तम्भ चित्र',
    xAxisLabel: 'पशुका नाम',
    yAxisLabel: 'पशु सङ्ख्या',
    scaleText: 'Y-अक्ष: १ से.मि. = ५ वटा',
    data: [
      { label: 'गाई', val: 15 },
      { label: 'भैंसी', val: 10 },
      { label: 'भेडा', val: 35 },
      { label: 'बाख्रा', val: 40 },
      { label: 'सुँगुर', val: 25 }
    ]
  }
};

const barThemes = {
  indigo: ['#3b82f6', '#2563eb', '#1d4ed8', '#4f46e5', '#6366f1', '#818cf8'],
  emerald: ['#10b981', '#059669', '#047857', '#14b8a6', '#0d9488', '#2dd4bf'],
  amber: ['#f59e0b', '#d97706', '#b45309', '#f97316', '#ea580c', '#fbbf24'],
  multi: ['#f43f5e', '#f59e0b', '#10b981', '#06b6d4', '#6366f1', '#ec4899']
};

function loadBarPreset(key) {
  currentBarPreset = key;
  document.querySelectorAll('.bar-preset-btn').forEach(b => {
    b.className = 'bar-preset-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-700 text-slate-200 hover:bg-slate-600 transition';
  });
  const btn = document.getElementById('btn-bar-' + key);
  if (btn) btn.className = 'bar-preset-btn px-3 py-1.5 rounded-xl text-xs font-bold bg-blue-600 text-white transition';
  renderBarStudio();
}

function renderBarStudio() {
  const gGrid = document.getElementById('bar-grid-group');
  const gBars = document.getElementById('bar-elements-group');
  const gAxes = document.getElementById('bar-axes-group');
  const gLabels = document.getElementById('bar-labels-group');
  if (!gGrid || !gBars || !gAxes || !gLabels) return;

  gGrid.innerHTML = '';
  gBars.innerHTML = '';
  gAxes.innerHTML = '';
  gLabels.innerHTML = '';

  const ds = barDatasets[currentBarPreset] || barDatasets['absent'];
  const titleEl = document.getElementById('bar-chart-title');
  const scaleEl = document.getElementById('bar-scale-text');
  if (titleEl) titleEl.textContent = ds.title;
  if (scaleEl) scaleEl.textContent = ds.scaleText;

  const themeKey = (document.getElementById('ch20-bar-theme') || {}).value || 'indigo';
  const colors = barThemes[themeKey] || barThemes['indigo'];

  // Dimensions
  const svgW = 540, svgH = 340;
  const padLeft = 65, padBottom = 60, padTop = 35, padRight = 30;
  const plotW = svgW - padLeft - padRight;
  const plotH = svgH - padTop - padBottom;

  const values = ds.data.map(d => d.val);
  const maxVal = Math.max(...values);
  const minVal = Math.min(...values);
  const sumVal = values.reduce((a, b) => a + b, 0);
  const avgVal = (sumVal / values.length).toFixed(2);

  // Update metrics cards
  const mMax = document.getElementById('bar-metric-max');
  const mMin = document.getElementById('bar-metric-min');
  const mSum = document.getElementById('bar-metric-sum');
  const mAvg = document.getElementById('bar-metric-avg');
  const mCount = document.getElementById('bar-items-count');
  if (mMax) mMax.textContent = maxVal;
  if (mMin) mMin.textContent = minVal;
  if (mSum) mSum.textContent = sumVal;
  if (mAvg) mAvg.textContent = avgVal;
  if (mCount) mCount.textContent = `${values.length} वटा स्तम्भ`;

  // Scale Y
  let yAxisMax = Math.ceil(maxVal * 1.15 / 5) * 5;
  if (yAxisMax < 10) yAxisMax = 10;
  const numGridLines = 5;

  // Draw Grid Lines & Y ticks
  let gridHtml = '';
  for (let i = 0; i <= numGridLines; i++) {
    let tickVal = Math.round((yAxisMax / numGridLines) * i);
    let y = padTop + plotH - (tickVal / yAxisMax) * plotH;
    gridHtml += `<line x1="${padLeft}" y1="${y}" x2="${padLeft + plotW}" y2="${y}" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>`;
    gridHtml += `<text x="${padLeft - 8}" y="${y + 4}" fill="#94a3b8" font-size="11" text-anchor="end" font-family="monospace">${tickVal}</text>`;
  }
  gGrid.innerHTML = gridHtml;

  // Axes lines
  const originX = padLeft, originY = padTop + plotH;
  let axesHtml = `
    <!-- X-Axis -->
    <line x1="${originX}" y1="${originY}" x2="${originX + plotW + 15}" y2="${originY}" stroke="#e2e8f0" stroke-width="2.5"/>
    <polygon points="${originX + plotW + 18},${originY} ${originX + plotW + 10},${originY - 4} ${originX + plotW + 10},${originY + 4}" fill="#e2e8f0"/>
    <text x="${originX + plotW + 22}" y="${originY + 4}" fill="#38bdf8" font-size="12" font-weight="black">X</text>

    <!-- Y-Axis -->
    <line x1="${originX}" y1="${originY}" x2="${originX}" y2="${padTop - 15}" stroke="#e2e8f0" stroke-width="2.5"/>
    <polygon points="${originX},${padTop - 18} ${originX - 4},${padTop - 10} ${originX + 4},${padTop - 10}" fill="#e2e8f0"/>
    <text x="${originX}" y="${padTop - 22}" fill="#38bdf8" font-size="12" font-weight="black" text-anchor="middle">Y</text>
    <text x="${originX - 10}" y="${originY + 18}" fill="#94a3b8" font-size="11" font-weight="bold">O</text>
  `;
  gAxes.innerHTML = axesHtml;

  // Draw Bars & Labels
  const n = ds.data.length;
  const slotW = plotW / n;
  const barW = Math.min(slotW * 0.58, 48); // Equal width rule!
  let barsHtml = '';
  let labelsHtml = '';

  ds.data.forEach((item, idx) => {
    const cx = originX + idx * slotW + slotW / 2;
    const x = cx - barW / 2;
    const bHeight = (item.val / yAxisMax) * plotH;
    const y = originY - bHeight;
    const barCol = colors[idx % colors.length];

    barsHtml += `
      <rect x="${x}" y="${y}" width="${barW}" height="${bHeight}" fill="${barCol}" rx="5" stroke="rgba(255,255,255,0.2)" stroke-width="1.5">
        <title>${item.label}: ${item.val}</title>
      </rect>
    `;

    // Top value on bar
    labelsHtml += `<text x="${cx}" y="${y - 6}" fill="#f8fafc" font-size="11" font-weight="black" text-anchor="middle">${item.val}</text>`;

    // X-Axis category label below bar
    labelsHtml += `<text x="${cx}" y="${originY + 18}" fill="#cbd5e1" font-size="11" font-weight="bold" text-anchor="middle">${item.label}</text>`;
  });

  gBars.innerHTML = barsHtml;
  gLabels.innerHTML = labelsHtml;
}

// ================= MODE 2: TALLY MARKS & FREQUENCY GENERATOR =================
let currentTallyPreset = 'scores';
let tallyFreqMap = {}; // item -> count

const tallyPresets = {
  scores: {
    title: 'कक्षा ६ का ३० जना विद्यार्थीहरूको २० पूर्णाङ्कको गणित प्राप्ताङ्क',
    items: [
      2, 14, 9, 6, 13, 7, 8, 11, 12, 9,
      5, 4, 15, 19, 20, 17, 16, 13, 20, 19,
      15, 9, 15, 12, 17, 13, 18, 19, 16, 15
    ]
  },
  heights: {
    title: 'कक्षा १० का ३२ जना विद्यार्थीहरूको उचाइ (से.मि. मा)',
    items: [
      123, 122, 121, 120, 124, 120, 122, 121, 120, 123, 120, 122,
      124, 123, 121, 124, 120, 124, 122, 121, 123, 122, 123, 123,
      122, 121, 120, 124, 120, 121, 123, 122
    ]
  },
  transport: {
    title: 'विद्यालय आउने यातायातका साधनहरू (४० जना)',
    items: [
      'बस', 'साइकल', 'साइकल', 'ट्याक्सी', 'मोटरसाइकल', 'पैदल', 'बस',
      'पैदल', 'ट्याक्सी', 'पैदल', 'बस', 'पैदल', 'ट्याक्सी', 'पैदल',
      'पैदल', 'साइकल', 'मोटरसाइकल', 'पैदल', 'साइकल', 'साइकल', 'ट्याक्सी',
      'ट्याक्सी', 'बस', 'साइकल', 'बस', 'ट्याक्सी', 'पैदल', 'पैदल',
      'बस', 'मोटरसाइकल', 'पैदल', 'बस', 'मोटरसाइकल', 'मोटरसाइकल', 'बस',
      'पैदल', 'ट्याक्सी', 'बस', 'साइकल', 'पैदल'
    ]
  },
  dice: {
    title: 'पासा (Dice) २५ पटक फ्याँक्दा प्राप्त सङ्ख्याहरू',
    items: [
      3, 5, 2, 6, 1, 4, 3, 2, 6, 5,
      1, 4, 3, 6, 2, 5, 4, 1, 6, 3,
      2, 5, 6, 4, 3
    ]
  }
};

function initTallyLab() {
  loadTallyPreset('scores');
}

function loadTallyPreset(key) {
  currentTallyPreset = key;
  const ds = tallyPresets[key] || tallyPresets['scores'];
  tallyFreqMap = {};
  ds.items.forEach(val => {
    tallyFreqMap[val] = (tallyFreqMap[val] || 0) + 1;
  });

  const tEl = document.getElementById('tally-dataset-title');
  if (tEl) tEl.textContent = ds.title;
  renderTallyTableDom();
}

function addTallyItem() {
  const input = document.getElementById('tally-custom-item');
  if (!input) return;
  const val = input.value.trim();
  if (!val) return;
  tallyFreqMap[val] = (tallyFreqMap[val] || 0) + 1;
  input.value = '';
  renderTallyTableDom();
}

function renderTallyMarkString(count) {
  const fullBundles = Math.floor(count / 5);
  const remainder = count % 5;
  let str = '';
  for (let i = 0; i < fullBundles; i++) {
    str += '<span class="text-emerald-400 font-mono font-bold mr-2"><s>||||</s></span>';
  }
  if (remainder > 0) {
    str += `<span class="text-blue-400 font-mono font-bold">${'|'.repeat(remainder)}</span>`;
  }
  return str || '<span class="text-slate-500 font-mono">-</span>';
}

function renderTallyTableDom() {
  const tbody = document.getElementById('tally-table-body');
  const countBadge = document.getElementById('tally-total-count');
  if (!tbody) return;
  tbody.innerHTML = '';

  let keys = Object.keys(tallyFreqMap);
  // Sort numerically if all keys are numbers, else alphabetically
  const isAllNumeric = keys.every(k => !isNaN(k));
  if (isAllNumeric) {
    keys.sort((a, b) => Number(a) - Number(b));
  } else {
    keys.sort();
  }

  let totalN = 0;
  keys.forEach((key, idx) => {
    const count = tallyFreqMap[key];
    totalN += count;
    const tr = document.createElement('tr');
    tr.className = 'hover:bg-slate-900 transition';
    tr.innerHTML = `
      <td class="p-3 text-center text-slate-500 font-mono">${idx + 1}</td>
      <td class="p-3 font-bold text-slate-200">${key}</td>
      <td class="p-3">${renderTallyMarkString(count)}</td>
      <td class="p-3 text-center font-black text-cyan-300 text-sm">${count}</td>
    `;
    tbody.appendChild(tr);
  });

  if (countBadge) {
    countBadge.textContent = `कुल सङ्ख्या N = ${totalN}`;
  }
}

// ================= MODE 3: BAR CHART READER LAB =================
const readerQuestions = [
  {
    q: 'कुन कक्षामा सबैभन्दा धेरै विद्यार्थीहरू अध्ययनरत छन्?',
    options: ['कक्षा ६', 'कक्षा ७', 'कक्षा ८ (१०० जना)', 'कक्षा १२'],
    correct: 2,
    explanation: 'कक्षा ८ को स्तम्भ १०० जना (सबैभन्दा अग्लो) छ।'
  },
  {
    q: 'सबैभन्दा थोरै विद्यार्थी भएको कक्षा कुन हो र कति जना छन्?',
    options: ['कक्षा १० (७० जना)', 'कक्षा ११ (७५ जना)', 'कक्षा ६ (८० जना)', 'कक्षा ७ (८५ जना)'],
    correct: 0,
    explanation: 'कक्षा १० को स्तम्भ ७० जनामा सीमित छ (सबैभन्दा होचो)।'
  },
  {
    q: 'कक्षा ६ देखि १२ सम्मका कुल विद्यार्थी सङ्ख्या कति हो?',
    options: ['५०० जना', '५९० जना', '६०० जना', '५५० जना'],
    correct: 1,
    explanation: '८० + ८५ + १०० + ९० + ७० + ७५ + ९० = ५९० जना।'
  },
  {
    q: 'कक्षा ८ र कक्षा १० का विद्यार्थी सङ्ख्या बीचको अन्तर (Difference) कति छ?',
    options: ['२० जना', '३० जना', '२५ जना', '१५ जना'],
    correct: 1,
    explanation: 'कक्षा ८ (१००) - कक्षा १० (७०) = ३० जना।'
  },
  {
    q: 'कुन दुई कक्षाहरूमा बराबर ९०-९० जना विद्यार्थी छन्?',
    options: ['कक्षा ६ र ७', 'कक्षा ९ र १२', 'कक्षा ७ र ११', 'कक्षा ८ र ९'],
    correct: 1,
    explanation: 'कक्षा ९ र कक्षा १२ दुवैमा ९०-९० जना विद्यार्थी छन्।'
  }
];

let readerCurrentQIndex = 0;
let readerUserScore = 0;
let readerAnswered = false;

function initReaderLab() {
  readerCurrentQIndex = 0;
  readerUserScore = 0;
  readerAnswered = false;
  renderReaderSvg();
  renderReaderQuestion();
}

function renderReaderSvg() {
  const g = document.getElementById('reader-svg-elements');
  if (!g) return;

  const data = [
    { label: '६', val: 80, col: '#f59e0b' },
    { label: '७', val: 85, col: '#10b981' },
    { label: '८', val: 100, col: '#38bdf8' },
    { label: '९', val: 90, col: '#6366f1' },
    { label: '१०', val: 70, col: '#ec4899' },
    { label: '११', val: 75, col: '#84cc16' },
    { label: '१२', val: 90, col: '#14b8a6' }
  ];

  const padLeft = 45, padBottom = 45, padTop = 25, padRight = 20;
  const w = 460 - padLeft - padRight;
  const h = 300 - padTop - padBottom;
  const originX = padLeft, originY = padTop + h;
  const yMax = 120;

  let html = `
    <!-- Axes -->
    <line x1="${originX}" y1="${originY}" x2="${originX + w + 10}" y2="${originY}" stroke="#94a3b8" stroke-width="2"/>
    <line x1="${originX}" y1="${originY}" x2="${originX}" y2="${padTop - 10}" stroke="#94a3b8" stroke-width="2"/>
    <text x="${originX + w + 12}" y="${originY + 4}" fill="#38bdf8" font-size="11" font-weight="bold">X</text>
    <text x="${originX}" y="${padTop - 14}" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Y</text>
  `;

  // Grid lines
  for (let val = 20; val <= 100; val += 20) {
    let y = originY - (val / yMax) * h;
    html += `
      <line x1="${originX}" y1="${y}" x2="${originX + w}" y2="${y}" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
      <text x="${originX - 6}" y="${y + 4}" fill="#64748b" font-size="10" text-anchor="end" font-family="monospace">${val}</text>
    `;
  }

  // Bars
  const slotW = w / data.length;
  const barW = slotW * 0.65;
  data.forEach((d, i) => {
    let cx = originX + i * slotW + slotW / 2;
    let bx = cx - barW / 2;
    let bH = (d.val / yMax) * h;
    let by = originY - bH;

    html += `
      <rect x="${bx}" y="${by}" width="${barW}" height="${bH}" fill="${d.col}" rx="4" opacity="0.9"/>
      <text x="${cx}" y="${by - 4}" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">${d.val}</text>
      <text x="${cx}" y="${originY + 16}" fill="#94a3b8" font-size="10" font-weight="bold" text-anchor="middle">कक्षा ${d.label}</text>
    `;
  });

  g.innerHTML = html;
}

function renderReaderQuestion() {
  const qObj = readerQuestions[readerCurrentQIndex];
  if (!qObj) return;

  readerAnswered = false;
  const qNum = document.getElementById('reader-q-num');
  const qText = document.getElementById('reader-q-text');
  const optContainer = document.getElementById('reader-options-container');
  const fb = document.getElementById('reader-feedback');
  const scoreBadge = document.getElementById('reader-score-badge');

  if (qNum) qNum.textContent = `प्रश्न ${readerCurrentQIndex + 1} / ${readerQuestions.length}`;
  if (qText) qText.textContent = qObj.q;
  if (scoreBadge) scoreBadge.textContent = `अङ्क: ${readerUserScore} / ${readerQuestions.length}`;
  if (fb) {
    fb.textContent = 'विकल्प छानेर आफ्नो उत्तर परीक्षण गर्नुहोस्!';
    fb.className = 'p-3 rounded-xl bg-slate-900/80 border border-slate-800 text-xs font-semibold text-slate-400 min-h-[36px]';
  }

  if (optContainer) {
    optContainer.innerHTML = '';
    qObj.options.forEach((opt, idx) => {
      const btn = document.createElement('button');
      btn.className = 'w-full text-left p-2.5 rounded-xl border border-slate-700 bg-slate-900/60 hover:bg-slate-800 text-slate-200 text-xs font-semibold transition cursor-pointer flex justify-between items-center';
      btn.innerHTML = `<span>${String.fromCharCode(65 + idx)}. ${opt}</span>`;
      btn.onclick = () => handleReaderAnswer(idx);
      optContainer.appendChild(btn);
    });
  }
}

function handleReaderAnswer(selectedIdx) {
  if (readerAnswered) return;
  readerAnswered = true;
  const qObj = readerQuestions[readerCurrentQIndex];
  const fb = document.getElementById('reader-feedback');
  const optContainer = document.getElementById('reader-options-container');
  const scoreBadge = document.getElementById('reader-score-badge');

  const btns = optContainer.querySelectorAll('button');
  btns.forEach((b, idx) => {
    b.disabled = true;
    if (idx === qObj.correct) {
      b.className = 'w-full text-left p-2.5 rounded-xl border border-emerald-500 bg-emerald-950/60 text-emerald-200 text-xs font-bold flex justify-between items-center';
      b.innerHTML += '<span class="text-emerald-400">✓ सही</span>';
    } else if (idx === selectedIdx) {
      b.className = 'w-full text-left p-2.5 rounded-xl border border-rose-500 bg-rose-950/60 text-rose-200 text-xs font-bold flex justify-between items-center';
      b.innerHTML += '<span class="text-rose-400">✗ गलत</span>';
    } else {
      b.className += ' opacity-50';
    }
  });

  if (selectedIdx === qObj.correct) {
    readerUserScore++;
    if (scoreBadge) scoreBadge.textContent = `अङ्क: ${readerUserScore} / ${readerQuestions.length}`;
    if (fb) {
      fb.innerHTML = `<span class="text-emerald-400 font-bold">🎉 सही उत्तर!</span> <span class="text-slate-300">${qObj.explanation}</span>`;
      fb.className = 'p-3 rounded-xl bg-emerald-950/40 border border-emerald-800/60 text-xs';
    }
  } else {
    if (fb) {
      fb.innerHTML = `<span class="text-rose-400 font-bold">⚠️ गलत उत्तर!</span> <span class="text-slate-300">${qObj.explanation}</span>`;
      fb.className = 'p-3 rounded-xl bg-rose-950/40 border border-rose-800/60 text-xs';
    }
  }
}

function nextReaderQuestion() {
  readerCurrentQIndex = (readerCurrentQIndex + 1) % readerQuestions.length;
  renderReaderQuestion();
}

// ================= 4. SELF-ASSESSMENT QUIZ ENGINE =================
const ch20QuizQuestions = [
  {
    id: 'q1',
    question: 'कुनै तथ्याङ्कमा कुनै मान दोहोरिने सङ्ख्यालाई के भनिन्छ?',
    options: ['परास (Range)', 'बारम्बारता (Frequency)', 'मध्यक (Mean)', 'कोरा तथ्याङ्क'],
    correct: 1,
    explanation: 'कुनै विशेष मान तथ्याङ्कमा कति पटक दोहोरिएको छ, त्यो सङ्ख्या नै उक्त मानको बारम्बारता (Frequency) हो।'
  },
  {
    id: 'q2',
    question: 'मिलान चिह्न (Tally marks) मा ५ को मान देखाउन कस्तो सङ्केत कोरिन्छ?',
    options: ['५ वटा ठाडो धर्सा', '४ वटा ठाडो र १ वटा छड्के धर्सा (<s>||||</s>)', '३ वटा ठाडो र २ छड्के', '१ वटा तेर्सो धर्सा'],
    correct: 1,
    explanation: 'चारवटा ठाडो धर्सा तानेपछि पाँचौँ गणनाले छड्के काटेर ५ को बण्डल बनाइन्छ।'
  },
  {
    id: 'q3',
    question: 'साधारण स्तम्भ चित्र बनाउँदा तेर्सो X-अक्षमा सामान्यतया के राखिन्छ?',
    options: ['बारम्बारता वा सङ्ख्या', 'अध्ययन गरिने विषय वा शीर्षकहरू', 'स्केल (Scale)', 'कुल योगफल'],
    correct: 1,
    explanation: 'तेर्सो X-अक्षमा अध्ययन गरिने चर/शीर्षक (जस्तै दिन, विषय, कक्षा) राखिन्छ र ठाडो Y-अक्षमा बारम्बारता राखिन्छ।'
  },
  {
    id: 'q4',
    question: 'साधारण स्तम्भ चित्रमा सबै स्तम्भहरूको के अनिवार्य रूपमा बराबर हुनुपर्छ?',
    options: ['स्तम्भको उचाइ', 'स्तम्भको चौडाइ', 'स्तम्भको रङ', 'स्तम्भको क्षेत्रफल'],
    correct: 1,
    explanation: 'स्तम्भको मान उचाइले मात्र जनाउने हुनाले तुलनामा भ्रम नहोस् भन्न सबै स्तम्भको चौडाइ ठ्याक्कै बराबर हुनुपर्छ।'
  },
  {
    id: 'q5',
    question: 'स्तम्भ चित्रमा दुईवटा स्तम्भहरू बिचको दूरी कस्तो हुनुपर्दछ?',
    options: ['असमान हुनुपर्छ', 'जति राखे पनि हुन्छ', 'सधैँ समान हुनुपर्छ', 'शून्य (खप्टिएको) हुनुपर्छ'],
    correct: 2,
    explanation: 'साधारण स्तम्भ चित्रमा कुनै पनि दुई स्तम्भहरूको बिचको खाली दूरी सधैँ समान हुनुपर्छ।'
  },
  {
    id: 'q6',
    question: 'यदि Y-अक्षमा १ से.मि. = ५ जना मानिएको छ र एउटा स्तम्भको उचाइ ६ से.मि. छ भने सो स्तम्भले कति विद्यार्थी जनाउँछ?',
    options: ['११ जना', '३० जना', '२५ जना', '३६ जना'],
    correct: 1,
    explanation: 'मान = उचाइ × स्केल = ६ × ५ = ३० जना।'
  },
  {
    id: 'q7',
    question: '३० जना विद्यार्थीको परीक्षामा १५ अङ्क पाउने ४ जना छन् भने १५ अङ्कको बारम्बारता कति हुन्छ?',
    options: ['१५', '३०', '४', '२'],
    correct: 2,
    explanation: '१५ अङ्क पाउने विद्यार्थी ४ जना भएकाले यसको बारम्बारता ४ हुन्छ।'
  },
  {
    id: 'q8',
    question: 'सुरुवाती अवस्थामा सङ्कलन गरिएको तर कुनै तालिका वा समूहमा नराखिएको तथ्याङ्कलाई के भनिन्छ?',
    options: ['माध्यमिक तथ्याङ्क', 'कोरा तथ्याङ्क (Raw Data)', 'बारम्बारता', 'स्तम्भ'],
    correct: 1,
    explanation: 'सुरुमा सङ्कलन गरिएको अव्यवस्थित सुरुवाती तथ्याङ्कलाई कोरा तथ्याङ्क भनिन्छ।'
  },
  {
    id: 'q9',
    question: 'परिवारको कुल खर्च १ लाख ४० हजारमा खानामा ५० हजार खर्च हुन्छ भने खानामा भएको खर्च प्रतिशत कति हो?',
    options: ['२५%', '५०%', '३५.७१%', '४०%'],
    correct: 2,
    explanation: '(५० / १४०) × १००% = ३५.७१%।'
  },
  {
    id: 'q10',
    question: 'अनुसन्धानकर्ता आफैँले स्थलगत रूपमा प्रत्यक्ष सोधपुछ वा अवलोकन गरी सङ्कलन गरेको तथ्याङ्कलाई के भनिन्छ?',
    options: ['प्राथमिक तथ्याङ्क (Primary Data)', 'द्वितीयक तथ्याङ्क', 'अनुमानित तथ्याङ्क', 'समूहकृत तथ्याङ्क'],
    correct: 0,
    explanation: 'आफैँले प्रत्यक्ष सङ्कलन गरेको मौलिक तथ्याङ्क प्राथमिक तथ्याङ्क हो।'
  }
];

let ch20UserAnswers = {};

function renderCh20Quiz() {
  const container = document.getElementById('ch20-quiz-container');
  if (!container) return;
  container.innerHTML = '';

  ch20QuizQuestions.forEach((q, idx) => {
    const answered = ch20UserAnswers.hasOwnProperty(q.id);
    const selectedOpt = ch20UserAnswers[q.id];

    const card = document.createElement('div');
    card.className = 'bg-white border border-slate-200 rounded-2xl p-5 shadow-sm space-y-3';

    let optionsHtml = '';
    q.options.forEach((opt, oIdx) => {
      let optClass = 'w-full text-left p-3 rounded-xl border text-xs md:text-sm font-semibold transition flex items-center justify-between ';
      if (!answered) {
        optClass += 'border-slate-200 hover:bg-slate-50 text-slate-700 cursor-pointer';
      } else {
        if (oIdx === q.correct) {
          optClass += 'border-emerald-500 bg-emerald-50 text-emerald-900 font-bold';
        } else if (oIdx === selectedOpt) {
          optClass += 'border-rose-500 bg-rose-50 text-rose-900 font-bold';
        } else {
          optClass += 'border-slate-200 text-slate-400 opacity-60';
        }
      }

      optionsHtml += `
        <button onclick="handleCh20QuizAnswer('${q.id}', ${oIdx})" ${answered ? 'disabled' : ''} class="${optClass}">
          <span>${String.fromCharCode(65 + oIdx)}. ${opt}</span>
          ${answered && oIdx === q.correct ? '<span class="text-emerald-600 font-black">✓ सही</span>' : ''}
          ${answered && oIdx === selectedOpt && oIdx !== q.correct ? '<span class="text-rose-600 font-black">✗ गलत</span>' : ''}
        </button>
      `;
    });

    let explanationHtml = '';
    if (answered) {
      explanationHtml = `
        <div class="mt-3 p-3 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-600 space-y-1">
          <strong class="text-slate-800">💡 व्याख्या:</strong> ${q.explanation}
        </div>
      `;
    }

    card.innerHTML = `
      <div class="flex items-center justify-between border-b border-slate-100 pb-2">
        <span class="text-xs font-bold text-blue-600">प्रश्न ${idx + 1} / ${ch20QuizQuestions.length}</span>
        <span class="text-[11px] font-mono text-slate-400">१ अङ्क</span>
      </div>
      <p class="font-extrabold text-sm md:text-base text-slate-800">${q.question}</p>
      <div class="space-y-2 pt-1">
        ${optionsHtml}
      </div>
      ${explanationHtml}
    `;

    container.appendChild(card);
  });
}

function handleCh20QuizAnswer(qId, optIdx) {
  if (ch20UserAnswers.hasOwnProperty(qId)) return;
  ch20UserAnswers[qId] = optIdx;

  let score = 0;
  ch20QuizQuestions.forEach(q => {
    if (ch20UserAnswers[q.id] === q.correct) {
      score++;
    }
  });

  const scoreEl = document.getElementById('ch20-quiz-score');
  if (scoreEl) {
    scoreEl.textContent = `${score} / ${ch20QuizQuestions.length}`;
  }

  renderCh20Quiz();
}

function resetCh20Quiz() {
  ch20UserAnswers = {};
  const scoreEl = document.getElementById('ch20-quiz-score');
  if (scoreEl) {
    scoreEl.textContent = `० / ${ch20QuizQuestions.length}`;
  }
  renderCh20Quiz();
}

// Expose to window for global access
window.setTabCh20 = setTabCh20;
window.filterCh20Exercises = filterCh20Exercises;
window.switchCh20Lab = switchCh20Lab;
window.loadBarPreset = loadBarPreset;
window.renderBarStudio = renderBarStudio;
window.initTallyLab = initTallyLab;
window.loadTallyPreset = loadTallyPreset;
window.addTallyItem = addTallyItem;
window.renderTallyTableDom = renderTallyTableDom;
window.initReaderLab = initReaderLab;
window.renderReaderSvg = renderReaderSvg;
window.renderReaderQuestion = renderReaderQuestion;
window.handleReaderAnswer = handleReaderAnswer;
window.nextReaderQuestion = nextReaderQuestion;
window.renderCh20Quiz = renderCh20Quiz;
window.handleCh20QuizAnswer = handleCh20QuizAnswer;
window.resetCh20Quiz = resetCh20Quiz;


    

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

// ================= CLASS 9 UNIT 1: SCIENTIFIC STUDY SCRIPT =================

// Tab Switching
function setTabC9U1(tab) {
  const tabs = ['concepts', 'exercises', 'tiers', 'quiz'];
  tabs.forEach(t => {
    const view = document.getElementById(`c9u1-view-${t}`);
    const btn = document.getElementById(`c9u1-tab-${t}`);
    if (view) {
      if (t === tab) {
        view.classList.remove('hidden');
      } else {
        view.classList.add('hidden');
      }
    }
    if (btn) {
      if (t === tab) {
        btn.className = 'px-5 py-2.5 rounded-xl bg-cyan-600 text-white shadow-sm font-bold transition whitespace-nowrap cursor-pointer';
      } else {
        btn.className = 'px-5 py-2.5 rounded-xl text-slate-600 hover:bg-slate-100 transition whitespace-nowrap cursor-pointer';
      }
    }
  });
  if (tab === 'quiz') {
    renderC9U1Quiz();
  }
}

// Virtual Lab Mode Switcher
function switchC9U1Lab(mode) {
  const modes = ['notation', 'leastcount', 'inquiry'];
  modes.forEach(m => {
    const container = document.getElementById(`c9u1-lab-mode-${m}`);
    const btn = document.getElementById(`c9u1-lab-btn-${m}`);
    if (container) {
      if (m === mode) {
        container.classList.remove('hidden');
      } else {
        container.classList.add('hidden');
      }
    }
    if (btn) {
      if (m === mode) {
        btn.className = 'px-3.5 py-2 rounded-xl text-xs font-black transition bg-cyan-600 text-white shadow-sm cursor-pointer';
      } else {
        btn.className = 'px-3.5 py-2 rounded-xl text-xs font-bold transition text-slate-300 hover:text-white cursor-pointer';
      }
    }
  });
  if (mode === 'leastcount') {
    selectC9U1Instrument('ruler');
  }
}

// Convert English numbers to Nepali numerals
function toNepaliNumC9(numStr) {
  const nep = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९'];
  return String(numStr).replace(/[0-9]/g, d => nep[parseInt(d, 10)]);
}

// Mode 1: Scientific Notation Converter
function calculateScientificNotation() {
  const inputEl = document.getElementById('c9u1-num-input');
  if (!inputEl) return;
  let raw = inputEl.value.trim().replace(/,/g, '');
  if (!raw || isNaN(raw) || Number(raw) === 0) {
    document.getElementById('c9u1-res-notation').textContent = 'अमान्य वा शून्य';
    document.getElementById('c9u1-res-eng').textContent = 'Enter valid non-zero number';
    return;
  }

  const num = parseFloat(raw);
  const expStr = num.toExponential();
  const parts = expStr.split('e');
  let m = parseFloat(parts[0]);
  let n = parseInt(parts[1], 10);

  // Format M to reasonable decimals
  let mStr = m.toString();
  if (mStr.length > 7) {
    mStr = m.toFixed(4).replace(/\.?0+$/, '');
  }

  const nepM = toNepaliNumC9(mStr);
  const nepN = toNepaliNumC9(Math.abs(n));
  const signSymbol = n >= 0 ? '' : '-';
  const nepSign = n >= 0 ? '' : '-';

  const resNotation = document.getElementById('c9u1-res-notation');
  const resEng = document.getElementById('c9u1-res-eng');
  const resM = document.getElementById('c9u1-res-m');
  const resN = document.getElementById('c9u1-res-n');
  const resShift = document.getElementById('c9u1-res-shift');
  const resSig = document.getElementById('c9u1-res-sig');

  if (resNotation) resNotation.textContent = `${nepM} × १०^${nepSign}${nepN}`;
  if (resEng) resEng.textContent = `${mStr} × 10^(${signSymbol}${Math.abs(n)})`;
  if (resM) resM.textContent = `${mStr} (${nepM})`;
  if (resN) resN.textContent = (n >= 0 ? `+${n}` : `${n}`) + ` (${toNepaliNumC9(n)})`;

  if (resShift) {
    if (n > 0) {
      resShift.textContent = `बायाँतर्फ ${toNepaliNumC9(n)} स्थान (धनात्मक घाताङ्क)`;
    } else if (n < 0) {
      resShift.textContent = `दायाँतर्फ ${toNepaliNumC9(Math.abs(n))} स्थान (ऋणात्मक घाताङ्क)`;
    } else {
      resShift.textContent = `दशमलव सार्न नपर्ने (घाताङ्क ०)`;
    }
  }

  if (resSig) {
    // Count significant figures in mStr
    const cleanDigits = mStr.replace('.', '');
    resSig.textContent = `${toNepaliNumC9(cleanDigits.length)} वटा (${cleanDigits.split('').join(', ')})`;
  }
}

function setC9U1Preset(val) {
  const inputEl = document.getElementById('c9u1-num-input');
  if (inputEl) {
    inputEl.value = val;
    calculateScientificNotation();
  }
}

// Mode 2: Least Count Lab
const c9u1Instruments = {
  ruler: {
    title: 'साधारण मिटर स्केल (Meter Scale)',
    badge: 'LC = 1 mm (0.1 cm)',
    reading: '३.७ cm (३७ mm)',
    desc: '१ सेन्टिमिटरलाई १० बराबर साना भागहरूमा बाँडिएको हुन्छ। १ सानो भाग = ०.१ cm = १ mm। १ mm भन्दा सानो नाप यसले सिधै लिन सक्दैन।',
    render: function(svg) {
      svg.innerHTML = `
        <rect x="20" y="30" width="460" height="70" fill="#fef08a" stroke="#ca8a04" stroke-width="2" rx="6"/>
        <!-- Main markings: 0 to 5 cm -->
        ${Array.from({length: 6}).map((_, i) => `
          <line x1="${50 + i * 75}" y1="30" x2="${50 + i * 75}" y2="70" stroke="#713f12" stroke-width="2"/>
          <text x="${50 + i * 75}" y="92" fill="#713f12" font-size="14" font-weight="bold" text-anchor="middle">${i}</text>
          <!-- 10 mm subdivisions -->
          ${i < 5 ? Array.from({length: 9}).map((_, j) => `
            <line x1="${50 + i * 75 + (j + 1) * 7.5}" y1="30" x2="${50 + i * 75 + (j + 1) * 7.5}" y2="${j === 4 ? 58 : 46}" stroke="#854d0e" stroke-width="${j === 4 ? 1.5 : 1}"/>
          `).join('') : ''}
        `).join('')}
        <!-- Reading Indicator arrow at 3.7 cm = 50 + 3*75 + 7*7.5 = 327.5 -->
        <polygon points="327.5,10 322,0 333,0" fill="#ef4444"/>
        <line x1="327.5" y1="10" x2="327.5" y2="75" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,2"/>
        <text x="327.5" y="125" fill="#ef4444" font-size="12" font-weight="bold" text-anchor="middle">३.७ cm (न्यूनतम नाप १ mm)</text>
      `;
    }
  },
  stopwatch: {
    title: 'डिजिटल स्टपवाच (Digital Stopwatch)',
    badge: 'LC = 0.01 s (१ सेन्टीसेकेन्ड)',
    reading: '०.६३ s (१०० भागको ६३ भाग)',
    desc: 'डिजिटल स्टपवाचले १ सेकेन्डलाई १०० बराबर भागमा विभाजन गर्छ। यसको न्यूनतम नाप ०.०१ सेकेन्ड (१/१०० s) हुन्छ।',
    render: function(svg) {
      svg.innerHTML = `
        <rect x="140" y="20" width="220" height="110" rx="20" fill="#1e293b" stroke="#38bdf8" stroke-width="3"/>
        <rect x="160" y="40" width="180" height="50" rx="8" fill="#0f172a" stroke="#0284c7" stroke-width="1.5"/>
        <text x="250" y="75" fill="#38bdf8" font-size="28" font-weight="bold" font-family="monospace" text-anchor="middle">00 : 00 . 63</text>
        <text x="250" y="115" fill="#94a3b8" font-size="11" font-weight="bold" text-anchor="middle">न्यूनतम नाप = ०.०१ सेकेन्ड</text>
        <!-- Buttons on top -->
        <rect x="180" y="8" width="30" height="12" rx="4" fill="#64748b"/>
        <rect x="290" y="8" width="30" height="12" rx="4" fill="#64748b"/>
      `;
    }
  },
  ammeter: {
    title: 'माइक्रो-एमिटर (Microammeter - क्रियाकलाप १.५)',
    badge: 'LC = 1 μA',
    reading: '२४ μA',
    desc: '० देखि ५० μA नाप्ने मिटरमा ० देखि १० सम्म १० वटा साना खण्ड हुन्छन्। त्यसैले १ सानो खण्ड = १०/१० = १ μA हुन्छ।',
    render: function(svg) {
      svg.innerHTML = `
        <rect x="100" y="15" width="300" height="125" rx="16" fill="#18181b" stroke="#71717a" stroke-width="2"/>
        <path d="M 130 90 A 120 120 0 0 1 370 90" fill="none" stroke="#e4e4e7" stroke-width="2"/>
        <!-- Ticks for 0, 10, 20, 30, 40, 50 -->
        <text x="140" y="105" fill="#e4e4e7" font-size="11" font-weight="bold">0</text>
        <text x="180" y="65" fill="#e4e4e7" font-size="11" font-weight="bold">10</text>
        <text x="245" y="48" fill="#e4e4e7" font-size="11" font-weight="bold">25</text>
        <text x="310" y="65" fill="#e4e4e7" font-size="11" font-weight="bold">40</text>
        <text x="350" y="105" fill="#e4e4e7" font-size="11" font-weight="bold">50</text>
        <text x="250" y="90" fill="#38bdf8" font-size="14" font-weight="bold" text-anchor="middle">μA</text>
        <!-- Needle pointing to 24 -->
        <line x1="250" y1="120" x2="242" y2="45" stroke="#ef4444" stroke-width="2"/>
        <circle cx="250" cy="120" r="5" fill="#ef4444"/>
      `;
    }
  },
  cylinder: {
    title: 'मेजरिङ सिलिन्डर (Measuring Cylinder - क्रियाकलाप १.५)',
    badge: 'LC = 1 mL',
    reading: '३२ mL',
    desc: '० देखि ५० mL सिलिन्डरमा प्रत्येक १० mL बीचमा १० वटा साना खण्डहरू हुन्छन्। १ खण्ड = १०/१० = १ mL हुन्छ।',
    render: function(svg) {
      svg.innerHTML = `
        <rect x="210" y="20" width="80" height="120" fill="none" stroke="#67e8f9" stroke-width="2" rx="4"/>
        <!-- Water level at 32 ml (height ~ 70px) -->
        <rect x="212" y="60" width="76" height="78" fill="rgba(6, 182, 212, 0.35)"/>
        <!-- Graduation lines -->
        ${Array.from({length: 6}).map((_, i) => `
          <line x1="210" y1="${135 - i * 22}" x2="235" y2="${135 - i * 22}" stroke="#67e8f9" stroke-width="2"/>
          <text x="242" y="${139 - i * 22}" fill="#67e8f9" font-size="10" font-weight="bold">${i * 10}</text>
        `).join('')}
        <text x="310" y="70" fill="#38bdf8" font-size="12" font-weight="bold">तरलको सतह = ३२ mL</text>
      `;
    }
  }
};

function selectC9U1Instrument(type) {
  const conf = c9u1Instruments[type];
  if (!conf) return;

  const btns = ['ruler', 'stopwatch', 'ammeter', 'cylinder'];
  btns.forEach(b => {
    const btn = document.getElementById(`btn-inst-${b}`);
    if (btn) {
      if (b === type) {
        btn.className = 'w-full text-left p-3.5 rounded-2xl transition border border-cyan-500 bg-cyan-950/40 text-cyan-200 font-bold text-xs flex justify-between items-center cursor-pointer';
      } else {
        btn.className = 'w-full text-left p-3.5 rounded-2xl transition border border-slate-700 bg-slate-800 text-slate-300 hover:text-white font-bold text-xs flex justify-between items-center cursor-pointer';
      }
    }
  });

  const svg = document.getElementById('c9u1-inst-svg');
  if (svg) conf.render(svg);

  const readingEl = document.getElementById('c9u1-inst-reading');
  const titleEl = document.getElementById('c9u1-inst-title');
  const badgeEl = document.getElementById('c9u1-inst-badge');
  const descEl = document.getElementById('c9u1-inst-desc');

  if (readingEl) readingEl.textContent = conf.reading;
  if (titleEl) titleEl.textContent = conf.title;
  if (badgeEl) badgeEl.textContent = conf.badge;
  if (descEl) descEl.textContent = conf.desc;
}

// Mode 3: Simulation Trial
function runC9U1InquiryTrial() {
  const t1 = (0.61 + Math.random() * 0.05).toFixed(2);
  const t2 = (0.63 + Math.random() * 0.05).toFixed(2);
  const t3 = (0.61 + Math.random() * 0.04).toFixed(2);
  const avg = ((parseFloat(t1) + parseFloat(t2) + parseFloat(t3)) / 3).toFixed(2);

  const el1 = document.getElementById('c9u1-trial-1');
  const el2 = document.getElementById('c9u1-trial-2');
  const el3 = document.getElementById('c9u1-trial-3');

  if (el1) el1.textContent = `${toNepaliNumC9(t1)} s`;
  if (el2) el2.textContent = `${toNepaliNumC9(t2)} s`;
  if (el3) el3.textContent = `${toNepaliNumC9(t3)} s`;
}

// Exercise Sub-filter
function filterC9U1Ex(group) {
  const groups = ['all', 'mcq', 'theory', 'math', 'activity'];
  groups.forEach(g => {
    const btn = document.getElementById(`btn-c9u1-filter-${g}`);
    if (btn) {
      if (g === group) {
        btn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-blue-600 text-white shadow-xs cursor-pointer';
      } else {
        btn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-white text-slate-600 hover:bg-slate-100 border border-slate-200 cursor-pointer';
      }
    }
  });

  const cards = document.querySelectorAll('.c9u1-ex-group');
  cards.forEach(c => {
    const cGroup = c.getAttribute('data-group');
    if (group === 'all' || cGroup === group) {
      c.style.display = '';
    } else {
      c.style.display = 'none';
    }
  });
}

// Tiered Questions Filter
function filterC9U1Tiers(tier) {
  const tiers = ['all', 'k', 'u', 'ha'];
  tiers.forEach(t => {
    const btn = document.getElementById(`btn-c9u1-tier-${t}`);
    if (btn) {
      if (t === tier) {
        btn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-blue-600 text-white shadow-xs cursor-pointer';
      } else {
        btn.className = 'px-3 py-1.5 rounded-xl text-xs font-bold bg-white text-slate-600 hover:bg-slate-100 border border-slate-200 cursor-pointer';
      }
    }
  });

  const sections = document.querySelectorAll('.c9u1-tier-section');
  sections.forEach(s => {
    const sTier = s.getAttribute('data-tier');
    if (tier === 'all' || sTier === tier) {
      s.style.display = '';
    } else {
      s.style.display = 'none';
    }
  });
}

// Quiz Questions Data (10 Questions)
const c9u1QuizData = [
  {
    q: '१. भेटेनरी पेसा विज्ञानको कुन शाखासँग प्रत्यक्ष सम्बन्धित छ?',
    options: ['भौतिक विज्ञान', 'जीव विज्ञान', 'रसायन विज्ञान', 'भू विज्ञान'],
    ans: 1,
    exp: 'भेटेनरी पेसा जनावर तथा पशुपक्षीहरूको स्वास्थ्य, रोग निदान र उपचारसँग सम्बन्धित भएकाले जीव विज्ञानअन्तर्गत पर्छ।'
  },
  {
    q: '२. आनुवंशिकी वा वंशाणुशास्त्रका पिता (Father of Genetics) कसलाई मानिन्छ?',
    options: ['सर आइज्याक न्युटन', 'जोन डाल्टन', 'ग्रेगर जोन मेन्डेल', 'दिमित्रि मेन्डेलिभ'],
    ans: 2,
    exp: 'ग्रेगर मेन्डेलले केराउको बोटमा अध्ययन गरी वंशाणुगत गुण सर्ने नियमहरू प्रतिपादन गरेका थिए।'
  },
  {
    q: '३. साधारण मिटर स्केलको प्रयोग गरी नाप्दा लिइने न्यूनतम नाप (Least Count) कति हुन्छ?',
    options: ['१ सेन्टिमिटर (१ cm)', '१ मिलिमिटर (०.१ cm)', '०.०१ मिलिमिटर', '१ मिटर'],
    ans: 1,
    exp: 'साधारण स्केलको १ सानो खण्ड = १/१० cm = ०.१ cm = १ mm हुन्छ।'
  },
  {
    q: '४. 0.000024 अङ्कलाई वैज्ञानिक सङ्केतन (Scientific Notation) मा कसरी लेखिन्छ?',
    options: ['२.४ × १०⁻⁵', '२४ × १०⁻⁵', '०.२४ × १०⁻⁶', '२ × १०⁻⁵'],
    ans: 0,
    exp: 'दशमलव ५ स्थान दायाँ सार्दा पहिलो गैर-शून्य अङ्कपछि २.४ बन्छ र १० को घाताङ्क -५ हुन्छ।'
  },
  {
    q: '५. गिगा (Giga) मेट्रिक उपसर्गको गुणक मान कति हुन्छ?',
    options: ['१०⁶', '१०⁹', '१०¹²', '१०⁻⁹'],
    ans: 1,
    exp: 'गिगा (Giga - G) = १०⁹ (अर्थात् १ अर्ब) हुन्छ।'
  },
  {
    q: '६. डा. सन्दुक रुइतले विकास गरेको इन्ट्राअकुलर लेन्स (IOL) कुन दुई क्षेत्रको अन्तरसम्बन्ध हो?',
    options: ['जीव विज्ञान र भौतिक विज्ञान (बायोफिजिक्स)', 'रसायन र भू-विज्ञान', 'भौतिक र खगोल विज्ञान', 'जीव विज्ञान र वातावरण विज्ञान'],
    ans: 0,
    exp: 'भौतिक विज्ञानको प्रकाश/लेन्सको सिद्धान्त र जीव विज्ञानको आँखाको शल्यक्रिया मिलेर बायोफिजिक्स/चिकित्सा विज्ञान बनेको छ।'
  },
  {
    q: '७. कुनै उपकरणले सही रूपमा नाप्न सक्ने सबैभन्दा सानो परिमाणलाई के भनिन्छ?',
    options: ['अधिकतम नाप', 'औसत नाप', 'न्यूनतम नाप (Least Count)', 'सार्थक अङ्क'],
    ans: 2,
    exp: 'कुनै पनि यन्त्रले सही रूपमा मापन गर्न सक्ने लघुतम परिमाणलाई त्यसको न्यूनतम नाप (Least Count) भनिन्छ।'
  },
  {
    q: '८. १ माइक्रोमिटर (1 μm) कति मिटर बराबर हुन्छ?',
    options: ['१०⁻³ मिटर', '१०⁻⁶ मिटर', '१०⁻⁹ मिटर', '१०⁻¹² मिटर'],
    ans: 1,
    exp: 'माइक्रो (Micro - μ) = १०⁻⁶ (मिटरको दश लाखौं भाग) हुन्छ।'
  },
  {
    q: '९. वैज्ञानिक पद्धतिमा कुनै परिकल्पना (Hypothesis) को सत्यता प्रमाणित गर्ने मुख्य आधार के हो?',
    options: ['अनुमान', 'प्रयोग (Experiment)', 'छलफल', 'पुस्तक अध्ययन'],
    ans: 1,
    exp: 'वैज्ञानिक पद्धतिमा प्रयोगबिना कुनै पनि परिकल्पना प्रमाणित मानिँदैन।'
  },
  {
    q: '१०. रासायनिक प्रयोगशालामा कडा अम्ल वा क्षारको बोतलमा कुन खतराको सङ्केत (Hazard Symbol) हुन्छ?',
    options: ['ज्वलनशील (Flammable)', 'संक्षारक (Corrosive)', 'विस्फोटक (Explosive)', 'जैविक जोखिम (Biohazard)'],
    ans: 1,
    exp: 'कडा अम्ल वा क्षारले छाला र धातु जलाउने/खियाउने हुँदा संक्षारक (Corrosive) सङ्केत राखिन्छ।'
  }
];

let c9u1QuizAnswers = {};

function renderC9U1Quiz() {
  const container = document.getElementById('c9u1-quiz-container');
  if (!container) return;

  container.innerHTML = c9u1QuizData.map((item, qIdx) => {
    const selected = c9u1QuizAnswers[qIdx];
    return `
      <div class="bg-white border border-slate-200 rounded-2xl p-5 shadow-xs space-y-3">
        <div class="font-bold text-slate-800 text-sm md:text-base">${item.q}</div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs md:text-sm">
          ${item.options.map((opt, optIdx) => {
            let btnClass = 'p-3 rounded-xl border border-slate-200 text-left font-medium transition cursor-pointer hover:bg-slate-50';
            let icon = '';
            if (selected !== undefined) {
              if (optIdx === item.ans) {
                btnClass = 'p-3 rounded-xl border border-emerald-500 bg-emerald-50 text-emerald-900 font-bold';
                icon = ' ✓';
              } else if (optIdx === selected) {
                btnClass = 'p-3 rounded-xl border border-rose-500 bg-rose-50 text-rose-900 font-bold';
                icon = ' ✗';
              } else {
                btnClass = 'p-3 rounded-xl border border-slate-200 text-slate-400 opacity-60';
              }
            }
            return `
              <button onclick="checkC9U1Quiz(${qIdx}, ${optIdx})" class="${btnClass}" ${selected !== undefined ? 'disabled' : ''}>
                ${opt}${icon}
              </button>
            `;
          }).join('')}
        </div>
        ${selected !== undefined ? `
          <div class="text-xs p-3 rounded-xl ${selected === item.ans ? 'bg-emerald-50 text-emerald-800 border border-emerald-200' : 'bg-rose-50 text-rose-800 border border-rose-200'}">
            <strong>${selected === item.ans ? 'सबास! सही उत्तर।' : 'गलत उत्तर।'}</strong> ${item.exp}
          </div>
        ` : ''}
      </div>
    `;
  }).join('');

  // Update Score
  let score = 0;
  Object.keys(c9u1QuizAnswers).forEach(k => {
    if (c9u1QuizAnswers[k] === c9u1QuizData[k].ans) score++;
  });
  const scoreBadge = document.getElementById('c9u1-quiz-score-badge');
  if (scoreBadge) {
    scoreBadge.textContent = `${toNepaliNumC9(score)} / १०`;
  }
}

function checkC9U1Quiz(qIdx, optIdx) {
  if (c9u1QuizAnswers[qIdx] !== undefined) return;
  c9u1QuizAnswers[qIdx] = optIdx;
  renderC9U1Quiz();
}

function resetC9U1Quiz() {
  c9u1QuizAnswers = {};
  renderC9U1Quiz();
}



  const urlParams = new URLSearchParams(window.location.search);
  const gradeParam = urlParams.get('grade');
  const unitParam = urlParams.get('unit');
  const activeChParam = urlParams.get('ch');

  if (gradeParam === '9') {
    selectGrade(9);
    if (unitParam) switchGrade9Unit(parseInt(unitParam, 10));
  } else if (!activeChParam && !gradeParam && (function(){ try { return localStorage.getItem('digital_guru_grade') === '9'; } catch(e){ return false; } })()) {
    selectGrade(9);
  } else {
    selectGrade(6);
    if (activeChParam === '20') {
      switchChapter(20);
      if (urlParams.get('tab')) {
        setTabCh20(urlParams.get('tab'));
      }
    } else if (activeChParam === '19') {
      switchChapter(19);
      if (urlParams.get('tab')) {
        setTabCh19(urlParams.get('tab'));
      }
    } else if (activeChParam === '18') {
      switchChapter(18);
      if (urlParams.get('tab')) {
        setTabCh18(urlParams.get('tab'));
      }
    } else if (activeChParam === '17') {
      switchChapter(17);
      if (urlParams.get('tab')) {
        setTabCh17(urlParams.get('tab'));
      }
    } else if (activeChParam === '16') {
      switchChapter(16);
      if (urlParams.get('tab')) {
        setTabCh16(urlParams.get('tab'));
      }
    } else if (activeChParam === '15') {
      switchChapter(15);
      if (urlParams.get('tab')) {
        setTabCh15(urlParams.get('tab'));
      }
    } else if (activeChParam === '14') {
      switchChapter(14);
      if (urlParams.get('tab')) {
        setTabCh14(urlParams.get('tab'));
      }
      if (urlParams.get('sec')) {
        setExerciseCh14(urlParams.get('sec'));
      }
      if (urlParams.get('testquiz') === '1') {
        setTimeout(() => {
          checkQuizCh14(0, 2);
          checkQuizCh14(1, 1);
        }, 500);
      }
      if (urlParams.get('scroll')) {
        setTimeout(() => {
          window.scrollTo(0, parseInt(urlParams.get('scroll')));
        }, 600);
      }
    } else if (activeChParam === '13') {
      switchChapter(13);
      if (urlParams.get('tab')) {
        setTabCh13(urlParams.get('tab'));
      }
      if (urlParams.get('sec')) {
        setExerciseCh13(urlParams.get('sec'));
      }
      if (urlParams.get('testquiz') === '1') {
        setTimeout(() => {
          checkQuizCh13(0, 1);
          checkQuizCh13(1, 1);
        }, 500);
      }
      if (urlParams.get('scroll')) {
        setTimeout(() => {
          window.scrollTo(0, parseInt(urlParams.get('scroll')));
        }, 600);
      }
    } else if (activeChParam === '12') {
      switchChapter(12);
      if (urlParams.get('tab')) {
        setTabCh12(urlParams.get('tab'));
      }
      if (urlParams.get('sec')) {
        setExerciseCh12(urlParams.get('sec'));
      }
      if (urlParams.get('testquiz') === '1') {
        setTimeout(() => {
          checkQuizCh12(0, 1);
          checkQuizCh12(1, 2);
        }, 500);
      }
      if (urlParams.get('scroll')) {
        setTimeout(() => {
          window.scrollTo(0, parseInt(urlParams.get('scroll')));
        }, 600);
      }
    } else if (activeChParam === '11') {
      switchChapter(11);
      if (urlParams.get('tab')) {
        setTabCh11(urlParams.get('tab'));
      }
      if (urlParams.get('testquiz') === '1') {
        setTimeout(() => {
          checkQuizCh11(0, 1);
          checkQuizCh11(1, 1);
        }, 500);
      }
      if (urlParams.get('scroll')) {
        setTimeout(() => {
          window.scrollTo(0, parseInt(urlParams.get('scroll')));
        }, 600);
      }
    } else if (activeChParam === '9') {
      switchChapter(9);
      if (urlParams.get('tab')) {
        setTabCh9(urlParams.get('tab'));
      }
      if (urlParams.get('sec')) {
        setExerciseCh9(urlParams.get('sec'));
      }
      if (urlParams.get('testquiz') === '1') {
        setTimeout(() => {
          checkQuizCh9(0, 1);
          checkQuizCh9(1, 0);
        }, 500);
      }
      if (urlParams.get('scroll')) {
        setTimeout(() => {
          window.scrollTo(0, parseInt(urlParams.get('scroll')));
        }, 600);
      }
    } else if (activeChParam === '8') {
      switchChapter(8);
      if (urlParams.get('tab')) {
        setTabCh8(urlParams.get('tab'));
      }
      if (urlParams.get('sec')) {
        setExerciseCh8(urlParams.get('sec'));
      }
      if (urlParams.get('testquiz') === '1') {
        setTimeout(() => {
          checkQuizCh8(0, 2);
          checkQuizCh8(1, 0);
        }, 500);
      }
      if (urlParams.get('scroll')) {
        setTimeout(() => {
          window.scrollTo(0, parseInt(urlParams.get('scroll')));
        }, 600);
      }
    } else if (activeChParam === '7') {
      switchChapter(7);
      if (urlParams.get('tab')) {
        setTabCh7(urlParams.get('tab'));
      }
      if (urlParams.get('sec')) {
        setExerciseCh7(urlParams.get('sec'));
      }
      if (urlParams.get('testquiz') === '1') {
        setTimeout(() => {
          checkQuizCh7(0, 1);
          checkQuizCh7(1, 2);
        }, 500);
      }
      if (urlParams.get('scroll')) {
        setTimeout(() => {
          window.scrollTo(0, parseInt(urlParams.get('scroll')));
        }, 600);
      }
    } else if (activeChParam === '6') {
      switchChapter(6);
      if (urlParams.get('tab')) {
        setTabCh6(urlParams.get('tab'));
      }
      if (urlParams.get('sec')) {
        setExerciseCh6(urlParams.get('sec'));
      }
      if (urlParams.get('testquiz') === '1') {
        setTimeout(() => {
          checkQuizCh6(0, 2);
          checkQuizCh6(1, 0);
        }, 500);
      }
      if (urlParams.get('scroll')) {
        setTimeout(() => {
          window.scrollTo(0, parseInt(urlParams.get('scroll')));
        }, 600);
      }
    } else if (urlParams.get('ch') === '5') {
      switchChapter(5);
      if (urlParams.get('tab')) {
        setTabCh5(urlParams.get('tab'));
      }
      if (urlParams.get('ex')) {
        setExerciseCh5(urlParams.get('ex'));
      }
      if (urlParams.get('testquiz') === '1') {
        setTimeout(() => {
          checkQuizCh5(0, 1);
          checkQuizCh5(1, 1);
        }, 500);
      }
      if (urlParams.get('scroll')) {
        setTimeout(() => {
          window.scrollTo(0, parseInt(urlParams.get('scroll')));
        }, 600);
      }
    } else if (urlParams.get('ch') === '4') {
      switchChapter(4);
      if (urlParams.get('tab')) {
        setTabCh4(urlParams.get('tab'));
      }
      if (urlParams.get('ex')) {
        setExerciseCh4(urlParams.get('ex'));
      }
      if (urlParams.get('testquiz') === '1') {
        setTimeout(() => {
          checkQuizCh4(0, 2);
          checkQuizCh4(1, 1);
        }, 500);
      }
      if (urlParams.get('scroll')) {
        setTimeout(() => {
          window.scrollTo(0, parseInt(urlParams.get('scroll')));
        }, 600);
      }
    } else if (urlParams.get('ch') === '3') {
      switchChapter(3);
      if (urlParams.get('tab')) {
        setTabCh3(urlParams.get('tab'));
      }
      if (urlParams.get('testquiz') === '1') {
        setTimeout(() => {
          checkQuizCh3(0, 1, 1, 'सङ्ख्या रेखामा -४ सङ्ख्या -१२ भन्दा दायाँतर्फ पर्दछ, त्यसैले -४ ठूलो हो।');
          checkQuizCh3(1, 2, 2, 'शून्य न त धनात्मक हो न त ऋणात्मक, यो दुवै वर्गमा नपर्ने तटस्थ (neutral) पूर्णाङ्क हो।');
        }, 500);
      }
      if (urlParams.get('scroll')) {
        setTimeout(() => {
          window.scrollTo(0, parseInt(urlParams.get('scroll')));
        }, 600);
      }
    } else if (urlParams.get('ch') === '2') {
      switchChapter(2);
      if (urlParams.get('tab')) {
        setTabCh2(urlParams.get('tab'));
      }
      if (urlParams.get('ex')) {
        showExSectionCh2(urlParams.get('ex'));
      }
    }
  