print('**Hoşgeldiniz**')
print('Kullanıcı Adınızı Girin:')
 
kullaniciadi='Tolga'
sifre='5353'
dogrulama=False
 
if(input()==kullaniciadi):
    print('Hoşgeldin Tolga!')
    print('Sifrenizi Girin:')
 
    while dogrulama!=True:
        if(input()==sifre):
            dogrulama=True
            print('Giriş Başarılı!')
            
        else:
            dogrulama=False
            print('Şifre Hatalı')
            print('Şifreyi Tekrar Girin:')
    
        
 
else:
    print('Üzgünüm Yanlış Şifre :(')