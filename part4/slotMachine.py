import random

# -------------------- GAME CONFIG --------------------

SYMBOLS = ["⭐", "🔔", "🍉", "🍇"]

PAYOUTS = {
    "⭐": 20,
    "🔔": 15,
    "🍉": 10,
    "🍇": 5
}

STARTING_BALANCE = 20

# -------------------- CORE FUNCTIONS --------------------

def get_bet(balance):
    """Ask the player for a valid bet."""
    while True:
        try:
            bet = int(input("Enter bet amount: "))
            if bet <= 0:
                print("Bet must be greater than 0.")
            elif bet > balance:
                print("You cannot bet more than your balance.")
            else:
                return bet
        except ValueError:
            print("Please enter a number.")


def spin_reels():
    """Spin the slot machine reels."""
    return [
        random.choice(SYMBOLS),
        random.choice(SYMBOLS),
        random.choice(SYMBOLS)
    ]


def display_reels(reels):
    """Display the reels."""
    print("\n🎰 Spinning...")
    print(" | ".join(reels))


def check_win(reels):
    """Check if all symbols match."""
    return reels[0] == reels[1] == reels[2]


def calculate_payout(symbol, bet):
    """Calculate winnings based on symbol."""
    multiplier = PAYOUTS.get(symbol, 0)
    return bet * multiplier


def ask_to_continue():
    """Ask the player if they want to continue."""
    while True:
        choice = input("Play again? (Y / N): ").strip().upper()
        if choice in ("Y", "N"):
            return choice == "Y"
        print("Please enter Y or N.")

# -------------------- GAME LOOP --------------------

def play_slot_machine():
    balance = STARTING_BALANCE
    print("🎰 Welcome to the Slot Machine!")
    print(f"Starting balance: {balance}")

    running = True

    while running and balance > 0:
        print(f"\nCurrent balance: {balance}")
        bet = get_bet(balance)
        balance -= bet

        reels = spin_reels()
        display_reels(reels)

        if check_win(reels):
            winnings = calculate_payout(reels[0], bet)
            balance += winnings
            print(f"🎉 You won {winnings}!")
        else:
            print("❌ You lost.")

        print(f"Balance: {balance}")

        if balance == 0:
            print("💸 You ran out of money!")
            break

        running = ask_to_continue()

    print("\nThanks for playing! 👋")

# -------------------- START GAME --------------------

play_slot_machine()
