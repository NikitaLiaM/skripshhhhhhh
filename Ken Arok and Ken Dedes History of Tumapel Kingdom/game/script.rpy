# Kamu dapat taruh script game mu di file ini.

# Deklarasikan gambar di bawah line ini, menggunakan pernyataan image.
# cnth. image eileen happy = "eileen_happy.png"
image bg room dedes = "kamardedes.png"
image bg black = "bgblack.png"
image bg ruangtamudedes = "ruangtamudedes.png"
image bg depanrumahdedes = "depanrumahdedes.png"
image bg hutan = "bghutan.png"
image war = "war.png"
image lorongtumapel = "lorongluarkadiri.png"
image badending = "badending.png"
image trueending = "trueending.png"
image dedessmile = "dedesdesa.png"
image dedescry = "dedesdesacry.png"
image dedesangry = "dedesdesaangry.png"
image dedestalk = "dedesdesatalk.png"
image arokflat = "Arokflat.png"
image kenarokangry = "kenarokangry.png"
image TAlaugh = "tunggulametunglaugh.png"
image lohgawe = "lohgawe.png"
image B213 = "BAB2scene13.png"
image B214 = "BAB2scene14part2.png"
image narasib2s1 = "Narasibab2scene1.png"
image bab2dedeslari = Movie(play="BAB2scene14.mpeg", size=(1920,1080), loop=False, xalign=0, yalign=0)


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

#BAB 2 
label start:
    scene bg blck
    show narasib2s1
    pause
    scene bg ruangtamudedes with dissolve
    show lohgawe
    p "'Dedes, bapak dengan para santri dan para brahmana akan pergi berkelana ke kaki Gunung Kelud."
    p "Bapak akan pergi selama 10 hari, jadi tolong jaga baik-baik rumah ini..."
    p "Dan juga tolong jaga dirimu sendiri selama bapak pergi."
    hide lohgawe
    show dedessmile
    d "Baik Ayahanda"
    hide dedessmile
    scene bg black
    "Dedes membantu Lohgawe untuk mempersiapkan kebutuhan perjalanan"
    scene bg depanrumahdedes with dissolve
    show lohgawe at left 
    p "Kalau begitu bapak pamit pergi dulu..."
    p "Emban Ina (Dayang), tolong bantu Dedes ya selama saya berkelana."
    p "Dedes, jangan lupa mengunci rumah dan pastikan semuanya aman sebelum kamu tidur."
    hide lohgawe
    i "Baik Tuan."
    show dedestalk at right
    d "Baik Ayahanda, Tolong berhati-hati selama perjalanan."
    d "Emban Ina, mohon bantuannya selama Ayah pergi berkelana selama sepuluh hari kedepan."
    hide dedestalk
    
    scene bg hutan 
    show TAlaugh
    t "Orang-orang bilang bahwa tiada wanita Kadiri yang dapat menandingi kecantikan Dedes putri Brahmana Mpu Purwa"
    t "Mhmphhhh-Hahahaha,..ini membuatku sangat penasaran." 
    t "Apakah dia mengira jika dia bilang kepada sedang ada di hutan, aku tidak akan mencarinya?"
    t "Berani sekali Lohgawe dan putri brahmana itu bersembunyi di hutan tidak menyambut kedatanganku!"
    hide TAlaugh
    "Mendengar suara asing yang berasal dari hutan memanggil Dedes..."
    "...Dedes menyadari bahwa itu suara dari seseorang yang sangat dibencinya."
    show dedescry
    d "S-suara itu! Jangan-jangan,..."
    d "Oh tidak, apakah aku ketahuan?"
    d "aku harus bergegas lari keluar dari hutan ini."
    hide dedescry
    "*drap-drap"
    "Suara langkah kuda mulai terdengar jelas."
    t "HIHIHIHI,...DEDES, KETEMU KAU!"
    show B213
    pause
    "Ditengah langkah kakinya, Dedes menoleh kebelakang"
    "Tiba-tiba dibelakangnya ada laki-laki bergelang dan berkalung emas yang menunggangi kuda"
    "Saat melihat Dedes pertama kali, Tunggul Ametung terdiam."
    "'Cantik sekali'"
    "Itulah kata pertama yang diucapkan Tunggul Ametung didalam hati."
    "Tunggul Ametung mendengarkan suara detak jantungnya yang semakin kencang..."
    "...hingga kicauan burung dan suara angin pun tak lagi terdengar."
    scene bg hutan

    show TAlaugh at left
    t "Kacau sekali, Ahahahaha...Memang benar apa yang dikatakan oleh banyak orang selama ini"
    t "Lima atau sepuluh Paramesyawari (Permaisuri) Kadiri, masih kalah jauh kecantikannya dengan Dedes"
    t "Kau cantik sekali Dedes"
    hide TAlaughu7

    show dedesangry
    d "(dari pada aku harus berlutut salam hormat kepada penjahat itu, lebih baik aku mati saja)"
    hide dedesangry
    show dedestalk
    d "Ayahanda Brahmana Mpu Purwa sedang tidak ada di Desa Panawijil ini."
    hide dedestalk

    show TAlaugh
    t "Ahahahaa,...aku masuk ke Hutan ini tidak untuk mencari ."
    t "Bukannya ada kamu, Dedes? Mana sopan santunmu kepada sang penguasa Tumapel?"
    hide TAlaugh

    show dedesangry
    d "Apa yang kau tunggu? Seumur hidupku, aku tidak akan pernah memberikan rasa hormat kepadamu!"
    d "Bagaimana bisa aku kaum Brahmana memberikan hormat kepada kaum Sudra yang telah melakukan kekejian terhadap warga dan kaum brahmana?"
    d "Jadi kau pergilah!"
    show bab2dedeslari
    pause

    show B214
    pause
    d "*sepertinya aku harus lari sekuat tenaga ke Desa Panawijil"
    t "HEI DEDES! LARI KEMANA KAU?"
    scene war with dissolve
    show kenarokangry
    a "Sampai tetes darah terakhirku, aku akan merebut Dedes dan menghancurkan Kerajaan Kadiri!"
    
    #scene gameover with dissolve
    #pause



#BAB 3
label choices:
    scene bg blck
    scene lorongtumapel with dissolve
    show dedesangry at left with easeinleft
    d "Arok memang benar Tunggul Ametung sedang mabuk hingga tertidur. Tolong berhati-hati! "
    hide dedesangry
    
    show arokflat at right with easeinright
    a "Bagus."
    a "Ini Kesempatan! Aku harus segera menghabisi akuwu Tunggul Ametung."
    hide arokflat

    show arokflat with dissolve
menu bunuhakuwu:
    "Cari cara untuk menghabisi Tunggul Ametung!"
    "Tusuk dengan Keris Mpu Gandring":
        scene trueending with dissolve
        pause
        #jump tusukakuwu
    "Terkam leher dengan Kain":
        scene badending with dissolve
        pause
        #jump terkamleher

label tusukakuwu:
    a "Ini karma yang kau terima Tunggul Ametung! *jlebbb"

label cekamleher:
    t "Arghhh! Apa yang kau lakukan! Beraninya!"
    jump game_over
    return
#label game_over:
    #call screen game_over_screen
    #return

#screen game_over_screen:
    #image "gameover.png" at fullscreen
    #frame:
        #   xalign 0.5
        #  yalign 0.5
        # textbutton _("Kembali ke Menu Utama") action Return()


