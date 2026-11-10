from colorama import *
import requests
import random
import operator
import json 

init(autoreset=True)

print(Fore.GREEN+Style.BRIGHT+"\t\t[ Assalomu Alaykum Xush kelibsiz ⭐ ]")
dk={}
tizim=0

while 1:
    print(Fore.CYAN+"\t\t\t < Bosh Menyu >")
    print(Fore.BLUE+"📝 [1]- Royxatda o'tish")
    print(Fore.BLUE+"🔑 [2]- Tizimga kirish")
    print(Fore.BLUE+"✏️  [3]- Tahrirlash")
    print(Fore.RED+"🚫 [4]- Obunani ochirish !")
    print(Fore.RED+Style.BRIGHT+"🚪 [0]- Dasturdan chiqish :(")

    try:
        tanlov=int(input(Fore.GREEN+Style.BRIGHT+"Tanlang: "))
    except:
        print(Fore.LIGHTRED_EX+"\t\tFaqat raqam kiriting ❗")
        continue
    if not tanlov:
        print(Fore.YELLOW+Style.BRIGHT+"-Yana qayta kelishingizni kutamiz 😊")
        exit()



    # Royxatdan otish 
    if tanlov==1:
        l=1
        print(Fore.LIGHTBLUE_EX+"\t\t { ROHATDAN O'TISH }\n")
        while l:
            number=input(Fore.CYAN+Style.BRIGHT+"📞 Raqamingizni kiriting: ")
            number=number.replace(" ","")
            if len(str(number))!=9:
                print(Fore.LIGHTRED_EX+"📞 Raqamingiz xato")
                continue
            username=input(Fore.CYAN+Style.BRIGHT+"👤 Login kiriting: ")
            if not username=='':
                    while l:
                        password=input(Fore.CYAN+"🔒 Password kiriting: ")
                        if not password=='':
                            while 1:
                                ran = random.randint(100,1000)
                                print(Fore.LIGHTYELLOW_EX+f"\t\t\t\t\t\t[💬 SMS kod:{ran} ]")
                                newran=int(input((Fore.LIGHTCYAN_EX+Style.BRIGHT+"SMS kodni kiriting: ")))
                                if ran==newran:
                                    dk[username]=password
                                    print(Fore.GREEN+Style.BRIGHT+"\n\t\tRoyhatdan muvofaqiyatli otdingiz ✅\n")
                                    print(Fore.LIGHTCYAN_EX+"Malumotingiz saqlansimi ? (ha/yoq)")
                                    a=input("...")
                                    if a=="ha":
                                        print("doimiyga saqlandi")
                                        user = {
                                                "login": username,
                                                "parol": password
                                            }
                                        with open("bir.json" ,"w") as f:
                                            json.dump(user, f, indent=4)
                                        
                                        
                        
                                    else:
                                        print("1 martalik saqlandi")
                                    print(Fore.GREEN+Style.BRIGHT+"\n\t\tTizimga kirishingiz mumkin ✅\n")
                                    l=0
                                    break
                                else:
                                    print(Fore.LIGHTRED_EX+Style.BRIGHT+"SMS kod xato ❌")
                                    print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"\t\t\tQayta sms kod yubordim")
                        else:
                            print(Fore.RED+Style.BRIGHT+"Parolga hechnarsa kiritmadingiz ❌")
            else:
                print(Fore.RED+Style.BRIGHT+" Login kiritmadingiz ❗")

    # Tizimga kirish
    elif tanlov==2:
        l=1
        print(Fore.LIGHTBLUE_EX+"\t\t { TIZIMGA KIRISH }\n")
        username = input(Fore.CYAN+"👤 Login: ")
        password = input(Fore.CYAN+"🔒 Password: ")
        try:
            if dk[username]==password:
                print(Fore.BLUE+Style.BRIGHT+"\t\t{ Tizimga xush kelibsiz ⭐}\n") 
                tizim=1               
        except:
            print(Fore.LIGHTRED_EX+"\t\tLogin yoki password xato ❌")

    #  Taxrirlash
    elif tanlov==3:
        print(Fore.LIGHTBLUE_EX+"\t\t { TAHRIRLASH }\n")
        username=input(Fore.CYAN+"Mavjud loginni kiriting: ")
        ra = random.randint(100,1000)
        print(Fore.LIGHTYELLOW_EX+f"\t\t\t\t\t\t[💬 SMS kod:{ran} ]")
        num=int(input("SMS codni kiriting: "))
        if ra==num:
            newpasword=input(Fore.CYAN+"🔒 Yangi password: ")
            dk[username]=newpasword
            print("\t\tPassword muvofaqiyatli almashtirildi ✅")
        else:
            print(Fore.LIGHTRED_EX+Style.BRIGHT+"SMS kod xato ❌")

    #  Obunani ochirish
    elif tanlov==4:

        print(Fore.LIGHTBLUE_EX+"\t\t { Obunani ochirish }\n")
        username=input(Fore.CYAN+"👤 Login kiriting: ")
        ran = random.randint(100,1000)
        print(Fore.LIGHTYELLOW_EX+f"\t\t\t\t\t\t[💬 SMS kod:{ran} ]")
        newran=int(input((Fore.LIGHTCYAN_EX+Style.BRIGHT+"SMS kodni kiriting: ")))
        if ran==newran:
            dk.pop(username)
            print(Fore.LIGHTRED_EX+Style.BRIGHT+"\n\t\tHisob muvofaqiyatli ochirildi ✅")
        else:
            print(Fore.LIGHTRED_EX+Style.BRIGHT+"SMS kod xato ❌")

    #  tizim ichi 
    if tizim:
        
        print(Fore.LIGHTGREEN_EX+"\t\t  [ KITOB DOKONI ]")
        while 1:
            print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"Kitob nomini kiriting")
            book= input(Fore.LIGHTCYAN_EX+"... ")

            # kitob qirish

            url = f"https://openlibrary.org/search.json?q={book}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                docs = data.get('docs', [])
            
                # Agar kitob topilgan bo'lsa
                if docs:
                    book = docs[0]  
                    
                    title = book.get('title', 'Noma\'lum')
                    author = book.get('author_name', ['Noma\'lum'])[0]
                    year = book.get('first_publish_year', 'Noma\'lum')
                    
                    print(Fore.BLUE+"\n\t--- Kitob malumotlari ---")
                    print(f"📖 Nomi: {title}")
                    print(f" ✍️ Muallif: {author}")
                    print(f"📅 Noshirlik yili: {year}\n")

                    print(Fore.CYAN+"[0]- Bosh menyu")
                    print(Fore.CYAN+"[1]- Davom etish")
                    a=int(input("... "))
                    if not a:
                        print("")
                        break
                    else:
                        print(Fore.BLUE+"\t\tDavom etish uchun misol yechishimgiz kerak !! ")
                        while 1:
                            a = random.randint(1,10)
                            b = random.randint(1,10)
                            amallar = [('+', operator.add),('-', operator.sub),
                                        ('*', operator.mul),
                                        ('/', operator.truediv)]
                            belgi, funksiya = random.choice(amallar)
                            natija = funksiya(a, b)
                            c = float(input(f"{a} {belgi} {b} = "))
                            if c==natija:
                                print(Fore.LIGHTGREEN_EX+"Togri")
                                break
                            else:
                                print(Fore.LIGHTRED_EX+Style.BRIGHT+f"togri javob {natija}")    
                else:
                    print("Kechirasiz, bunday kitob topilmadi.")
            else:
                print("Xatolik yuz berdi:", response.status_code)







        



        
        




                




