// Apex Auto Body concept: reveals, pinstripes, menu, demo form
(function(){
 var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
 var els = document.querySelectorAll('.rv,.pin');
 if (reduce || !('IntersectionObserver' in window)) { els.forEach(function(e){ e.classList.add('in'); }); }
 else {
  var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target);} }); },{rootMargin:'0px 0px -6% 0px',threshold:.05});
  els.forEach(function(e){ io.observe(e); });
 }
 var b = document.querySelector('.menu-btn'), m = document.getElementById('menu');
 if (b && m) {
  b.addEventListener('click', function(){ var o = m.classList.toggle('open'); b.setAttribute('aria-expanded', o); b.textContent = o ? 'Close' : 'Menu'; });
  document.addEventListener('keydown', function(e){ if (e.key === 'Escape' && m.classList.contains('open')) { m.classList.remove('open'); b.setAttribute('aria-expanded', false); b.textContent = 'Menu'; b.focus(); } });
 }
 var f = document.getElementById('qform');
 if (f) f.addEventListener('submit', function(ev){ ev.preventDefault(); document.getElementById('qmsg').textContent = 'Thanks. This is a demo, so nothing was sent. On the real site this goes to the shop desk.'; });
})();
