#!/usr/bin/env python3
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth

R=Path(__file__).resolve().parents[1]
OUT=R/"output/pdf/Case2_RunawayRobot_001.pdf"
ART=R/"assets/case-02/illustrations"
W,H=letter
INK=HexColor("#24343A"); TEAL=HexColor("#2E7C83"); PALE=HexColor("#E8F3F1")
GOLD=HexColor("#E0A82E"); CORAL=HexColor("#D96B4B"); CREAM=HexColor("#FBF8EE")
MIST=HexColor("#F2F5F3"); GRAY=HexColor("#69777B"); RED=HexColor("#B34F45")
for n,f in [("Body","DejaVuSans.ttf"),("Bold","DejaVuSans-Bold.ttf"),("Serif","DejaVuSerif.ttf"),("SerifB","DejaVuSerif-Bold.ttf")]:
    pdfmetrics.registerFont(TTFont(n,"/usr/share/fonts/truetype/dejavu/"+f))
c=canvas.Canvas(str(OUT),pagesize=letter,pageCompression=1)
c.setTitle("Thinking Detectives Case 02: The Case of the Runaway Robot")
L=48; CW=W-96; pn=0

def lines(text,font="Body",size=10,width=CW):
    out=[]; cur=""
    for word in text.split():
        trial=word if not cur else cur+" "+word
        if stringWidth(trial,font,size)<=width: cur=trial
        else: out.append(cur); cur=word
    if cur: out.append(cur)
    return out

def txt(text,x,y,width=CW,size=10,font="Body",lead=None,color=INK,gap=6):
    lead=lead or size*1.36; c.setFillColor(color); c.setFont(font,size)
    for para in text.split("\n"):
        if not para: y-=lead*.5; continue
        for s in lines(para,font,size,width): c.drawString(x,y,s); y-=lead
    return y-gap

def box(x,y,w,h,fill=white,stroke=TEAL,r=7,lw=1):
    c.setFillColor(fill); c.setStrokeColor(stroke); c.setLineWidth(lw)
    c.roundRect(x,y,w,h,r,fill=1,stroke=1)

def label(s,x,y,color=TEAL,size=10):
    c.setFillColor(color); c.setFont("Bold",size); c.drawString(x,y,s)

def begin(title,kicker="CASE FILE",guide=False):
    global pn
    pn+=1; c.setFillColor(MIST if guide else CREAM); c.rect(0,0,W,H,fill=1,stroke=0)
    c.setFillColor(TEAL); c.rect(0,H-17,W,17,fill=1,stroke=0)
    label(kicker.upper(),L,H-39,CORAL if not guide else TEAL,8.2)
    y=H-63; c.setFillColor(INK); c.setFont("SerifB",21)
    for s in lines(title,"SerifB",21,CW): c.drawString(L,y,s); y-=26
    c.setStrokeColor(GOLD); c.setLineWidth(2); c.line(L,y+8,L+84,y+8)
    return y-8

def end(section="LEARNER CASE"):
    c.setFillColor(GRAY); c.setFont("Body",7.5); c.drawString(L,24,section); c.drawRightString(W-L,24,str(pn)); c.showPage()

def art(name,x,y,w,h):
    im=ImageReader(str(ART/name)); iw,ih=im.getSize(); s=min(w/iw,h/ih)
    c.drawImage(im,x+(w-iw*s)/2,y+(h-ih*s)/2,iw*s,ih*s,mask="auto")

def write_lines(top,bottom,n=4,x=L,w=CW):
    c.setStrokeColor(HexColor("#B8C6C4")); c.setLineWidth(.7)
    for i in range(n):
        y=top-(top-bottom)*i/max(n-1,1); c.line(x,y,x+w,y)

def bullet(s,x,y,width=CW,size=9.3):
    c.setFillColor(TEAL); c.circle(x+3,y+3,2.2,fill=1,stroke=0)
    return txt(s,x+14,y+7,width-14,size=size,gap=3)

def stop(y,s):
    ls=lines(s,"Bold",9.1,CW-28); h=28+13*len(ls)
    box(L,y-h,CW,h,PALE,TEAL)
    label("STOP & SOLVE",L+13,y-18,CORAL,8.8)
    yy=y-34
    for q in ls: c.setFillColor(INK); c.setFont("Bold",9.1); c.drawString(L+13,yy,q); yy-=13
    return y-h-7

