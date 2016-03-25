/*! modernizr 3.3.1 (Custom Build) | MIT *
 * http://modernizr.com/download/?-checked-cssanimations-svg-svgasimg-setclasses !*/
!function(e,n,t){function r(e,n){return typeof e===n}function o(){var e,n,t,o,i,s,a;for(var l in _)if(_.hasOwnProperty(l)){if(e=[],n=_[l],n.name&&(e.push(n.name.toLowerCase()),n.options&&n.options.aliases&&n.options.aliases.length))for(t=0;t<n.options.aliases.length;t++)e.push(n.options.aliases[t].toLowerCase());for(o=r(n.fn,"function")?n.fn():n.fn,i=0;i<e.length;i++)s=e[i],a=s.split("."),1===a.length?Modernizr[a[0]]=o:(!Modernizr[a[0]]||Modernizr[a[0]]instanceof Boolean||(Modernizr[a[0]]=new Boolean(Modernizr[a[0]])),Modernizr[a[0]][a[1]]=o),w.push((o?"":"no-")+a.join("-"))}}function i(e){var n=b.className,t=Modernizr._config.classPrefix||"";if(x&&(n=n.baseVal),Modernizr._config.enableJSClass){var r=new RegExp("(^|\\s)"+t+"no-js(\\s|$)");n=n.replace(r,"$1"+t+"js$2")}Modernizr._config.enableClasses&&(n+=" "+t+e.join(" "+t),x?b.className.baseVal=n:b.className=n)}function s(){return"function"!=typeof n.createElement?n.createElement(arguments[0]):x?n.createElementNS.call(n,"http://www.w3.org/2000/svg",arguments[0]):n.createElement.apply(n,arguments)}function a(e,n){if("object"==typeof e)for(var t in e)S(e,t)&&a(t,e[t]);else{e=e.toLowerCase();var r=e.split("."),o=Modernizr[r[0]];if(2==r.length&&(o=o[r[1]]),"undefined"!=typeof o)return Modernizr;n="function"==typeof n?n():n,1==r.length?Modernizr[r[0]]=n:(!Modernizr[r[0]]||Modernizr[r[0]]instanceof Boolean||(Modernizr[r[0]]=new Boolean(Modernizr[r[0]])),Modernizr[r[0]][r[1]]=n),i([(n&&0!=n?"":"no-")+r.join("-")]),Modernizr._trigger(e,n)}return Modernizr}function l(){var e=n.body;return e||(e=s(x?"svg":"body"),e.fake=!0),e}function f(e,t,r,o){var i,a,f,u,c="modernizr",d=s("div"),p=l();if(parseInt(r,10))for(;r--;)f=s("div"),f.id=o?o[r]:c+(r+1),d.appendChild(f);return i=s("style"),i.type="text/css",i.id="s"+c,(p.fake?p:d).appendChild(i),p.appendChild(d),i.styleSheet?i.styleSheet.cssText=e:i.appendChild(n.createTextNode(e)),d.id=c,p.fake&&(p.style.background="",p.style.overflow="hidden",u=b.style.overflow,b.style.overflow="hidden",b.appendChild(p)),a=t(d,e),p.fake?(p.parentNode.removeChild(p),b.style.overflow=u,b.offsetHeight):d.parentNode.removeChild(d),!!a}function u(e,n){return!!~(""+e).indexOf(n)}function c(e){return e.replace(/([a-z])-([a-z])/g,function(e,n,t){return n+t.toUpperCase()}).replace(/^-/,"")}function d(e,n){return function(){return e.apply(n,arguments)}}function p(e,n,t){var o;for(var i in e)if(e[i]in n)return t===!1?e[i]:(o=n[e[i]],r(o,"function")?d(o,t||n):o);return!1}function m(e){return e.replace(/([A-Z])/g,function(e,n){return"-"+n.toLowerCase()}).replace(/^ms-/,"-ms-")}function h(n,r){var o=n.length;if("CSS"in e&&"supports"in e.CSS){for(;o--;)if(e.CSS.supports(m(n[o]),r))return!0;return!1}if("CSSSupportsRule"in e){for(var i=[];o--;)i.push("("+m(n[o])+":"+r+")");return i=i.join(" or "),f("@supports ("+i+") { #modernizr { position: absolute; } }",function(e){return"absolute"==getComputedStyle(e,null).position})}return t}function g(e,n,o,i){function a(){f&&(delete P.style,delete P.modElem)}if(i=r(i,"undefined")?!1:i,!r(o,"undefined")){var l=h(e,o);if(!r(l,"undefined"))return l}for(var f,d,p,m,g,v=["modernizr","tspan"];!P.style;)f=!0,P.modElem=s(v.shift()),P.style=P.modElem.style;for(p=e.length,d=0;p>d;d++)if(m=e[d],g=P.style[m],u(m,"-")&&(m=c(m)),P.style[m]!==t){if(i||r(o,"undefined"))return a(),"pfx"==n?m:!0;try{P.style[m]=o}catch(y){}if(P.style[m]!=g)return a(),"pfx"==n?m:!0}return a(),!1}function v(e,n,t,o,i){var s=e.charAt(0).toUpperCase()+e.slice(1),a=(e+" "+z.join(s+" ")+s).split(" ");return r(n,"string")||r(n,"undefined")?g(a,n,o,i):(a=(e+" "+E.join(s+" ")+s).split(" "),p(a,n,t))}function y(e,n,r){return v(e,t,t,n,r)}var w=[],_=[],C={_version:"3.3.1",_config:{classPrefix:"",enableClasses:!0,enableJSClass:!0,usePrefixes:!0},_q:[],on:function(e,n){var t=this;setTimeout(function(){n(t[e])},0)},addTest:function(e,n,t){_.push({name:e,fn:n,options:t})},addAsyncTest:function(e){_.push({name:null,fn:e})}},Modernizr=function(){};Modernizr.prototype=C,Modernizr=new Modernizr,Modernizr.addTest("svg",!!n.createElementNS&&!!n.createElementNS("http://www.w3.org/2000/svg","svg").createSVGRect);var S,b=n.documentElement,x="svg"===b.nodeName.toLowerCase();!function(){var e={}.hasOwnProperty;S=r(e,"undefined")||r(e.call,"undefined")?function(e,n){return n in e&&r(e.constructor.prototype[n],"undefined")}:function(n,t){return e.call(n,t)}}(),C._l={},C.on=function(e,n){this._l[e]||(this._l[e]=[]),this._l[e].push(n),Modernizr.hasOwnProperty(e)&&setTimeout(function(){Modernizr._trigger(e,Modernizr[e])},0)},C._trigger=function(e,n){if(this._l[e]){var t=this._l[e];setTimeout(function(){var e,r;for(e=0;e<t.length;e++)(r=t[e])(n)},0),delete this._l[e]}},Modernizr._q.push(function(){C.addTest=a}),Modernizr.addTest("svgasimg",n.implementation.hasFeature("http://www.w3.org/TR/SVG11/feature#Image","1.1"));var T=C.testStyles=f;Modernizr.addTest("checked",function(){return T("#modernizr {position:absolute} #modernizr input {margin-left:10px} #modernizr :checked {margin-left:20px;display:block}",function(e){var n=s("input");return n.setAttribute("type","checkbox"),n.setAttribute("checked","checked"),e.appendChild(n),20===n.offsetLeft})});var k="Moz O ms Webkit",z=C._config.usePrefixes?k.split(" "):[];C._cssomPrefixes=z;var E=C._config.usePrefixes?k.toLowerCase().split(" "):[];C._domPrefixes=E;var N={elem:s("modernizr")};Modernizr._q.push(function(){delete N.elem});var P={style:N.elem.style};Modernizr._q.unshift(function(){delete P.style}),C.testAllProps=v,C.testAllProps=y,Modernizr.addTest("cssanimations",y("animationName","a",!0)),o(),i(w),delete C.addTest,delete C.addAsyncTest;for(var j=0;j<Modernizr._q.length;j++)Modernizr._q[j]();e.Modernizr=Modernizr}(window,document);