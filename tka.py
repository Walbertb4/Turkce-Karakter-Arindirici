print(r"""
████████╗██╗  ██╗ █████╗ 
╚══██╔══╝██║ ██╔╝██╔══██╗
   ██║   █████╔╝ ███████║
   ██║   ██╔═██╗ ██╔══██║
   ██║   ██║  ██╗██║  ██║
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
""")

metin= input("Arındırmak itediğiniz metni giriniz: ")

karakterler = "öüğışçÖÜĞİŞÇ"
degisiklikler = "ougiscOUGISC"

arındırılmıs = metin.translate(str.maketrans(karakterler, degisiklikler))

x= input("Boşlukları kaldırmak veya değiştirmek ister misiniz?(e/h)")
if x== "e":
    y= input("Ne ile değiştirmek istersiniz: ")
    arındırılmıs= arındırılmıs.split(" ")
    arındırılmıs= y.join(arındırılmıs)

z= input("Büyük harfleri küçültmek ister misiniz?(e/h)")
if z== "e":
    arındırılmıs= arındırılmıs.lower()
    print(arındırılmıs)
else:
    print(arındırılmıs)