def simple(title,paras,image=None,kicker="CASE FILE"):
    y=begin(title,kicker)
    if image: art(image,L,y-240,CW,228); y-=252
    for p in paras: y=txt(p,L,y,size=10.05,lead=13.5)
    end()

# 1 cover
pn+=1; c.setFillColor(CREAM); c.rect(0,0,W,H,fill=1,stroke=0)
art("SA-1-cover-chase.jpg",276,32,304,710); c.setFillColor(TEAL); c.rect(0,0,264,H,fill=1,stroke=0)
c.setFillColor(white); c.setFont("Bold",13); c.drawString(34,704,"THINKING DETECTIVES")
c.setFillColor(GOLD); c.setFont("Bold",16); c.drawString(34,665,"CASE 02")
c.setFillColor(white); c.setFont("SerifB",30)
for i,s in enumerate(["The Case","of the","Runaway","Robot"]): c.drawString(34,600-i*41,s)
c.setStrokeColor(GOLD); c.setLineWidth(3); c.line(34,414,164,414)
c.setFont("Bold",11); c.drawString(34,382,"Featuring Remy the Raccoon")
c.setFont("Body",8); c.drawString(34,42,"A SHOW YOUR PATH ADVENTURE"); c.showPage()

# 2
y=begin("Your Case File","BEFORE YOU BEGIN")
y=txt("At the OddSpark Invention Expo, strange ideas are normal.",L,y,size=11)
y=txt("A toaster that butters bread? Normal.\nShoes that tie themselves together? Not useful - but normal.\nA delivery robot racing away with the most important trophy at the fair? That is a case.",L,y,size=10.5)
y=txt("You are Remy's thinking partner. You will find useful clues, show how you are thinking, test ideas, change a plan when facts change, and solve the mystery.",L,y,size=10.3)
y=txt("You do not need to know the perfect path before you begin.",L,y,size=10.4,font="Bold")
box(L,y-116,CW,108,PALE,TEAL); yy=y-32
for s in ["Look for a fact or clue you can start with.","Use it to try a path.","Check your path.","Revise if you need to."]:
    c.setFillColor(INK); c.setFont("Bold",11); c.drawCentredString(W/2,yy,s); yy-=22
box(L,70,CW,88,white,GOLD); label("WHEN YOU SEE STOP & SOLVE",L+13,137,CORAL,8.8)
txt("Pause the story and complete the mission. Optional hints are on pages 23-27. The characters have a deadline, but your thinking is not timed.",L+13,118,CW-26,size=9.1)
end()

simple("Welcome to OddSpark",[
"At 2:25, the OddSpark Invention Expo buzzed, clanked, flashed, and - near Booth 12 - made a noise like a duck sneezing into a trumpet.",
"Remy adjusted his detective cap. 'Excellent. Everything here looks suspicious.' Above the stage: GOLDEN QUESTION MARK PRESENTATION - 3:00.",
"Sunburned Calamari introduced DASH-3. 'He can scan a label, find the matching destination, and deliver almost anything.' Beside the robot sat a silver parcel labeled FINAL PRIZE. Nearby gleamed the trophy.",
"Cammy began, 'Let me overthink this. Did you check what happens when two objects have the same -' Calamari grinned. 'What could go wrong?'"
],"SA-2-stage-presentation.jpg")

simple("BEEP. SCAN. GONE.",[
"DASH-3's scanner flashed. BEEP. Two robot arms lifted the Golden Question Mark. WHIRRRR. The robot rolled offstage and vanished.",
"'A runaway robot. A missing trophy,' said Remy. 'This has all the signs of an International Robot Trophy Syndicate.' Cammy asked, 'Is that real?' 'It has an official name,' said Remy. 'That is usually a strong start.'",
"Behind the curtain, several observations waited - but not all would help. The clock read 2:27. The detectives had until 3:00. Their clock was running. Yours is not."
],"SA-3-robot-departure.jpg")

