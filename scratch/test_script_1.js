
    window.MathJax.Hub.Config({
      tex2jax: {
        inlineMath: [["$","$"], ["\\(","\\)"]],
        displayMath: [["$$","$$"], ["\\[","\\]"]],
        processEscapes: true,
        skipTags: ["script", "noscript", "style", "textarea", "pre", "code"]
      },
      "HTML-CSS": {
        linebreaks: { automatic: true },
        preferredFont: "TeX",
        availableFonts: ["TeX"],
        matchFontHeight: true,
        styles: {
          ".MathJax": { "font-size": "104% !important", "color": "#1e293b" },
          ".MathJax_Display": { "margin": "0.7em 0 !important" }
        }
      },
      CommonHTML: {
        mtextFontInherit: true,
        linebreaks: { automatic: true },
        matchFontHeight: false
      },
      "HTML-CSS": {
        mtextFontInherit: true,
        linebreaks: { automatic: true }
      },
      SVG: { linebreaks: { automatic: true } },
      messageStyle: "none"
    });
  