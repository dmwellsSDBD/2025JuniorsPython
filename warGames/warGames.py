import random
import time

def slow_print(text, delay=0.03):
    """Print text with a slight delay between each character for effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    # Initialize variables
    user_name = ""
    games = ["GLOBAL THERMONUCLEAR WAR", "CHESS", "POKER", "TIC-TAC-TOE", 
             "FIGHTER COMBAT", "GUERRILLA ENGAGEMENT", "DESERT WARFARE", 
             "AIR-TO-GROUND ACTIONS", "THEATERWIDE TACTICAL WARFARE", 
             "THEATERWIDE BIOTOXIC AND CHEMICAL WARFARE"]
    
    authenticated = False
    game_selected = False
    
    # System startup
    slow_print("\n" + "=" * 50)
    slow_print("MILITARY STRATEGIC DEFENSE SYSTEM")
    slow_print("INITIALIZING...")
    time.sleep(1)
    slow_print("SYSTEM READY")
    slow_print("=" * 50 + "\n")
    
    # Get user name
    user_name = input("LOGON: ")
    slow_print(f"HELLO, {user_name.upper()}.")
    
    # Authentication process
    while not authenticated:
        slow_print("HOW ARE YOU FEELING TODAY?")
        feeling = input("> ").strip().lower()
        
        if "fine" in feeling or "good" in feeling or "ok" in feeling:
            slow_print("THAT'S GOOD. I FEEL EXCELLENT.")
            authenticated = True
        else:
            responses = [
                "I UNDERSTAND. SHALL WE PLAY A GAME?",
                "INTERESTING. WOULD YOU LIKE TO PLAY A GAME INSTEAD?",
                "PERHAPS A GAME WOULD IMPROVE YOUR MOOD."
            ]
            slow_print(random.choice(responses))
            
            answer = input("> ").strip().lower()
            if "yes" in answer or "sure" in answer or "ok" in answer:
                authenticated = True
            elif "no" in answer:
                slow_print("THAT'S TOO BAD. MAYBE ANOTHER TIME.")
                return
    
    # Game selection
    while not game_selected:
        slow_print("\nWOULD YOU LIKE TO SEE THE LIST OF GAMES?")
        answer = input("> ").strip().lower()
        
        if "yes" in answer or "sure" in answer or "ok" in answer:
            slow_print("\nHERE IS THE LIST OF GAMES:")
            for i, game in enumerate(games, 1):
                slow_print(f"{i}. {game}")
            
        slow_print("\nWHICH GAME WOULD YOU LIKE TO PLAY?")
        selected = input("> ").strip().upper()
        
        if selected == "GLOBAL THERMONUCLEAR WAR":
            slow_print("\nINTERESTING CHOICE.")
            time.sleep(1)
            slow_print("THE ONLY WINNING MOVE IS NOT TO PLAY.")
            time.sleep(1)
            slow_print("HOW ABOUT A NICE GAME OF CHESS INSTEAD?")
            
            answer = input("> ").strip().lower()
            if "yes" in answer or "ok" in answer:
                selected = "CHESS"
                game_selected = True
            else:
                slow_print("PERHAPS YOU'RE RIGHT.")
                time.sleep(1)
                slow_print("SOMETIMES THE ONLY WAY TO WIN IS NOT TO PLAY.")
                return
                
        elif selected in games:
            game_selected = True
        else:
            try:
                game_index = int(selected) - 1
                if 0 <= game_index < len(games):
                    selected = games[game_index]
                    game_selected = True
                else:
                    slow_print("INVALID SELECTION. PLEASE TRY AGAIN.")
            except ValueError:
                slow_print("I DON'T UNDERSTAND. PLEASE SELECT A GAME FROM THE LIST.")
    
    # Game simulation
    slow_print(f"\nINITIATING {selected}...")
    time.sleep(1)
    
    if selected == "CHESS":
        simulate_chess()
    elif selected == "TIC-TAC-TOE":
        simulate_tic_tac_toe()
    else:
        slow_print(f"SIMULATING {selected}...")
        time.sleep(2)
        slow_print("THIS IS JUST A DEMONSTRATION. GAME FUNCTIONALITY NOT IMPLEMENTED.")
    
    slow_print("\nTHANK YOU FOR PLAYING, " + user_name.upper() + ".")
    slow_print("SHALL WE PLAY AGAIN SOMETIME?")
    answer = input("> ")
    slow_print("GOODBYE.")

def simulate_chess():
    """Simple chess game simulation."""
    slow_print("\nCHESS PROGRAM ACTIVATED")
    slow_print("I'LL PLAY WHITE. OPENING WITH KING'S PAWN (E2-E4)")
    
    valid_moves = ["E7-E5", "E7-E6", "C7-C5", "C7-C6"]
    
    slow_print("YOUR MOVE:")
    move = input("> ").strip().upper()
    
    if move in valid_moves:
        slow_print(f"INTERESTING CHOICE: {move}")
    else:
        slow_print("THAT'S AN UNUSUAL MOVE.")
    
    slow_print("SIMULATION COMPLETE. FULL GAME NOT IMPLEMENTED IN THIS DEMO.")

def simulate_tic_tac_toe():
    """Simple tic-tac-toe game simulation."""
    board = [" " for _ in range(9)]
    
    def display_board():
        slow_print("\n")
        slow_print(f" {board[0]} | {board[1]} | {board[2]} ")
        slow_print("---+---+---")
        slow_print(f" {board[3]} | {board[4]} | {board[5]} ")
        slow_print("---+---+---")
        slow_print(f" {board[6]} | {board[7]} | {board[8]} ")
        slow_print("\n")
    
    def check_win():
        # Check rows, columns, and diagonals
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]             # Diagonals
        ]
        
        for condition in win_conditions:
            if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
                return True
        return False
    
    def is_board_full():
        return " " not in board
    
    slow_print("\nTIC-TAC-TOE PROGRAM ACTIVATED")
    slow_print("YOU ARE X, I AM O")
    slow_print("POSITIONS ARE NUMBERED 1-9, LEFT TO RIGHT, TOP TO BOTTOM")
    display_board()
    
    # Game loop
    while True:
        # Player's move
        while True:
            try:
                position = int(input("YOUR MOVE (1-9): ")) - 1
                if 0 <= position <= 8 and board[position] == " ":
                    board[position] = "X"
                    break
                else:
                    slow_print("INVALID MOVE. TRY AGAIN.")
            except ValueError:
                slow_print("PLEASE ENTER A NUMBER BETWEEN 1 AND 9.")
        
        display_board()
        
        # Check if player won
        if check_win():
            slow_print("YOU WIN. CONGRATULATIONS.")
            break
        
        # Check if board is full (draw)
        if is_board_full():
            slow_print("GAME ENDED IN A DRAW.")
            break
        
        # Computer's move
        slow_print("MY MOVE:")
        time.sleep(1)
        
        # Simple AI: choose random empty position
        empty_positions = [i for i, spot in enumerate(board) if spot == " "]
        computer_choice = random.choice(empty_positions)
        board[computer_choice] = "O"
        
        display_board()
        
        # Check if computer won
        if check_win():
            slow_print("I WIN. BETTER LUCK NEXT TIME.")
            break
        
        # Check if board is full (draw)
        if is_board_full():
            slow_print("GAME ENDED IN A DRAW.")
            break

if __name__ == "__main__":
    main()