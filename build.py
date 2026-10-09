# Static page builder for the Apex Auto Body Specialists concept. Run: python3 build.py
import json
BASE = 'https://apex-auto-body-specialists-demo.vercel.app/'  # Vercel production URL
TEL, TEL_H = '+19193637995', '(919) 363&#8209;7995'
EXA = 'https://exa.ai/library/place/lfn11r5c263'
LAW = 'https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_58/GS_58-3-180.html'
MAP = 'https://www.google.com/maps/search/?api=1&query=Apex+Auto+Body+Specialists+2465+Reliance+Ave+Apex+NC+27539'
ORG = {"@context":"https://schema.org","@type":"AutoBodyShop","name":"Apex Auto Body Specialists",
 "url":BASE,"telephone":"+1-919-363-7995","email":"aabsdesk@gmail.com","faxNumber":"+1-919-363-9861",
 "founder":{"@type":"Person","name":"Darin Fridley"},
 "address":{"@type":"PostalAddress","streetAddress":"2465 Reliance Ave","addressLocality":"Apex","addressRegion":"NC","postalCode":"27539","addressCountry":"US"},
 "geo":{"@type":"GeoCoordinates","latitude":35.716429,"longitude":-78.82033},
 "openingHours":"Mo-Fr 09:00-17:00","areaServed":["Apex, NC","Cary, NC","Holly Springs, NC"],
 "sameAs":["https://facebook.com/1422782404666459"],
 "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.7","reviewCount":"152"}}

def K(t, cls=''): return f'<p class="kicker {cls}">{t}</p>'
def PIN(cls=''): return f'<span class="pin {cls}" aria-hidden="true"></span>'

HEAD = '''<!doctype html><html lang="en" class="no-js"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Apex Auto Body Specialists (concept)"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{url}"><meta property="og:image" content="{base}og.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{base}og.png">
<meta name="robots" content="noindex, nofollow"><!-- concept demo, not for indexing -->
<meta name="theme-color" content="#15171b">
<link rel="preload" as="font" type="font/woff2" href="fonts/chakra-petch-normal-700-latin.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="fonts/source-sans-3-normal-400-700-latin.woff2" crossorigin>
<link rel="stylesheet" href="css/design-system.css"><link rel="stylesheet" href="css/components.css"><link rel="stylesheet" href="css/pages.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%2315171b'/%3E%3Cpath d='M4 22h24' stroke='%233b7be0' stroke-width='2'/%3E%3Cpath d='M4 26h24' stroke='%23f0642a' stroke-width='2'/%3E%3Ctext x='16' y='17' font-family='Arial' font-weight='700' font-size='11' fill='%23fff' text-anchor='middle'%3EAABS%3C/text%3E%3C/svg%3E">
<script>document.documentElement.classList.replace('no-js','js-ready')</script><script type="application/ld+json">{ld}</script></head><body>
<a class="skip" href="#main">Skip to content</a>
<div class="demo-bar">Concept by <a href="https://luminarch.pro">LuminArch</a>. Not an official Apex Auto Body Specialists site; the old domain has lapsed. Reviews are real and sourced; placeholders are labeled.</div>
<header class="top"><div class="wrap nav"><a class="mark" href="index.html"><span class="mk" aria-hidden="true">AA</span><span><b>Apex Auto Body Specialists</b><small>Independent collision repair &middot; Apex, NC</small></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button><ul id="menu">{nav}</ul><a class="btn btn--go btn--call" href="tel:{tel}"><span class="cl-full">{telh}</span><span class="cl-short">Call</span></a></div></header><main id="main">'''

