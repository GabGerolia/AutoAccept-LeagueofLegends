import pyautogui
import time


imageAcceptbtn = "KRacceptbtn.png" #change image name depends on language
champtoBan = "leblanc" #change who to ban

#do not change beyond this point
delay = 1 #1second
def autoaccept():
    while True:
        try:
            print("Finding accept...")
            accept = pyautogui.locateCenterOnScreen(imageAcceptbtn , confidence=0.8)
            if accept is not None:
                pyautogui.click(accept)
                print("Accepted")
                break

        except Exception as e:
            print(f"{e}")
        
        time.sleep(delay)

def autoban():
    global insideMatch
    global done

    #1280x720 resolution league only
    i = 0
    while True:
        try:
            print("Finding searchbar...")
            search = pyautogui.locateCenterOnScreen('search.png', confidence=0.8)
            if search is not None:
                x, y = search #save coordinates
                pyautogui.moveTo(search) #move cursor to searchbar
                print("Match found")
                print("Waiting for Banning phase!")
                time.sleep(20) #buffer 20secs (wait for ban phase)
                print("Ban Phase detected")
                pyautogui.click(search) #click searchbar
                pyautogui.write(champtoBan)

                #change coords
                x = x - 356
                y = y + 59

                time.sleep(1)
                pyautogui.click(x, y) #click champ

                #change coords
                x = x + 245
                y = y + 445

                time.sleep(1)
                pyautogui.click(x, y) #click ban btn
                print("DONE")
                done = True
                break
        except Exception as e:
            print(f"{e}")

        i += 1 
        if i >= 20: #wait for 20 secs
            print("Assumed Match Declined")
            insideMatch = False
        elif i >=10: #wait for 10 secs
            try:
                print(f"checking if in game: {i}")
                print("Finding accept...")
                accept = pyautogui.locateCenterOnScreen(imageAcceptbtn , confidence=0.8)
                if accept is not None:
                    pyautogui.click(accept)
                    print("Accepted")
                    break
            except Exception as e:
                print(f"{e}")
            else:
                continue
        else:
            print(f"checking if in game: {i}")
            insideMatch = True

        if insideMatch == False:
            insideMatch = False
            break
        time.sleep(delay)


def main():
    global insideMatch
    global done
    insideMatch = False
    done = False

    while True:
        if insideMatch == True:
            autoban()
            if done == True:
                break
            else:
                continue
        else:
            autoaccept()
            insideMatch = True


if __name__ == "__main__":
    main()