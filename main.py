from flask import Flask
import random

app = Flask(__name__)

facts_list  =  ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar." , 
                "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor." , 
                "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir." , 
                "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor." ,
                "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır." 
               ]


@app.route("/hihihihaa")
def bsailmem():  
    return  '<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ">You wanted that</a> '

@app.route("/boyhaveyoulostyourmnd")
def bislmem():  
    return  '<a href="/hihihihaa">Boi have you lost your mind ??</a> '
       

@app.route("/the_truth1")
def dontcare():  
    return  '<a href="/boyhaveyoulostyourmnd">I bet you cant click that!!!</a>'



@app.route("/the_truth")
def DUNNO():  
    return  '<a href="/the_truth1">Dont click that!!!</a> '




@app.route("/")
def list():
    return  ' <a href="/the_truth">Do not !! görüntüle!</a> '

    
app.run(port = 5001 , debug=True)
