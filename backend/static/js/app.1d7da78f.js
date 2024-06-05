(function(){"use strict";var e={240:function(e,a,n){var r=n(751),t=n(641);const o={id:"app"},l=(0,t.Lk)("h1",null,"Welcome to Your Vue.js App",-1),s=[l];function i(e,a,n,r,l,i){return(0,t.uX)(),(0,t.CE)("div",o,s)}var u={name:"App"},c=n(262);const m=(0,c.A)(u,[["render",i]]);var d=m,p=n(220),b=n(33);const f=e=>((0,t.Qi)("data-v-6478f74b"),e=e(),(0,t.jt)(),e),v=f((()=>(0,t.Lk)("h1",null,"Welcome to the Home Page",-1))),k={key:0},g=f((()=>(0,t.Lk)("h2",null,"Your Files:",-1))),L=["href"],h=["onSubmit"],y=f((()=>(0,t.Lk)("button",{type:"submit",class:"btn btn-danger btn-sm"},"Delete",-1))),F=[y],w={key:1};function _(e,a,n,o,l,s){const i=(0,t.g2)("Navbar"),u=(0,t.g2)("router-link");return(0,t.uX)(),(0,t.CE)("div",null,[(0,t.bF)(i),v,l.isAuthenticated?((0,t.uX)(),(0,t.CE)("div",k,[g,(0,t.Lk)("ul",null,[((0,t.uX)(!0),(0,t.CE)(t.FK,null,(0,t.pI)(l.files,(a=>((0,t.uX)(),(0,t.CE)("li",{key:a.id},[(0,t.Lk)("a",{href:s.getFileUrl(a.filename)},(0,b.v_)(a.filename),9,L),(0,t.Lk)("form",{onSubmit:(0,r.D$)((n=>e.deleteFile(a.id)),["prevent"]),style:{display:"inline"}},F,40,h)])))),128))]),(0,t.bF)(u,{to:"/upload"},{default:(0,t.k6)((()=>[(0,t.eW)("Upload New File")])),_:1})])):((0,t.uX)(),(0,t.CE)("div",w,[(0,t.Lk)("p",null,[(0,t.eW)("Please "),(0,t.bF)(u,{to:"/login"},{default:(0,t.k6)((()=>[(0,t.eW)("log in")])),_:1}),(0,t.eW)(" to see your files.")])]))])}const U=e=>((0,t.Qi)("data-v-34a5fbe8"),e=e(),(0,t.jt)(),e),C={class:"navbar navbar-expand-lg bg-body-tertiary"},P={class:"container-fluid"},E=U((()=>(0,t.Lk)("button",{class:"navbar-toggler",type:"button","data-bs-toggle":"collapse","data-bs-target":"#navbarTogglerDemo01","aria-controls":"navbarTogglerDemo01","aria-expanded":"false","aria-label":"Toggle navigation"},[(0,t.Lk)("span",{class:"navbar-toggler-icon"})],-1))),A={class:"collapse navbar-collapse",id:"navbarTogglerDemo01"},X=U((()=>(0,t.Lk)("a",{class:"navbar-brand",href:"/frontend/my-vue-app/public"},"Online Drive",-1))),W={class:"navbar-nav me-auto mb-2 mb-lg-0"},j={class:"nav-item"},D={class:"nav-item"},N=U((()=>(0,t.Lk)("form",{class:"d-flex",role:"search"},[(0,t.Lk)("input",{class:"form-control me-2",type:"search",placeholder:"Search","aria-label":"Search"}),(0,t.Lk)("button",{class:"btn btn-outline-success",type:"submit"},"Search")],-1))),O={class:"navbar-nav me-auto mb-2 mb-lg-0"},x={key:0,class:"nav-item"},Q={key:1,class:"nav-item"},S={key:2,class:"nav-item"},I=U((()=>(0,t.Lk)("a",{class:"nav-link",href:"/logout"},"Logout",-1))),V=[I];function J(e,a,n,r,o,l){const s=(0,t.g2)("router-link");return(0,t.uX)(),(0,t.CE)("nav",C,[(0,t.Lk)("div",P,[E,(0,t.Lk)("div",A,[X,(0,t.Lk)("ul",W,[(0,t.Lk)("li",j,[(0,t.bF)(s,{class:"nav-link active",to:"/"},{default:(0,t.k6)((()=>[(0,t.eW)("Drive")])),_:1})]),(0,t.Lk)("li",D,[(0,t.bF)(s,{class:"nav-link",to:"/profile"},{default:(0,t.k6)((()=>[(0,t.eW)("Your profile")])),_:1})])]),N,(0,t.Lk)("ul",O,[o.isAuthenticated?(0,t.Q3)("",!0):((0,t.uX)(),(0,t.CE)("li",x,[(0,t.bF)(s,{class:"nav-link active",to:"/login"},{default:(0,t.k6)((()=>[(0,t.eW)("Login")])),_:1})])),o.isAuthenticated?(0,t.Q3)("",!0):((0,t.uX)(),(0,t.CE)("li",Q,[(0,t.bF)(s,{class:"nav-link",to:"/register"},{default:(0,t.k6)((()=>[(0,t.eW)("Register")])),_:1})])),o.isAuthenticated?((0,t.uX)(),(0,t.CE)("li",S,V)):(0,t.Q3)("",!0)])])])])}var T={name:"NavbarComponent",data(){return{isAuthenticated:!1}},mounted(){}};const $=(0,c.A)(T,[["render",J],["__scopeId","data-v-34a5fbe8"]]);var R=$,Y={name:"HomePageComponent",components:{Navbar:R},data(){return{isAuthenticated:!1,files:[]}},methods:{getFileUrl(e){return`/uploads/${e}`}},mounted(){}};const H=(0,c.A)(Y,[["render",_],["__scopeId","data-v-6478f74b"]]);var B=H;const K=e=>((0,t.Qi)("data-v-1c15b798"),e=e(),(0,t.jt)(),e),q=K((()=>(0,t.Lk)("h1",null,"Login",-1))),z={class:"mb-3"},G=K((()=>(0,t.Lk)("label",{for:"username",class:"form-label"},"Username",-1))),M={class:"mb-3"},Z=K((()=>(0,t.Lk)("label",{for:"password",class:"form-label"},"Password",-1))),ee=K((()=>(0,t.Lk)("button",{type:"submit",class:"btn btn-primary"},"Login",-1)));function ae(e,a,n,o,l,s){const i=(0,t.g2)("Navbar"),u=(0,t.g2)("router-link");return(0,t.uX)(),(0,t.CE)("div",null,[(0,t.bF)(i),q,(0,t.Lk)("form",{onSubmit:a[2]||(a[2]=(0,r.D$)(((...e)=>s.login&&s.login(...e)),["prevent"]))},[(0,t.Lk)("div",z,[G,(0,t.bo)((0,t.Lk)("input",{type:"text",class:"form-control",id:"username","onUpdate:modelValue":a[0]||(a[0]=e=>l.form.username=e)},null,512),[[r.Jo,l.form.username]])]),(0,t.Lk)("div",M,[Z,(0,t.bo)((0,t.Lk)("input",{type:"password",class:"form-control",id:"password","onUpdate:modelValue":a[1]||(a[1]=e=>l.form.password=e)},null,512),[[r.Jo,l.form.password]])]),ee],32),(0,t.Lk)("p",null,[(0,t.eW)("Don't have an account? "),(0,t.bF)(u,{to:"/register"},{default:(0,t.k6)((()=>[(0,t.eW)("Register")])),_:1})])])}var ne={name:"LoginPage",components:{Navbar:R},data(){return{form:{username:"",password:""}}},methods:{login(){}}};const re=(0,c.A)(ne,[["render",ae],["__scopeId","data-v-1c15b798"]]);var te=re;const oe=e=>((0,t.Qi)("data-v-3dd62d6e"),e=e(),(0,t.jt)(),e),le=oe((()=>(0,t.Lk)("h1",null,"Register",-1))),se={class:"mb-3"},ie=oe((()=>(0,t.Lk)("label",{for:"username",class:"form-label"},"Username",-1))),ue={class:"mb-3"},ce=oe((()=>(0,t.Lk)("label",{for:"email",class:"form-label"},"Email",-1))),me={class:"mb-3"},de=oe((()=>(0,t.Lk)("label",{for:"password",class:"form-label"},"Password",-1))),pe={class:"mb-3"},be=oe((()=>(0,t.Lk)("label",{for:"confirmPassword",class:"form-label"},"Confirm Password",-1))),fe=oe((()=>(0,t.Lk)("button",{type:"submit",class:"btn btn-primary"},"Register",-1)));function ve(e,a,n,o,l,s){const i=(0,t.g2)("Navbar"),u=(0,t.g2)("router-link");return(0,t.uX)(),(0,t.CE)("div",null,[(0,t.bF)(i),le,(0,t.Lk)("form",{onSubmit:a[4]||(a[4]=(0,r.D$)(((...e)=>s.register&&s.register(...e)),["prevent"]))},[(0,t.Lk)("div",se,[ie,(0,t.bo)((0,t.Lk)("input",{type:"text",class:"form-control",id:"username","onUpdate:modelValue":a[0]||(a[0]=e=>l.form.username=e)},null,512),[[r.Jo,l.form.username]])]),(0,t.Lk)("div",ue,[ce,(0,t.bo)((0,t.Lk)("input",{type:"email",class:"form-control",id:"email","onUpdate:modelValue":a[1]||(a[1]=e=>l.form.email=e)},null,512),[[r.Jo,l.form.email]])]),(0,t.Lk)("div",me,[de,(0,t.bo)((0,t.Lk)("input",{type:"password",class:"form-control",id:"password","onUpdate:modelValue":a[2]||(a[2]=e=>l.form.password=e)},null,512),[[r.Jo,l.form.password]])]),(0,t.Lk)("div",pe,[be,(0,t.bo)((0,t.Lk)("input",{type:"password",class:"form-control",id:"confirmPassword","onUpdate:modelValue":a[3]||(a[3]=e=>l.form.confirmPassword=e)},null,512),[[r.Jo,l.form.confirmPassword]])]),fe],32),(0,t.Lk)("p",null,[(0,t.eW)("Already have an account? "),(0,t.bF)(u,{to:"/login"},{default:(0,t.k6)((()=>[(0,t.eW)("Log in")])),_:1})])])}var ke={name:"RegisterPage",components:{Navbar:R},data(){return{form:{username:"",email:"",password:"",confirmPassword:""}}},methods:{register(){}}};const ge=(0,c.A)(ke,[["render",ve],["__scopeId","data-v-3dd62d6e"]]);var Le=ge;const he=e=>((0,t.Qi)("data-v-4ca97046"),e=e(),(0,t.jt)(),e),ye={key:0},Fe=he((()=>(0,t.Lk)("p",null,"You are a premium member!",-1))),we=[Fe],_e={key:1},Ue=he((()=>(0,t.Lk)("button",{type:"submit",class:"btn btn-primary"},"Buy Premium",-1))),Ce=[Ue];function Pe(e,a,n,o,l,s){const i=(0,t.g2)("Navbar");return(0,t.uX)(),(0,t.CE)("div",null,[(0,t.bF)(i),(0,t.Lk)("h2",null,"Hello, "+(0,b.v_)(l.currentUser.username),1),(0,t.Lk)("p",null,"Username: "+(0,b.v_)(l.currentUser.username),1),(0,t.Lk)("p",null,"Email: "+(0,b.v_)(l.currentUser.email),1),(0,t.Lk)("p",null,"Premium: "+(0,b.v_)(l.currentUser.premium?"Yes":"No"),1),l.currentUser.premium?((0,t.uX)(),(0,t.CE)("div",ye,we)):((0,t.uX)(),(0,t.CE)("div",_e,[(0,t.Lk)("form",{onSubmit:a[0]||(a[0]=(0,r.D$)(((...e)=>s.buyPremium&&s.buyPremium(...e)),["prevent"]))},Ce,32)]))])}var Ee={name:"ProfilePageComponent",components:{Navbar:R},data(){return{currentUser:{username:"",email:"",premium:!1}}},methods:{buyPremium(){}},mounted(){}};const Ae=(0,c.A)(Ee,[["render",Pe],["__scopeId","data-v-4ca97046"]]);var Xe=Ae;const We=e=>((0,t.Qi)("data-v-3dfa6a94"),e=e(),(0,t.jt)(),e),je=We((()=>(0,t.Lk)("h1",null,"Upload File",-1))),De={class:"mb-3"},Ne=We((()=>(0,t.Lk)("label",{for:"file",class:"form-label"},"File",-1))),Oe=We((()=>(0,t.Lk)("button",{type:"submit",class:"btn btn-primary"},"Upload",-1)));function xe(e,a,n,o,l,s){const i=(0,t.g2)("Navbar");return(0,t.uX)(),(0,t.CE)("div",null,[(0,t.bF)(i),je,(0,t.Lk)("form",{onSubmit:a[1]||(a[1]=(0,r.D$)(((...e)=>s.uploadFile&&s.uploadFile(...e)),["prevent"])),enctype:"multipart/form-data"},[(0,t.Lk)("div",De,[Ne,(0,t.Lk)("input",{type:"file",class:"form-control",id:"file",onChange:a[0]||(a[0]=(...e)=>s.handleFileUpload&&s.handleFileUpload(...e))},null,32)]),Oe],32)])}var Qe={name:"UploadPage",components:{Navbar:R},data(){return{selectedFile:null}},methods:{handleFileUpload(e){this.selectedFile=e.target.files[0]},uploadFile(){const e=new FormData;e.append("file",this.selectedFile)}}};const Se=(0,c.A)(Qe,[["render",xe],["__scopeId","data-v-3dfa6a94"]]);var Ie=Se;const Ve=[{path:"/",component:B},{path:"/login",component:te},{path:"/register",component:Le},{path:"/profile",component:Xe},{path:"/upload",component:Ie}],Je=(0,p.aE)({history:(0,p.LA)(),routes:Ve});var Te=Je;(0,r.Ef)(d).use(Te).mount("#app")}},a={};function n(r){var t=a[r];if(void 0!==t)return t.exports;var o=a[r]={exports:{}};return e[r](o,o.exports,n),o.exports}n.m=e,function(){var e=[];n.O=function(a,r,t,o){if(!r){var l=1/0;for(c=0;c<e.length;c++){r=e[c][0],t=e[c][1],o=e[c][2];for(var s=!0,i=0;i<r.length;i++)(!1&o||l>=o)&&Object.keys(n.O).every((function(e){return n.O[e](r[i])}))?r.splice(i--,1):(s=!1,o<l&&(l=o));if(s){e.splice(c--,1);var u=t();void 0!==u&&(a=u)}}return a}o=o||0;for(var c=e.length;c>0&&e[c-1][2]>o;c--)e[c]=e[c-1];e[c]=[r,t,o]}}(),function(){n.d=function(e,a){for(var r in a)n.o(a,r)&&!n.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:a[r]})}}(),function(){n.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"===typeof window)return window}}()}(),function(){n.o=function(e,a){return Object.prototype.hasOwnProperty.call(e,a)}}(),function(){var e={524:0};n.O.j=function(a){return 0===e[a]};var a=function(a,r){var t,o,l=r[0],s=r[1],i=r[2],u=0;if(l.some((function(a){return 0!==e[a]}))){for(t in s)n.o(s,t)&&(n.m[t]=s[t]);if(i)var c=i(n)}for(a&&a(r);u<l.length;u++)o=l[u],n.o(e,o)&&e[o]&&e[o][0](),e[o]=0;return n.O(c)},r=self["webpackChunkmy_vue_app"]=self["webpackChunkmy_vue_app"]||[];r.forEach(a.bind(null,0)),r.push=a.bind(null,r.push.bind(r))}();var r=n.O(void 0,[504],(function(){return n(240)}));r=n.O(r)})();
//# sourceMappingURL=app.1d7da78f.js.map