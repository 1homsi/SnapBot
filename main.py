from colorama import Fore
import pyautogui, keyboard, time

class snapchat:
    def __init__(self):
        self.sent_snaps = 0
        self.delay = 5
        self.shortcutUsers = 0
                        
    def get_positions(self):
        self.print_console("Move your mouse to the camera button, then press F")
        while True:
            if keyboard.is_pressed("F"):
                self.switch_to_camera = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to the take picture button, then press F")
        while True:
            if keyboard.is_pressed("F"):
                self.take_picture = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to the Edit & Send button, then press F")
        while True:
            if keyboard.is_pressed("F"):
                self.edit_send = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to the Send To button, then press F")
        while True:
            if keyboard.is_pressed("F"):
                self.send_to = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to your shortcut, then press F")
        while True:
            if keyboard.is_pressed("F"):
                self.shortcut = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to select all in shortcut, then press F")
        while True:
            if keyboard.is_pressed("F"):
                self.select_all = pyautogui.position()
                break
        time.sleep(0.5)
        self.print_console("Move your mouse to send snap button, then press F")
        while True:
            if keyboard.is_pressed("F"):
                self.send_snap_button = pyautogui.position()
                break
    
    def send_snap(self):
        pyautogui.moveTo(self.switch_to_camera)
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(self.take_picture)
        for i in range(7):
            pyautogui.click()
            time.sleep(self.delay - 1)
        pyautogui.moveTo(self.edit_send)
        time.sleep(self.delay)
        pyautogui.click()
        pyautogui.moveTo(self.send_to)
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(self.shortcut)
        pyautogui.click()
        time.sleep(self.delay + 1.5)
        pyautogui.moveTo(self.select_all)
        pyautogui.click()
        time.sleep(self.delay - 1)
        pyautogui.moveTo(self.send_snap_button)
        pyautogui.click()
        time.sleep(self.delay)
        self.sent_snaps += 7
       
    def print_console(self, arg, status = "Console"):
        print(f"\n       {Fore.WHITE}[{Fore.RED}{status}{Fore.WHITE}] {arg}")
    
    def main(self):
        print("Enter Number of users in the shortcut:")
        num_users = int(input())
        self.shortcutUsers = num_users
        self.get_positions()
        self.print_console("Press F to start")
        shortcut_users = 0
        self.print_console("Go to your chats, then press F when you're ready.")
        time.sleep(1)
        while True:
            if keyboard.is_pressed("F"):
                break
        self.print_console("Sending snaps...")
        self.started_time = time.time()
        while True:
            if keyboard.is_pressed("p"):
                break
            self.send_snap()
            print(f"{Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] {Fore.GREEN}Sending snaps...")
            time.sleep(6)
        self.print_console(f"Finished sending {self.sent_snaps} snaps.")
        
snapchat().main()