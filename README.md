# Python Blind Auction

A command-line **blind auction program** built with Python.

The program allows multiple bidders to enter their names and bids without seeing the bids entered by other participants. Once bidding is complete, the program identifies the highest bidder and displays the winning bid.

This project was created as part of my Python learning journey to practise **dictionaries, functions, loops, conditional statements, and working with user input**.

## Features

* Multiple bidders can enter bids
* Bids are stored in a Python dictionary
* Previous bids are hidden from subsequent bidders
* Automatically identifies the highest bidder
* Displays the winning bidder and bid amount
* Uses a simple command-line interface
* Includes an ASCII-art auction logo

## How It Works

Each bidder provides:

1. Their name
2. Their bid amount

The information is stored in a dictionary:

```python
bids[name] = price
```

For example:

```python
bids = {
    "Alice": 100,
    "Bob": 150,
    "Charlie": 125
}
```

When bidding is finished, the program loops through the dictionary and compares each bid to the current highest bid.

```python
for bidder in bidding_dictionary:
    bid_amount = bidding_dictionary[bidder]

    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
```

The bidder with the highest bid is then announced as the winner.

## Example

```text
Please tell me your name: Alice
Please enter your bid: £100

Are there any other bidders? Type 'yes' or 'no':
yes

Please tell me your name: Bob
Please enter your bid: £150

Are there any other bidders? Type 'yes' or 'no':
yes

Please tell me your name: Charlie
Please enter your bid: £125

Are there any other bidders? Type 'yes' or 'no':
no

The winner is Bob with a bid of £150
```

## Technologies Used

* Python 3
* `art` Python module

## What I Learned

Through this project, I practised:

* Defining and calling functions
* Function parameters
* Python dictionaries
* Adding key-value pairs to dictionaries
* `for` loops
* `while` loops
* `if` / `elif` statements
* Comparing numerical values
* Finding the highest value in a collection
* User input with `input()`
* Converting strings to integers using `int()`
* Boolean variables
* Using `.lower()` to normalise user input
* Importing and using a Python module

## How to Run

Clone the repository and navigate to the project directory:

```bash
cd Python_Blind_Auction
```

Run the program:

```bash
python main.py
```

If the `art` module is not installed:

```bash
pip install art
```

## Future Improvements

Possible improvements include:

* Validate that bid amounts are valid numbers
* Handle duplicate bidder names
* Allow bidders to update their bids
* Improve input validation for `yes`/`no`
* Display the winning bid with consistent currency formatting
* Add automated tests
* Separate the auction logic from user interaction
* Add a graphical interface
# Blackjack_game_in_python
