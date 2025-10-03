# PSOBB Mag Feeder

This script will automatically feed your mag with an item of your choice. It also keeps the item topped up by buying it from the shop.

## Running it

### Prerequisites
* It's smart to start with a mag that's already gone through all of its evolutions, so its food preferences don't change
* Python is installed on your system.
* Download `main.py` and `requirements.txt` from this repository
  * Navigate to where these are downloaded and run `pip install -r requirements.txt` 
### Game Setup
1. Run the game in windowed mode
2. Withdraw all of your meseta
3. Deposit all consumable items, except the one you want to feed to your mag
4. Stand your character in front of the shop
5. Find out what position the item is in the shop. For example, if I want to feed my mag Trifluids, and I have to move down `10` items in the shop to buy it, then `10` is the number I want.
6. Close the shop, do not move your character.
7. Feed your mag once and make sure the menu is still on MAG when you exit
8. Wait 3.5 minutes...


In the command line, navigate to where you downloaded `main.py`, then run:

```python main.py 10```

Where you replace `10` with whatever number you came up with in step 5.

**Once you run the script, you have 10 seconds to focus the window. THE WINDOW MUST BE FOCUSED, otherwise the script will start hitting a bunch of random buttons on your desktop!**

To stop the execution of the script, hit Ctrl-C in your command-line/terminal, or close the terminal window.
