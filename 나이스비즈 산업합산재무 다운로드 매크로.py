import pyautogui
import keyboard
import time

#print(pyautogui.position())

def exitIfPressed():
    if keyboard.is_pressed('\\'):
        exit()

def setting():
    print('---F5이후 세팅---')
    pyautogui.moveTo(950,513,0.3)
    pyautogui.click()
    #최신순서->과거>최신
    pyautogui.hotkey("shift","tab")
    pyautogui.hotkey("shift","tab")
    time.sleep(1)#대기 걸어줘야 입력이 됨..
    pyautogui.press("up")
    #표기방식->약식
    pyautogui.hotkey("shift","tab")
    time.sleep(1)
    pyautogui.hotkey("up")
    #표시기간->5개년
    pyautogui.hotkey("shift","tab")
    time.sleep(1)
    pyautogui.press("up")

def download():
    print('---마우스 자동 이동/클릭---')
    #검색클릭
    pyautogui.moveTo(1500,528,0.3)
    pyautogui.click()
    time.sleep(0.3)
    #다운로드클릭
    pyautogui.moveTo(1835,263,0.3)
    pyautogui.click()
    time.sleep(0.3)
    #현재페이지 엑셀
    pyautogui.moveTo(1800,430,0.3)
    pyautogui.click()
    time.sleep(0.3)
    

while True:
    exitIfPressed()
    if keyboard.is_pressed('.'):#마우스 위치 디버깅 용
        print(pyautogui.position())
        time.sleep(0.1)

    if keyboard.is_pressed('`'):
        setting()

    if keyboard.is_pressed('1'):
        download()
        
    if keyboard.is_pressed('2'):
        pyautogui.moveTo(467,363,0.3)
        pyautogui.click()
        pyautogui.press("tab")
        time.sleep(1)
        for i in range(2):
            pyautogui.press("down")
        download()

    if keyboard.is_pressed('3'):
        pyautogui.moveTo(467,363,0.3)
        pyautogui.click()
        pyautogui.press("tab")
        time.sleep(1.5)
        for i in range(3):
            pyautogui.press("down")
        download()
    
    if keyboard.is_pressed('4'):
        pyautogui.moveTo(467,363,0.3)
        pyautogui.click()
        pyautogui.press("tab")
        time.sleep(1)
        for i in range(4):
            pyautogui.press("down")
        download()
    
    if keyboard.is_pressed('5'):
        pyautogui.moveTo(467,363,0.3)
        pyautogui.click()
        pyautogui.press("tab")
        time.sleep(1)
        for i in range(5):
            pyautogui.press("down")
        download()
        

                


