print("====== TIME1 VS TIME2 ======")
time1 = int(input("Gols do time1: "))
time2 = int(input("Gols do time2: "))
if(time1==time2):
    print("\t===> Pênaultis")
    penaultiT1 = int(input("\tPênaultis do time1 (0-5): "))
    while(penaultiT1<0 or penaultiT1>5):
        penaultiT1 = int(input("\t[ERRO]: Pênaultis do time1: "))

    penaultiT2 = int(input("\tPênaultis do time2 (0-5): "))
    while(penaultiT2<0 or penaultiT2>5):
        penaultiT2 = int(input("\t[ERRO]: Pênaultis do time2: "))

    if(penaultiT1>penaultiT2):
        timeWin1 = "time1"
        print("Time1 venceu!")
    else:
        timeWin1 = "time2"
        print("Time2 venceu!")
elif(time1>time2):
    timeWin1 = "time1"
    print("\tTime1 venceu!")
else:
    timeWin1 = "time2"
    print("\tTime2 venceu!")


print("\n====== TIME3 VS TIME4 ======")
time3 = int(input("Gols do time3: "))
time4 = int(input("Gols do time4: "))
if(time3==time4):
    print("===> Pênaultis")
    penaultiT3 = int(input("\tPênaultis do time3 (0-5): "))
    while(penaultiT3<0 or penaultiT3>5):
        penaultiT3 = int(input("\t[ERRO] Pênaultis do time3: "))

    penaultiT4 = int(input("\tPênaultis do time4 (0-5): "))
    while(penaultiT4<0 or penaultiT4>5):
        penaultiT4 = int(input("\t[ERRO] Pênaultis do time4: "))

    if(penaultiT1>penaultiT2):
        timeWin2 = "time3"
        print("Time3 venceu!")
    else:
        timeWin2 = "time4"
        print("Time4 venceu!")
elif(time3>time4):
    timeWin2 = "time3"
    print("\tTime3 venceu!")
else:
    timeWin2 = "time4"
    print("\tTime4 venceu!")

print("\n[RESULTADO]: Os times {} e {} estão na grande final!".format(timeWin1, timeWin2))