window.MathJax = {tex:{inlineMath:[['\\(','\\)']],displayMath:[['\\[','\\]']],processEscapes:true},svg:{fontCache:'local'},options:{skipHtmlTags:['script','noscript','style','textarea','pre','code']}};
const narrow = window.matchMedia('(max-width:720px)');
function updateNavigation(){document.querySelectorAll('.sidebar details').forEach(el=>{el.open=!narrow.matches;});}
updateNavigation();
narrow.addEventListener('change',updateNavigation);
document.querySelectorAll('.section-nav a').forEach(link=>link.addEventListener('click',()=>{if(narrow.matches) link.closest('details').open=false;}));
