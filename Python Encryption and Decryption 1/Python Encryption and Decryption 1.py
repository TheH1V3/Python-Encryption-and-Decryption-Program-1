import time
import random
while __name__ == "__main__":
    aexit=""
    print("1) Create Random key")
    print("2) Encryption")
    print("3) Decryption")
    print("4) Help")
    print("5) Exit")
    print("Enter the number of what you want to do.")
    menu=input("")
    if menu == "1":
        while __name__ == "__main__":
            key=""
            check1=0
            check2=1
            checknumber2=""
            number1=0
            number2=0
            work1=""
            print("Enter how long you want each letter to be, you can choose form 3 to 10.")
            number1=input("")
            while True:
                try:
                    ver=int(number1)
                except ValueError:
                    checknumber1="Error"
                    break
                else:
                    checknumber1="Works"
                    break

            while check1 != check2:
                if checknumber1 == "Error":
                    break

                elif int(number1) == int(1):
                    print("Enter the ammount of different numbers per each letter.")
                    print("You can choose between 1 and 1.")
                    number2=input("")
                    while True:
                        try:
                            ver=int(number2)
                        except ValueError:
                            checknumber1="Error"
                            break
                        else:
                            checknumber2="Works"
                            if int(number2) > 1 or int(number2) < 1:
                                checknumber2="Error"
                                break
                            else:
                                break
                    break
                
                elif int(number1) == int(2):
                    print("Enter the ammount of different numbers per each letter.")
                    print("You can choose between 1 and 94.")
                    number2=input("")
                    while True:
                        try:
                            ver=int(number2)
                        except ValueError:
                            checknumber1="Error"
                            break
                        else:
                            checknumber2="Works"
                            if int(number2) > 94 or int(number2) < 1:
                                checknumber2="Error"
                                break
                            else:
                                break
                    break
                
                elif int(number1) == int(3):
                    print("Enter the ammount of different numbers per each letter.")
                    print("You can choose between 1 and 8,836.")
                    number2=input("")
                    while True:
                        try:
                            ver=int(number2)
                        except ValueError:
                            checknumber1="Error"
                            break
                        else:
                            checknumber2="Works"
                            if int(number2) > 8836 or int(number2) < 1:
                                checknumber2="Error"
                                break
                            else:
                                break
                    break

                elif int(number1) == int(4):
                    print("Enter the ammount of different numbers per each letter.")
                    print("You can choose between 1 and 830,584.")
                    number2=input("")
                    while True:
                        try:
                            ver=int(number2)
                        except ValueError:
                            checknumber2="Error"
                            break
                        else:
                            checknumber2="Works"
                            if int(number2) > 830584 or int(number2) < 1:
                                checknumber1="Error"
                                break
                            else:
                                break
                    break
                
                elif int(number1) == int(5):
                    print("Enter the ammount of different numbers per each letter.")
                    print("You can choose between 1 and 78,074,896.")
                    number2=input("")
                    while True:
                        try:
                            ver=int(number2)
                        except ValueError:
                            checknumber2="Error"
                            break
                        else:
                            checknumber2="Works"
                            if int(number2) > 78074896 or int(number2) < 1:
                                checknumber1="Error"
                                break
                            else:
                                break
                    break

                elif int(number1) == int(6):
                    print("Enter the ammount of different numbers per each letter.")
                    print("You can choose between 1 and 7,339,040,224.")
                    number2=input("")
                    while True:
                        try:
                            ver=int(number2)
                        except ValueError:
                            checknumber2="Error"
                            break
                        else:
                            checknumber2="Works"
                            if int(number2) > 7339040224 or int(number2) < 1:
                                checknumber1="Error"
                                break
                            else:
                                break
                    break

                elif int(number1) == int(7):
                    print("Enter the ammount of different numbers per each letter.")
                    print("You can choose between 1 and 689,869,781,100.")
                    number2=input("")
                    while True:
                        try:
                            ver=int(number2)
                        except ValueError:
                            checknumber2="Error"
                            break
                        else:
                            checknumber2="Works"
                            if int(number2) > 689869781100 or int(number2) < 1:
                                checknumber1="Error"
                                break
                            else:
                                break
                    break

                elif int(number1) == int(8):
                    print("Enter the ammount of different numbers per each letter.")
                    print("You can choose between 1 and 64,847,759,420,000.")
                    number2=input("")
                    while True:
                        try:
                            ver=int(number2)
                        except ValueError:
                            checknumber2="Error"
                            break
                        else:
                            checknumber2="Works"
                            if int(number2) > 64847759420000 or int(number2) < 1:
                                checknumber1="Error"
                                break
                            else:
                                break
                    break

                elif int(number1) == int(9):
                    print("Enter the ammount of different numbers per each letter.")
                    print("You can choose between 1 and 6,095,689,385,000,000.")
                    number2=input("")
                    while True:
                        try:
                            ver=int(number2)
                        except ValueError:
                            checknumber2="Error"
                            break
                        else:
                            checknumber2="Works"
                            if int(number2) > 6095689385000000 or int(number2) < 1:
                                checknumber1="Error"
                                break
                            else:
                                break
                    break

                elif int(number1) == int(10):
                    print("Enter the ammount of different numbers per each letter.")
                    print("You can choose betweem 1 and 572,994,802,200,000,000.")
                    number2=input("")
                    while True:
                        try:
                            ver=int(number2)
                        except ValueError:
                            checknumber2="Error"
                            break
                        else:
                            checknumber2="Works"
                            if int(number2) > 572994802200000000 or int(number2) < 1:
                                checknumber1="Error"
                                break
                            else:
                                break
                elif int(number1) < int(1) or int(number1) > int(10):
                    work1="Error"
                    break
                break

            while True:
                try:
                    ver=int(number1)
                except ValueError:
                    works="No"
                    break
                else:
                    works="Yes"
                    break

            if works == "No":
                works="No"
            else:
                if checknumber2 == "Error":
                    break
                numwhile=94*int(number2)*int(number1)
                while len(key) != numwhile:
                    if int(number1) == 1:
                        if int(number2) > int(1):
                            work1="Error"
                            break
                        one=int(numwhile)*0.1
                        two=int(numwhile)*0.2
                        three=int(numwhile)*0.3
                        four=int(numwhile)*0.4
                        five=int(numwhile)*0.5
                        six=int(numwhile)*0.6
                        seven=int(numwhile)*0.7
                        eight=int(numwhile)*0.8
                        nine=int(numwhile)*0.9
                        ten=int(numwhile)*0.95
                        numone=0
                        numtwo=0
                        numthree=0
                        numfour=0
                        numfive=0
                        numsix=0
                        numseven=0
                        numeight=0
                        numnine=0
                        numten=0
                        rannum1=int(100)
                        rannum2=int(999)
                        num1=int(0)
                        num2=int(num1)+int(number1)
                        print(numwhile)
                        time.sleep(1)
                        key1=str(random.randint(int(rannum1),int(rannum2)))
                        key=str(key)+str(key1)
                        while len(key) != numwhile:
                            if num2 == len(key):
                                if len(key) >= int(one) and numone == 0:
                                    numone=int(numone)+int(1)
                                    print("10%")
                                if len(key) >= int(two) and numtwo == 0:
                                    numtwo=int(numtwo)+int(1)
                                    print("20%")
                                if len(key) >= int(three) and numthree == 0:
                                    numthree=int(numthree)+int(1)
                                    print("30%")
                                if len(key) >= int(four) and numfour == 0:
                                    numfour=int(numfour)+int(1)
                                    print("40%")
                                if len(key) >= int(five) and numfive == 0:
                                    numfive=int(numfive)+int(1)
                                    print("50%")
                                if len(key) >= int(six) and numsix == 0:
                                    numsix=int(numsix)+int(1)
                                    print("60%")
                                if len(key) >= int(seven) and numseven == 0:
                                    numseven=int(numseven)+int(1)
                                    print("70%")
                                if len(key) >= int(eight) and numeight == 0:
                                    numeight=int(numeight)+int(1)
                                    print("80%")
                                if len(key) >= int(nine) and numnine == 0:
                                    numnine=int(numnine)+int(1)
                                    print("90%")
                                if len(key) >= int(ten) and numten == 0:
                                    numten=int(numten)+int(1)
                                    print("100%")
                                num1=0
                                num2=int(num1)+int(number1)
                                key=str(key)+str(key1)
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 == key[int(num1):int(num2)]:
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 != key[int(num1):int(num2)]:
                                num1=int(num1)+int(number1)
                                num2=int(num2)+int(number1)
                    
                    if int(number1) == 2:
                        if int(number2) > int(94):
                            work1="Error"
                            break
                        one=int(numwhile)*0.1
                        two=int(numwhile)*0.2
                        three=int(numwhile)*0.3
                        four=int(numwhile)*0.4
                        five=int(numwhile)*0.5
                        six=int(numwhile)*0.6
                        seven=int(numwhile)*0.7
                        eight=int(numwhile)*0.8
                        nine=int(numwhile)*0.9
                        ten=int(numwhile)*0.95
                        numone=0
                        numtwo=0
                        numthree=0
                        numfour=0
                        numfive=0
                        numsix=0
                        numseven=0
                        numeight=0
                        numnine=0
                        numten=0
                        rannum1=int(100)
                        rannum2=int(999)
                        num1=int(0)
                        num2=int(num1)+int(number1)
                        print(numwhile)
                        time.sleep(1)
                        key1=str(random.randint(int(rannum1),int(rannum2)))
                        key=str(key)+str(key1)
                        while len(key) != numwhile:
                            if num2 == len(key):
                                if len(key) >= int(one) and numone == 0:
                                    numone=int(numone)+int(1)
                                    print("10%")
                                if len(key) >= int(two) and numtwo == 0:
                                    numtwo=int(numtwo)+int(1)
                                    print("20%")
                                if len(key) >= int(three) and numthree == 0:
                                    numthree=int(numthree)+int(1)
                                    print("30%")
                                if len(key) >= int(four) and numfour == 0:
                                    numfour=int(numfour)+int(1)
                                    print("40%")
                                if len(key) >= int(five) and numfive == 0:
                                    numfive=int(numfive)+int(1)
                                    print("50%")
                                if len(key) >= int(six) and numsix == 0:
                                    numsix=int(numsix)+int(1)
                                    print("60%")
                                if len(key) >= int(seven) and numseven == 0:
                                    numseven=int(numseven)+int(1)
                                    print("70%")
                                if len(key) >= int(eight) and numeight == 0:
                                    numeight=int(numeight)+int(1)
                                    print("80%")
                                if len(key) >= int(nine) and numnine == 0:
                                    numnine=int(numnine)+int(1)
                                    print("90%")
                                if len(key) >= int(ten) and numten == 0:
                                    numten=int(numten)+int(1)
                                    print("100%")
                                num1=0
                                num2=int(num1)+int(number1)
                                key=str(key)+str(key1)
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 == key[int(num1):int(num2)]:
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 != key[int(num1):int(num2)]:
                                num1=int(num1)+int(number1)
                                num2=int(num2)+int(number1)
                    
                    if int(number1) == 3:
                        if int(number2) > int(8836):
                            work1="Error"
                            break
                        one=int(numwhile)*0.1
                        two=int(numwhile)*0.2
                        three=int(numwhile)*0.3
                        four=int(numwhile)*0.4
                        five=int(numwhile)*0.5
                        six=int(numwhile)*0.6
                        seven=int(numwhile)*0.7
                        eight=int(numwhile)*0.8
                        nine=int(numwhile)*0.9
                        ten=int(numwhile)*0.95
                        numone=0
                        numtwo=0
                        numthree=0
                        numfour=0
                        numfive=0
                        numsix=0
                        numseven=0
                        numeight=0
                        numnine=0
                        numten=0
                        rannum1=int(100)
                        rannum2=int(999)
                        num1=int(0)
                        num2=int(num1)+int(number1)
                        print(numwhile)
                        time.sleep(1)
                        key1=str(random.randint(int(rannum1),int(rannum2)))
                        key=str(key)+str(key1)
                        while len(key) != numwhile:
                            if num2 == len(key):
                                if len(key) >= int(one) and numone == 0:
                                    numone=int(numone)+int(1)
                                    print("10%")
                                if len(key) >= int(two) and numtwo == 0:
                                    numtwo=int(numtwo)+int(1)
                                    print("20%")
                                if len(key) >= int(three) and numthree == 0:
                                    numthree=int(numthree)+int(1)
                                    print("30%")
                                if len(key) >= int(four) and numfour == 0:
                                    numfour=int(numfour)+int(1)
                                    print("40%")
                                if len(key) >= int(five) and numfive == 0:
                                    numfive=int(numfive)+int(1)
                                    print("50%")
                                if len(key) >= int(six) and numsix == 0:
                                    numsix=int(numsix)+int(1)
                                    print("60%")
                                if len(key) >= int(seven) and numseven == 0:
                                    numseven=int(numseven)+int(1)
                                    print("70%")
                                if len(key) >= int(eight) and numeight == 0:
                                    numeight=int(numeight)+int(1)
                                    print("80%")
                                if len(key) >= int(nine) and numnine == 0:
                                    numnine=int(numnine)+int(1)
                                    print("90%")
                                if len(key) >= int(ten) and numten == 0:
                                    numten=int(numten)+int(1)
                                    print("100%")
                                num1=0
                                num2=int(num1)+int(number1)
                                key=str(key)+str(key1)
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 == key[int(num1):int(num2)]:
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 != key[int(num1):int(num2)]:
                                num1=int(num1)+int(number1)
                                num2=int(num2)+int(number1)

                    if int(number1) == 4:
                        if int(number2) > int(830584):
                            work1="Error"
                            break
                        one=int(numwhile)*0.1
                        two=int(numwhile)*0.2
                        three=int(numwhile)*0.3
                        four=int(numwhile)*0.4
                        five=int(numwhile)*0.5
                        six=int(numwhile)*0.6
                        seven=int(numwhile)*0.7
                        eight=int(numwhile)*0.8
                        nine=int(numwhile)*0.9
                        ten=int(numwhile)*0.95
                        numone=0
                        numtwo=0
                        numthree=0
                        numfour=0
                        numfive=0
                        numsix=0
                        numseven=0
                        numeight=0
                        numnine=0
                        numten=0
                        rannum1=int(1000)
                        rannum2=int(9999)
                        num1=int(0)
                        num2=int(num1)+int(number1)
                        print(numwhile)
                        time.sleep(1)
                        key=str(random.randint(int(rannum1),int(rannum2)))
                        key1=str(random.randint(int(rannum1),int(rannum2)))
                        while len(key) != numwhile:
                            if num2 == len(key):
                                if len(key) >= int(one) and numone == 0:
                                    numone=int(numone)+int(1)
                                    print("10%")
                                if len(key) >= int(two) and numtwo == 0:
                                    numtwo=int(numtwo)+int(1)
                                    print("20%")
                                if len(key) >= int(three) and numthree == 0:
                                    numthree=int(numthree)+int(1)
                                    print("30%")
                                if len(key) >= int(four) and numfour == 0:
                                    numfour=int(numfour)+int(1)
                                    print("40%")
                                if len(key) >= int(five) and numfive == 0:
                                    numfive=int(numfive)+int(1)
                                    print("50%")
                                if len(key) >= int(six) and numsix == 0:
                                    numsix=int(numsix)+int(1)
                                    print("60%")
                                if len(key) >= int(seven) and numseven == 0:
                                    numseven=int(numseven)+int(1)
                                    print("70%")
                                if len(key) >= int(eight) and numeight == 0:
                                    numeight=int(numeight)+int(1)
                                    print("80%")
                                if len(key) >= int(nine) and numnine == 0:
                                    numnine=int(numnine)+int(1)
                                    print("90%")
                                if len(key) >= int(ten) and numten == 0:
                                    numten=int(numten)+int(1)
                                    print("100%")
                                num1=0
                                num2=int(num1)+int(number1)
                                key=str(key)+str(key1)
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 == key[int(num1):int(num2)]:
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 != key[int(num1):int(num2)]:
                                num1=int(num1)+int(number1)
                                num2=int(num2)+int(number1)

                    if int(number1) == 5:
                        if int(number2) > int(78074896):
                            work1="Error"
                            break
                        one=int(numwhile)*0.1
                        two=int(numwhile)*0.2
                        three=int(numwhile)*0.3
                        four=int(numwhile)*0.4
                        five=int(numwhile)*0.5
                        six=int(numwhile)*0.6
                        seven=int(numwhile)*0.7
                        eight=int(numwhile)*0.8
                        nine=int(numwhile)*0.9
                        ten=int(numwhile)*0.95
                        numone=0
                        numtwo=0
                        numthree=0
                        numfour=0
                        numfive=0
                        numsix=0
                        numseven=0
                        numeight=0
                        numnine=0
                        numten=0
                        rannum1=int(10000)
                        rannum2=int(99999)
                        num1=int(0)
                        num2=int(num1)+int(number1)
                        print(numwhile)
                        time.sleep(1)
                        key=str(random.randint(int(rannum1),int(rannum2)))
                        key1=str(random.randint(int(rannum1),int(rannum2)))
                        while len(key) != numwhile:
                            if num2 == len(key):
                                if len(key) >= int(one) and numone == 0:
                                    numone=int(numone)+int(1)
                                    print("10%")
                                if len(key) >= int(two) and numtwo == 0:
                                    numtwo=int(numtwo)+int(1)
                                    print("20%")
                                if len(key) >= int(three) and numthree == 0:
                                    numthree=int(numthree)+int(1)
                                    print("30%")
                                if len(key) >= int(four) and numfour == 0:
                                    numfour=int(numfour)+int(1)
                                    print("40%")
                                if len(key) >= int(five) and numfive == 0:
                                    numfive=int(numfive)+int(1)
                                    print("50%")
                                if len(key) >= int(six) and numsix == 0:
                                    numsix=int(numsix)+int(1)
                                    print("60%")
                                if len(key) >= int(seven) and numseven == 0:
                                    numseven=int(numseven)+int(1)
                                    print("70%")
                                if len(key) >= int(eight) and numeight == 0:
                                    numeight=int(numeight)+int(1)
                                    print("80%")
                                if len(key) >= int(nine) and numnine == 0:
                                    numnine=int(numnine)+int(1)
                                    print("90%")
                                if len(key) >= int(ten) and numten == 0:
                                    numten=int(numten)+int(1)
                                    print("100%")
                                num1=0
                                num2=int(num1)+int(number1)
                                key=str(key)+str(key1)
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 == key[int(num1):int(num2)]:
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 != key[int(num1):int(num2)]:
                                num1=int(num1)+int(number1)
                                num2=int(num2)+int(number1)

                    elif int(number1) == 6:
                        if int(number2) > int(7339040224):
                            work1="Error"
                            break
                        one=int(numwhile)*0.1
                        two=int(numwhile)*0.2
                        three=int(numwhile)*0.3
                        four=int(numwhile)*0.4
                        five=int(numwhile)*0.5
                        six=int(numwhile)*0.6
                        seven=int(numwhile)*0.7
                        eight=int(numwhile)*0.8
                        nine=int(numwhile)*0.9
                        ten=int(numwhile)*0.95
                        numone=0
                        numtwo=0
                        numthree=0
                        numfour=0
                        numfive=0
                        numsix=0
                        numseven=0
                        numeight=0
                        numnine=0
                        numten=0
                        rannum1=int(100000)
                        rannum2=int(999999)
                        num1=int(0)
                        num2=int(num1)+int(number1)
                        print(numwhile)
                        time.sleep(1)
                        key=str(random.randint(int(rannum1),int(rannum2)))
                        key1=str(random.randint(int(rannum1),int(rannum2)))
                        while len(key) != numwhile:
                            if num2 == len(key):
                                if len(key) >= int(one) and numone == 0:
                                    numone=int(numone)+int(1)
                                    print("10%")
                                if len(key) >= int(two) and numtwo == 0:
                                    numtwo=int(numtwo)+int(1)
                                    print("20%")
                                if len(key) >= int(three) and numthree == 0:
                                    numthree=int(numthree)+int(1)
                                    print("30%")
                                if len(key) >= int(four) and numfour == 0:
                                    numfour=int(numfour)+int(1)
                                    print("40%")
                                if len(key) >= int(five) and numfive == 0:
                                    numfive=int(numfive)+int(1)
                                    print("50%")
                                if len(key) >= int(six) and numsix == 0:
                                    numsix=int(numsix)+int(1)
                                    print("60%")
                                if len(key) >= int(seven) and numseven == 0:
                                    numseven=int(numseven)+int(1)
                                    print("70%")
                                if len(key) >= int(eight) and numeight == 0:
                                    numeight=int(numeight)+int(1)
                                    print("80%")
                                if len(key) >= int(nine) and numnine == 0:
                                    numnine=int(numnine)+int(1)
                                    print("90%")
                                if len(key) >= int(ten) and numten == 0:
                                    numten=int(numten)+int(1)
                                    print("100%")
                                num1=0
                                num2=int(num1)+int(number1)
                                key=str(key)+str(key1)
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 == key[int(num1):int(num2)]:
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 != key[int(num1):int(num2)]:
                                num1=int(num1)+int(number1)
                                num2=int(num2)+int(number1)

                    elif int(number1) == 7:
                        if int(number2) > int(689869781100):
                            work1="Error"
                            break
                        one=int(numwhile)*0.1
                        two=int(numwhile)*0.2
                        three=int(numwhile)*0.3
                        four=int(numwhile)*0.4
                        five=int(numwhile)*0.5
                        six=int(numwhile)*0.6
                        seven=int(numwhile)*0.7
                        eight=int(numwhile)*0.8
                        nine=int(numwhile)*0.9
                        ten=int(numwhile)*0.95
                        numone=0
                        numtwo=0
                        numthree=0
                        numfour=0
                        numfive=0
                        numsix=0
                        numseven=0
                        numeight=0
                        numnine=0
                        numten=0
                        rannum1=int(1000000)
                        rannum2=int(9999999)
                        num1=int(0)
                        num2=int(num1)+int(number1)
                        print(numwhile)
                        time.sleep(1)
                        key=str(random.randint(int(rannum1),int(rannum2)))
                        key1=str(random.randint(int(rannum1),int(rannum2)))
                        while len(key) != numwhile:
                            if num2 == len(key):
                                num1=0
                                num2=int(num1)+int(number1)
                                key=str(key)+str(key1)
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 == key[int(num1):int(num2)]:
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 != key[int(num1):int(num2)]:
                                num1=int(num1)+int(number1)
                                num2=int(num2)+int(number1)

                    elif int(number1) == 8:
                        if int(number2) > int(64847759420000):
                            work1="Error"
                            break
                        one=int(numwhile)*0.1
                        two=int(numwhile)*0.2
                        three=int(numwhile)*0.3
                        four=int(numwhile)*0.4
                        five=int(numwhile)*0.5
                        six=int(numwhile)*0.6
                        seven=int(numwhile)*0.7
                        eight=int(numwhile)*0.8
                        nine=int(numwhile)*0.9
                        ten=int(numwhile)*0.95
                        numone=0
                        numtwo=0
                        numthree=0
                        numfour=0
                        numfive=0
                        numsix=0
                        numseven=0
                        numeight=0
                        numnine=0
                        numten=0
                        rannum1=int(10000000)
                        rannum2=int(99999999)
                        num1=int(0)
                        num2=int(num1)+int(number1)
                        print(numwhile)
                        time.sleep(1)
                        key=str(random.randint(int(rannum1),int(rannum2)))
                        key1=str(random.randint(int(rannum1),int(rannum2)))
                        while len(key) != numwhile:
                            if num2 == len(key):
                                if len(key) >= int(one) and numone == 0:
                                    numone=int(numone)+int(1)
                                    print("10%")
                                if len(key) >= int(two) and numtwo == 0:
                                    numtwo=int(numtwo)+int(1)
                                    print("20%")
                                if len(key) >= int(three) and numthree == 0:
                                    numthree=int(numthree)+int(1)
                                    print("30%")
                                if len(key) >= int(four) and numfour == 0:
                                    numfour=int(numfour)+int(1)
                                    print("40%")
                                if len(key) >= int(five) and numfive == 0:
                                    numfive=int(numfive)+int(1)
                                    print("50%")
                                if len(key) >= int(six) and numsix == 0:
                                    numsix=int(numsix)+int(1)
                                    print("60%")
                                if len(key) >= int(seven) and numseven == 0:
                                    numseven=int(numseven)+int(1)
                                    print("70%")
                                if len(key) >= int(eight) and numeight == 0:
                                    numeight=int(numeight)+int(1)
                                    print("80%")
                                if len(key) >= int(nine) and numnine == 0:
                                    numnine=int(numnine)+int(1)
                                    print("90%")
                                if len(key) >= int(ten) and numten == 0:
                                    numten=int(numten)+int(1)
                                    print("100%")
                                num1=0
                                num2=int(num1)+int(number1)
                                key=str(key)+str(key1)
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 == key[int(num1):int(num2)]:
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 != key[int(num1):int(num2)]:
                                num1=int(num1)+int(number1)
                                num2=int(num2)+int(number1)

                    elif int(number1) == 9:
                        if int(number2) > int(6095689385000000):
                            work1="Error"
                            break
                        one=int(numwhile)*0.1
                        two=int(numwhile)*0.2
                        three=int(numwhile)*0.3
                        four=int(numwhile)*0.4
                        five=int(numwhile)*0.5
                        six=int(numwhile)*0.6
                        seven=int(numwhile)*0.7
                        eight=int(numwhile)*0.8
                        nine=int(numwhile)*0.9
                        ten=int(numwhile)*0.95
                        numone=0
                        numtwo=0
                        numthree=0
                        numfour=0
                        numfive=0
                        numsix=0
                        numseven=0
                        numeight=0
                        numnine=0
                        numten=0
                        rannum1=int(100000000)
                        rannum2=int(999999999)
                        num1=int(0)
                        num2=int(num1)+int(number1)
                        print(numwhile)
                        time.sleep(1)
                        key=str(random.randint(int(rannum1),int(rannum2)))
                        key1=str(random.randint(int(rannum1),int(rannum2)))
                        while len(key) != numwhile:
                            if num2 == len(key):
                                if len(key) >= int(one) and numone == 0:
                                    numone=int(numone)+int(1)
                                    print("10%")
                                if len(key) >= int(two) and numtwo == 0:
                                    numtwo=int(numtwo)+int(1)
                                    print("20%")
                                if len(key) >= int(three) and numthree == 0:
                                    numthree=int(numthree)+int(1)
                                    print("30%")
                                if len(key) >= int(four) and numfour == 0:
                                    numfour=int(numfour)+int(1)
                                    print("40%")
                                if len(key) >= int(five) and numfive == 0:
                                    numfive=int(numfive)+int(1)
                                    print("50%")
                                if len(key) >= int(six) and numsix == 0:
                                    numsix=int(numsix)+int(1)
                                    print("60%")
                                if len(key) >= int(seven) and numseven == 0:
                                    numseven=int(numseven)+int(1)
                                    print("70%")
                                if len(key) >= int(eight) and numeight == 0:
                                    numeight=int(numeight)+int(1)
                                    print("80%")
                                if len(key) >= int(nine) and numnine == 0:
                                    numnine=int(numnine)+int(1)
                                    print("90%")
                                if len(key) >= int(ten) and numten == 0:
                                    numten=int(numten)+int(1)
                                    print("100%")
                                num1=0
                                num2=int(num1)+int(number1)
                                key=str(key)+str(key1)
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 == key[int(num1):int(num2)]:
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 != key[int(num1):int(num2)]:
                                num1=int(num1)+int(number1)
                                num2=int(num2)+int(number1)

                    elif int(number1) == 10:
                        if int(number2) > int(572994802200000000):
                            work1="Error"
                            break
                        one=int(numwhile)*0.1
                        two=int(numwhile)*0.2
                        three=int(numwhile)*0.3
                        four=int(numwhile)*0.4
                        five=int(numwhile)*0.5
                        six=int(numwhile)*0.6
                        seven=int(numwhile)*0.7
                        eight=int(numwhile)*0.8
                        nine=int(numwhile)*0.9
                        ten=int(numwhile)*0.95
                        numone=0
                        numtwo=0
                        numthree=0
                        numfour=0
                        numfive=0
                        numsix=0
                        numseven=0
                        numeight=0
                        numnine=0
                        numten=0
                        rannum1=int(1000000000)
                        rannum2=int(9999999999)
                        num1=int(0)
                        num2=int(num1)+int(number1)
                        print(numwhile)
                        time.sleep(1)
                        key=str(random.randint(int(rannum1),int(rannum2)))
                        key1=str(random.randint(int(rannum1),int(rannum2)))
                        while len(key) != numwhile:
                            if num2 == len(key):
                                if len(key) >= int(one) and numone == 0:
                                    numone=int(numone)+int(1)
                                    print("10%")
                                if len(key) >= int(two) and numtwo == 0:
                                    numtwo=int(numtwo)+int(1)
                                    print("20%")
                                if len(key) >= int(three) and numthree == 0:
                                    numthree=int(numthree)+int(1)
                                    print("30%")
                                if len(key) >= int(four) and numfour == 0:
                                    numfour=int(numfour)+int(1)
                                    print("40%")
                                if len(key) >= int(five) and numfive == 0:
                                    numfive=int(numfive)+int(1)
                                    print("50%")
                                if len(key) >= int(six) and numsix == 0:
                                    numsix=int(numsix)+int(1)
                                    print("60%")
                                if len(key) >= int(seven) and numseven == 0:
                                    numseven=int(numseven)+int(1)
                                    print("70%")
                                if len(key) >= int(eight) and numeight == 0:
                                    numeight=int(numeight)+int(1)
                                    print("80%")
                                if len(key) >= int(nine) and numnine == 0:
                                    numnine=int(numnine)+int(1)
                                    print("90%")
                                if len(key) >= int(ten) and numten == 0:
                                    numten=int(numten)+int(1)
                                    print("100%")
                                num1=0
                                num2=int(num1)+int(number1)
                                key=str(key)+str(key1)
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 == key[int(num1):int(num2)]:
                                key1=str(random.randint(int(rannum1),int(rannum2)))
                            elif key1 != key[int(num1):int(num2)]:
                                num1=int(num1)+int(number1)
                                num2=int(num2)+int(number1)

            while check1 != check2:
                if checknumber1 != "Error":
                    if int(number1) == 1 or int(number1) == 2 or int(number1) == 3 or int(number1) == 4 or int(number1) == 5 or int(number1) == 6 or int(number1) == 7 or int(number1) == 8 or int(number1) == 9:
                        key=str(number1)+str("a")+str(number2)+str("a")+str(key)
                        break
                    elif int(number1) == 10:
                        number1=0
                        key=str(number1)+str("a")+str(number2)+str("a")+str(key)
                        break
                else:
                    break

            while check1 != check2:
                if checknumber1 == "Error":
                    break
                else:
                    if work1 == "Error":
                        key=""
                    elif key != "":
                        print(key)
                        print(len(key))
                        break
            break

    if menu == "2":
        while __name__ == "__main__":
            message=""
            key=""
            print("Enter the message that you want to encrypt.")
            message=input("")
            print("Enter the key you want to uses to encrypt the message.")
            key=str(input(""))
            if message == "":
                break
            elif key == "":
                break
            number1=str(key[0:1])
            try:
                ver=int(number1)
            except ValueError:
                break
            else:
                break
            check1=0
            check2=1
            num=int(len(message))
            num1=0
            num2=1
            num3=2
            num4=3
            num5=0
            new=""
            while check1 != check2:
                if key[int(num3):int(num4)] == "a":
                    number2=key[int(2):int(num4-1)]
                    break
                else:
                    num3=num3+1
                    num4=num4+1
            a=int(num4)-int(3)

            if 1 == 1:
                lengthkey=len(str(key))
                lengthkey1=int(a)+int(3)
                key=key[int(lengthkey1):int(lengthkey)]

            number3=int(number1)*int(number2)
            number4=int(94)*int(number1)*int(number2)
            if len(key) != number4:
                break
            letter1a=int(0)
            letter1b=int(number3)
            letter111a=int(letter1a)
            letter221b=int(letter1a)+int(number1)

            letter2a=int(letter1b)
            letter2b=int(letter1b)+int(number3)
            letter112a=int(letter2a)
            letter222b=int(letter2a)+int(number1)

            letter3a=int(letter2b)
            letter3b=int(letter2b)+int(number3)
            letter113a=int(letter3a)
            letter223b=int(letter3a)+int(number1)

            letter4a=int(letter3b)
            letter4b=int(letter3b)+int(number3)
            letter114a=int(letter4a)
            letter224b=int(letter4a)+int(number1)

            letter5a=int(letter4b)
            letter5b=int(letter4b)+int(number3)
            letter115a=int(letter5a)
            letter225b=int(letter5a)+int(number1)

            letter6a=int(letter5b)
            letter6b=int(letter5b)+int(number3)
            letter116a=int(letter6a)
            letter226b=int(letter6a)+int(number1)

            letter7a=int(letter6b)
            letter7b=int(letter6b)+int(number3)
            letter117a=int(letter7a)
            letter227b=int(letter7a)+int(number1)

            letter8a=int(letter7b)
            letter8b=int(letter7b)+int(number3)
            letter118a=int(letter8a)
            letter228b=int(letter8a)+int(number1)

            letter9a=int(letter8a)
            letter9b=int(letter8a)+int(number3)
            letter119a=int(letter9a)
            letter229b=int(letter9a)+int(number1)

            letter10a=int(letter9b)
            letter10b=int(letter9b)+int(number3)
            letter1110a=int(letter10a)
            letter2210b=int(letter10a)+int(number1)

            letter11a=int(letter10b)
            letter11b=int(letter10b)+int(number3)
            letter1111a=int(letter11a)
            letter2211b=int(letter11a)+int(number1)

            letter12a=int(letter11b)
            letter12b=int(letter11b)+int(number3)
            letter1112a=int(letter12a)
            letter2212b=int(letter12a)+int(number1)

            letter13a=int(letter12b)
            letter13b=int(letter12b)+int(number3)
            letter1113a=int(letter13a)
            letter2213b=int(letter13a)+int(number1)

            letter14a=int(letter13b)
            letter14b=int(letter13b)+int(number3)
            letter1114a=int(letter14a)
            letter2214b=int(letter14a)+int(number1)

            letter15a=int(letter14b)
            letter15b=int(letter14b)+int(number3)
            letter1115a=int(letter15a)
            letter2215b=int(letter15a)+int(number1)


            letter16a=int(letter15b)
            letter16b=int(letter15b)+int(number3)
            letter1116a=int(letter16a)
            letter2216b=int(letter16a)+int(number1)

            letter17a=int(letter16b)
            letter17b=int(letter16b)+int(number3)
            letter1117a=int(letter17a)
            letter2217b=int(letter17a)+int(number1)

            letter18a=int(letter17b)
            letter18b=int(letter17b)+int(number3)
            letter1118a=int(letter18a)
            letter2218b=int(letter18a)+int(number1)

            letter19a=int(letter18b)
            letter19b=int(letter18b)+int(number3)
            letter1119a=int(letter19a)
            letter2219b=int(letter19a)+int(number1)

            letter20a=int(letter19b)
            letter20b=int(letter19b)+int(number3)
            letter1120a=int(letter20a)
            letter2220b=int(letter20a)+int(number1)

            letter21a=int(letter20b)
            letter21b=int(letter20b)+int(number3)
            letter1121a=int(letter21a)
            letter2221b=int(letter21a)+int(number1)

            letter22a=int(letter21b)
            letter22b=int(letter21b)+int(number3)
            letter1122a=int(letter22a)
            letter2222b=int(letter22a)+int(number1)

            letter23a=int(letter22b)
            letter23b=int(letter22b)+int(number3)
            letter1123a=int(letter23a)
            letter2223b=int(letter23a)+int(number1)

            letter24a=int(letter23b)
            letter24b=int(letter23b)+int(number3)
            letter1124a=int(letter24a)
            letter2224b=int(letter24a)+int(number1)

            letter25a=int(letter24b)
            letter25b=int(letter24b)+int(number3)
            letter1125a=int(letter25a)
            letter2225b=int(letter25a)+int(number1)

            letter26a=int(letter25b)
            letter26b=int(letter25b)+int(number3)
            letter1126a=int(letter26a)
            letter2226b=int(letter26a)+int(number1)

            letter27a=int(letter26b)
            letter27b=int(letter26b)+int(number3)
            letter1127a=int(letter27a)
            letter2227b=int(letter27a)+int(number1)

            letter28a=int(letter27b)
            letter28b=int(letter27b)+int(number3)
            letter1128a=int(letter28a)
            letter2228b=int(letter28a)+int(number1)

            letter29a=int(letter28b)
            letter29b=int(letter28b)+int(number3)
            letter1129a=int(letter29a)
            letter2229b=int(letter29a)+int(number1)

            letter30a=int(letter29b)
            letter30b=int(letter29b)+int(number3)
            letter1130a=int(letter30a)
            letter2230b=int(letter30a)+int(number1)

            letter31a=int(letter30b)
            letter31b=int(letter30b)+int(number3)
            letter1131a=int(letter31a)
            letter2231b=int(letter31a)+int(number1)

            letter32a=int(letter31b)
            letter32b=int(letter31b)+int(number3)
            letter1132a=int(letter32a)
            letter2232b=int(letter32a)+int(number1)

            letter33a=int(letter32b)
            letter33b=int(letter32b)+int(number3)
            letter1133a=int(letter33a)
            letter2233b=int(letter33a)+int(number1)

            letter34a=int(letter33b)
            letter34b=int(letter33b)+int(number3)
            letter1134a=int(letter34a)
            letter2234b=int(letter34a)+int(number1)

            letter35a=int(letter34b)
            letter35b=int(letter34b)+int(number3)
            letter1135a=int(letter35a)
            letter2235b=int(letter35a)+int(number1)

            letter36a=int(letter35b)
            letter36b=int(letter35b)+int(number3)
            letter1136a=int(letter36a)
            letter2236b=int(letter36a)+int(number1)

            letter37a=int(letter36b)
            letter37b=int(letter36b)+int(number3)
            letter1137a=int(letter37a)
            letter2237b=int(letter37a)+int(number1)

            letter38a=int(letter37b)
            letter38b=int(letter37b)+int(number3)
            letter1138a=int(letter38a)
            letter2238b=int(letter38a)+int(number1)

            letter39a=int(letter38b)
            letter39b=int(letter38b)+int(number3)
            letter1139a=int(letter39a)
            letter2239b=int(letter39a)+int(number1)

            letter40a=int(letter39b)
            letter40b=int(letter39b)+int(number3)
            letter1140a=int(letter40a)
            letter2240b=int(letter40a)+int(number1)

            letter41a=int(letter40b)
            letter41b=int(letter40b)+int(number3)
            letter1141a=int(letter41a)
            letter2241b=int(letter41a)+int(number1)

            letter42a=int(letter41b)
            letter42b=int(letter41b)+int(number3)
            letter1142a=int(letter42a)
            letter2242b=int(letter42a)+int(number1)

            letter43a=int(letter42b)
            letter43b=int(letter42b)+int(number3)
            letter1143a=int(letter43a)
            letter2243b=int(letter43a)+int(number1)

            letter44a=int(letter43b)
            letter44b=int(letter43b)+int(number3)
            letter1144a=int(letter44a)
            letter2244b=int(letter44a)+int(number1)

            letter45a=int(letter44b)
            letter45b=int(letter44b)+int(number3)
            letter1145a=int(letter45a)
            letter2245b=int(letter45a)+int(number1)

            letter46a=int(letter45b)
            letter46b=int(letter45b)+int(number3)
            letter1146a=int(letter46a)
            letter2246b=int(letter46a)+int(number1)

            letter47a=int(letter46b)
            letter47b=int(letter46b)+int(number3)
            letter1147a=int(letter47a)
            letter2247b=int(letter47a)+int(number1)

            letter48a=int(letter47b)
            letter48b=int(letter47b)+int(number3)
            letter1148a=int(letter48a)
            letter2248b=int(letter48a)+int(number1)

            letter49a=int(letter48b)
            letter49b=int(letter48b)+int(number3)
            letter1149a=int(letter49a)
            letter2249b=int(letter49a)+int(number1)

            letter50a=int(letter49b)
            letter50b=int(letter49b)+int(number3)
            letter1150a=int(letter50a)
            letter2250b=int(letter50a)+int(number1)

            letter51a=int(letter50b)
            letter51b=int(letter50b)+int(number3)
            letter1151a=int(letter51a)
            letter2251b=int(letter51a)+int(number1)

            letter52a=int(letter51b)
            letter52b=int(letter51b)+int(number3)
            letter1152a=int(letter52a)
            letter2252b=int(letter52a)+int(number1)

            letter53a=int(letter52b)
            letter53b=int(letter52b)+int(number3)
            letter1153a=int(letter53a)
            letter2253b=int(letter53a)+int(number1)

            letter54a=int(letter53b)
            letter54b=int(letter53b)+int(number3)
            letter1154a=int(letter54a)
            letter2254b=int(letter54a)+int(number1)

            letter55a=int(letter54b)
            letter55b=int(letter54b)+int(number3)
            letter1155a=int(letter55a)
            letter2255b=int(letter55a)+int(number1)

            letter56a=int(letter55b)
            letter56b=int(letter55b)+int(number3)
            letter1156a=int(letter56a)
            letter2256b=int(letter56a)+int(number1)

            letter57a=int(letter56b)
            letter57b=int(letter56b)+int(number3)
            letter1157a=int(letter57a)
            letter2257b=int(letter57a)+int(number1)

            letter58a=int(letter57b)
            letter58b=int(letter57b)+int(number3)
            letter1158a=int(letter58a)
            letter2258b=int(letter58a)+int(number1)

            letter59a=int(letter58b)
            letter59b=int(letter58b)+int(number3)
            letter1159a=int(letter59a)
            letter2259b=int(letter59a)+int(number1)

            letter60a=int(letter59b)
            letter60b=int(letter59b)+int(number3)
            letter1160a=int(letter60a)
            letter2260b=int(letter60a)+int(number1)

            letter61a=int(letter60b)
            letter61b=int(letter60b)+int(number3)
            letter1161a=int(letter61a)
            letter2261b=int(letter61a)+int(number1)

            letter62a=int(letter61b)
            letter62b=int(letter61b)+int(number3)
            letter1162a=int(letter62a)
            letter2262b=int(letter62a)+int(number1)

            letter63a=int(letter62b)
            letter63b=int(letter62b)+int(number3)
            letter1163a=int(letter63a)
            letter2263b=int(letter63a)+int(number1)

            letter64a=int(letter63b)
            letter64b=int(letter63b)+int(number3)
            letter1164a=int(letter64a)
            letter2264b=int(letter64a)+int(number1)

            letter65a=int(letter64b)
            letter65b=int(letter64b)+int(number3)
            letter1165a=int(letter65a)
            letter2265b=int(letter65a)+int(number1)

            letter66a=int(letter65b)
            letter66b=int(letter65b)+int(number3)
            letter1166a=int(letter66a)
            letter2266b=int(letter66a)+int(number1)

            letter67a=int(letter66b)
            letter67b=int(letter66b)+int(number3)
            letter1167a=int(letter67a)
            letter2267b=int(letter67a)+int(number1)

            letter68a=int(letter67b)
            letter68b=int(letter67b)+int(number3)
            letter1168a=int(letter68a)
            letter2268b=int(letter68a)+int(number1)

            letter69a=int(letter68b)
            letter69b=int(letter68b)+int(number3)
            letter1169a=int(letter69a)
            letter2269b=int(letter69a)+int(number1)

            letter70a=int(letter69b)
            letter70b=int(letter69b)+int(number3)
            letter1170a=int(letter70a)
            letter2270b=int(letter70a)+int(number1)

            letter71a=int(letter70b)
            letter71b=int(letter70b)+int(number3)
            letter1171a=int(letter71a)
            letter2271b=int(letter71a)+int(number1)

            letter72a=int(letter71b)
            letter72b=int(letter71b)+int(number3)
            letter1172a=int(letter72a)
            letter2272b=int(letter72a)+int(number1)

            letter73a=int(letter72b)
            letter73b=int(letter72b)+int(number3)
            letter1173a=int(letter73a)
            letter2273b=int(letter73a)+int(number1)

            letter74a=int(letter73b)
            letter74b=int(letter73b)+int(number3)
            letter1174a=int(letter74a)
            letter2274b=int(letter74a)+int(number1)

            letter75a=int(letter74b)
            letter75b=int(letter74b)+int(number3)
            letter1175a=int(letter75a)
            letter2275b=int(letter75a)+int(number1)

            letter76a=int(letter75b)
            letter76b=int(letter75b)+int(number3)
            letter1176a=int(letter76a)
            letter2276b=int(letter76a)+int(number1)

            letter77a=int(letter76b)
            letter77b=int(letter76b)+int(number3)
            letter1177a=int(letter77a)
            letter2277b=int(letter77a)+int(number1)

            letter78a=int(letter77b)
            letter78b=int(letter77b)+int(number3)
            letter1178a=int(letter78a)
            letter2278b=int(letter78a)+int(number1)

            letter79a=int(letter78b)
            letter79b=int(letter78b)+int(number3)
            letter1179a=int(letter79a)
            letter2279b=int(letter79a)+int(number1)

            letter80a=int(letter79b)
            letter80b=int(letter79b)+int(number3)
            letter1180a=int(letter80a)
            letter2280b=int(letter80a)+int(number1)

            letter81a=int(letter80b)
            letter81b=int(letter80b)+int(number3)
            letter1181a=int(letter81a)
            letter2281b=int(letter81a)+int(number1)

            letter82a=int(letter81b)
            letter82b=int(letter81b)+int(number3)
            letter1182a=int(letter82a)
            letter2282b=int(letter82a)+int(number1)

            letter83a=int(letter82b)
            letter83b=int(letter82b)+int(number3)
            letter1183a=int(letter83a)
            letter2283b=int(letter83a)+int(number1)

            letter84a=int(letter83b)
            letter84b=int(letter83b)+int(number3)
            letter1184a=int(letter84a)
            letter2284b=int(letter84a)+int(number1)

            letter85a=int(letter84b)
            letter85b=int(letter84b)+int(number3)
            letter1185a=int(letter85a)
            letter2285b=int(letter85a)+int(number1)

            letter86a=int(letter85b)
            letter86b=int(letter85b)+int(number3)
            letter1186a=int(letter86a)
            letter2286b=int(letter86a)+int(number1)

            letter87a=int(letter86b)
            letter87b=int(letter86b)+int(number3)
            letter1187a=int(letter87a)
            letter2287b=int(letter87a)+int(number1)

            letter88a=int(letter87b)
            letter88b=int(letter87b)+int(number3)
            letter1188a=int(letter88a)
            letter2288b=int(letter88a)+int(number1)

            letter89a=int(letter88b)
            letter89b=int(letter88b)+int(number3)
            letter1189a=int(letter89a)
            letter2289b=int(letter89a)+int(number1)

            letter90a=int(letter89b)
            letter90b=int(letter89b)+int(number3)
            letter1190a=int(letter90a)
            letter2290b=int(letter90a)+int(number1)

            letter91a=int(letter90b)
            letter91b=int(letter90b)+int(number3)
            letter1191a=int(letter91a)
            letter2291b=int(letter91a)+int(number1)

            letter92a=int(letter91b)
            letter92b=int(letter91b)+int(number3)
            letter1192a=int(letter92a)
            letter2292b=int(letter92a)+int(number1)

            letter93a=int(letter92b)
            letter93b=int(letter92b)+int(number3)
            letter1193a=int(letter93a)
            letter2293b=int(letter93a)+int(number1)

            letter94a=int(letter93b)
            letter94b=int(letter93b)+int(number3)
            letter1194a=int(letter94a)
            letter2294b=int(letter94a)+int(number1)

            number4=int(94)*int(number1)*int(number2)

            while num1 != num:
                if message[int(num1):int(num2)] == "a":
                    new=str(new)+str(key[int(letter111a):int(letter221b)])
                    letter111a=int(letter111a)+int(number1)
                    letter221b=int(letter221b)+int(number1)
                    if letter111a == letter1b:
                        letter111a=int(letter1a)
                        letter221b=int(letter1a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "b":
                    new=str(new)+str(key[int(letter112a):int(letter222b)])
                    letter112a=int(letter112a)+int(number1)
                    letter222b=int(letter222b)+int(number1)
                    if letter112a == letter2b:
                        letter112a=int(letter2a)
                        letter222b=int(letter2a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "c":
                    new=str(new)+str(key[int(letter113a):int(letter223b)])
                    letter113a=int(letter113a)+int(number1)
                    letter223b=int(letter223b)+int(number1)
                    if letter113a == letter3b:
                        letter113a=int(letter3a)
                        letter223b=int(letter3a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "d":
                    new=str(new)+str(key[int(letter114a):int(letter224b)])
                    letter114a=int(letter114a)+int(number1)
                    letter224b=int(letter224b)+int(number1)
                    if letter114a == letter4b:
                        letter114a=int(letter4a)
                        letter224b=int(letter4a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "e":
                    new=str(new)+str(key[int(letter115a):int(letter225b)])
                    letter115a=int(letter115a)+int(number1)
                    letter225b=int(letter225b)+int(number1)
                    if letter115a == letter5b:
                        letter115a=int(letter5a)
                        letter225b=int(letter5a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "f":
                    new=str(new)+str(key[int(letter116a):int(letter226b)])
                    letter116a=int(letter116a)+int(number1)
                    letter226b=int(letter226b)+int(number1)
                    if letter116a == letter6b:
                        letter116a=int(letter6a)
                        letter226b=int(letter6a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "g":
                    new=str(new)+str(key[int(letter117a):int(letter227b)])
                    letter117a=int(letter117a)+int(number1)
                    letter227b=int(letter227b)+int(number1)
                    if letter117a == letter7b:
                        letter117a=int(letter7a)
                        letter227b=int(letter7a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "h":
                    new=str(new)+str(key[int(letter118a):int(letter228b)])
                    letter118a=int(letter118a)+int(number1)
                    letter228b=int(letter228b)+int(number1)
                    if letter118a == letter8b:
                        letter118a=int(letter8a)
                        letter228b=int(letter8a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "i":
                    new=str(new)+str(key[int(letter119a):int(letter229b)])
                    letter119a=int(letter119a)+int(number1)
                    letter229b=int(letter229b)+int(number1)
                    if letter119a == letter9b:
                        letter119a=int(letter9a)
                        letter229b=int(letter9a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "j":
                    new=str(new)+str(key[int(letter1110a):int(letter2210b)])
                    letter1110a=int(letter1110a)+int(number1)
                    letter2210b=int(letter2210b)+int(number1)
                    if letter1110a == letter10b:
                        letter1110a=int(letter10a)
                        letter2210b=int(letter10a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "k":
                    new=str(new)+str(key[int(letter1111a):int(letter2211b)])
                    letter1111a=int(letter1111a)+int(number1)
                    letter2211b=int(letter2211b)+int(number1)
                    if letter1111a == letter11b:
                        letter1111a=int(letter11a)
                        letter2211b=int(letter11a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "l":
                    new=str(new)+str(key[int(letter1112a):int(letter2212b)])
                    letter1112a=int(letter1112a)+int(number1)
                    letter2212b=int(letter2212b)+int(number1)
                    if letter1112a == letter12b:
                        letter1112a=int(letter12a)
                        letter2212b=int(letter12a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "m":
                    new=str(new)+str(key[int(letter1113a):int(letter2213b)])
                    letter1113a=int(letter1113a)+int(number1)
                    letter2213b=int(letter2213b)+int(number1)
                    if letter1113a == letter13b:
                        letter1113a=int(letter13a)
                        letter2213b=int(letter13a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "n":
                    new=str(new)+str(key[int(letter1114a):int(letter2214b)])
                    letter1114a=int(letter1114a)+int(number1)
                    letter2214b=int(letter2214b)+int(number1)
                    if letter1114a == letter14b:
                        letter1114a=int(letter14a)
                        letter2214b=int(letter14a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "o":
                    new=str(new)+str(key[int(letter1115a):int(letter2215b)])
                    letter1115a=int(letter1115a)+int(number1)
                    letter2215b=int(letter2215b)+int(number1)
                    if letter1115a == letter15b:
                        letter1115a=int(letter15a)
                        letter2215b=int(letter15a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "p":
                    new=str(new)+str(key[int(letter1116a):int(letter2216b)])
                    letter1116a=int(letter1116a)+int(number1)
                    letter2216b=int(letter2216b)+int(number1)
                    if letter1116a == letter16b:
                        letter1116a=int(letter16a)
                        letter2216b=int(letter16a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "q":
                    new=new+key[int(letter1117a):int(letter2217b)]
                    letter1117a=int(letter1117a)+int(number1)
                    letter2217b=int(letter2217b)+int(number1)
                    if letter1117a == letter17b:
                        letter1117a=int(letter17a)
                        letter2217b=int(letter17a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "r":
                    new=str(new)+str(key[int(letter1118a):int(letter2218b)])
                    letter1118a=int(letter1118a)+int(number1)
                    letter2218b=int(letter2218b)+int(number1)
                    if letter1118a == letter18b:
                        letter1118a=int(letter18a)
                        letter2218b=int(letter18a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "s":
                    new=str(new)+str(key[int(letter1119a):int(letter2219b)])
                    letter1119a=int(letter1119a)+int(number1)
                    letter2219b=int(letter2219b)+int(number1)
                    if letter1119a == letter19b:
                        letter1119a=int(letter19a)
                        letter2219b=int(letter19a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "t":
                    new=str(new)+str(key[int(letter1120a):int(letter2220b)])
                    letter1120a=int(letter1120a)+int(number1)
                    letter2220b=int(letter2220b)+int(number1)
                    if letter1120a == letter20b:
                        letter1120a=int(letter20a)
                        letter2220b=int(letter20a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "u":
                    new=str(new)+str(key[int(letter1121a):int(letter2221b)])
                    letter1121a=int(letter1121a)+int(number1)
                    letter2221b=int(letter2221b)+int(number1)
                    if letter1121a == letter21b:
                        letter1121a=int(letter21a)
                        letter2221b=int(letter21a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "v":
                    new=str(new)+str(key[int(letter1122a):int(letter2222b)])
                    letter1122a=int(letter1122a)+int(number1)
                    letter2222b=int(letter2222b)+int(number1)
                    if letter1122a == letter22b:
                        letter1122a=int(letter22a)
                        letter2222b=int(letter22a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "w":
                    new=str(new)+str(key[int(letter1123a):int(letter2223b)])
                    letter1123a=int(letter1123a)+int(number1)
                    letter2223b=int(letter2223b)+int(number1)
                    if letter1123a == letter23b:
                        letter1123a=int(letter23a)
                        letter2223b=int(letter23a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "x":
                    new=str(new)+str(key[int(letter1124a):int(letter2224b)])
                    letter1124a=int(letter1124a)+int(number1)
                    letter2224b=int(letter2224b)+int(number1)
                    if letter1124a == letter24b:
                        letter1124a=int(letter24a)
                        letter2224b=int(letter24a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "y":
                    new=str(new)+str(key[int(letter1125a):int(letter2225b)])
                    letter1125a=int(letter1125a)+int(number1)
                    letter2225b=int(letter2225b)+int(number1)
                    if letter1125a == letter25b:
                        letter1125a=int(letter25a)
                        letter2225b=int(letter25a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "z":
                    new=str(new)+str(key[int(letter1126a):int(letter2226b)])
                    letter1126a=int(letter1126a)+int(number1)
                    letter2226b=int(letter2226b)+int(number1)
                    if letter1126a == letter26b:
                        letter1126a=int(letter26a)
                        letter2226b=int(letter26a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "A":
                    new=str(new)+str(key[int(letter1127a):int(letter2227b)])
                    letter1127a=int(letter1127a)+int(number1)
                    letter2227b=int(letter2227b)+int(number1)
                    if letter1127a == letter27b:
                        letter1127a=int(letter27a)
                        letter2227b=int(letter27a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "B":
                    new=str(new)+str(key[int(letter1128a):int(letter2228b)])
                    letter1128a=int(letter1128a)+int(number1)
                    letter2228b=int(letter2228b)+int(number1)
                    if letter1128a == letter28b:
                        letter1128a=int(letter28a)
                        letter2228b=int(letter28a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "C":
                    new=str(new)+str(key[int(letter1129a):int(letter2229b)])
                    letter1129a=int(letter1129a)+int(number1)
                    letter2229b=int(letter2229b)+int(number1)
                    if letter1129a == letter29b:
                        letter1129a=int(letter29a)
                        letter2229b=int(letter29a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "D":
                    new=str(new)+str(key[int(letter1130a):int(letter2230b)])
                    letter1130a=int(letter1130a)+int(number1)
                    letter2230b=int(letter2230b)+int(number1)
                    if letter1130a == letter30b:
                        letter1130a=int(letter30a)
                        letter2230b=int(letter30a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "E":
                    new=str(new)+str(key[int(letter1131a):int(letter2231b)])
                    letter1131a=int(letter1131a)+int(number1)
                    letter2231b=int(letter2231b)+int(number1)
                    if letter1131a == letter31b:
                        letter1131a=int(letter31a)
                        letter2231b=int(letter31a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "F":
                    new=str(new)+str(key[int(letter1132a):int(letter2232b)])
                    letter1132a=int(letter1132a)+int(number1)
                    letter2232b=int(letter2232b)+int(number1)
                    if letter1132a == letter32b:
                        letter1132a=int(letter32a)
                        letter2232b=int(letter32a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "G":
                    new=str(new)+str(key[int(letter1133a):int(letter2233b)])
                    letter1133a=int(letter1133a)+int(number1)
                    letter2233b=int(letter2233b)+int(number1)
                    if letter1133a == letter33b:
                        letter1133a=int(letter33a)
                        letter2233b=int(letter33a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "H":
                    new=str(new)+str(key[int(letter1134a):int(letter2234b)])
                    letter1134a=int(letter1134a)+int(number1)
                    letter2234b=int(letter2234b)+int(number1)
                    if letter1134a == letter34b:
                        letter1134a=int(letter34a)
                        letter2234b=int(letter34a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "I":
                    new=str(new)+str(key[int(letter1135a):int(letter2235b)])
                    letter1135a=int(letter1135a)+int(number1)
                    letter2235b=int(letter2235b)+int(number1)
                    if letter1135a == letter35b:
                        letter1135a=int(letter35a)
                        letter2235b=int(letter35a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "J":
                    new=str(new)+str(key[int(letter1136a):int(letter2236b)])
                    letter1136a=int(letter1136a)+int(number1)
                    letter2236b=int(letter2236b)+int(number1)
                    if letter1136a == letter36b:
                        letter1136a=int(letter36a)
                        letter2236b=int(letter36a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "K":
                    new=str(new)+str(key[int(letter1137a):int(letter2237b)])
                    letter1137a=int(letter1137a)+int(number1)
                    letter2237b=int(letter2237b)+int(number1)
                    if letter1137a == letter37b:
                        letter1137a=int(letter37a)
                        letter2237b=int(letter37a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "L":
                    new=str(new)+str(key[int(letter1138a):int(letter2238b)])
                    letter1138a=int(letter1138a)+int(number1)
                    letter2238b=int(letter2238b)+int(number1)
                    if letter1138a == letter38b:
                        letter1138a=int(letter38a)
                        letter2238b=int(letter38a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "M":
                    new=str(new)+str(key[int(letter1139a):int(letter2239b)])
                    letter1139a=int(letter1139a)+int(number1)
                    letter2239b=int(letter2239b)+int(number1)
                    if letter1139a == letter39b:
                        letter1139a=int(letter39a)
                        letter2239b=int(letter39a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "N":
                    new=str(new)+str(key[int(letter1140a):int(letter2240b)])
                    letter1140a=int(letter1140a)+int(number1)
                    letter2240b=int(letter2240b)+int(number1)
                    if letter1140a == letter40b:
                        letter1140a=int(letter40a)
                        letter2240b=int(letter40a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "O":
                    new=str(new)+str(key[int(letter1141a):int(letter2241b)])
                    letter1141a=int(letter1141a)+int(number1)
                    letter2241b=int(letter2241b)+int(number1)
                    if letter1141a == letter41b:
                        letter1141a=int(letter41a)
                        letter2241b=int(letter41a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "P":
                    new=str(new)+str(key[int(letter1142a):int(letter2242b)])
                    letter1142a=int(letter1142a)+int(number1)
                    letter2242b=int(letter2242b)+int(number1)
                    if letter1142a == letter42b:
                        letter1142a=int(letter42a)
                        letter2242b=int(letter42a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "Q":
                    new=str(new)+str(key[int(letter1143a):int(letter2243b)])
                    letter1143a=int(letter1143a)+int(number1)
                    letter2243b=int(letter2243b)+int(number1)
                    if letter1143a == letter43b:
                        letter1143a=int(letter43a)
                        letter2243b=int(letter43a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "R":
                    new=str(new)+str(key[int(letter1144a):int(letter2244b)])
                    letter1144a=int(letter1144a)+int(number1)
                    letter2244b=int(letter2244b)+int(number1)
                    if letter1144a == letter44b:
                        letter1144a=int(letter44a)
                        letter2244b=int(letter44a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "S":
                    new=str(new)+str(key[int(letter1145a):int(letter2245b)])
                    letter1145a=int(letter1145a)+int(number1)
                    letter2245b=int(letter2245b)+int(number1)
                    if letter1145a == letter45b:
                        letter1145a=int(letter45a)
                        letter2245b=int(letter45a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "T":
                    new=str(new)+str(key[int(letter1146a):int(letter2246b)])
                    letter11a=int(letter1146a)+int(number1)
                    letter22b=int(letter2246b)+int(number1)
                    if letter1146a == letter46b:
                        letter1146a=int(letter46a)
                        letter2246b=int(letter46a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "U":
                    new=str(new)+str(key[int(letter1147a):int(letter2247b)])
                    letter1147a=int(letter1147a)+int(number1)
                    letter2247b=int(letter2247b)+int(number1)
                    if letter1147a == letter47b:
                        letter1147a=int(letter47a)
                        letter2247b=int(letter47a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "V":
                    new=str(new)+str(key[int(letter1148a):int(letter2248b)])
                    letter1148a=int(letter1148a)+int(number1)
                    letter2248b=int(letter2248b)+int(number1)
                    if letter1148a == letter48b:
                        letter1148a=int(letter48a)
                        letter2248b=int(letter48a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "W":
                    new=str(new)+str(key[int(letter1149a):int(letter2249b)])
                    letter1149a=int(letter1149a)+int(number1)
                    letter2249b=int(letter2249b)+int(number1)
                    if letter1149a == letter49b:
                        letter1149a=int(letter49a)
                        letter2249b=int(letter49a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "X":
                    new=str(new)+str(key[int(letter1150a):int(letter2250b)])
                    letter1150a=int(letter1150a)+int(number1)
                    letter2250b=int(letter2250b)+int(number1)
                    if letter1150a == letter50b:
                        letter1150a=int(letter50a)
                        letter2250b=int(letter50a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "Y":
                    new=str(new)+str(key[int(letter1151a):int(letter2251b)])
                    letter1151a=int(letter1151a)+int(number1)
                    letter2251b=int(letter2251b)+int(number1)
                    if letter1151a == letter51b:
                        letter1151a=int(letter51a)
                        letter2251b=int(letter51a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "Z":
                    new=str(new)+str(key[int(letter1152a):int(letter2252b)])
                    letter1152a=int(letter1152a)+int(number1)
                    letter2252b=int(letter2252b)+int(number1)
                    if letter1152a == letter52b:
                        letter1152a=int(letter52a)
                        letter2252b=int(letter52a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "1":
                    new=str(new)+str(key[int(letter1153a):int(letter2253b)])
                    letter1153a=int(letter1153a)+int(number1)
                    letter2253b=int(letter2253b)+int(number1)
                    if letter1153a == letter53b:
                        letter1153a=int(letter53a)
                        letter2253b=int(letter53a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "2":
                    new=str(new)+str(key[int(letter1154a):int(letter2254b)])
                    letter1154a=int(letter1154a)+int(number1)
                    letter2254b=int(letter2254b)+int(number1)
                    if letter1154a == letter54b:
                        letter1154a=int(letter54a)
                        letter2254b=int(letter54a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "3":
                    new=str(new)+str(key[int(letter1155a):int(letter2255b)])
                    letter1155a=int(letter1155a)+int(number1)
                    letter2255b=int(letter2255b)+int(number1)
                    if letter1155a == letter55b:
                        letter1155a=int(letter55a)
                        letter2255b=int(letter55a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "4":
                    new=str(new)+str(key[int(letter1156a):int(letter2256b)])
                    letter1156a=int(letter1156a)+int(number1)
                    letter2256b=int(letter2256b)+int(number1)
                    if letter1156a == letter56b:
                        letter1156a=int(letter56a)
                        letter2256b=int(letter56a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "5":
                    new=str(new)+str(key[int(letter1157a):int(letter2257b)])
                    letter1157a=int(letter1157a)+int(number1)
                    letter2257b=int(letter2257b)+int(number1)
                    if letter1157a == letter57b:
                        letter1157a=int(letter57a)
                        letter2257b=int(letter57a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "6":
                    new=str(new)+str(key[int(letter1158a):int(letter2258b)])
                    letter1158a=int(letter1158a)+int(number1)
                    letter2258b=int(letter2258b)+int(number1)
                    if letter1158a == letter58b:
                        letter1158a=int(letter58a)
                        letter2258b=int(letter58a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "7":
                    new=str(new)+str(key[int(letter1159a):int(letter2259b)])
                    letter1159a=int(letter1159a)+int(number1)
                    letter2259b=int(letter2259b)+int(number1)
                    if letter1159a == letter59b:
                        letter1159a=int(letter59a)
                        letter2259b=int(letter59a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "8":
                    new=str(new)+str(key[int(letter1160a):int(letter2260b)])
                    letter1160a=int(letter1160a)+int(number1)
                    letter2260b=int(letter2260b)+int(number1)
                    if letter1160a == letter60b:
                        letter1160a=int(letter60a)
                        letter2260b=int(letter60a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "9":
                    new=str(new)+str(key[int(letter1161a):int(letter2261b)])
                    letter1161a=int(letter1161a)+int(number1)
                    letter2261b=int(letter2261b)+int(number1)
                    if letter1161a == letter61b:
                        letter1161a=int(letter61a)
                        letter2261b=int(letter61a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "0":
                    new=str(new)+str(key[int(letter1162a):int(letter2262b)])
                    letter1162a=int(letter1162a)+int(number1)
                    letter2262b=int(letter2262b)+int(number1)
                    if letter1162a == letter62b:
                        letter1162a=int(letter62a)
                        letter2262b=int(letter62a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "!":
                    new=str(new)+str(key[int(letter1163a):int(letter2263b)])
                    letter1163a=int(letter1163a)+int(number1)
                    letter2263b=int(letter2263b)+int(number1)
                    if letter1163a == letter63b:
                        letter1163a=int(letter63a)
                        letter2263b=int(letter63a)+int(number1)
                    
                elif message[int(num1):int(num2)] == '"':
                    new=str(new)+str(key[int(letter1164a):int(letter2264b)])
                    letter1164a=int(letter1164a)+int(number1)
                    letter2264b=int(letter2264b)+int(number1)
                    if letter1164a == letter64b:
                        letter1164a=int(letter64a)
                        letter2264b=int(letter64a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "$":
                    new=str(new)+str(key[int(letter1165a):int(letter2265b)])
                    letter1165a=int(letter1165a)+int(number1)
                    letter2265b=int(letter2265b)+int(number1)
                    if letter1165a == letter65b:
                        letter1165a=int(letter65a)
                        letter2265b=int(letter65a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "%":
                    new=str(new)+str(key[int(letter1166a):int(letter2266b)])
                    letter1166a=int(letter1166a)+int(number1)
                    letter2266b=int(letter2266b)+int(number1)
                    if letter1166a == letter66b:
                        letter1166a=int(letter66a)
                        letter2266b=int(letter66a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "^":
                    new=str(new)+str(key[int(letter1167a):int(letter2267b)])
                    letter1167a=int(letter1167a)+int(number1)
                    letter2267b=int(letter2267b)+int(number1)
                    if letter1167a == letter67b:
                        letter1167a=int(letter67a)
                        letter2267b=int(letter67a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "&":
                    new=str(new)+str(key[int(letter1168a):int(letter2268b)])
                    letter1168a=int(letter1168a)+int(number1)
                    letter2268b=int(letter2268b)+int(number1)
                    if letter1168a == letter68b:
                        letter1168a=int(letter68a)
                        letter2268b=int(letter68a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "*":
                    new=str(new)+str(key[int(letter1169a):int(letter2269b)])
                    letter1169a=int(letter1169a)+int(number1)
                    letter2269b=int(letter2269b)+int(number1)
                    if letter1169a == letter69b:
                        letter1169a=int(letter69a)
                        letter2269b=int(letter69a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "(":
                    new=str(new)+str(key[int(letter1170a):int(letter2270b)])
                    letter1170a=int(letter1170a)+int(number1)
                    letter2270b=int(letter2270b)+int(number1)
                    if letter1170a == letter70b:
                        letter1170a=int(letter70a)
                        letter2270b=int(letter70a)+int(number1)
                    
                elif message[int(num1):int(num2)] == ")":
                    new=str(new)+str(key[int(letter1171a):int(letter2271b)])
                    letter1171a=int(letter1171a)+int(number1)
                    letter2271b=int(letter2271b)+int(number1)
                    if letter1171a == letter71b:
                        letter1171a=int(letter71a)
                        letter2271b=int(letter71a)+int(number1)
                    
                elif message[int(num1):int(num2)] == '_':
                    new=str(new)+str(key[int(letter1172a):int(letter2272b)])
                    letter1172a=int(letter1172a)+int(number1)
                    letter2272b=int(letter2272b)+int(number1)
                    if letter1172a == letter72b:
                        letter1172a=int(letter72a)
                        letter2272b=int(letter72a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "-":
                    new=str(new)+str(key[int(letter1173a):int(letter2273b)])
                    letter1173a=int(letter1173a)+int(number1)
                    letter2273b=int(letter2273b)+int(number1)
                    if letter1173a == letter73b:
                        letter1173a=int(letter73a)
                        letter2273b=int(letter73a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "+":
                    new=str(new)+str(key[int(letter1174a):int(letter2274b)])
                    letter1174a=int(letter1174a)+int(number1)
                    letter2274b=int(letter2274b)+int(number1)
                    if letter1174a == letter74b:
                        letter1174a=int(letter74a)
                        letter2274b=int(letter74a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "=":
                    new=str(new)+str(key[int(letter1175a):int(letter2275b)])
                    letter1175a=int(letter1175a)+int(number1)
                    letter2275b=int(letter2275b)+int(number1)
                    if letter1175a == letter75b:
                        letter1175a=int(letter75a)
                        letter2275b=int(letter75a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "{":
                    new=str(new)+str(key[int(letter1176a):int(letter2276b)])
                    letter1176a=int(letter1176a)+int(number1)
                    letter2276b=int(letter2276b)+int(number1)
                    if letter1176a == letter76b:
                        letter1176a=int(letter76a)
                        letter2276b=int(letter76a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "}":
                    new=str(new)+str(key[int(letter1177a):int(letter2277b)])
                    letter1177a=int(letter1177a)+int(number1)
                    letter2277b=int(letter2277b)+int(number1)
                    if letter1177a == letter77b:
                        letter1177a=int(letter77a)
                        letter2277b=int(letter77a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "[":
                    new=str(new)+str(key[int(letter1178a):int(letter2278b)])
                    letter1178a=int(letter1178a)+int(number1)
                    letter2278b=int(letter2278b)+int(number1)
                    if letter1178a == letter78b:
                        letter1178a=int(letter78a)
                        letter2278b=int(letter78a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "]":
                    new=str(new)+str(key[int(letter1179a):int(letter2279b)])
                    letter1179a=int(letter1179a)+int(number1)
                    letter2279b=int(letter2279b)+int(number1)
                    if letter1179a == letter79b:
                        letter1179a=int(letter79a)
                        letter2279b=int(letter79a)+int(number1)
                    
                elif message[int(num1):int(num2)] == ":":
                    new=str(new)+str(key[int(letter1180a):int(letter2280b)])
                    letter1180a=int(letter1180a)+int(number1)
                    letter2280b=int(letter2280b)+int(number1)
                    if letter1180a == letter80b:
                        letter1180a=int(letter80a)
                        letter2280b=int(letter80a)+int(number1)
                    
                elif message[int(num1):int(num2)] == ";":
                    new=str(new)+str(key[int(letter1181a):int(letter2281b)])
                    letter1181a=int(letter1181a)+int(number1)
                    letter2281b=int(letter2281b)+int(number1)
                    if letter1181a == letter81b:
                        letter1181a=int(letter81a)
                        letter2281b=int(letter81a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "@":
                    new=str(new)+str(key[int(letter1182a):int(letter2282b)])
                    letter1182a=int(letter1182a)+int(number1)
                    letter2282b=int(letter2282b)+int(number1)
                    if letter1182a == letter82b:
                        letter1182a=int(letter82a)
                        letter2282b=int(letter82a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "'":
                    new=str(new)+str(key[int(letter1183a):int(letter2283b)])
                    letter1183a=int(letter1183a)+int(number1)
                    letter2283b=int(letter2283b)+int(number1)
                    if letter1183a == letter83b:
                        letter1183a=int(letter83a)
                        letter2283b=int(letter83a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "~":
                    new=str(new)+str(key[int(letter1184a):int(letter2284b)])
                    letter1184a=int(letter1184a)+int(number1)
                    letter2284b=int(letter2284b)+int(number1)
                    if letter1184a == letter84b:
                        letter1184a=int(letter84a)
                        letter2284b=int(letter84a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "#":
                    new=str(new)+str(key[int(letter1185a):int(letter2285b)])
                    letter1185a=int(letter1185a)+int(number1)
                    letter2285b=int(letter2285b)+int(number1)
                    if letter1185a == letter85b:
                        letter1185a=int(letter85a)
                        letter2285b=int(letter85a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "<":
                    new=str(new)+str(key[int(letter1186a):int(letter2286b)])
                    letter1186a=int(letter1186a)+int(number1)
                    letter2286b=int(letter2286b)+int(number1)
                    if letter1186a == letter86b:
                        letter1186a=int(letter86a)
                        letter2286b=int(letter86a)+int(number1)
                    
                elif message[int(num1):int(num2)] == ">":
                    new=str(new)+str(key[int(letter1187a):int(letter2287b)])
                    letter1187a=int(letter1187a)+int(number1)
                    letter2287b=int(letter2287b)+int(number1)
                    if letter1187a == letter87b:
                        letter1187a=int(letter87a)
                        letter2287b=int(letter87a)+int(number1)
                    
                elif message[int(num1):int(num2)] == ",":
                    new=str(new)+str(key[int(letter1188a):int(letter2288b)])
                    letter1188a=int(letter1188a)+int(number1)
                    letter2288b=int(letter2288b)+int(number1)
                    if letter1188a == letter88b:
                        letter1188a=int(letter88a)
                        letter2288b=int(letter88a)+int(number1)
                    
                elif message[int(num1):int(num2)] == ".":
                    new=str(new)+str(key[int(letter1189a):int(letter2289b)])
                    letter1189a=int(letter1189a)+int(number1)
                    letter2289b=int(letter2289b)+int(number1)
                    if letter1189a == letter89b:
                        letter1189a=int(letter89a)
                        letter2289b=int(letter89a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "?":
                    new=str(new)+str(key[int(letter1190a):int(letter2290b)])
                    letter1190a=int(letter1190a)+int(number1)
                    letter2290b=int(letter2290b)+int(number1)
                    if letter1190a == letter90b:
                        letter1190a=int(letter90a)
                        letter2290b=int(letter90a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "/":
                    new=str(new)+str(key[int(letter1191a):int(letter2291b)])
                    letter1191a=int(letter1191a)+int(number1)
                    letter2291b=int(letter2291b)+int(number1)
                    if letter1191a == letter91b:
                        letter1191a=int(letter91a)
                        letter2291b=int(letter91a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "|":
                    new=str(new)+str(key[int(letter1192a):int(letter2292b)])
                    letter1192a=int(letter1192a)+int(number1)
                    letter2292b=int(letter2292b)+int(number1)
                    if letter1192a == letter92b:
                        letter1192a=int(letter92a)
                        letter2292b=int(letter92a)+int(number1)
                    
                elif message[int(num1):int(num2)] == " ":
                    new=str(new)+str(key[int(letter1193a):int(letter2293b)])
                    letter1193a=int(letter1193a)+int(number1)
                    letter2293b=int(letter2293b)+int(number1)
                    if letter1193a == letter93b:
                        letter1193a=int(letter93a)
                        letter2293b=int(letter93a)+int(number1)
                    
                elif message[int(num1):int(num2)] == "    ":
                    new=str(new)+str(key[int(letter1194a):int(letter2294b)])
                    letter1194a=int(letter1194a)+int(number1)
                    letter2294b=int(letter2294b)+int(number1)
                    if letter1194a == letter94b:
                        letter1194a=int(letter94a)
                        letter2294b=int(letter94a)+int(number1)
                num1=int(num1)+int(1)
                num2=int(num2)+int(1)
            print(new)
            break
            
    if menu == "3":
        while __name__ == "__main__":
            message=""
            key=""
            print("Enter the message that you want to decrypt.")
            message=input("")
            print("Enter the key you want to uses to decrypt the message.")
            key=str(input(""))
            if message == "":
                break
            elif key == "":
                break
            number1=str(key[0:1])
            try:
                ver=int(number1)
            except ValueError:
                break
            else:
                break
            check1=0
            check2=1
            num=int(len(message))
            num1=0
            num2=int(number1)
            num3=2
            num4=3
            new=""
            while check1 != check2:
                if key[int(num3):int(num4)] == "a":
                    number2=key[int(2):int(num4-1)]
                    break
                else:
                    num3=num3+1
                    num4=num4+1
                    
            a=int(num4)-int(3)

            if 1 == 1:
                lengthkey=len(str(key))
                lengthkey1=int(a)+int(3)
                key=key[int(lengthkey1):int(lengthkey)]

            number3=int(number1)*int(number2)
            number4=int(94)*int(number1)*int(number2)
            if len(key) != number4:
                break
            letter1a=int(0)
            letter1b=int(number3)
            letter111a=int(letter1a)
            letter221b=int(letter1a)+int(number1)

            letter2a=int(letter1b)
            letter2b=int(letter1b)+int(number3)
            letter112a=int(letter2a)
            letter222b=int(letter2a)+int(number1)

            letter3a=int(letter2b)
            letter3b=int(letter2b)+int(number3)
            letter113a=int(letter3a)
            letter223b=int(letter3a)+int(number1)

            letter4a=int(letter3b)
            letter4b=int(letter3b)+int(number3)
            letter114a=int(letter4a)
            letter224b=int(letter4a)+int(number1)

            letter5a=int(letter4b)
            letter5b=int(letter4b)+int(number3)
            letter115a=int(letter5a)
            letter225b=int(letter5a)+int(number1)

            letter6a=int(letter5b)
            letter6b=int(letter5b)+int(number3)
            letter116a=int(letter6a)
            letter226b=int(letter6a)+int(number1)

            letter7a=int(letter6b)
            letter7b=int(letter6b)+int(number3)
            letter117a=int(letter7a)
            letter227b=int(letter7a)+int(number1)

            letter8a=int(letter7b)
            letter8b=int(letter7b)+int(number3)
            letter118a=int(letter8a)
            letter228b=int(letter8a)+int(number1)

            letter9a=int(letter8a)
            letter9b=int(letter8a)+int(number3)
            letter119a=int(letter9a)
            letter229b=int(letter9a)+int(number1)

            letter10a=int(letter9b)
            letter10b=int(letter9b)+int(number3)
            letter1110a=int(letter10a)
            letter2210b=int(letter10a)+int(number1)

            letter11a=int(letter10b)
            letter11b=int(letter10b)+int(number3)
            letter1111a=int(letter11a)
            letter2211b=int(letter11a)+int(number1)

            letter12a=int(letter11b)
            letter12b=int(letter11b)+int(number3)
            letter1112a=int(letter12a)
            letter2212b=int(letter12a)+int(number1)

            letter13a=int(letter12b)
            letter13b=int(letter12b)+int(number3)
            letter1113a=int(letter13a)
            letter2213b=int(letter13a)+int(number1)

            letter14a=int(letter13b)
            letter14b=int(letter13b)+int(number3)
            letter1114a=int(letter14a)
            letter2214b=int(letter14a)+int(number1)

            letter15a=int(letter14b)
            letter15b=int(letter14b)+int(number3)
            letter1115a=int(letter15a)
            letter2215b=int(letter15a)+int(number1)


            letter16a=int(letter15b)
            letter16b=int(letter15b)+int(number3)
            letter1116a=int(letter16a)
            letter2216b=int(letter16a)+int(number1)

            letter17a=int(letter16b)
            letter17b=int(letter16b)+int(number3)
            letter1117a=int(letter17a)
            letter2217b=int(letter17a)+int(number1)

            letter18a=int(letter17b)
            letter18b=int(letter17b)+int(number3)
            letter1118a=int(letter18a)
            letter2218b=int(letter18a)+int(number1)

            letter19a=int(letter18b)
            letter19b=int(letter18b)+int(number3)
            letter1119a=int(letter19a)
            letter2219b=int(letter19a)+int(number1)

            letter20a=int(letter19b)
            letter20b=int(letter19b)+int(number3)
            letter1120a=int(letter20a)
            letter2220b=int(letter20a)+int(number1)

            letter21a=int(letter20b)
            letter21b=int(letter20b)+int(number3)
            letter1121a=int(letter21a)
            letter2221b=int(letter21a)+int(number1)

            letter22a=int(letter21b)
            letter22b=int(letter21b)+int(number3)
            letter1122a=int(letter22a)
            letter2222b=int(letter22a)+int(number1)

            letter23a=int(letter22b)
            letter23b=int(letter22b)+int(number3)
            letter1123a=int(letter23a)
            letter2223b=int(letter23a)+int(number1)

            letter24a=int(letter23b)
            letter24b=int(letter23b)+int(number3)
            letter1124a=int(letter24a)
            letter2224b=int(letter24a)+int(number1)

            letter25a=int(letter24b)
            letter25b=int(letter24b)+int(number3)
            letter1125a=int(letter25a)
            letter2225b=int(letter25a)+int(number1)

            letter26a=int(letter25b)
            letter26b=int(letter25b)+int(number3)
            letter1126a=int(letter26a)
            letter2226b=int(letter26a)+int(number1)

            letter27a=int(letter26b)
            letter27b=int(letter26b)+int(number3)
            letter1127a=int(letter27a)
            letter2227b=int(letter27a)+int(number1)

            letter28a=int(letter27b)
            letter28b=int(letter27b)+int(number3)
            letter1128a=int(letter28a)
            letter2228b=int(letter28a)+int(number1)

            letter29a=int(letter28b)
            letter29b=int(letter28b)+int(number3)
            letter1129a=int(letter29a)
            letter2229b=int(letter29a)+int(number1)

            letter30a=int(letter29b)
            letter30b=int(letter29b)+int(number3)
            letter1130a=int(letter30a)
            letter2230b=int(letter30a)+int(number1)

            letter31a=int(letter30b)
            letter31b=int(letter30b)+int(number3)
            letter1131a=int(letter31a)
            letter2231b=int(letter31a)+int(number1)

            letter32a=int(letter31b)
            letter32b=int(letter31b)+int(number3)
            letter1132a=int(letter32a)
            letter2232b=int(letter32a)+int(number1)

            letter33a=int(letter32b)
            letter33b=int(letter32b)+int(number3)
            letter1133a=int(letter33a)
            letter2233b=int(letter33a)+int(number1)

            letter34a=int(letter33b)
            letter34b=int(letter33b)+int(number3)
            letter1134a=int(letter34a)
            letter2234b=int(letter34a)+int(number1)

            letter35a=int(letter34b)
            letter35b=int(letter34b)+int(number3)
            letter1135a=int(letter35a)
            letter2235b=int(letter35a)+int(number1)

            letter36a=int(letter35b)
            letter36b=int(letter35b)+int(number3)
            letter1136a=int(letter36a)
            letter2236b=int(letter36a)+int(number1)

            letter37a=int(letter36b)
            letter37b=int(letter36b)+int(number3)
            letter1137a=int(letter37a)
            letter2237b=int(letter37a)+int(number1)

            letter38a=int(letter37b)
            letter38b=int(letter37b)+int(number3)
            letter1138a=int(letter38a)
            letter2238b=int(letter38a)+int(number1)

            letter39a=int(letter38b)
            letter39b=int(letter38b)+int(number3)
            letter1139a=int(letter39a)
            letter2239b=int(letter39a)+int(number1)

            letter40a=int(letter39b)
            letter40b=int(letter39b)+int(number3)
            letter1140a=int(letter40a)
            letter2240b=int(letter40a)+int(number1)

            letter41a=int(letter40b)
            letter41b=int(letter40b)+int(number3)
            letter1141a=int(letter41a)
            letter2241b=int(letter41a)+int(number1)

            letter42a=int(letter41b)
            letter42b=int(letter41b)+int(number3)
            letter1142a=int(letter42a)
            letter2242b=int(letter42a)+int(number1)

            letter43a=int(letter42b)
            letter43b=int(letter42b)+int(number3)
            letter1143a=int(letter43a)
            letter2243b=int(letter43a)+int(number1)

            letter44a=int(letter43b)
            letter44b=int(letter43b)+int(number3)
            letter1144a=int(letter44a)
            letter2244b=int(letter44a)+int(number1)

            letter45a=int(letter44b)
            letter45b=int(letter44b)+int(number3)
            letter1145a=int(letter45a)
            letter2245b=int(letter45a)+int(number1)

            letter46a=int(letter45b)
            letter46b=int(letter45b)+int(number3)
            letter1146a=int(letter46a)
            letter2246b=int(letter46a)+int(number1)

            letter47a=int(letter46b)
            letter47b=int(letter46b)+int(number3)
            letter1147a=int(letter47a)
            letter2247b=int(letter47a)+int(number1)

            letter48a=int(letter47b)
            letter48b=int(letter47b)+int(number3)
            letter1148a=int(letter48a)
            letter2248b=int(letter48a)+int(number1)

            letter49a=int(letter48b)
            letter49b=int(letter48b)+int(number3)
            letter1149a=int(letter49a)
            letter2249b=int(letter49a)+int(number1)

            letter50a=int(letter49b)
            letter50b=int(letter49b)+int(number3)
            letter1150a=int(letter50a)
            letter2250b=int(letter50a)+int(number1)

            letter51a=int(letter50b)
            letter51b=int(letter50b)+int(number3)
            letter1151a=int(letter51a)
            letter2251b=int(letter51a)+int(number1)

            letter52a=int(letter51b)
            letter52b=int(letter51b)+int(number3)
            letter1152a=int(letter52a)
            letter2252b=int(letter52a)+int(number1)

            letter53a=int(letter52b)
            letter53b=int(letter52b)+int(number3)
            letter1153a=int(letter53a)
            letter2253b=int(letter53a)+int(number1)

            letter54a=int(letter53b)
            letter54b=int(letter53b)+int(number3)
            letter1154a=int(letter54a)
            letter2254b=int(letter54a)+int(number1)

            letter55a=int(letter54b)
            letter55b=int(letter54b)+int(number3)
            letter1155a=int(letter55a)
            letter2255b=int(letter55a)+int(number1)

            letter56a=int(letter55b)
            letter56b=int(letter55b)+int(number3)
            letter1156a=int(letter56a)
            letter2256b=int(letter56a)+int(number1)

            letter57a=int(letter56b)
            letter57b=int(letter56b)+int(number3)
            letter1157a=int(letter57a)
            letter2257b=int(letter57a)+int(number1)

            letter58a=int(letter57b)
            letter58b=int(letter57b)+int(number3)
            letter1158a=int(letter58a)
            letter2258b=int(letter58a)+int(number1)

            letter59a=int(letter58b)
            letter59b=int(letter58b)+int(number3)
            letter1159a=int(letter59a)
            letter2259b=int(letter59a)+int(number1)

            letter60a=int(letter59b)
            letter60b=int(letter59b)+int(number3)
            letter1160a=int(letter60a)
            letter2260b=int(letter60a)+int(number1)

            letter61a=int(letter60b)
            letter61b=int(letter60b)+int(number3)
            letter1161a=int(letter61a)
            letter2261b=int(letter61a)+int(number1)

            letter62a=int(letter61b)
            letter62b=int(letter61b)+int(number3)
            letter1162a=int(letter62a)
            letter2262b=int(letter62a)+int(number1)

            letter63a=int(letter62b)
            letter63b=int(letter62b)+int(number3)
            letter1163a=int(letter63a)
            letter2263b=int(letter63a)+int(number1)

            letter64a=int(letter63b)
            letter64b=int(letter63b)+int(number3)
            letter1164a=int(letter64a)
            letter2264b=int(letter64a)+int(number1)

            letter65a=int(letter64b)
            letter65b=int(letter64b)+int(number3)
            letter1165a=int(letter65a)
            letter2265b=int(letter65a)+int(number1)

            letter66a=int(letter65b)
            letter66b=int(letter65b)+int(number3)
            letter1166a=int(letter66a)
            letter2266b=int(letter66a)+int(number1)

            letter67a=int(letter66b)
            letter67b=int(letter66b)+int(number3)
            letter1167a=int(letter67a)
            letter2267b=int(letter67a)+int(number1)

            letter68a=int(letter67b)
            letter68b=int(letter67b)+int(number3)
            letter1168a=int(letter68a)
            letter2268b=int(letter68a)+int(number1)

            letter69a=int(letter68b)
            letter69b=int(letter68b)+int(number3)
            letter1169a=int(letter69a)
            letter2269b=int(letter69a)+int(number1)

            letter70a=int(letter69b)
            letter70b=int(letter69b)+int(number3)
            letter1170a=int(letter70a)
            letter2270b=int(letter70a)+int(number1)

            letter71a=int(letter70b)
            letter71b=int(letter70b)+int(number3)
            letter1171a=int(letter71a)
            letter2271b=int(letter71a)+int(number1)

            letter72a=int(letter71b)
            letter72b=int(letter71b)+int(number3)
            letter1172a=int(letter72a)
            letter2272b=int(letter72a)+int(number1)

            letter73a=int(letter72b)
            letter73b=int(letter72b)+int(number3)
            letter1173a=int(letter73a)
            letter2273b=int(letter73a)+int(number1)

            letter74a=int(letter73b)
            letter74b=int(letter73b)+int(number3)
            letter1174a=int(letter74a)
            letter2274b=int(letter74a)+int(number1)

            letter75a=int(letter74b)
            letter75b=int(letter74b)+int(number3)
            letter1175a=int(letter75a)
            letter2275b=int(letter75a)+int(number1)

            letter76a=int(letter75b)
            letter76b=int(letter75b)+int(number3)
            letter1176a=int(letter76a)
            letter2276b=int(letter76a)+int(number1)

            letter77a=int(letter76b)
            letter77b=int(letter76b)+int(number3)
            letter1177a=int(letter77a)
            letter2277b=int(letter77a)+int(number1)

            letter78a=int(letter77b)
            letter78b=int(letter77b)+int(number3)
            letter1178a=int(letter78a)
            letter2278b=int(letter78a)+int(number1)

            letter79a=int(letter78b)
            letter79b=int(letter78b)+int(number3)
            letter1179a=int(letter79a)
            letter2279b=int(letter79a)+int(number1)

            letter80a=int(letter79b)
            letter80b=int(letter79b)+int(number3)
            letter1180a=int(letter80a)
            letter2280b=int(letter80a)+int(number1)

            letter81a=int(letter80b)
            letter81b=int(letter80b)+int(number3)
            letter1181a=int(letter81a)
            letter2281b=int(letter81a)+int(number1)

            letter82a=int(letter81b)
            letter82b=int(letter81b)+int(number3)
            letter1182a=int(letter82a)
            letter2282b=int(letter82a)+int(number1)

            letter83a=int(letter82b)
            letter83b=int(letter82b)+int(number3)
            letter1183a=int(letter83a)
            letter2283b=int(letter83a)+int(number1)

            letter84a=int(letter83b)
            letter84b=int(letter83b)+int(number3)
            letter1184a=int(letter84a)
            letter2284b=int(letter84a)+int(number1)

            letter85a=int(letter84b)
            letter85b=int(letter84b)+int(number3)
            letter1185a=int(letter85a)
            letter2285b=int(letter85a)+int(number1)

            letter86a=int(letter85b)
            letter86b=int(letter85b)+int(number3)
            letter1186a=int(letter86a)
            letter2286b=int(letter86a)+int(number1)

            letter87a=int(letter86b)
            letter87b=int(letter86b)+int(number3)
            letter1187a=int(letter87a)
            letter2287b=int(letter87a)+int(number1)

            letter88a=int(letter87b)
            letter88b=int(letter87b)+int(number3)
            letter1188a=int(letter88a)
            letter2288b=int(letter88a)+int(number1)

            letter89a=int(letter88b)
            letter89b=int(letter88b)+int(number3)
            letter1189a=int(letter89a)
            letter2289b=int(letter89a)+int(number1)

            letter90a=int(letter89b)
            letter90b=int(letter89b)+int(number3)
            letter1190a=int(letter90a)
            letter2290b=int(letter90a)+int(number1)

            letter91a=int(letter90b)
            letter91b=int(letter90b)+int(number3)
            letter1191a=int(letter91a)
            letter2291b=int(letter91a)+int(number1)

            letter92a=int(letter91b)
            letter92b=int(letter91b)+int(number3)
            letter1192a=int(letter92a)
            letter2292b=int(letter92a)+int(number1)

            letter93a=int(letter92b)
            letter93b=int(letter92b)+int(number3)
            letter1193a=int(letter93a)
            letter2293b=int(letter93a)+int(number1)

            letter94a=int(letter93b)
            letter94b=int(letter93b)+int(number3)
            letter1194a=int(letter94a)
            letter2294b=int(letter94a)+int(number1)

            while num1 != num:
                if message[int(num1):int(num2)] == key[int(letter111a):int(letter221b)]:
                    new=new+str("a")
                    letter111a=int(letter111a)+int(number1)
                    letter221b=int(letter221b)+int(number1)
                    if letter111a == letter1b:
                        letter111a=int(letter1a)
                        letter221b=int(letter1a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter112a):int(letter222b)]:
                    new=new+str("b")
                    letter112a=int(letter112a)+int(number1)
                    letter222b=int(letter222b)+int(number1)
                    if letter112a == letter2b:
                        letter112a=int(letter2a)
                        letter222b=int(letter2a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter113a):int(letter223b)]:
                    new=new+str("c")
                    letter113a=int(letter113a)+int(number1)
                    letter223b=int(letter223b)+int(number1)
                    if letter113a == letter3b:
                        letter113a=int(letter3a)
                        letter223b=int(letter3a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter114a):int(letter224b)]:
                    new=new+str("d")
                    letter114a=int(letter114a)+int(number1)
                    letter224b=int(letter224b)+int(number1)
                    if letter114a == letter4b:
                        letter114a=int(letter4a)
                        letter224b=int(letter4a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter115a):int(letter225b)]:
                    new=new+str("e")
                    letter115a=int(letter115a)+int(number1)
                    letter225b=int(letter225b)+int(number1)
                    if letter115a == letter5b:
                        letter115a=int(letter5a)
                        letter225b=int(letter5a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter116a):int(letter226b)]:
                    new=new+str("f")
                    letter116a=int(letter116a)+int(number1)
                    letter226b=int(letter226b)+int(number1)
                    if letter116a == letter6b:
                        letter116a=int(letter6a)
                        letter226b=int(letter6a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter117a):int(letter227b)]:
                    new=new+str("g")
                    letter117a=int(letter117a)+int(number1)
                    letter227b=int(letter227b)+int(number1)
                    if letter117a == letter7b:
                        letter117a=int(letter7a)
                        letter227b=int(letter7a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter118a):int(letter228b)]:
                    new=new+str("h")
                    letter118a=int(letter118a)+int(number1)
                    letter228b=int(letter228b)+int(number1)
                    if letter118a == letter8b:
                        letter118a=int(letter8a)
                        letter228b=int(letter8a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter119a):int(letter229b)]:
                    new=new+str("i")
                    letter119a=int(letter119a)+int(number1)
                    letter229b=int(letter229b)+int(number1)
                    if letter119a == letter9b:
                        letter119a=int(letter9a)
                        letter229b=int(letter9a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1110a):int(letter2210b)]:
                    new=new+str("j")
                    letter1110a=int(letter1110a)+int(number1)
                    letter2210b=int(letter2210b)+int(number1)
                    if letter1110a == letter10b:
                        letter1110a=int(letter10a)
                        letter2210b=int(letter10a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1111a):int(letter2211b)]:
                    new=new+str("k")
                    letter1111a=int(letter1111a)+int(number1)
                    letter2211b=int(letter2211b)+int(number1)
                    if letter1111a == letter11b:
                        letter1111a=int(letter11a)
                        letter2211b=int(letter11a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1112a):int(letter2212b)]:
                    new=new+str("l")
                    letter1112a=int(letter1112a)+int(number1)
                    letter2212b=int(letter2212b)+int(number1)
                    if letter1112a == letter12b:
                        letter1112a=int(letter12a)
                        letter2212b=int(letter12a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1113a):int(letter2213b)]:
                    new=new+str("m")
                    letter1113a=int(letter1113a)+int(number1)
                    letter2213b=int(letter2213b)+int(number1)
                    if letter1113a == letter13b:
                        letter1113a=int(letter13a)
                        letter2213b=int(letter13a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1114a):int(letter2214b)]:
                    new=new+str("n")
                    letter1114a=int(letter1114a)+int(number1)
                    letter2214b=int(letter2214b)+int(number1)
                    if letter1114a == letter14b:
                        letter1114a=int(letter14a)
                        letter2214b=int(letter14a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1115a):int(letter2215b)]:
                    new=new+str("o")
                    letter1115a=int(letter1115a)+int(number1)
                    letter2215b=int(letter2215b)+int(number1)
                    if letter1115a == letter15b:
                        letter1115a=int(letter15a)
                        letter2215b=int(letter15a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1116a):int(letter2216b)]:
                    new=new+str("p")
                    letter1116a=int(letter1116a)+int(number1)
                    letter2216b=int(letter2216b)+int(number1)
                    if letter1116a == letter16b:
                        letter1116a=int(letter16a)
                        letter2216b=int(letter16a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1117a):int(letter2217b)]:
                    new=new+str("q")
                    letter1117a=int(letter1117a)+int(number1)
                    letter2217b=int(letter2217b)+int(number1)
                    if letter1117a == letter17b:
                        letter1117a=int(letter17a)
                        letter2217b=int(letter17a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1118a):int(letter2218b)]:
                    new=new+str("r")
                    letter1118a=int(letter1118a)+int(number1)
                    letter2218b=int(letter2218b)+int(number1)
                    if letter1118a == letter18b:
                        letter1118a=int(letter18a)
                        letter2218b=int(letter18a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1119a):int(letter2219b)]:
                    new=new+str("s")
                    letter1119a=int(letter1119a)+int(number1)
                    letter2219b=int(letter2219b)+int(number1)
                    if letter1119a == letter19b:
                        letter1119a=int(letter19a)
                        letter2219b=int(letter19a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1120a):int(letter2220b)]:
                    new=new+str("t")
                    letter1120a=int(letter1120a)+int(number1)
                    letter2220b=int(letter2220b)+int(number1)
                    if letter1120a == letter20b:
                        letter1120a=int(letter20a)
                        letter2220b=int(letter20a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1121a):int(letter2221b)]:
                    new=new+str("u")
                    letter1121a=int(letter1121a)+int(number1)
                    letter2221b=int(letter2221b)+int(number1)
                    if letter1121a == letter21b:
                        letter1121a=int(letter21a)
                        letter2221b=int(letter21a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1122a):int(letter2222b)]:
                    new=new+str("v")
                    letter1122a=int(letter1122a)+int(number1)
                    letter2222b=int(letter2222b)+int(number1)
                    if letter1122a == letter22b:
                        letter1122a=int(letter22a)
                        letter2222b=int(letter22a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1123a):int(letter2223b)]:
                    new=new+str("w")
                    letter1123a=int(letter1123a)+int(number1)
                    letter2223b=int(letter2223b)+int(number1)
                    if letter1123a == letter23b:
                        letter1123a=int(letter23a)
                        letter2223b=int(letter23a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1124a):int(letter2224b)]:
                    new=new+str("x")
                    letter1124a=int(letter1124a)+int(number1)
                    letter2224b=int(letter2224b)+int(number1)
                    if letter1124a == letter24b:
                        letter1124a=int(letter24a)
                        letter2224b=int(letter24a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1125a):int(letter2225b)]:
                    new=new+str("y")
                    letter1125a=int(letter1125a)+int(number1)
                    letter2225b=int(letter2225b)+int(number1)
                    if letter1125a == letter25b:
                        letter1125a=int(letter25a)
                        letter2225b=int(letter25a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1126a):int(letter2226b)]:
                    new=new+str("z")
                    letter1126a=int(letter1126a)+int(number1)
                    letter2226b=int(letter2226b)+int(number1)
                    if letter1126a == letter26b:
                        letter1126a=int(letter26a)
                        letter2226b=int(letter26a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1127a):int(letter2227b)]:
                    new=new+str("A")
                    letter1127a=int(letter1127a)+int(number1)
                    letter2227b=int(letter2227b)+int(number1)
                    if letter1127a == letter27b:
                        letter1127a=int(letter27a)
                        letter2227b=int(letter27a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1128a):int(letter2228b)]:
                    new=new+str("B")
                    letter1128a=int(letter1128a)+int(number1)
                    letter2228b=int(letter2228b)+int(number1)
                    if letter1128a == letter28b:
                        letter1128a=int(letter28a)
                        letter2228b=int(letter28a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1129a):int(letter2229b)]:
                    new=new+str("C")
                    letter1129a=int(letter1129a)+int(number1)
                    letter2229b=int(letter2229b)+int(number1)
                    if letter1129a == letter29b:
                        letter1129a=int(letter29a)
                        letter2229b=int(letter29a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1130a):int(letter2230b)]:
                    new=new+str("D")
                    letter1130a=int(letter1130a)+int(number1)
                    letter2230b=int(letter2230b)+int(number1)
                    if letter1130a == letter30b:
                        letter1130a=int(letter30a)
                        letter2230b=int(letter30a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1131a):int(letter2231b)]:
                    new=new+str("E")
                    letter1131a=int(letter1131a)+int(number1)
                    letter2231b=int(letter2231b)+int(number1)
                    if letter1131a == letter31b:
                        letter1131a=int(letter31a)
                        letter2231b=int(letter31a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1132a):int(letter2232b)]:
                    new=new+str("F")
                    letter1132a=int(letter1132a)+int(number1)
                    letter2232b=int(letter2232b)+int(number1)
                    if letter1132a == letter32b:
                        letter1132a=int(letter32a)
                        letter2232b=int(letter32a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1133a):int(letter2233b)]:
                    new=new+str("G")
                    letter1133a=int(letter1133a)+int(number1)
                    letter2233b=int(letter2233b)+int(number1)
                    if letter1133a == letter33b:
                        letter1133a=int(letter33a)
                        letter2233b=int(letter33a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1134a):int(letter2234b)]:
                    new=new+str("H")
                    letter1134a=int(letter1134a)+int(number1)
                    letter2234b=int(letter2234b)+int(number1)
                    if letter1134a == letter34b:
                        letter1134a=int(letter34a)
                        letter2234b=int(letter34a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1135a):int(letter2235b)]:
                    new=new+str("I")
                    letter1135a=int(letter1135a)+int(number1)
                    letter2235b=int(letter2235b)+int(number1)
                    if letter1135a == letter35b:
                        letter1135a=int(letter35a)
                        letter2235b=int(letter35a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1136a):int(letter2236b)]:
                    new=new+str("J")
                    letter1136a=int(letter1136a)+int(number1)
                    letter2236b=int(letter2236b)+int(number1)
                    if letter1136a == letter36b:
                        letter1136a=int(letter36a)
                        letter2236b=int(letter36a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1137a):int(letter2237b)]:
                    new=new+str("K")
                    letter1137a=int(letter1137a)+int(number1)
                    letter2237b=int(letter2237b)+int(number1)
                    if letter1137a == letter37b:
                        letter1137a=int(letter37a)
                        letter2237b=int(letter37a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1138a):int(letter2238b)]:
                    new=new+str("L")
                    letter1138a=int(letter1138a)+int(number1)
                    letter2238b=int(letter2238b)+int(number1)
                    if letter1138a == letter38b:
                        letter1138a=int(letter38a)
                        letter2238b=int(letter38a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1139a):int(letter2239b)]:
                    new=new+str("M")
                    letter1139a=int(letter1139a)+int(number1)
                    letter2239b=int(letter2239b)+int(number1)
                    if letter1139a == letter39b:
                        letter1139a=int(letter39a)
                        letter2239b=int(letter39a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1140a):int(letter2240b)]:
                    new=new+str("N")
                    letter1140a=int(letter1140a)+int(number1)
                    letter2240b=int(letter2240b)+int(number1)
                    if letter1140a == letter40b:
                        letter1140a=int(letter40a)
                        letter2240b=int(letter40a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1141a):int(letter2241b)]:
                    new=new+str("O")
                    letter1141a=int(letter1141a)+int(number1)
                    letter2241b=int(letter2241b)+int(number1)
                    if letter1141a == letter41b:
                        letter1141a=int(letter41a)
                        letter2241b=int(letter41a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1142a):int(letter2242b)]:
                    new=new+str("P")
                    letter1142a=int(letter1142a)+int(number1)
                    letter2242b=int(letter2242b)+int(number1)
                    if letter1142a == letter42b:
                        letter1142a=int(letter42a)
                        letter2242b=int(letter42a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1143a):int(letter2243b)]:
                    new=new+str("Q")
                    letter1143a=int(letter1143a)+int(number1)
                    letter2243b=int(letter2243b)+int(number1)
                    if letter1143a == letter43b:
                        letter1143a=int(letter43a)
                        letter2243b=int(letter43a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1144a):int(letter2244b)]:
                    new=new+str("R")
                    letter1144a=int(letter1144a)+int(number1)
                    letter2244b=int(letter2244b)+int(number1)
                    if letter1144a == letter44b:
                        letter1144a=int(letter44a)
                        letter2244b=int(letter44a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1145a):int(letter2245b)]:
                    new=new+str("S")
                    letter1145a=int(letter1145a)+int(number1)
                    letter2245b=int(letter2245b)+int(number1)
                    if letter1145a == letter45b:
                        letter1145a=int(letter45a)
                        letter2245b=int(letter45a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1146a):int(letter2246b)]:
                    new=new+str("T")
                    letter11a=int(letter1146a)+int(number1)
                    letter22b=int(letter2246b)+int(number1)
                    if letter1146a == letter46b:
                        letter1146a=int(letter46a)
                        letter2246b=int(letter46a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1147a):int(letter2247b)]:
                    new=new+str("U")
                    letter1147a=int(letter1147a)+int(number1)
                    letter2247b=int(letter2247b)+int(number1)
                    if letter1147a == letter47b:
                        letter1147a=int(letter47a)
                        letter2247b=int(letter47a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1148a):int(letter2248b)]:
                    new=new+str("V")
                    letter1148a=int(letter1148a)+int(number1)
                    letter2248b=int(letter2248b)+int(number1)
                    if letter1148a == letter48b:
                        letter1148a=int(letter48a)
                        letter2248b=int(letter48a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1149a):int(letter2249b)]:
                    new=new+str("W")
                    letter1149a=int(letter1149a)+int(number1)
                    letter2249b=int(letter2249b)+int(number1)
                    if letter1149a == letter49b:
                        letter1149a=int(letter49a)
                        letter2249b=int(letter49a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1150a):int(letter2250b)]:
                    new=new+str("X")
                    letter1150a=int(letter1150a)+int(number1)
                    letter2250b=int(letter2250b)+int(number1)
                    if letter1150a == letter50b:
                        letter1150a=int(letter50a)
                        letter2250b=int(letter50a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1151a):int(letter2251b)]:
                    new=new+str("Y")
                    letter1151a=int(letter1151a)+int(number1)
                    letter2251b=int(letter2251b)+int(number1)
                    if letter1151a == letter51b:
                        letter1151a=int(letter51a)
                        letter2251b=int(letter51a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1152a):int(letter2252b)]:
                    new=new+str("Z")
                    letter1152a=int(letter1152a)+int(number1)
                    letter2252b=int(letter2252b)+int(number1)
                    if letter1152a == letter52b:
                        letter1152a=int(letter52a)
                        letter2252b=int(letter52a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1153a):int(letter2253b)]:
                    new=new+str("1")
                    letter1153a=int(letter1153a)+int(number1)
                    letter2253b=int(letter2253b)+int(number1)
                    if letter1153a == letter53b:
                        letter1153a=int(letter53a)
                        letter2253b=int(letter53a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1154a):int(letter2254b)]:
                    new=new+str("2")
                    letter1154a=int(letter1154a)+int(number1)
                    letter2254b=int(letter2254b)+int(number1)
                    if letter1154a == letter54b:
                        letter1154a=int(letter54a)
                        letter2254b=int(letter54a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1155a):int(letter2255b)]:
                    new=new+str("3")
                    letter1155a=int(letter1155a)+int(number1)
                    letter2255b=int(letter2255b)+int(number1)
                    if letter1155a == letter55b:
                        letter1155a=int(letter55a)
                        letter2255b=int(letter55a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1156a):int(letter2256b)]:
                    new=new+str("4")
                    letter1156a=int(letter1156a)+int(number1)
                    letter2256b=int(letter2256b)+int(number1)
                    if letter1156a == letter56b:
                        letter1156a=int(letter56a)
                        letter2256b=int(letter56a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1157a):int(letter2257b)]:
                    new=new+str("5")
                    letter1157a=int(letter1157a)+int(number1)
                    letter2257b=int(letter2257b)+int(number1)
                    if letter1157a == letter57b:
                        letter1157a=int(letter57a)
                        letter2257b=int(letter57a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1158a):int(letter2258b)]:
                    new=new+str("6")
                    letter1158a=int(letter1158a)+int(number1)
                    letter2258b=int(letter2258b)+int(number1)
                    if letter1158a == letter58b:
                        letter1158a=int(letter58a)
                        letter2258b=int(letter58a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1159a):int(letter2259b)]:
                    new=new+str("7")
                    letter1159a=int(letter1159a)+int(number1)
                    letter2259b=int(letter2259b)+int(number1)
                    if letter1159a == letter59b:
                        letter1159a=int(letter59a)
                        letter2259b=int(letter59a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1160a):int(letter2260b)]:
                    new=new+str("8")
                    letter1160a=int(letter1160a)+int(number1)
                    letter2260b=int(letter2260b)+int(number1)
                    if letter1160a == letter60b:
                        letter1160a=int(letter60a)
                        letter2260b=int(letter60a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1161a):int(letter2261b)]:
                    new=new+str("9")
                    letter1161a=int(letter1161a)+int(number1)
                    letter2261b=int(letter2261b)+int(number1)
                    if letter1161a == letter61b:
                        letter1161a=int(letter61a)
                        letter2261b=int(letter61a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1162a):int(letter2262b)]:
                    new=new+str("0")
                    letter1162a=int(letter1162a)+int(number1)
                    letter2262b=int(letter2262b)+int(number1)
                    if letter1162a == letter62b:
                        letter1162a=int(letter62a)
                        letter2262b=int(letter62a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1163a):int(letter2263b)]:
                    new=new+str("!")
                    letter1163a=int(letter1163a)+int(number1)
                    letter2263b=int(letter2263b)+int(number1)
                    if letter1163a == letter63b:
                        letter1163a=int(letter63a)
                        letter2263b=int(letter63a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1164a):int(letter2264b)]:
                    new=new+str('"')
                    letter1164a=int(letter1164a)+int(number1)
                    letter2264b=int(letter2264b)+int(number1)
                    if letter1164a == letter64b:
                        letter1164a=int(letter64a)
                        letter2264b=int(letter64a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1165a):int(letter2265b)]:
                    new=new+str("$")
                    letter1165a=int(letter1165a)+int(number1)
                    letter2265b=int(letter2265b)+int(number1)
                    if letter1165a == letter65b:
                        letter1165a=int(letter65a)
                        letter2265b=int(letter65a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1166a):int(letter2266b)]:
                    new=new+str("%")
                    letter1166a=int(letter1166a)+int(number1)
                    letter2266b=int(letter2266b)+int(number1)
                    if letter1166a == letter66b:
                        letter1166a=int(letter66a)
                        letter2266b=int(letter66a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1167a):int(letter2267b)]:
                    new=new+str("^")
                    letter1167a=int(letter1167a)+int(number1)
                    letter2267b=int(letter2267b)+int(number1)
                    if letter1167a == letter67b:
                        letter1167a=int(letter67a)
                        letter2267b=int(letter67a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1168a):int(letter2268b)]:
                    new=new+str("&")
                    letter1168a=int(letter1168a)+int(number1)
                    letter2268b=int(letter2268b)+int(number1)
                    if letter1168a == letter68b:
                        letter1168a=int(letter68a)
                        letter2268b=int(letter68a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1169a):int(letter2269b)]:
                    new=new+str("*")
                    letter1169a=int(letter1169a)+int(number1)
                    letter2269b=int(letter2269b)+int(number1)
                    if letter1169a == letter69b:
                        letter1169a=int(letter69a)
                        letter2269b=int(letter69a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1170a):int(letter2270b)]:
                    new=new+str("(")
                    letter1170a=int(letter1170a)+int(number1)
                    letter2270b=int(letter2270b)+int(number1)
                    if letter1170a == letter70b:
                        letter1170a=int(letter70a)
                        letter2270b=int(letter70a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1171a):int(letter2271b)]:
                    new=new+str(")")
                    letter1171a=int(letter1171a)+int(number1)
                    letter2271b=int(letter2271b)+int(number1)
                    if letter1171a == letter71b:
                        letter1171a=int(letter71a)
                        letter2271b=int(letter71a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1172a):int(letter2272b)]:
                    new=new+str('_')
                    letter1172a=int(letter1172a)+int(number1)
                    letter2272b=int(letter2272b)+int(number1)
                    if letter1172a == letter72b:
                        letter1172a=int(letter72a)
                        letter2272b=int(letter72a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1173a):int(letter2273b)]:
                    new=new+str("-")
                    letter1173a=int(letter1173a)+int(number1)
                    letter2273b=int(letter2273b)+int(number1)
                    if letter1173a == letter73b:
                        letter1173a=int(letter73a)
                        letter2273b=int(letter73a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1174a):int(letter2274b)]:
                    new=new+str("+")
                    letter1174a=int(letter1174a)+int(number1)
                    letter2274b=int(letter2274b)+int(number1)
                    if letter1174a == letter74b:
                        letter1174a=int(letter74a)
                        letter2274b=int(letter74a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1175a):int(letter2275b)]:
                    new=new+str("=")
                    letter1175a=int(letter1175a)+int(number1)
                    letter2275b=int(letter2275b)+int(number1)
                    if letter1175a == letter75b:
                        letter1175a=int(letter75a)
                        letter2275b=int(letter75a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1176a):int(letter2276b)]:
                    new=new+str("{")
                    letter1176a=int(letter1176a)+int(number1)
                    letter2276b=int(letter2276b)+int(number1)
                    if letter1176a == letter76b:
                        letter1176a=int(letter76a)
                        letter2276b=int(letter76a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1177a):int(letter2277b)]:
                    new=new+str("}")
                    letter1177a=int(letter1177a)+int(number1)
                    letter2277b=int(letter2277b)+int(number1)
                    if letter1177a == letter77b:
                        letter1177a=int(letter77a)
                        letter2277b=int(letter77a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1178a):int(letter2278b)]:
                    new=new+str("[")
                    letter1178a=int(letter1178a)+int(number1)
                    letter2278b=int(letter2278b)+int(number1)
                    if letter1178a == letter78b:
                        letter1178a=int(letter78a)
                        letter2278b=int(letter78a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1179a):int(letter2279b)]:
                    new=new+str("]")
                    letter1179a=int(letter1179a)+int(number1)
                    letter2279b=int(letter2279b)+int(number1)
                    if letter1179a == letter79b:
                        letter1179a=int(letter79a)
                        letter2279b=int(letter79a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1180a):int(letter2280b)]:
                    new=new+str(":")
                    letter1180a=int(letter1180a)+int(number1)
                    letter2280b=int(letter2280b)+int(number1)
                    if letter1180a == letter80b:
                        letter1180a=int(letter80a)
                        letter2280b=int(letter80a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1181a):int(letter2281b)]:
                    new=new+str(";")
                    letter1181a=int(letter1181a)+int(number1)
                    letter2281b=int(letter2281b)+int(number1)
                    if letter1181a == letter81b:
                        letter1181a=int(letter81a)
                        letter2281b=int(letter81a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1182a):int(letter2282b)]:
                    new=new+str("@")
                    letter1182a=int(letter1182a)+int(number1)
                    letter2282b=int(letter2282b)+int(number1)
                    if letter1182a == letter82b:
                        letter1182a=int(letter82a)
                        letter2282b=int(letter82a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1183a):int(letter2283b)]:
                    new=new+str("'")
                    letter1183a=int(letter1183a)+int(number1)
                    letter2283b=int(letter2283b)+int(number1)
                    if letter1183a == letter83b:
                        letter1183a=int(letter83a)
                        letter2283b=int(letter83a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1184a):int(letter2284b)]:
                    new=new+str("~")
                    letter1184a=int(letter1184a)+int(number1)
                    letter2284b=int(letter2284b)+int(number1)
                    if letter1184a == letter84b:
                        letter1184a=int(letter84a)
                        letter2284b=int(letter84a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1185a):int(letter2285b)]:
                    new=new+str("#")
                    letter1185a=int(letter1185a)+int(number1)
                    letter2285b=int(letter2285b)+int(number1)
                    if letter1185a == letter85b:
                        letter1185a=int(letter85a)
                        letter2285b=int(letter85a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1186a):int(letter2286b)]:
                    new=new+str("<")
                    letter1186a=int(letter1186a)+int(number1)
                    letter2286b=int(letter2286b)+int(number1)
                    if letter1186a == letter86b:
                        letter1186a=int(letter86a)
                        letter2286b=int(letter86a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1187a):int(letter2287b)]:
                    new=new+str(">")
                    letter1187a=int(letter1187a)+int(number1)
                    letter2287b=int(letter2287b)+int(number1)
                    if letter1187a == letter87b:
                        letter1187a=int(letter87a)
                        letter2287b=int(letter87a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1188a):int(letter2288b)]:
                    new=new+str(",")
                    letter1188a=int(letter1188a)+int(number1)
                    letter2288b=int(letter2288b)+int(number1)
                    if letter1188a == letter88b:
                        letter1188a=int(letter88a)
                        letter2288b=int(letter88a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1189a):int(letter2289b)]:
                    new=new+str(".")
                    letter1189a=int(letter1189a)+int(number1)
                    letter2289b=int(letter2289b)+int(number1)
                    if letter1189a == letter89b:
                        letter1189a=int(letter89a)
                        letter2289b=int(letter89a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1190a):int(letter2290b)]:
                    new=new+str("?")
                    letter1190a=int(letter1190a)+int(number1)
                    letter2290b=int(letter2290b)+int(number1)
                    if letter1190a == letter90b:
                        letter1190a=int(letter90a)
                        letter2290b=int(letter90a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1191a):int(letter2291b)]:
                    new=new+str("/")
                    letter1191a=int(letter1191a)+int(number1)
                    letter2291b=int(letter2291b)+int(number1)
                    if letter1191a == letter91b:
                        letter1191a=int(letter91a)
                        letter2291b=int(letter91a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1192a):int(letter2292b)]:
                    new=new+str("|")
                    letter1192a=int(letter1192a)+int(number1)
                    letter2292b=int(letter2292b)+int(number1)
                    if letter1192a == letter92b:
                        letter1192a=int(letter92a)
                        letter2292b=int(letter92a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1193a):int(letter2293b)]:
                    new=new+str(" ")
                    letter1193a=int(letter1193a)+int(number1)
                    letter2293b=int(letter2293b)+int(number1)
                    if letter1193a == letter93b:
                        letter1193a=int(letter93a)
                        letter2293b=int(letter93a)+int(number1)
                    
                elif message[int(num1):int(num2)] == key[int(letter1194a):int(letter2294b)]:
                    new=new+str("   ")
                    letter1194a=int(letter1194a)+int(number1)
                    letter2294b=int(letter2294b)+int(number1)
                    if letter1194a == letter94b:
                        letter1194a=int(letter94a)
                        letter2294b=int(letter94a)+int(number1)

                num1=int(num1)+int(number1)
                num2=int(num2)+int(number1)
            print(new)
            break

    if menu == "4":
        while __name__ == "__main__":
            print("1) How to use the Random Key Creater")
            print("2) How to use the Encryption")
            print("3) How to use the Decryption")
            print("4) Why is the program slowing down")
            print("5) Back")
            menu4=input("")
            if menu4 == "1":
                while __name__ == "__main__":
                    print("To use the Random Key Creater you will need to enter a number between 3 and 10 for the second number it will show what numbers that you can choose from between.")
                    print("It will not work if you do not enter between the two numbers given for the first and second number it will also not work if you enter a letter rather than a letter.")
                    print("1) Back")
                    back=input("")
                    if back == "1":
                        break

            elif menu4 == "2":
                while __name__ == "__main__":
                    print("To use the Encryption you will need to firstly enter the message that you want to encrypt and then you will need to enter the key that you want to use to encrypt the message.")
                    print("It will not work if you do not enter a key that was created by the Random Key Creater.")
                    print("1) Back")
                    back=input("")
                    if back == "1":
                        break

            elif menu4 == "3":
                while __name__ == "__main__":
                    print("To use the Decryption you will need to firstly enter the message that you want to decrypt and then you will need to enter the key that you want to use to decrypt the message.")
                    print("It will not work if you do not enter a key that was created by the Random Key Creater.")

            elif menu4 == "4":
                while __name__ == "__main__":
                    print("The program will slow down mainly because of the Random Key Creater when it prints out a large key this will make the program slow down.")

            elif menu4 == "5":
                break
            
    if menu == "5":
        while __name__ == "__main__":
            print("Do you want to exit this program.")
            print("1) Yes")
            print("2) No")
            menu5=input("")
            if menu5 == "1":
                aexit="Yes"
                break
            
            elif menu5 == "2":
                break
    if aexit == "Yes":
        break