FOOT = f'''</main><footer class="site-foot">{PIN()}<div class="wrap">
<div class="sign">
 <p class="sign-k">Had a wreck?</p>
 <p class="sign-h">Call the shop before you call it settled.</p>
 <a class="sign-num" href="tel:{TEL}">{TEL_H}</a>
 <p class="sign-sub">Monday to Friday, 9am to 5pm &middot; 2465 Reliance Ave, Apex, NC 27539</p>
</div>
<div class="foot-grid">
 <p class="foot-quote">&ldquo;Committed to you the Customer not the Insurance Company!&rdquo;<span>The shop&rsquo;s own line, from its old website (archived 2018)</span></p>
 <nav aria-label="Footer"><a href="services.html">Repairs</a><a href="your-rights.html">Your rights</a><a href="reviews.html">Reviews</a><a href="about.html">About Darin</a><a href="contact.html">Estimate</a><a href="mailto:aabsdesk@gmail.com">Email the desk</a></nav>
</div>
<div class="foot-row"><span>Apex Auto Body Specialists Inc. &middot; Apex, North Carolina</span><span>Concept by <a href="https://luminarch.pro">LuminArch</a></span></div></div></footer>
<script src="js/main.js"></script></body></html>'''

NAV = [('services.html','Repairs'),('your-rights.html','Your rights'),('reviews.html','Reviews'),('about.html','About'),('contact.html','Estimate')]
def bc(*n): return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":a,"item":BASE+b} for i,(a,b) in enumerate(n)]}
def page(fn, t, d, body, ld=None):
    assert 50 <= len(t) <= 60, (fn, len(t), t)
    assert 140 <= len(d) <= 160, (fn, len(d), d)
    nav = ''.join(f'<li><a href="{h}"' + (' aria-current="page"' if h == fn else '') + f'>{n}</a></li>' for h, n in NAV)
    url = BASE + ('' if fn == 'index.html' else fn)
    open(fn,'w').write(HEAD.format(t=t,d=d,url=url,base=BASE,nav=nav,ld=json.dumps(ld or [ORG]),tel=TEL,telh=TEL_H) + body + FOOT)

# Google reviews, word for word, from the Exa place page (Google listing data, checked 9 Oct 2026). All 5 out of 5.
# Not used on purpose: five generic reviews all posted 2026-02-20 (same day, no names, no cars). See FACTS_LOG.md.
REV = [
 ('2026-02-27','Feb 2026','We brought Apex Auto Body Specialist our older Mazda CX5 with some front fender damage. They did a PHENOMENAL job with the repair and we could not be happier! Thank you so much!!','Mazda CX5 &middot; front fender'),
 ('2026-02-11','Feb 2026','If I could rate 10 stars I would! Darren and his crew are awesome! Frankie painted my 2 door Ford Bronco and did an AMAZING job!!! He paid attention to every single detail! I highly recommend this place!','Ford Bronco &middot; paint'),
 ('2025-09-15','Sep 2025','Thank goodness I found this place!! After I was quoted something ridiculous at [another shop] for a detached fender, I decided to take my van to Apex Auto Body Specialist where I met Darren. Darren took one look at my fender and said &ldquo;we can take care of that no problem&rdquo;. And they did! Service was fast and friendly. I highly recommend everyone start here to avoid being overcharged. Thank you!','Van &middot; detached fender'),
]
# NB: [another shop] replaces a national chain the reviewer named. Reviewers spell the owner "Darren"; NC records spell it Darin.
def rcard(r, cls=''):
    iso,d,txt,job = r
    return (f'<figure class="rcard rv {cls}"><div class="rc-top"><span>{job}</span><span class="stars" aria-label="5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</span></div>'
            f'<blockquote><p>{txt}</p></blockquote><figcaption>Google review &middot; <time datetime="{iso}">{d}</time></figcaption></figure>')

STEPS = [('Call or email the desk','(919) 363&#8209;7995 or aabsdesk@gmail.com. Photos of the damage help.'),
 ('Get the estimate','The old site offered free computerized estimates; ask Darin how it works today.'),
 ('Tell your insurer where the car is going','NC law says the choice is yours. Your insurer still pays what it owes.'),
 ('Repair and paint','Body work, paint and refinish in the shop on Reliance Ave.'),
 ('Pick it up','Monday to Friday, 9 to 5.')]

