from deck_gen import gen_rand_deck
import display_funct
import game_classes
from enum import Enum
import game_AI
import game_logic

#GAME STATE
state_list = ['START_MENU', 'PLAYING']
game_state = Enum('game_state', state_list)
curr_state = game_state.START_MENU
print(curr_state)

#START BUTTONS
start_buttons_list = ['START_BUTTON', 'QUIT_BUTTON']
start_buttons = Enum('button', start_buttons_list)
curr_button = start_buttons.START_BUTTON
print(curr_button)

# loop for allowing multiple games to be restarted
while True:
    if(curr_state == game_state.START_MENU):
        print('start_menu')
        display_funct.start_menu()
        display_funct.process()
    elif(curr_state == game_state.PLAYING):
        print('playing')


        # initilizing the board to be used within the game
        board1 = game_classes.Board("board1")
        # initilizing a deck to be used within the game (3 copies are added to
        # each other)
        deck1 = gen_rand_deck("deck1", 0)
        # defining a 7 player uno game
        player1 = game_classes.Player("player_1")
        player1.grab_cards(deck1, 7)
        player2AI = game_AI.make_AI_basic(deck1, "player_2AI", 7)
        player3AI = game_AI.make_AI_basic(deck1, "player_3AI", 7)
        player4AI = game_AI.make_AI_basic(deck1, "player_4AI", 7)
        player5AI = game_AI.make_AI_basic(deck1, "player_5AI", 7)
        player6AI = game_AI.make_AI_basic(deck1, "player_6AI", 7)
        player7AI = game_AI.make_AI_basic(deck1, "player_7AI", 7)
        display_funct.redraw_hand_visble(player1, None)
        # enters into playing the game
        game_logic.game_loop(board1, deck1, [player1, player2AI, player3AI, player4AI,
                             player5AI, player6AI, player7AI])

# function to find if
# given point lies inside
# a given rectangle or not.
def FindPoint(x1, y1, x2,
              y2, x, y) :
    if (x > x1 and x < x2 and
            y > y1 and y < y2) :
        return True
    else :
        return False