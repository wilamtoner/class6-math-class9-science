
    if (typeof MathJax === "undefined" || !window.MathJax.Hub) {
      var mjFallback = document.createElement("script");
      mjFallback.src = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS_CHTML";
      document.head.appendChild(mjFallback);
    }
  