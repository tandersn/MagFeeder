from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
import sys

def press_then_sleep(key, ms=500):
    print(f"Pressing {key}")
    keyboard.press(key)
    time.sleep(75/1000)
    keyboard.release(key)

    print(f"Sleeping for {ms}")
    time.sleep(ms/1000)


def spam_feed(seconds):
    """seconds: Number of seconds to spam feeding before backing out"""
    start_time = time.time()
    print(f"Spamming feed for {seconds} seconds")
    while start_time > time.time() - seconds:
        press_then_sleep(Key.enter, ms=100)


def feed_mag():
    # Use a breakpoint in the code line below to debug your script.
    press_then_sleep(Key.home)
    press_then_sleep(Key.enter, ms=200)
    press_then_sleep(Key.down, ms=100)
    press_then_sleep(Key.down, ms=100)
    press_then_sleep(Key.enter, ms=200)
    press_then_sleep(Key.enter, ms=200)
    press_then_sleep(Key.enter, ms=200)
    spam_feed(20)
    press_then_sleep(Key.home)


def move_down_menu(pos_x):
    i = 0
    while i < pos_x:
        press_then_sleep(Key.down, ms=100)
        i = i + 1


def buy_items(item_pos):
    press_then_sleep(Key.enter)
    press_then_sleep(Key.enter)

    move_down_menu(pos_x=item_pos)

    # Max out stacks
    press_then_sleep(Key.enter)
    press_then_sleep(Key.down)

    # Buy item
    press_then_sleep(Key.enter)
    press_then_sleep(Key.enter)

    # Leave menu
    press_then_sleep(Key.esc)
    press_then_sleep(Key.esc)
    press_then_sleep(Key.esc)


if __name__ == '__main__':
    item_pos = int(sys.argv[1:][0])
    print("Waiting 10 seconds before beginning script.")
    print("Please click on the PSOBB window now!")
    time.sleep(10)
    while True:
        print("Beginning mag feed round!")
        feed_mag()
        buy_items(item_pos)

        print("Waiting for next round")
        waited = 0
        while waited < 19:
            time.sleep(10)
            waited = waited + 1
            print(f"waited {waited*10} seconds")