# ---------- HOME ----------
page('index.html','Apex Auto Body Specialists | Collision Repair in Apex, NC',
 'Independent collision repair in Apex, NC since 2003. Darin Fridley and his crew on Reliance Ave fix fenders, paint and body damage. 4.7 on Google. Call today.', f'''
<section class="hero on-dark"><div class="wrap hero-grid">
 <div class="hero-copy">{K('Independent collision repair &middot; Apex, NC')}
  <h1>You pick the body shop. <em>Not your insurance company.</em></h1>
  <p class="lede">Darin Fridley&rsquo;s independent shop has done collision repair, body work and paint in Apex since 2003. North Carolina law says the car goes where you send it.</p>
  <div class="cta"><a class="btn btn--go" href="tel:{TEL}">Call {TEL_H}</a><a class="btn btn--line" href="contact.html">Start an estimate</a></div>
  <dl class="hero-facts"><div><dt>Google</dt><dd><b>4.7</b> <span class="stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span> 152 reviews</dd></div><div><dt>Hours</dt><dd>Mon to Fri, 9 to 5</dd></div><div><dt>Shop</dt><dd>2465 Reliance Ave</dd></div></dl>
 </div>
 <aside class="statute" aria-labelledby="st-h">
  <p class="st-k">Margin note</p>
  <p id="st-h" class="st-cite">N.C. Gen. Stat. &sect; 58&#8209;3&#8209;180(a)</p>
  <blockquote class="st-q"><p>&ldquo;A policy covering damage to a motor vehicle shall allow the claimant to select the repair service or source for the repair of the damage.&rdquo;</p></blockquote>
  <p class="st-plain">In plain words: your insurer can recommend a shop. It can&rsquo;t make you use it.</p>
  <a class="st-link" href="your-rights.html">What else the law says &rarr;</a>
 </aside>
</div>{PIN('pin--hero')}</section>

<section class="why wrap" aria-labelledby="why-h">
 <div class="why-head rv">{K('Why it matters')}<h2 id="why-h">The shop works for the person who owns the car.</h2></div>
 <div class="why-grid">
  <div class="why-copy rv"><p>Apex Auto Body Specialists has billed itself as an independent shop for years. Its old website put it bluntly: <q>Work for you (the insured or claimant), not the Insurance Company.</q></p>
  <p>It also said the shop works with the major insurance companies, just not under contract to them. That means you bring the estimate, the photos and the claim number, and Darin&rsquo;s crew fixes the car.</p>
  <p class="fine">Quotes in this section are from the shop&rsquo;s own website as archived in 2018. Worth confirming with Darin that it still runs this way.</p></div>
  <ol class="why-list rv">{''.join(f'<li><span class="wl-n">{i+1:02d}</span><b>{a}</b><span>{b}</span></li>' for i,(a,b) in enumerate(STEPS))}</ol>
 </div>
</section>

<section class="board on-dark" aria-labelledby="bd-h"><div class="wrap">
 <div class="board-head rv">{K('What they fix')}<h2 id="bd-h">Dents to frames. Domestic and import.</h2></div>
 <ul class="board-list">
  <li class="rv"><a href="services.html#collision"><b>Collision repair</b><span>Front, rear, side. The core of the shop.</span></a></li>
  <li class="rv"><a href="services.html#paint"><b>Body work and paint</b><span>Panels, bumpers, full refinish. A Bronco in the reviews.</span></a></li>
  <li class="rv"><a href="services.html#hail"><b>Hail damage</b><span>Dents from the spring storms.</span></a></li>
  <li class="rv"><a href="services.html#scratch"><b>Scratches and scuffs</b><span>Parking lot damage, keyed doors.</span></a></li>
  <li class="rv"><a href="services.html#interior"><b>Interior repair</b><span>Listed on the shop&rsquo;s directory profiles.</span></a></li>
  <li class="rv"><a href="services.html#protect"><b>Appearance and protection</b><span>Listed on the shop&rsquo;s directory profiles.</span></a></li>
 </ul>
</div></section>

<section class="voices wrap" aria-labelledby="vo-h">
 <div class="voices-head rv">{K('What customers say')}<h2 id="vo-h">152 Google reviews. Here is what they keep saying.</h2>{PIN('pin--short')}</div>
 <div class="voices-grid">{rcard(REV[1],'rcard--lead')}{rcard(REV[0])}{rcard(REV[2])}</div>
 <a class="btn btn--line rv" href="reviews.html">More reviews</a>
</section>

<section class="shop wrap" aria-labelledby="sh-h">
 <div class="phbox rv"><p><span class="ph">Placeholder</span> Photo of the shop front on Reliance Ave, or Frankie in the paint booth. The shop&rsquo;s Facebook page is the first place to look.</p></div>
 <div class="shop-copy rv">{K('Where')}<h2 id="sh-h">On Reliance Ave in Apex.</h2>
 <p>2465 Reliance Ave, Apex, NC 27539. Open Monday to Friday, 9am to 5pm. Closed weekends.</p>
 <p><a class="tlink" href="{MAP}" rel="noopener">Directions in Google Maps</a></p></div>
</section>
''', ld=[ORG, bc(('Home',''))])

