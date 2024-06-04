import time
print("--------------------------------------------------")
#Welcome the user
print("\033[1mSelamat Datang ke Kuiz Berkenaan Online Game!\033[0m") #Untuk bold dan unbold semula teks
time.sleep(1) #Masa dipaparan skrin selepas 1 saat
print("--------------------------------------------------")

#Chances
chances=1 #Percubaan menjawab hanya sekali
print("Pilih", chances,"jawapan yang betul.\n1 Markah akan diberikan bagi jawapan yang betul\n")
time.sleep(3) #Masa delay untuk paparan selepas 3 saat

#score
score=0 #Set markah kepada 0

#question 1
print("==================================================")
question_1=print("1) ONLINE GAME YANG TIDAK TERSENARAI SEBAGAI 10 GAME MOBILE YANG TERKENAL?\n(A) FORTNITE MOBILE\n(B) CLASH ROYALE\n(C) PUBG\n(D) SOLITARE\n\n")
answer_1= "D"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.upper() == answer_1): #Jawapan ditukarkan kepada lower case walaupun user masukkan uppercase
        print("CORRECT! GOOD JOB!\n")
        score = score + 1 #Dapat satu markah sekiranya betul
        break 
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_1, "\n\n")

time.sleep(2)

#question 2
print("==================================================")
question_2 = print("2) ONLINE YOUTUBER GAMER YANG TERKENAL?\n(A) FERNANFLOO\n(B) AZFAR HERI\n(C) ISMA NOUR\n(D) JUEGA\n\n")  
answer_2 = "A"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.upper() == answer_2):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n ")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_2, "\n\n")

time.sleep(2)

#question 3
print("==================================================")
question_3 =print("3) BILAKAH MINECRAFT DICIPTA?\n(A) 2008\n(B) 2009\n(C) 2010\n(D) 2011\n\n")
answer_3= "B"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.upper() == answer_3):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS", answer_3, "\n\n")

time.sleep(2)

#question 4
print("==================================================")
question_4 =print("4) ANTARA BERIKUT MANAKAH BUKAN ROLE DALAM MOBILE LEGEND?\n(A) MARKSMAN\n(B) ASSASSIN\n(C) LOSER\n(D) FIGHTER\n\n")
answer_4= "C"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.upper() == answer_4):
        print("CORRECT! GOOD JOB!\n")
        score = score + 1
        break
    else:
        print("INCORRECT!\n")
        time.sleep(0.5)
        print("THE CORRECT ANSWER IS",answer_4, "\n\n")

time.sleep(2)

#print the score
print("==================================================")
print("KUIZ TELAH TAMAT")
time.sleep(2)
print("REKOD PENCAPAIAN ANDA")
print("==================================================")
time.sleep(1)
while score >=2:
    print("\nTAHNIAH! ANDA MELEPASI MARKAH MINIMUM.\nMARKAH KESELURUHAN ANDA ADALAH :", score)
    break
while score <2:
    print("SILA CUBA LAGI! \n MARKAH ANDA ADALAH : ",score)
    break

#Goobye message
print("\n==================================================")
print("TERIMA KASIH KERANA CUBA MENJAWAB!")