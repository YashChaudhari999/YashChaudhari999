```aura width=860 height=200
 <div style={{
 width: '100%', height: '100%', background: '#08080c',
 display: 'flex', alignItems: 'center', fontFamily: 'Inter',
 position: 'relative', overflow: 'hidden', borderRadius: 16,
 border: '1px solid rgba(110,80,220,0.18)'
}}>

 <style>
   {`
     @keyframes float-slow {
       0%, 100% { transform: translateX(0px); opacity: 0.8; }
       50% { transform: translateX(350px); opacity: 1.2; }
     }
     @keyframes float-medium {
       0%, 100% { transform: translateX(0px); opacity: 0.7; }
       50% { transform: translateX(-250px); opacity: 1.1; }
     }
     @keyframes float-fast {
       0%, 100% { transform: translateX(0px); opacity: 0.9; }
       50% { transform: translateX(200px); opacity: 0.6; }
     }
     @keyframes float-diagonal {
       0%, 100% { transform: translateX(0px); opacity: 0.75; }
       50% { transform: translateX(300px); opacity: 1.0; }
     }
     @keyframes float-wave {
       0%, 100% { transform: translateX(0px); opacity: 0.65; }
       33% { transform: translateX(-160px); opacity: 0.9; }
       66% { transform: translateX(80px); opacity: 1.0; }
     }
     @keyframes float-pulse {
       0%, 100% { transform: scale(1); opacity: 0.8; }
       50% { transform: scale(1.3); opacity: 0.4; }
     }
     #glow-1 { animation: float-slow 8s ease-in-out infinite; }
     #glow-2 { animation: float-medium 12s ease-in-out infinite; }
     #glow-3 { animation: float-fast 9s ease-in-out infinite; }
     #glow-4 { animation: float-slow 11s ease-in-out infinite reverse; }
     #glow-5 { animation: float-medium 14s ease-in-out infinite reverse; }
     #glow-6 { animation: float-diagonal 10s ease-in-out infinite; }
     #glow-7 { animation: float-wave 13s ease-in-out infinite; }
     #glow-8 { animation: float-pulse 7s ease-in-out infinite; }
   `}
 </style>

 <svg width="860" height="200" style={{ position: 'absolute', top: 0, left: 0 }}>
   <defs>
     <radialGradient id="g1" cx="50%" cy="50%" r="50%">
       <stop offset="0%" stopColor="rgba(110,20,210,0.72)" />
       <stop offset="40%" stopColor="rgba(90,15,180,0.35)" />
       <stop offset="70%" stopColor="rgba(90,15,180,0)" />
     </radialGradient>
     <radialGradient id="g2" cx="50%" cy="50%" r="50%">
       <stop offset="0%" stopColor="rgba(40,60,255,0.6)" />
       <stop offset="45%" stopColor="rgba(30,50,200,0.25)" />
       <stop offset="70%" stopColor="rgba(30,50,200,0)" />
     </radialGradient>
     <radialGradient id="g3" cx="50%" cy="50%" r="50%">
       <stop offset="0%" stopColor="rgba(0,130,255,0.45)" />
       <stop offset="50%" stopColor="rgba(0,100,220,0.18)" />
       <stop offset="70%" stopColor="rgba(0,100,220,0)" />
     </radialGradient>
     <radialGradient id="g4" cx="50%" cy="50%" r="50%">
       <stop offset="0%" stopColor="rgba(0,190,230,0.32)" />
       <stop offset="70%" stopColor="rgba(0,190,230,0)" />
     </radialGradient>
     <radialGradient id="g5" cx="50%" cy="50%" r="50%">
       <stop offset="0%" stopColor="rgba(90,30,200,0.38)" />
       <stop offset="70%" stopColor="rgba(90,30,200,0)" />
     </radialGradient>
     <radialGradient id="g6" cx="50%" cy="50%" r="50%">
       <stop offset="0%" stopColor="rgba(160,30,255,0.55)" />
       <stop offset="45%" stopColor="rgba(130,20,220,0.22)" />
       <stop offset="70%" stopColor="rgba(130,20,220,0)" />
     </radialGradient>
     <radialGradient id="g7" cx="50%" cy="50%" r="50%">
       <stop offset="0%" stopColor="rgba(20,60,255,0.42)" />
       <stop offset="50%" stopColor="rgba(10,40,200,0.16)" />
       <stop offset="70%" stopColor="rgba(10,40,200,0)" />
     </radialGradient>
     <radialGradient id="g8" cx="50%" cy="50%" r="50%">
       <stop offset="0%" stopColor="rgba(0,170,255,0.40)" />
       <stop offset="50%" stopColor="rgba(0,130,220,0.15)" />
       <stop offset="70%" stopColor="rgba(0,130,220,0)" />
     </radialGradient>
   </defs>

   <ellipse id="glow-1" cx="180" cy="230" rx="260" ry="190" fill="url(#g1)" />
   <ellipse id="glow-2" cx="300" cy="240" rx="220" ry="160" fill="url(#g2)" />
   <ellipse id="glow-3" cx="420" cy="240" rx="180" ry="140" fill="url(#g3)" />
   <ellipse id="glow-4" cx="550" cy="250" rx="150" ry="120" fill="url(#g4)" />
   <ellipse id="glow-5" cx="750" cy="250" rx="130" ry="110" fill="url(#g5)" />
   <ellipse id="glow-6" cx="300" cy="240" rx="180" ry="140" fill="url(#g6)" />
   <ellipse id="glow-7" cx="490" cy="230" rx="220" ry="170" fill="url(#g7)" />
   <ellipse id="glow-8" cx="590" cy="250" rx="150" ry="130" fill="url(#g8)" />
 </svg>

 <div style={{
   position: 'absolute', left: 48, top: 52, width: 96, height: 96,
   borderRadius: 48, background: 'linear-gradient(135deg, #6622ee, #0088ff)',
   display: 'flex', alignItems: 'center', justifyContent: 'center',
 }}>
   <img src={github.user.avatarUrl} width={88} height={88} style={{ borderRadius: 44 }} />
 </div>

 <div style={{ display:'flex', flexDirection:'column', marginLeft:168, gap:8, zIndex: 10 }}>
   <div style={{ display:'flex', fontSize:38, fontWeight:800, color:'#ffffff', letterSpacing:'-1px', lineHeight:1 }}>
     Yash Chaudhari
   </div>
   <div style={{ display:'flex', fontSize:15, color:'rgba(180,165,255,0.8)', fontWeight:400, letterSpacing:'0.3px' }}>
     IT Undergraduate · Full-Stack Developer · Open Source Builder
   </div>
   <div style={{ display:'flex', gap:8, marginTop:6 }}>
     {['Java', 'Node.js', 'PHP', 'Python', 'MySQL'].map(function(tag) {
       return (
         <div key={tag} style={{
           display:'flex', padding:'4px 12px', borderRadius:20,
           background:'rgba(80,40,220,0.18)', border:'1px solid rgba(100,70,240,0.32)',
           color:'rgba(205,195,255,0.85)', fontSize:12, fontWeight:600,
         }}>{tag}</div>
       );
     })}
   </div>
 </div>
</div>
```

