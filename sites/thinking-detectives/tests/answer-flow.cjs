const vm=require('node:vm'),fs=require('node:fs'),assert=require('node:assert/strict');
const code=fs.readFileSync('dist/app.js','utf8')+'\n'+fs.readFileSync('dist/case2.js','utf8')+'\n'+fs.readFileSync('dist/navigation-route.js','utf8')+'\nrender();';
function harness(saved){const els={};const el=id=>els[id]??={textContent:'',disabled:false,hidden:false,focus(){},scrollIntoView(){}};const box={innerHTML:'',querySelectorAll(){return []}};const ctx=vm.createContext({document:{getElementById(id){return id==='app'?box:el(id)}},localStorage:{getItem(){return JSON.stringify(saved||null)},setItem(){}},location:{hash:'#mission1'},window:{addEventListener(){}},scrollTo(){},scrollY:0});vm.runInContext(code,ctx);return {ctx,el,run:x=>vm.runInContext(x,ctx)};}
let h=harness();const base={chosen:[0,1],path:'I connected the wheel marks.',answer:'North Concourse',checked:true,spoken:false};
for(const answer of ['North Concourse','NORTH CONCOURSE!','the north concourse','Remy should investigate the North Concourse.','I think we should go to North Concourse','north-concourse']){h.ctx.candidate={...base,answer};assert.equal(h.run('evaluateAnswer(candidate).kind'),'success',answer);}
for(const answer of ['','South Concourse','not North Concourse','North Concourse or Service Passage']){h.ctx.candidate={...base,answer};assert.notEqual(h.run('evaluateAnswer(candidate).kind'),'success',answer);}
for(const chosen of [[0,1],[0,1,2]]){h.ctx.candidate={...base,chosen};assert.equal(h.run('evaluateAnswer(candidate).kind'),'success');}
for(const chosen of [[0],[1],[0,1,3],[0,1,2,3,4,5]]){h.ctx.candidate={...base,chosen};assert.notEqual(h.run('evaluateAnswer(candidate).kind'),'success');}
h=harness({...base,answer:'Service Passage'});h.el('check-answer').onclick();assert.equal(h.run('s.verified'),false);assert.equal(h.el('continue').disabled,true);assert.equal(h.el('retry-actions').hidden,false);h.el('retry-hint').onclick();assert.equal(h.run('s.hints'),0,'visiting hints does not reveal one');h.el('hint').onclick();assert.equal(h.run('s.hints'),1);assert.equal(h.run('s.verified'),false);
h.el('answer').oninput({target:{value:'North Concourse'}});h.el('check-answer').onclick();assert.equal(h.el('continue').disabled,false);h.el('continue').onclick();assert.equal(h.run('s.complete'),true);
h.el('answer').oninput({target:{value:'Service Passage'}});assert.equal(h.run('s.complete'),false);assert.equal(h.el('continue').disabled,true);
h=harness({...base,complete:true});assert.equal(h.run('s.complete'),false,'legacy completion does not bypass check');
h=harness({...base,verified:true,complete:true});assert.equal(h.run('s.verified'),true,'valid checked progress survives reload');
h.ctx.candidate={...base,path:'',spoken:true};assert.equal(h.run('evaluateAnswer(candidate).kind'),'success','spoken reasoning accepted');
console.log('PASS: answer variants, conflicting answers, evidence, retry/hints, progression, invalidation, saved progress, spoken reasoning.');

// Regression: a wrong destination must receive encouragement even before prerequisites.
for(const partial of [{chosen:[]},{path:'',spoken:false},{checked:false},{chosen:[],path:'',checked:false}]){
 h=harness({...base,...partial,answer:'Service passage'});h.el('check-answer').onclick();
 assert.equal(h.run('feedback.kind'),'retry');assert.match(h.el('message').textContent,/Good effort/);
 assert.match(h.el('message').textContent,/Give it another try :\)/);assert.match(h.el('message').textContent,/hint section below/);
 assert.equal(h.el('continue').disabled,true);assert.equal(h.run('s.hints'),0);
}
console.log('PASS: screenshot regression, effort praise, optional hints, prerequisites retain progression gate.');
