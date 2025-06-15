import pyautogui
import time


delay = 1 

def autoaccept():
    while True:
        try:
            print("Finding accept...")
            #change image name depends on language
            accept = pyautogui.locateCenterOnScreen('KRacceptbtn.png', confidence=0.8)
            if accept is not None:
                pyautogui.click(accept)
                print("Accepted")
                break

        except Exception as e:
            print(f"-: {e}")
        
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
                pyautogui.write("leblanc") #write champ to ban

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
            insideMatch = False
        else:
            print(f"checking if in game: {i}")
            insideMatch = True
        ######    
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