# ---------- SERVICES ----------
SV = [('collision','Collision repair','Front end, rear end and side damage, domestic and import. The old site advertised computerized collision repair equipment and frame repair.',REV[0]),
 ('paint','Body work and paint','Panel repair, bumpers and refinish. A Google reviewer had Frankie paint a two door Ford Bronco.',REV[1]),
 ('hail','Hail damage repair','Listed on the shop&rsquo;s directory profiles.',None),
 ('scratch','Scratch removal','Listed on the shop&rsquo;s directory profiles.',None),
 ('interior','Interior repair','Listed on the shop&rsquo;s directory profiles.',None),
 ('protect','Appearance and protection','Listed on the shop&rsquo;s directory profiles.',None)]
def sv(i,s):
    k,n,d,r = s
    side = (f'<blockquote class="sv-q"><p>{r[2]}</p><footer>Google review, {r[1]}</footer></blockquote>' if r else
            '<p class="note"><span class="ph">Placeholder</span> A before and after pair from this kind of job, and one sentence from Darin on how the shop handles it.</p>')
    return f'<article id="{k}" class="sv rv"><span class="sv-n">{i+1:02d}</span><div class="sv-body"><h2>{n}</h2><p>{d}</p></div>{side}</article>'
page('services.html','Collision Repair and Paint Services | Apex Auto Body, NC',
 'Collision repair, body work and paint, hail damage, scratch removal and interior repair at Apex Auto Body Specialists on Reliance Ave in Apex, North Carolina.', f'''
<section class="sub on-dark"><div class="wrap">{K('Repairs')}<h1>What the shop fixes.</h1><p class="lede">Taken from the shop&rsquo;s directory listings and its old website. Nothing here is a guarantee; Darin will tell you what your car needs.</p></div>{PIN('pin--hero')}</section>
<section class="wrap svs">{''.join(sv(i,s) for i,s in enumerate(SV))}</section>
<section class="wrap band rv"><h2>Not sure if it&rsquo;s worth fixing?</h2><p>Send photos and the insurer&rsquo;s estimate, if you have one. The desk will tell you what it looks like.</p><a class="btn btn--go" href="contact.html">Start an estimate</a></section>
''', ld=[ORG, bc(('Home',''),('Repairs','services.html'))])

