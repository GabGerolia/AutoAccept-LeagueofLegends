import pyautogui
import time


delay = 0.5

def autoaccept():
    while True:
        try:
            print("Finding accept...")
            #change image name depends on language
            accept = pyautogui.locateCenterOnScreen('KRacceptbtn.png', confidence=0.8)
            if accept is not None:
                pyautogui.click(accept)
                print("found")
                break

        except Exception as e:
            print(f"-: {e}")
        
        time.sleep(delay)

def autoban():

    #1280x720 resolution league only

    while True:
        try:
            print("Finding searchbar...")
            search = pyautogui.locateCenterOnScreen('search.png', confidence=0.8)
            if search is not None:
                x, y = search #save coordinates

                time.sleep(25) #buffer 25secs (wait for ban phase)
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
                print("done")
                break
        except Exception as e:
            print(f"-: {e}")

        time.sleep(delay)

def main():
    autoaccept()
    autoban()

if __name__ == "__main__":
    main()