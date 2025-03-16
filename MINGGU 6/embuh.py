def winStreak(poin_player, win_streak, poin_ws):
    if win_streak == 1:
        print ("not win streak")
    else:
        for _ in range (win_streak):
            poin_player += poin_ws
            poin_ws = poin_ws + 100
        print(f"saya punya poin : {poin_player}")


winStreak(0,1,100)
winStreak(1000,3,100)
winStreak(9876,100,350)
winStreak(500,5,1000)
winStreak(100,7,300)
winStreak(1000,0,500)
winStreak(1000,1,500)
winStreak(123456789,1000,54321)