# 5
y=begin("The First Useful Trail","THINKING MISSION 1")
y=txt("Remy found six facts. Which ones show where the team should investigate first?",L,y,size=10.7)
cards=[("A","DASH-3's wheels have a double-chevron tread."),("B","Fresh double-chevron tracks curve from the curtain toward North Concourse."),("C","The Service Passage door was locked before the demonstration. Its security seal is still unbroken."),("D","Calamari wore his sunglasses on top of his head."),("E","A blue balloon popped at 2:26."),("F","The trophy ribbon had one crooked loop.")]
for i,(a,b) in enumerate(cards):
    x=L+(i%2)*258; by=y-94-(i//2)*101; box(x,by,244,84,white,HexColor("#9AB6B3"))
    c.setFillColor(TEAL); c.circle(x+22,by+62,12,fill=1,stroke=0); c.setFillColor(white); c.setFont("Bold",9); c.drawCentredString(x+22,by+59,a)
    txt(b,x+42,by+67,190,size=8.4,lead=10.5)
y=stop(y-307,"Circle facts you would use. Cross out facts you do not need. Explain how your useful facts connect.")
txt("Find the facts that answer the question - not simply the most facts.",L,y-15,size=9.1,font="Bold",color=TEAL); end()

# 6
y=begin("Show Your Path","MISSION 1 WORKING PAGE")
label("The useful facts are:",L,y); write_lines(y-22,y-118,4)
label("Here is how they connect:",L,y-150); write_lines(y-174,y-350,6)
box(L,154,CW,54,PALE,TEAL); txt("CHECK YOUR PATH: Could you still choose where to investigate using only the facts you selected?",L+12,188,CW-24,size=9,font="Bold")
label("Your Answer",L,126,CORAL,11); txt("Remy should investigate: __________________________________________",L,103,size=10.2)
txt("Turn the page after you have shown and checked a path - even if you are not completely certain.",L,69,size=8.6,color=GRAY); end()

simple("A Trail with Two Points",[
"'These tracks match DASH-3's wheels,' said Cammy. 'And they lead toward North Concourse,' said Calamari. Remy circled those facts. 'The locked passage helps too. The balloon and ribbon are dismissed.' A balloon popped. 'Temporarily dismissed.'",
"The tracks vanished where a floor-cleaning machine had polished the tiles. A tracking screen still showed DASH-3's last signal, but most numbers were missing.",
"'A half-labeled tracker,' Remy whispered. 'Very clue-ish.' The clock read 2:32."
])

# 8
y=begin("The Half-Labeled Tracker","THINKING MISSION 2")
y=txt("The tracker uses equal spaces to show distance from the stage. DASH-3's signal aligns with an unlabeled line.",L,y,size=10.4)
sx,base,gap=150,235,74; c.setStrokeColor(INK); c.setLineWidth(1.5); c.line(sx,base,sx,base+4*gap)
for i in range(5):
    yy=base+i*gap; c.setStrokeColor(HexColor("#90AAA7")); c.setLineWidth(1); c.line(sx-12,yy,sx+170,yy); c.setStrokeColor(INK); c.setLineWidth(2); c.line(sx-8,yy,sx+8,yy)
for i,s in [(0,"0 m"),(2,"50 m"),(4,"100 m")]: c.setFillColor(INK); c.setFont("Bold",10); c.drawRightString(sx-18,base+i*gap-4,s)
c.setFillColor(CORAL); c.circle(sx+136,base+3*gap,8,fill=1,stroke=0); label("DASH-3",sx+151,base+3*gap-4,INK,8.5)
box(360,230,182,304,white,HexColor("#9AB6B3")); label("LOCATION BOARD",376,510)
for i,s in enumerate(["North Gate - 25 m","Gear Gallery - 50 m","Prototype Plaza - 75 m","Transit Hall - 100 m"]): txt(s,376,477-i*55,150,size=8.8,font="Bold")
stop(190,"First determine what one space represents. Then determine DASH-3's distance and location."); end()

# 9
y=begin("Show Your Path","MISSION 2 WORKING PAGE")
y=txt("Label the missing tracker lines. Draw jumps, write an equation, or explain your thinking.",L,y,size=9.5)
write_lines(y-18,y-188,6)
txt("One interval represents: ______ meters",L,y-216,size=10,font="Bold")
txt("DASH-3's signal is at: ______ meters",L,y-242,size=10,font="Bold")
label("Your Answer",L,y-276,CORAL,11); txt("DASH-3 reached: __________________________________________",L,y-299,size=10)
box(L,222,CW,52,PALE,TEAL); txt("CHECK YOUR PATH: Starting at 50, can you make two equal jumps and land exactly on 100?",L+12,254,CW-24,size=8.9,font="Bold")
label("Quick transfer check",L,190); x0,yy=165,130; c.setStrokeColor(INK); c.setLineWidth(1.5); c.line(x0,yy,x0+240,yy)
for xx in [x0,x0+120,x0+240]: c.line(xx,yy-8,xx,yy+8)
c.setFont("Bold",10); c.drawCentredString(x0,yy-26,"10"); c.drawCentredString(x0+240,yy-26,"30")
c.setStrokeColor(CORAL); c.line(x0+120,yy+50,x0+120,yy+17); c.line(x0+120,yy+17,x0+114,yy+25); c.line(x0+120,yy+17,x0+126,yy+25)
txt("The middle tick represents: ______",L,75,size=9.6); end()

simple("Seventy-Five Meters",[
"'Zero to fifty takes two equal jumps,' said Remy. 'So each jump is twenty-five.' He labeled 0, 25, 50, 75, 100. The signal sat at 75 meters: Prototype Plaza.",
"At the plaza, DASH-3 was gone. A witness said it made three extremely precise turns near the Charging Dock.",
"A diagnostic strip curled from a printer. Remy studied it through his magnifying glass, though the words were huge. 'I know exactly what happened.' Cammy asked, 'Did you check the record?' Remy paused. 'Almost exactly.'"
])

# 11
y=begin("Remy's Extremely Convincing Theory","THINKING MISSION 3")
y=txt("Remy's theory: 'Someone is steering DASH-3 remotely to steal the trophy!' Test it against the record.",L,y,size=10)
rows=[("Current power","78%"),("Automatic charging rule","Return only below 20%"),("Remote commands during this trip","0"),("Operating mode","DELIVERY"),("Route status","STOP 2 OF 5 - ACTIVE"),("Witness observation","Three precise turns near the Charging Dock")]
top=y; rh=39
for i,(a,b) in enumerate(rows):
    by=top-(i+1)*rh; c.setFillColor(white if i%2==0 else PALE); c.setStrokeColor(HexColor("#AABAB8")); c.rect(L,by,CW,rh,fill=1,stroke=1); c.line(L+210,by,L+210,by+rh)
    txt(a,L+8,by+25,194,size=8,lead=9.4,font="Bold",gap=0); txt(b,L+218,by+25,278,size=8,lead=9.4,gap=0)
y=top-6*rh-29
for s in ["A. DASH-3 left because it needed to recharge.","B. Someone is steering DASH-3 remotely.","C. DASH-3 is completing a programmed delivery."]: y=bullet(s,L,y,size=8.9)
stop(y-2,"Check all three explanations against the complete record. Find the first record that supports or breaks each one."); end()

# 12
y=begin("Show Your Path","MISSION 3 WORKING PAGE"); top=y
for i,s in enumerate(["A - Recharge","B - Remote control","C - Programmed delivery"]):
    by=top-(i+1)*68; box(L,by,CW,60,white,HexColor("#9AB6B3"),4); c.line(L+135,by,L+135,by+60)
    txt(s,L+10,by+39,115,size=8.6,font="Bold"); txt("Which record supports or breaks it?",L+147,by+39,350,size=8.2,color=GRAY)
label("Where does Remy's theory first stop working?",L,top-235); write_lines(top-258,top-325,3)
label("How would you repair it?",L,top-356); write_lines(top-379,top-442,3)
box(L,130,CW,47,PALE,TEAL); txt("CHECK YOUR PATH: Does your repaired explanation fit every record - not only one?",L+12,159,CW-24,size=8.8,font="Bold")
label("Your Answer",L,105,CORAL,11); txt("The explanation that fits is: ______________________________",L,82,size=9.5); end()

simple("A Plan That Almost Works",[
"Remy checked the record. Zero remote commands broke his theory; DELIVERY and STOP 2 OF 5 supported a programmed route. 'DASH-3 is not escaping. He is delivering - with three stops left.' Only the Control Booth could read the destination.",
"Cammy traced a route: reach Blue Arch, cross the striped skybridge, enter the Control Booth, send DASH-3's recall command.",
"'A sensible plan,' said Cammy. 'Elegant,' said Remy. 'Only four opportunities for disaster,' said Cammy. 'Very restful.'",
"At Blue Arch, a foam-powered volcano launched purple bubbles over the skybridge. A worker lowered a sign: SKYBRIDGE CLOSED.",
"Remy stared. 'Farewell, beautiful plan.' 'Not all of it,' said Cammy."
],"SA-4-foam-skybridge.jpg")

# 14
y=begin("Back Up One Paw","THINKING MISSION 4"); y=txt("The skybridge is closed, but some of the original plan may still work.",L,y,size=10.4)
nodes={"Prototype\nPlaza":(90,470),"Blue Arch":(215,470),"Striped\nSkybridge":(360,560),"Control\nBooth":(485,470),"Workshop\nHall":(310,365),"Ground\nPassage":(450,365)}
edges=[("Prototype\nPlaza","Blue Arch"),("Blue Arch","Striped\nSkybridge"),("Striped\nSkybridge","Control\nBooth"),("Blue Arch","Workshop\nHall"),("Workshop\nHall","Ground\nPassage"),("Ground\nPassage","Control\nBooth")]
for a,b in edges: c.setStrokeColor(HexColor("#809896")); c.setLineWidth(5); c.line(*nodes[a],*nodes[b])
for s,(x,yy) in nodes.items():
    box(x-46,yy-23,92,46,HexColor("#F5D9D4") if "Striped" in s else white,RED if "Striped" in s else TEAL,10,1.5)
    c.setFillColor(INK); c.setFont("Bold",8.2)
    for j,q in enumerate(s.split("\n")): c.drawCentredString(x,yy+5-j*12,q)
c.setStrokeColor(RED); c.setLineWidth(5); c.line(326,535,394,585); c.line(394,535,326,585); label("CLOSED",336,516,RED,9)
label("Original plan",L,290)
for i,s in enumerate(["1. Reach Blue Arch.","2. Cross the striped skybridge.","3. Enter the Control Booth.","4. Send DASH-3's recall command."]): txt(s,L+10,268-i*22,size=9)
stop(168,"Which parts still work? Where does the plan first stop working? Change only what needs to change."); end()

#15
y=begin("What Still Works?","MISSION 4 WORKING PAGE"); write_lines(y-18,y-120,4)
label("What Will You Change?",L,y-154,TEAL,12); write_lines(y-177,y-279,4)
label("Your New Path",L,y-313,TEAL,12); write_lines(y-336,y-466,5)
box(L,123,CW,49,PALE,TEAL); txt("CHECK YOUR PATH: Which original steps did you keep, and why are they still valid?",L+12,153,CW-24,size=8.8,font="Bold")
label("Your Answer",L,96,CORAL,11); txt("Our revised route is: ______________________________________",L,74,size=9.5); end()

simple("The Part That Still Worked",[
"The team kept the useful beginning: reach Blue Arch. They replaced the blocked middle: Blue Arch - Workshop Hall - Ground Passage - Control Booth. Their goal stayed the same.",
"At 2:47, the recall screen replied: RECALL PAUSED: SAFE DELIVERY HANDOFF REQUIRED.",
"The record showed ITEM: FINAL PRIZE; ROUTE: STOP 4 OF 5; DESTINATION: F-5; DUE: 2:58. Calamari lowered his sunglasses. His parcel and the trophy card had the same label.",
"'DASH-3 scanned the wrong FINAL PRIZE,' said Remy. They knew why it vanished. Now they had eleven minutes to find F-5."
])
simple("Five Stops, No Numbers",[
"The delivery directory should have listed five F-stops. Unfortunately, a label-sorting invention had sorted the numbered labels into a wastebasket.",
"The names remained: Charging Dock, Snack Lab, Bubble Lab, Gear Gallery, Final Station.",
"Cammy found five routing rules. 'We can rebuild the order.' Remy arranged the cards. 'Diagram, table, list, movable cards - choose your detective equipment.'"
])

#18
y=begin("Build the Delivery Model","THINKING MISSION 5"); y=txt("Use the five rules to rebuild stops F-1 through F-5.",L,y,size=10.4)
names=["Charging Dock","Snack Lab","Bubble Lab","Gear Gallery","Final Station"]
for i,s in enumerate(names):
    x=L+(i%3)*172; by=y-66-(i//3)*63; box(x,by,158,47,white,HexColor("#9AB6B3")); c.setFillColor(INK); c.setFont("Bold",8.7); c.drawCentredString(x+79,by+18,s)
ry=y-156; label("ROUTING RULES",L,ry)
rules=["1. Charging Dock is F-1.","2. Gear Gallery comes immediately after Bubble Lab.","3. Snack Lab comes before Bubble Lab.","4. Final Station comes after Gear Gallery.","5. Final Station is not beside Charging Dock."]
for i,s in enumerate(rules): txt(s,L+8,ry-24-i*28,size=9)
stop(240,"Build a model that shows the complete order. Then use it to identify F-5. Number, copy, draw, or - with grown-up permission - cut out cards."); end()

#19
y=begin("Show Your Path","MISSION 5 WORKING PAGE"); y=txt("Draw boxes, make a table, write an ordered list, or arrange copied location cards.",L,y,size=9.5)
write_lines(y-30,190,9)
for i,s in enumerate(["F-1","F-2","F-3","F-4","F-5"]): c.setFillColor(GRAY); c.setFont("Bold",9); c.drawCentredString(95+i*104,157,s)
box(L,105,CW,42,PALE,TEAL); txt("CHECK YOUR MODEL: Can you point to where every routing rule appears?",L+12,131,CW-24,size=8.9,font="Bold")
txt("F-5 is: ______________________________________________",L,78,size=10.2,font="Bold",color=CORAL); end()

simple("The Last Stop",[
"Remy checked every rule. The route was F-1 Charging Dock, F-2 Snack Lab, F-3 Bubble Lab, F-4 Gear Gallery, F-5 Final Station.",
"'Final Station!' said Calamari. A voice called: 'DELIVERY WAITING. SIGNATURE REQUIRED.' The clock read 2:55.",
"DASH-3 tried to place the enormous trophy beside a miniature train. Calamari signed at 2:58. DASH-3 released the trophy and played a two-second victory tune."
],"SA-5-final-station.jpg")
simple("Case Closed",[
"The silver parcel contained a tiny golden caboose - the final prize for the Last-Car Challenge. That was why its label said FINAL PRIZE.",
"Cammy reviewed the evidence: matching labels, the nearer trophy, and a five-stop delivery route followed exactly as programmed.",
"Calamari looked at both labels. 'All right. That was one thing that could go wrong.' Remy crossed out INTERNATIONAL ROBOT TROPHY SYNDICATE. 'Magnificent. Also impossible.'",
"They checked that the tracks, tracker, diagnostic record, revised route, duplicate labels, and F-stop model all agreed. At 3:00 the winner received the trophy. Remy wrote CASE CLOSED - then added a very small question mark."
])

#22
y=begin("Look at All the Ways You Thought","THINKING DETECTIVE DEBRIEF"); y=txt("This case was solved by building a path. Mark any thinking behaviors you used:",L,y,size=10)
for i,s in enumerate(["Clue Finder - I noticed information that helped.","Path Builder - I created a way to organize or begin.","Brave Try - I tried without knowing whether it would work.","Check-It - I tested an answer, claim, or plan.","Try Again - I changed a path and kept going."]):
    yy=y-i*23; c.setStrokeColor(TEAL); c.rect(L,yy-2,11,11,fill=0,stroke=1); txt(s,L+20,yy+8,CW-20,size=9.3,font="Bold",gap=0)
txt("Badges are recognition, not a score.",L,y-119,size=8.7,color=GRAY)
for s,yy,n in [("One useful fact I found was:",330,3),("One thing I checked was:",230,3),("One part I kept when a plan changed was:",130,2)]: label(s,L,yy); write_lines(yy-22,yy-58,n)
txt("A strong thinker does not always know the answer first. A strong thinker knows how to keep moving.",L,54,size=9.2,font="Bold",color=CORAL); end()

hints=[
("Hints for Mission 1",[("Hint 1 - Attention","What is the question asking you to find: a color, a time, or a direction?"),("Hint 2 - Structure","Look for one fact about DASH-3 and another matching fact."),("Hint 3 - Directional","Compare wheel tread with tracks. Use the locked passage as a check."),("Strong hint","Double-chevron tracks lead toward North Concourse; the other passage stayed sealed.")]),
("Hints for Mission 2",[("Hint 1 - Attention","Between 0 and 50, how many equal jumps are there?"),("Hint 2 - Structure","The value changes by 50 across two equal spaces."),("Hint 3 - Directional","If two spaces represent 50, what does one represent?"),("Strong hint","Split 50 into two equal parts, then continue the pattern toward 100."),("Transfer check","From 10 to 30 are two equal jumps. What can you add twice?")]),
("Hints for Mission 3",[("Hint 1 - Attention","Compare each explanation with the record."),("Hint 2 - Structure","Ask what supports it and what must be true for it to work."),("Hint 3 - Directional","Recharge must fit power; remote control must fit commands."),("Strong hint","78% is not below 20%; zero remote commands; delivery mode is active.")]),
("Hints for Mission 4",[("Hint 1 - Attention","Find the first impossible step."),("Hint 2 - Structure","Which beginning, middle, or goal is unaffected?"),("Hint 3 - Directional","Keep Blue Arch; find an open connection to the booth."),("Strong hint","Use Workshop Hall and Ground Passage; keep the beginning and goal.")]),
("Hints for Mission 5",[("Hint 1 - Attention","Place the exact-position fact first."),("Hint 2 - Structure","Treat Bubble Lab and Gear Gallery as a block."),("Hint 3 - Directional","Snack Lab is before the block; Final Station is after."),("Strong hint","F-1 Charging Dock, then Snack, Bubble, Gear, Final.")])]
for title,items in hints:
    y=begin(title,"OPTIONAL HINT STATION"); y=txt("Reveal one hint at a time. Stop when your thinking starts moving again.",L,y,size=9.2,color=GRAY)
    for h,b in items:
        ht=72; box(L,y-ht,CW,ht,white,GOLD if "Strong" in h else HexColor("#9AB6B3")); label(h,L+13,y-20,CORAL if "Strong" in h else TEAL,9); txt(b,L+13,y-39,CW-26,size=8.7,lead=11); y-=ht+12
    end("OPTIONAL HINT STATION")

def guide(title,blocks):
    y=begin(title,"GROWN-UP GUIDE",True)
    for h,items in blocks:
        label(h,L,y,TEAL,10.2); y-=19
        if isinstance(items,list):
            for s in items: y=bullet(s,L,y,size=8.7)
        else: y=txt(items,L,y,size=8.9,lead=11.8)
        y-=4
    end("GROWN-UP GUIDE")

guide("How to Use This Case",[("Purpose","Practice finding a foothold, interpreting equal intervals, checking a claim, revising a plan, and building a model."),("Facilitation principles",["Let the learner attempt before offering a method.","Ask what she notices and could try.","Protect productive struggle without allowing paralysis.","Offer hints in order; stop when thinking resumes.","Continue after genuine engagement, even if incomplete.","Recognize specific behaviors; keep Show Your Path above speed."]),("Useful prompts",["What is the question asking?","Which fact gives you somewhere to start?","What could you draw or organize?","How could you check?","Which part still works?"])])
guide("Mission 1 Guide",[("Intended answer","North Concourse."),("Evidence",["A identifies the wheel tread.","B matches fresh tracks and gives direction.","C rules out the Service Passage.","D, E, and F do not answer the immediate question.","A plus B are enough; C is valid checking evidence."]),("Valid paths",["Match A to B.","Group by subject.","Cross out details that do not change destination.","Eliminate with C, then confirm with A and B."]),("Watch for","If memorable details distract, ask what the question needs rather than naming irrelevant cards.")])
guide("Mission 2 Guide: Main Task",[("Answers",["One interval: 25 meters.","Signal: 75 meters.","Location: Prototype Plaza."]),("Reasoning","From 0 to 50 there are two equal intervals, not three. So 50 / 2 = 25. Complete scale: 0, 25, 50, 75, 100."),("Valid paths",["Count equal jumps.","See halfway.","Split 50 equally.","Work backward from 100.","Label and verify every mark."]),("Critical observation","Target equal spaces. If the learner counts three lines, ask her to point to each jump. Do not begin by supplying division.")])
guide("Mission 2 Guide: Transfer and Observation",[("Transfer answer","20. The horizontal scale starts at 10 and uses a different increment, checking understanding rather than memory."),("Observe",["choosing anchors","counting intervals, not lines","splitting equally","transferring interval value","reading the signal","matching 75 to the place"]),("Recognize",["labels intermediate marks","uses anchors","checks the whole scale","corrects line-counting","transfers to a new orientation"]),("Production note","Record the reasoning sequence before deciding whether this becomes a permanent standalone dimension.")])
guide("Mission 3 Guide",[("Conclusion","C - programmed delivery - fits the complete packet."),("Checks",["A conflicts with 78% and return only below 20%.","B conflicts with zero remote commands.","C agrees with DELIVERY and STOP 2 OF 5 - ACTIVE."]),("Valid paths",["test in order","start with specific records","make supports/conflicts table","eliminate A and B, then verify C"]),("Recognize",["checks an exciting theory","finds conflicting evidence","distinguishes unsupported from supported","repairs a theory"]),("Caution","Remy's idea is plausible before checking; plausible ideas still need evidence.")])
guide("Mission 4 Guide",[("Revision","Keep Blue Arch and the Control Booth goal. Replace the blocked middle with Workshop Hall - Ground Passage."),("Valid paths",["backtrack to last valid point","circle open connections","preserve beginning and goal","redraw while naming retained work"]),("Recognize",["stops using blocked route","keeps useful work","names last valid point","checks open connections"]),("Emotional target","Revision should feel like progress, not wasted work.")])
guide("Mission 5 Guide",[("Model",["F-1 Charging Dock","F-2 Snack Lab","F-3 Bubble Lab","F-4 Gear Gallery","F-5 Final Station"]),("Why unique",["Charging Dock fixed first.","Bubble-Gear is an adjacent block.","Snack precedes the block.","Final follows Gear.","Remaining positions force the order.","Not-beside confirms it."]),("Representations",["ordered list","five-column table","boxes and arrows","numbered cards","physical arrangement"]),("Recognize","Fixed anchor, adjacent grouping, external model, and final rule check are all valuable behaviors.")])
guide("Finale, Badges, and Story Facilitation",[("Mystery",["Both objects said FINAL PRIZE.","The trophy was closer.","DASH-3 followed its programmed route.","The parcel held the tiny caboose.","The model identifies F-5.","DASH-3 waited for a signature."]),("Badges","Name observed behavior, not totals: useful facts, interval checking, theory repair, retained route steps, or visible constraints."),("Observe",["desire to continue after unlocks","remembered character moments","exciting rather than personal urgency","understanding of five-stop chase","segments that feel too long"])])

#36
y=begin("Learner Observation Record","GROWN-UP GUIDE",True)
obs=["Found a useful starting fact independently","Explained why a fact mattered","Counted intervals rather than lines","Inferred a constant interval","Checked the unit against another label","Attempted transfer check","Tested a theory against evidence","Found first broken plan point","Preserved useful work","Created a representation","Checked every constraint","Used a hint to resume","Had enough writing space","Maintained interest","Visuals felt older-kid"]
for i,s in enumerate(obs):
    col=i//8; row=i%8; x=L+col*260; yy=y-row*37; c.setStrokeColor(TEAL); c.rect(x,yy-7,11,11,fill=0,stroke=1); txt(s,x+18,yy+2,232,size=8.2,lead=9.7,gap=0)
label("Notes and exact learner quotes",L,334); write_lines(310,65,9)
end("GROWN-UP GUIDE")
assert pn==36,pn
c.save()
print(OUT)
