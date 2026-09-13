const vm=require('node:vm'),fs=require('node:fs'),assert=require('node:assert/strict');
const source=['app','case2','navigation-route'].map(n=>fs.readFileSync('dist/'+n+'.js','utf8')).join('\n');
const saved={},els={};let nav='';const app={innerHTML:'',insertAdjacentHTML(_,s){nav=s;},querySelectorAll(){return []}};
const ctx=vm.createContext({document:{getElementById(id){if(id==='app')return app;if(id==='page-navigation')return {remove(){nav=''}};return els[id]??={focus(){},scrollIntoView(){}};}},localStorage:{getItem:k=>saved[k]||null,setItem:(k,v)=>saved[k]=v},window:{addEventListener(){}},location:{hash:'#case2'},scrollTo(){},scrollY:0});
vm.runInContext(source,ctx);const run=x=>vm.runInContext(x,ctx);
for(let solved=0;solved<=5;solved++){run(`more.solvedThrough=${solved}`);const end=solved===5?11:solved*2+1;for(let i=0;i<12;i++)assert.equal(run(`routeAllowed(pageOrder[${i}])`),i<=end);}
run("more.solvedThrough=2;location.hash='#mission2';render()");assert.match(nav,/href="#trail"/);assert.match(nav,/href="#after2"/);
run("location.hash='#mission3';render()");assert.match(nav,/href="#after2"/);assert.match(nav,/disabled/);assert.doesNotMatch(nav,/href="#after3"/);
run("location.hash='#after3';render()");assert.equal(ctx.location.hash,'mission3');
run("more[2].path='Saved thinking';more[2].hints=2;location.hash='#mission1';render();location.hash='#mission2';render()");assert.equal(run('more[2].path'),'Saved thinking');assert.equal(run('more[2].hints'),2);
run("more[2].verified=false;more[2].complete=false;saveMore()");assert.equal(run("routeAllowed('mission3')"),true,'earned access survives edits');assert.equal(JSON.parse(saved['thinking-detectives.case2.remaining.v1']).solvedThrough,2);
run("more[4].route=['Blue Arch']");for(const place of ['Workshop Hall','Ground Passage','Control Booth']){ctx.tag={place,from:null};assert.equal(run('placeRouteTag(more[4].route,tag,more[4].route.length)'),true);}assert.equal(run('correctMore(4,more[4])'),true);
ctx.tag={place:'Striped Skybridge',from:null};run('placeRouteTag(more[4].route,tag,1)');assert.equal(run('correctMore(4,more[4])'),false);assert.equal(run('placeRouteTag(more[4].route,tag,0)'),false);
run("more[4].route=['Blue Arch','Ground Passage','Workshop Hall','Control Booth']");ctx.tag={place:'Workshop Hall',from:2};run('placeRouteTag(more[4].route,tag,1)');assert.equal(run('correctMore(4,more[4])'),true);
assert.equal(run('missionData[3].title'),'Why DASH-3 left the stage?');assert.doesNotMatch(run('missionData[3].path'),/Remy/);
console.log('PASS: all page boundaries, previous/next targets, direct-link guard, saved work, earned access and route placement/reordering.');
// Exercise the actual pointer and tap handlers with controlled drop targets.
const button={dataset:{tag:'Workshop Hall'},classList:{add(){},remove(){}},setPointerCapture(){},setAttribute(){}};
const drop={dataset:{drop:'1'},classList:{add(){},remove(){}}};
app.querySelectorAll=selector=>selector==='[data-tag]'?[button]:selector==='[data-drop]'?[drop]:[];
ctx.document.elementFromPoint=()=>({closest:()=>drop});run("more[4].route=['Blue Arch'];bindRouteBuilder(()=>{},()=>{})");
button.onpointerdown({button:0,clientX:10,clientY:10,pointerId:1});button.onpointermove({clientX:30,clientY:100});button.onpointerup({clientX:30,clientY:100});assert.equal(run('more[4].route[1]'),'Workshop Hall');
button.onclick(); // Suppress the synthetic click following a drag.
button.onclick();assert.equal(run('selectedTag.place'),'Workshop Hall');
console.log('PASS: pointer drag/drop and tap selection handlers.');