# ---------- YOUR RIGHTS ----------
page('your-rights.html','Your Right to Choose a Body Shop in NC | Apex Auto Body',
 'North Carolina law lets you choose who repairs your car after a claim. Here is what N.C. Gen. Stat. 58-3-180 says in plain words, from an independent Apex shop.', f'''
<section class="sub on-dark"><div class="wrap">{K('Your rights')}<h1>The law, in plain words.</h1><p class="lede">This is the statute Apex Auto Body Specialists points customers to. Quoted from the North Carolina General Assembly. Not legal advice.</p></div>{PIN('pin--hero')}</section>
<section class="wrap law">
 <article class="law-row rv"><p class="law-c">&sect; 58&#8209;3&#8209;180(a)</p><blockquote><p>&ldquo;A policy covering damage to a motor vehicle shall allow the claimant to select the repair service or source for the repair of the damage.&rdquo;</p></blockquote><p class="law-p">You choose the shop.</p></article>
 <article class="law-row rv"><p class="law-c">&sect; 58&#8209;3&#8209;180(b)</p><blockquote><p>&ldquo;The amount determined by the insurer to be payable under a policy covering damage to a motor vehicle shall be paid regardless of the repair service or source selected by the claimant.&rdquo;</p></blockquote><p class="law-p">Your insurer pays the same either way.</p></article>
 <article class="law-row rv"><p class="law-c">&sect; 58&#8209;3&#8209;180(b1)</p><blockquote><p>&ldquo;No insurer shall require that the insured or claimant must have a damaged vehicle repaired at an insurer&#8209;owned motor vehicle repair service.&rdquo;</p></blockquote><p class="law-p">If they recommend a shop, they have to tell you that you don&rsquo;t have to use it, and whether they have a financial interest in it.</p></article>
 <p class="fine rv">Source: <a href="{LAW}" rel="noopener">N.C. Gen. Stat. &sect; 58&#8209;3&#8209;180, ncleg.gov</a>. Read the full text for the details.</p>
</section>
<section class="wrap band rv"><h2>Already have an insurer&rsquo;s estimate?</h2><p>Bring it, or email it to the desk with photos.</p><a class="btn btn--go" href="contact.html">Send it over</a></section>
''', ld=[ORG, bc(('Home',''),('Your rights','your-rights.html'))])

# ---------- REVIEWS ----------
page('reviews.html','Reviews | Apex Auto Body Specialists, Collision Repair NC',
 'Real Google reviews for Apex Auto Body Specialists, quoted word for word with dates. 4.7 stars from 152 reviews for collision repair and paint in Apex, NC.', f'''
<section class="sub on-dark"><div class="wrap">{K('Reviews')}<h1>4.7 stars from 152 Google reviews.</h1><p class="lede">Three of them, word for word, with the date each was posted.</p></div>{PIN('pin--hero')}</section>
<section class="wrap rv-list">{''.join(rcard(r) for r in REV)}</section>
<section class="wrap"><p class="note rv"><span class="ph">Placeholder</span> On the real site, a live Google reviews feed or a hand picked set Darin approves. The bracketed words in the September 2025 review replace the name of a national chain.</p></section>
''', ld=[ORG, bc(('Home',''),('Reviews','reviews.html'))])