```aura width=860 height=140
(function() {
 var stats = [
   { label: 'Repos', value: String(github.stats.totalRepos), color: '#a78bfa' },
   { label: 'Stars', value: String(github.stats.totalStars), color: '#60a5fa' },
   { label: 'Commits', value: String(github.stats.totalCommits), color: '#f59e0b' },
 ];

 return (
   <div style={{
     width: '100%', height: '100%',
     background: '#08080c',
     display: 'flex', alignItems: 'center', justifyContent: 'center',
     fontFamily: 'Inter', borderRadius: 16,
     border: '1px solid rgba(110,80,220,0.18)',
     position: 'relative', overflow: 'hidden',
   }}>

     <style>
       {`
         @keyframes float-slow {
           0%, 100% { transform: translateX(0px); opacity: 0.8; }
           50% { transform: translateX(350px); opacity: 1.2; }
         }
         @keyframes float-medium {
           0%, 100% { transform: translateX(0px); opacity: 0.7; }
           50% { transform: translateX(-250px); opacity: 1.1; }
         }
         @keyframes float-fast {
           0%, 100% { transform: translateX(0px); opacity: 0.9; }
           50% { transform: translateX(200px); opacity: 0.6; }
         }
         @keyframes float-diagonal {
           0%, 100% { transform: translate(0px, 0px); opacity: 0.75; }
           50% { transform: translate(120px, 30px); opacity: 1.0; }
         }
         @keyframes float-wave {
           0%, 100% { transform: translateX(0px); opacity: 0.65; }
           33% { transform: translateX(-160px); opacity: 0.9; }
           66% { transform: translateX(80px); opacity: 1.0; }
         }
         @keyframes float-pulse {
           0%, 100% { transform: scale(1); opacity: 0.8; }
           50% { transform: scale(1.3); opacity: 0.4; }
         }
         #glow-1 { animation: float-slow 8s ease-in-out infinite; }
         #glow-2 { animation: float-medium 12s ease-in-out infinite; }
         #glow-3 { animation: float-fast 9s ease-in-out infinite; }
         #glow-4 { animation: float-diagonal 10s ease-in-out infinite; }
         #glow-5 { animation: float-wave 14s ease-in-out infinite; }
       `}
     </style>

     <svg width="860" height="140" style={{ position: 'absolute', top: 0, left: 0 }}>
       <defs>
         <radialGradient id="g1" cx="50%" cy="50%" r="50%">
           <stop offset="0%" stopColor="rgba(110,20,210,0.65)" />
           <stop offset="45%" stopColor="rgba(80,15,170,0.28)" />
           <stop offset="70%" stopColor="rgba(80,15,170,0)" />
         </radialGradient>
         <radialGradient id="g2" cx="50%" cy="50%" r="50%">
           <stop offset="0%" stopColor="rgba(40,70,255,0.55)" />
           <stop offset="45%" stopColor="rgba(20,50,200,0.22)" />
           <stop offset="70%" stopColor="rgba(20,50,200,0)" />
         </radialGradient>
         <radialGradient id="g3" cx="50%" cy="50%" r="50%">
           <stop offset="0%" stopColor="rgba(0,140,255,0.42)" />
           <stop offset="70%" stopColor="rgba(0,140,255,0)" />
         </radialGradient>
         <radialGradient id="g4" cx="50%" cy="50%" r="50%">
           <stop offset="0%" stopColor="rgba(0,195,235,0.30)" />
           <stop offset="70%" stopColor="rgba(0,195,235,0)" />
         </radialGradient>
         <radialGradient id="g5" cx="50%" cy="50%" r="50%">
           <stop offset="0%" stopColor="rgba(100,30,210,0.40)" />
           <stop offset="70%" stopColor="rgba(100,30,210,0)" />
         </radialGradient>
       </defs>
       <ellipse id="glow-1" cx="710" cy="150" rx="210" ry="150" fill="url(#g1)" />
       <ellipse id="glow-2" cx="550" cy="140" rx="190" ry="140" fill="url(#g2)" />
       <ellipse id="glow-3" cx="400" cy="130" rx="170" ry="130" fill="url(#g3)" />
       <ellipse id="glow-4" cx="250" cy="140" rx="150" ry="120" fill="url(#g4)" />
       <ellipse id="glow-5" cx="100" cy="150" rx="130" ry="110" fill="url(#g5)" />
     </svg>

     {stats.map(function(s, i) {
       return (
         <div key={s.label} style={{
           flexGrow: 1, display: 'flex', flexDirection: 'column',
           alignItems: 'center', justifyContent: 'center',
           padding: '16px 8px',
           borderRight: i < stats.length - 1 ? '1px solid rgba(255,255,255,0.06)' : 'none',
           gap: 5,
         }}>
           <div style={{ display:'flex', fontSize:30, fontWeight:800, color:s.color, lineHeight:1 }}>
             {s.value}
           </div>
           <div style={{ display:'flex', fontSize:11, color:'rgba(200,195,225,0.45)', fontWeight:600, letterSpacing:'1.5px' }}>
             {s.label.toUpperCase()}
           </div>
         </div>
       );
     })}
   </div>
 );
})()
```

