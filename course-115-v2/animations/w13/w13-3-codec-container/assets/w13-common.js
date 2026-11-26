/* 三支 W13 動畫共用的小工具：建立 SVG 元素、取樣本值。全部是確定性的（不用亂數、不用時鐘）。 */
(function () {
  var NS = "http://www.w3.org/2000/svg";
  function el(tag, attrs, parent, text) {
    var e = document.createElementNS(NS, tag);
    if (attrs) for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text != null) e.textContent = text;
    if (parent) parent.appendChild(e);
    return e;
  }
  /* 以固定種子產生「看起來隨機」的數列（線性同餘），保證每次渲染都一樣 */
  function seeded(seed) {
    var s = seed >>> 0;
    return function () {
      s = (s * 1664525 + 1013904223) >>> 0;
      return s / 4294967296;
    };
  }
  function range(n) {
    var a = [];
    for (var i = 0; i < n; i++) a.push(i);
    return a;
  }

  /* 數字計數器外掛：tl.to(el, { numText: { from, to, digits, prefix, suffix, comma } })（comma: true 加千分位）
     用外掛的 render（而不是 onUpdate），任意 seek 都會正確重畫 */
  if (window.gsap) {
    gsap.registerPlugin({
      name: "numText",
      init: function (target, v) {
        this._t = target; this._a = +v.from; this._b = +v.to;
        this._d = v.digits || 0; this._p = v.prefix || ""; this._s = v.suffix || ""; this._c = !!v.comma;
        return true;
      },
      render: function (ratio, data) {
        var x = data._a + (data._b - data._a) * ratio;
        var str = x.toFixed(data._d);
        if (data._c) { var parts = str.split("."); parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ","); str = parts.join("."); }
        data._t.textContent = data._p + str + data._s;
      },
    });
  }
  window.W13 = { NS: NS, el: el, seeded: seeded, range: range };
})();