# ---------- ABOUT ----------
page('about.html','About Darin Fridley | Apex Auto Body Specialists, Apex NC',
 'Apex Auto Body Specialists Inc. was incorporated in NC in 2002 and opened in 2003. Darin Fridley runs the shop with his crew on Reliance Ave in Apex.', f'''
<section class="sub on-dark"><div class="wrap">{K('About')}<h1>Darin Fridley&rsquo;s shop.</h1><p class="lede">Incorporated in North Carolina in 2002, open for business since 2003, per the Better Business Bureau.</p></div>{PIN('pin--hero')}</section>
<section class="wrap about">
 <div class="phbox rv"><p><span class="ph">Placeholder</span> Portrait of Darin at the shop. None is public that we could use.</p></div>
 <div class="about-copy rv">
  <h2>Small crew, owner on site.</h2>
  <p>Customers name Darin in their reviews (they spell it Darren) and they name Frankie, who paints. One reviewer&rsquo;s detached fender got a one look answer: &ldquo;we can take care of that no problem.&rdquo;</p>
  <p>The shop has called itself independent since at least its old website, which said it uses the same estimating software the insurers do but represents the customer.</p>
  <p class="note"><span class="ph">Placeholder</span> Two or three sentences from Darin: how he got into body work, why he stayed independent, what he wants a customer to know before a repair.</p>
 </div>
</section>
<section class="wrap facts rv"><h2 class="sr">Shop facts</h2><dl>
 <div><dt>Company</dt><dd>Apex Auto Body Specialists Inc.</dd></div>
 <div><dt>In business since</dt><dd>2003</dd></div>
 <div><dt>Address</dt><dd>2465 Reliance Ave, Apex, NC 27539</dd></div>
 <div><dt>Hours</dt><dd>Mon to Fri, 9am to 5pm</dd></div>
</dl></section>
''', ld=[ORG, bc(('Home',''),('About','about.html'))])

# ---------- CONTACT ----------
page('contact.html','Free Estimate Request | Apex Auto Body Specialists, Apex NC',
 'Start a collision repair estimate with Apex Auto Body Specialists. Call (919) 363-7995, email the desk, or send the damage details. Mon to Fri 9 to 5, Apex.', f'''
<section class="sub on-dark"><div class="wrap">{K('Estimate')}<h1>Start an estimate.</h1><p class="lede">Calling is fastest. The form below shows how a photo first estimate request could work.</p></div>{PIN('pin--hero')}</section>
<section class="wrap contact">
 <div class="c-info rv">
  <h2>Reach the desk</h2>
  <a class="c-big" href="tel:{TEL}">{TEL_H}</a>
  <a class="c-mail" href="mailto:aabsdesk@gmail.com">aabsdesk@gmail.com</a>
  <p>2465 Reliance Ave<br>Apex, NC 27539</p>
  <p>Monday to Friday, 9am to 5pm<br>Saturday and Sunday closed</p>
  <p class="fine">Fax (919) 363&#8209;9861, per the shop&rsquo;s BBB profile.</p>
  <p><a class="tlink" href="{MAP}" rel="noopener">Directions in Google Maps</a></p>
 </div>
 <form id="qform" class="form rv" novalidate>
  <p class="note"><span class="ph">Demo form</span> Nothing is sent. On a real site this would go to the desk email.</p>
  <fieldset><legend class="sr">Your details</legend>
   <div class="two"><label>Name<input name="n" autocomplete="name"></label><label>Phone<input name="p" type="tel" autocomplete="tel"></label></div>
   <div class="two"><label>Vehicle (year, make, model)<input name="v"></label><label>Insurance claim?<select name="i"><option>Yes, I have a claim number</option><option>Not yet</option><option>Paying myself</option></select></label></div>
   <label>What happened<textarea name="m"></textarea></label>
   <label>Photos of the damage<input name="f" type="file" accept="image/*" multiple></label>
  </fieldset>
  <button class="btn btn--go" type="submit">Send request</button>
  <p id="qmsg" role="status"></p>
 </form>
</section>
''', ld=[ORG, bc(('Home',''),('Estimate','contact.html'))])

# ---------- 404 ----------
page('404.html','Page Not Found | Apex Auto Body Specialists, Apex NC Shop',
 'That page is not here. Head back to the Apex Auto Body Specialists home page, or call (919) 363-7995 for collision repair and paint on Reliance Ave in Apex.', f'''
<section class="sub on-dark"><div class="wrap">{K('404')}<h1>Wrong turn.</h1><p class="lede">That page is not here.</p><div class="cta"><a class="btn btn--go" href="index.html">Home</a><a class="btn btn--line" href="tel:{TEL}">Call {TEL_H}</a></div></div>{PIN('pin--hero')}</section>
''')
print('built')
