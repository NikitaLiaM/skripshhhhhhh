# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg room dedes = "kamardedes.png"
image bg blck = "bgblack.png"
image war = "war.png"
image lorongtumapel = "lorongluarkadiri.png"
image gameover = "badending.png"
image trueending = "trueending.png"
image dedessmile = "dedesdesa.png"
image dedescry = "dedescry.png"
image dedestalk = "dedestalk.png"
image dedesangry = "dedesangry.png"
image kenarokangry = "kenarokangry.png"
image arokflat = "arokflat.png"
image gameover = "badending.png"
image scene13b2 = "BAB2scene13"


# Deklarasikan karakter yang digunakan di game.
define d = Character('Dedes', color="#fff200")
define a = Character('Ken Arok', color="#ff0000")
define l = Character('Lohgawe', color="#499eff")
define t = Character('Tunggul Ametung', color="#dd00ff")
define k = Character('Kertajaya', color="#9dff00")
define p = Character('Mpu Purwa', color="#9dff00")
define g = Character('Mpu Gandring', color="#00ffea")
define i = Character('Emban Ina', color="#ffffff")
define b = Character('Buto Ijo', color="#ffffff")

# Game dimulai disini.
label start:
    scene bg blck
    scene bg room dedes with dissolve
    show dedessmile
    d "Emban Ina, mohon bantuannya selama Ayah pergi berkelana ke kaki Gunung Kelud bersama dengan para murid selama sepuluh hari kedepan"
    
    scene war with dissolve
    show kenarokangry
    a "Sampai tetes darah terakhirku, aku akan merebut Dedes dan menghancurkan Kerajaan Kadiri!"
    
    scene gameover with dissolve
    pause
    scene trueending with dissolve
    pause

label choices:
    scene bg blck
    scene lorongtumapel with dissolve
    show dedescare at left with easeinleft
    d "Arok memang benar Tunggul Ametung sedang mabuk hingga tertidur. Tolong berhati-hati! "
    
    show arokflat at right with easeinright
    a "Ini Kesempatan! Aku harus segera menghabisi akuwu Tunggul Ametung."
    
    hide dedesscare
    hide arokflat

    show arokflat with dissolve
menu bunuhakuwu:
    "Cari cara untuk menghabisi Tunggul Ametung!"
    "Tusuk dengan Keris Mpu Gandring":
        jump tusukakuwu
    "Terkam leher dengan Kain":
        jump terkamleher

label tusukakuwu:
    a "Ini karma yang kau terima Tunggul Ametung! *jlebbb"

label cekamleher:
    t "Arghhh! Apa yang kau lakukan! Beraninya!"
    jump game_over
    return

#label game_over:
    #call screen game_over_screen
    #textbutton _("Kembali ke Menu Utama") action MainMenu()
    #return

#screen game_over_screen:
    #image "gameover.png" at fullscreen
    #frame:
        #xalign 0.5
        #yalign 0.5
        #textbutton _("Kembali ke Menu Utama") action Return()


