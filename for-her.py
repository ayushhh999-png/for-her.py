from flask import Flask, render_template_string

app = Flask(__name__)

page_template = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>For Her ❤️</title>
<link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&family=Poppins&display=swap" rel="stylesheet">
<style>
    body { margin:0; font-family:'Poppins',sans-serif; background:linear-gradient(135deg,#ffdde1,#ee9ca7); overflow-x:hidden; color:#fff; text-align:center; }
    h1,h2 { font-family:'Dancing Script',cursive; font-size:2.5em; text-shadow:2px 2px 6px rgba(0,0,0,0.3); }
    input[type=password]{padding:10px; font-size:18px; border:none; border-radius:10px; margin-top:15px; text-align:center;}
    button{padding:10px 20px; margin-top:15px; font-size:18px; border:none; border-radius:25px; background:#ff5e78; color:white; cursor:pointer; transition:0.3s;}
    button:hover{background:#ff3e60;}
    .heart{position:absolute; width:20px; height:20px; background:rgba(255,255,255,0.6); transform:rotate(45deg); animation:float 10s infinite;}
    .heart::before, .heart::after{content:""; position:absolute; width:20px; height:20px; background:rgba(255,255,255,0.6); border-radius:50%;}
    .heart::before{top:-10px; left:0;}
    .heart::after{left:-10px; top:0;}
    @keyframes float{from{transform:translateY(100vh) rotate(45deg);opacity:1;} to{transform:translateY(-10vh) rotate(45deg);opacity:0;}}
    .content{display:none; margin-top:40px;}
    .note-box{font-size:1.5em; margin:20px;}
    .gif-box img{width:250px; border-radius:20px; margin:10px; box-shadow:0px 4px 10px rgba(0,0,0,0.3);}
    .love-letter{white-space:pre-line; font-size:1.2em; margin:20px auto; width:80%; background: rgba(255,255,255,0.15); padding:20px; border-radius:15px; max-height:400px; overflow-y:auto; display:none;}
    #yt-player{display:none; position:fixed; top:0; left:0; width:0; height:0;} /* hidden YouTube player */
</style>
</head>
<body>
<script>
    for(let i=0;i<20;i++){
        let heart=document.createElement('div'); 
        heart.className='heart';
        heart.style.left=Math.random()*100+'vw'; 
        heart.style.animationDuration=(5+Math.random()*5)+'s'; 
        document.body.appendChild(heart);
    }
</script>

<div id="password-screen">
<h1>Enter Secret Password 🔐</h1>
<input type="password" id="passwordInput" maxlength="4" required><br>
<button type="button" onclick="checkPassword()">Unlock</button>
</div>

<div id="slideshow" class="content">
<h1 id="welcome"></h1>

<!-- Hidden YouTube player for autoplay music -->
<div id="music-container">
<iframe id="yt-player" 
src="https://www.youtube.com/embed/2Vv-BfVoq4g?autoplay=1&loop=1&playlist=2Vv-BfVoq4g" 
frameborder="0" allow="autoplay; encrypted-media" allowfullscreen>
</iframe>
</div>

<div id="notes" class="content">
<h2>Notes for You 💌</h2>
<div id="note-text" class="note-box"></div>
<button onclick="nextNote()">Next ➡️</button>
</div>

<div id="gifts" class="content">
<h2>Gifts for You 🎁</h2>
<div class="gif-box">
<img src="https://media.tenor.com/HSxxt1scQXYAAAAM/cat-hugs.gif">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRp0uhccz4d-XALtjHCF173ixQleZH26coOsw&s">
<img src="https://i.pinimg.com/736x/55/29/24/552924c5d913f43785c58e07371f8e53.jpg">
</div>
<button onclick="showLetter()">Next ➡️</button>
</div>

<div id="letter" class="content">
<h2>Love Letter from Ayushi ❤️</h2>
<button onclick="readLetter()">Read 📖</button>
<div class="love-letter" id="letter-text">
hi, this is your annoying husband hereee. first thing in your mind after you've seen this will be : 
"k lekhya hola yetroo chya ma ta padhina" tara hang on, and sorry pailai 🥲🥲not being dramatic pilichhh....
i never fail to make you angry but i also never fail to missyou and care and love for you; teibhayera once again i am here creating this for you. 
Please dont stay mad at me for long okay? yes you can get mad, yes you can not talk to me kei time samma tara you have to come back to me cause i wont feel happy and good without you. 
You make me happy real wala sachikai wala, and also seeing you happy makes my day and whenever you're stressed i get stressed too and i want to cheer you up so badd ykk!! 
i also want to take this moment to say that you are an amazing person inside out, you dont value yourself that much hola but yeah i see it in you. 
for me you are cool, charming, amazing, beautiful, pretty, gorgeous and what not....the list can go on and on but your appreciation wont end. 
BTW you think a lot too ma jastai tara dont think of this cringe way ma🥲 likee idk what you'll feel about this but i just wanna tell you how amazing of a person you've become...even in yeti thorai time...whatever i've known about you i really like all of them..i would accept all the good and bad in you causee yk im a MATURE man😎and i understand even though you think i dont..i do understand and im a mature manche just a little too open to the woman he loves, his first crush.
You are my favorite notification my favourite good morning text and my favourite goodnight text. 
You are my favorite person of all time likeee really and i've liked you since the moment i saw you...
maybe you didnot like me hola paila but i did and i still like you love you care for you and all in a non-cringey way...
i just built up the courage to talk to you and tried a few times now you're talking to me..i feel happy and i cant complain about anything..you're a great presence to me, and i make you mad,sad and everything and annoy you boar you tara i dont want you to stay mad at mee🥲❤️
So, can you pleasee forgive ayushi once again, he is your husband after all🙇🏻🙇🏻he'll be the one to spoil you and keep you happy pachi so pleasee, am i forgiven?
please reply your man on whatsapp if he's forgiven or not? please 🥺
</div>
<button onclick="endMessage()">Next ➡️</button>
</div>

<div id="final" class="content">
<h2>Thank you for visiting hamroo website hehe 💖</h2>
<h3>I love you, I like you, and I miss you ❤️👸🏻</h3>
</div>

<script>
let notes=[
"1) You are precious",
"2) You are beautiful",
"3) You make me happy",
"4) You are so soo special",
"5) I wanna kiss you smm",
"6) I be missing you a lot :(",
"7) You give this silly boy a reason everyday to look forward in his day",
"8) You are hardworking",
"9) Stay hydrated",
"10) Hehe forgive me 🙏"
];
let noteIndex=0;

function checkPassword(){
    let pw = document.getElementById('passwordInput').value;
    if(pw==='0629'){
        document.getElementById('password-screen').style.display='none';
        document.getElementById('slideshow').style.display='block';

        // Show hidden YouTube iframe to play music
        document.getElementById('yt-player').style.display='block';

        document.getElementById('welcome').innerHTML = "Welcome Mrs. Shrestha, My princess, my wife, the most beautiful woman ever 💕";
        setTimeout(()=>{
            document.getElementById('welcome').style.display='none';
            document.getElementById('notes').style.display='block';
            document.getElementById('note-text').innerHTML = notes[0];
        }, 4000);
    } else {
        alert("Incorrect password, try again ❤️");
    }
}

function nextNote(){noteIndex++; 
if(noteIndex<notes.length){
    document.getElementById('note-text').innerHTML=notes[noteIndex];
}else{
    document.getElementById('notes').style.display='none'; 
    document.getElementById('gifts').style.display='block';
}}

function showLetter(){document.getElementById('gifts').style.display='none'; document.getElementById('letter').style.display='block';}
function readLetter(){document.getElementById('letter-text').style.display='block';}
function endMessage(){document.getElementById('letter').style.display='none'; document.getElementById('final').style.display='block';}
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(page_template)

if __name__=="__main__":
    app.run(debug=True)