```aura width=860 height=220
(function() {
 var categories = [
   { title: 'Languages', color: '#a78bfa', items: ['Java', 'JavaScript', 'Python', 'PHP', 'TypeScript', 'HTML/CSS'] },
   { title: 'Backend',   color: '#60a5fa', items: ['Node.js', 'Express.js', 'Advanced Java'] },
   { title: 'Frontend',  color: '#34d399', items: ['React', 'HTML5', 'CSS3', 'Bootstrap'] },
   { title: 'Databases', color: '#f59e0b', items: ['MySQL', 'MongoDB'] },
 ];

 return (
   <div style={{
     width: '100%', height: '100%',
     background: '#08080c',
     display: 'flex', flexDirection: 'column',
     fontFamily: 'Inter', padding: '18px 32px', gap: 12,
     borderRadius: 16, border: '1px solid rgba(110,80,220,0.18)',
     position: 'relative', overflow: 'hidden',
   }}>

     <style>
       {`
         @keyframes float-slow {
           0%, 100% { transform: translateX(0px); opacity: 0.8; }
           50% { transform: translateX(350px); opacity: 1.2; }
         }
         @keyframes float-medium {
           0%, 100% { transform: translateX(0px); opacity: 0.7; }
           50% { transform: translateX(-250px); opacity: 1.1; }
         }
         @keyframes float-fast {
           0%, 100% { transform: translateX(0px); opacity: 0.9; }
           50% { transform: translateX(200px); opacity: 0.6; }
         }
         #glow-1 { animation: float-slow 9s ease-in-out infinite; }
         #glow-2 { animation: float-medium 12s ease-in-out infinite; }
         #glow-3 { animation: float-fast 8s ease-in-out infinite; }
       `}
     </style>

     <svg width="860" height="220" style={{ position: 'absolute', top: 0, left: 0 }}>
       <defs>
         <radialGradient id="g1" cx="50%" cy="50%" r="50%">
           <stop offset="0%" stopColor="rgba(115,20,215,0.68)" />
           <stop offset="42%" stopColor="rgba(85,15,175,0.30)" />
           <stop offset="70%" stopColor="rgba(85,15,175,0)" />
         </radialGradient>
         <radialGradient id="g2" cx="50%" cy="50%" r="50%">
           <stop offset="0%" stopColor="rgba(55,55,255,0.55)" />
           <stop offset="45%" stopColor="rgba(35,45,210,0.22)" />
           <stop offset="70%" stopColor="rgba(35,45,210,0)" />
         </radialGradient>
         <radialGradient id="g3" cx="50%" cy="50%" r="50%">
           <stop offset="0%" stopColor="rgba(0,130,255,0.42)" />
           <stop offset="70%" stopColor="rgba(0,100,220,0)" />
         </radialGradient>
       </defs>
       <ellipse id="glow-1" cx="170" cy="220" rx="260" ry="170" fill="url(#g1)" />
       <ellipse id="glow-2" cx="430" cy="220" rx="220" ry="140" fill="url(#g2)" />
       <ellipse id="glow-3" cx="720" cy="220" rx="190" ry="130" fill="url(#g3)" />
     </svg>

     <div style={{ display:'flex', fontSize:10, fontWeight:700, color:'rgba(155,140,210,0.5)', letterSpacing:'3px' }}>
       TECH STACK
     </div>
     <div style={{ display:'flex', flexDirection:'column', gap:12 }}>
       {categories.map(function(cat) {
         return (
           <div key={cat.title} style={{ display:'flex', alignItems:'center', gap:16 }}>
             <div style={{ display:'flex', fontSize:10, fontWeight:700, color:cat.color, letterSpacing:'1px', width:80 }}>
               {cat.title.toUpperCase()}
             </div>
             <div style={{ display:'flex', flexWrap:'wrap', gap:7 }}>
               {cat.items.map(function(item) {
                 return (
                   <div key={item} style={{
                     display:'flex', padding:'4px 13px', borderRadius:6,
                     background:cat.color + '15', border:'1px solid ' + cat.color + '35',
                     color:'rgba(225,220,255,0.85)', fontSize:12, fontWeight:600,
                   }}>{item}</div>
                 );
               })}
             </div>
           </div>
         );
       })}
     </div>
   </div>
 );
})()
```

```aura width=860 height=200
(function() {
 // ── Language → color map (GitHub's official language colors) ──
 var LANG_COLORS = {
   'JavaScript': '#f1e05a',
   'TypeScript': '#3178c6',
   'Python':     '#3572A5',
   'Java':       '#b07219',
   'PHP':        '#4F5D95',
   'HTML':       '#e34c26',
   'CSS':        '#563d7c',
   'C':          '#555555',
   'C++':        '#f34b7d',
   'C#':         '#178600',
   'Go':         '#00ADD8',
   'Rust':       '#dea584',
   'Ruby':       '#701516',
   'Swift':      '#F05138',
   'Kotlin':     '#A97BFF',
   'Shell':      '#89e051',
   'Vue':        '#41b883',
   'Dart':       '#00B4AB',
   'Node.js':    '#68a063',
 };

 // ── Dynamic: top-3 repos by stars (auto-sorted by GitHub API) ──
 var rawRepos = (github.repos || []).slice(0, 3);

 var projects = rawRepos.map(function(r) {
   var lang = r.language || 'Code';
   return {
     name: r.name,
     desc: r.description || 'No description provided.',
     lang: lang,
     langColor: LANG_COLORS[lang] || '#6e50dc',
     link: r.url || ('https://github.com/YashChaudhari999/' + r.name),
   };
 });

 return (
   <div style={{
     width: '100%', height: '100%',
     background: '#08080c',
     display: 'flex', flexDirection: 'column',
     fontFamily: 'Inter', padding: '18px 32px', gap: 10,
     borderRadius: 16, border: '1px solid rgba(110,80,220,0.18)',
     position: 'relative', overflow: 'hidden',
   }}>

     <svg width="860" height="200" style={{ position: 'absolute', top: 0, left: 0 }}>
       <defs>
         <radialGradient id="pg1" cx="50%" cy="50%" r="50%">
           <stop offset="0%" stopColor="rgba(110,20,210,0.5)" />
           <stop offset="70%" stopColor="rgba(110,20,210,0)" />
         </radialGradient>
         <radialGradient id="pg2" cx="50%" cy="50%" r="50%">
           <stop offset="0%" stopColor="rgba(0,140,255,0.35)" />
           <stop offset="70%" stopColor="rgba(0,140,255,0)" />
         </radialGradient>
       </defs>
       <ellipse cx="100" cy="200" rx="240" ry="160" fill="url(#pg1)" />
       <ellipse cx="750" cy="200" rx="200" ry="140" fill="url(#pg2)" />
     </svg>

     <div style={{ display:'flex', fontSize:10, fontWeight:700, color:'rgba(155,140,210,0.5)', letterSpacing:'3px' }}>
       FEATURED PROJECTS
     </div>

     <div style={{ display:'flex', gap:16, zIndex:10 }}>
       {projects.map(function(p) {
         return (
           <div key={p.name} style={{
             flex:1, display:'flex', flexDirection:'column', gap:6,
             padding:'12px 16px', borderRadius:10,
             background:'rgba(255,255,255,0.03)',
             border:'1px solid rgba(110,80,220,0.15)',
           }}>
             <div style={{ display:'flex', alignItems:'center', justifyContent:'space-between' }}>
               <div style={{ display:'flex', fontSize:13, fontWeight:700, color:'#e0d8ff' }}>{p.name}</div>
               <div style={{
                 display:'flex', padding:'2px 9px', borderRadius:20,
                 background: p.langColor + '22', border:'1px solid ' + p.langColor + '55',
                 color: p.langColor, fontSize:10, fontWeight:700,
               }}>{p.lang}</div>
             </div>
             <div style={{ display:'flex', fontSize:11, color:'rgba(180,170,220,0.6)', lineHeight:1.5 }}>
               {p.desc}
             </div>
           </div>
         );
       })}
     </div>
   </div>
 );
})()
```

```aura width=140 height=44 link="https://www.linkedin.com/in/yashchaudhari500/" inline align=center
<SocialMediaButton
  icon="https://raw.githubusercontent.com/collectioneur/collectioneur/main/icons/linkedin-icon.png"
  text="LinkedIn"
  backgroundColor="#000000"
  width={140}
  height={44}
  gradientStops={[
    { offset: '0%', color: '#b57af9' },
    { offset: '30%', color: '#000000' },
    { offset: '60%', color: '#9d6bf0' },
    { offset: '80%', color: '#000000' },
    { offset: '100%', color: '#c89dfb' },
  ]}
/>
```

```aura width=130 height=44 link="mailto:yashchaudhari500@gmail.com" inline align=center
<SocialMediaButton
  icon="https://raw.githubusercontent.com/collectioneur/collectioneur/main/icons/gmail-icon.svg"
  text="Email"
  backgroundColor="#000000"
  width={130}
  height={44}
  gradientStops={[
    { offset: '0%', color: '#d855f7' },
    { offset: '30%', color: '#000000' },
    { offset: '60%', color: '#b557e8' },
    { offset: '80%', color: '#000000' },
    { offset: '100%', color: '#cc6ef9' },
  ]}
/>
```

```aura width=150 height=44 link="https://yashchaudhari.me/" inline align=center
<SocialMediaButton
  icon="https://raw.githubusercontent.com/collectioneur/collectioneur/main/icons/x-icon.svg"
  text="Portfolio"
  backgroundColor="#000000"
  width={150}
  height={44}
  gradientStops={[
    { offset: '0%', color: '#60a5fa' },
    { offset: '30%', color: '#000000' },
    { offset: '60%', color: '#3b82f6' },
    { offset: '80%', color: '#000000' },
    { offset: '100%', color: '#93c5fd' },
  ]}
/>
```

<br>
<p align="center"><sub>𝗉𝗈𝗐𝖾𝗋𝖾𝖽 𝖻𝗒 <a href="https://github.com/collectioneur/readme-aura">𝗋𝖾𝖺𝖽𝗆𝖾-𝖺𝗎𝗋𝖺</a></sub></p>