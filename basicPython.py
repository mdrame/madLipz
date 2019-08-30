import sys
import time




print("\n")




def playGame_fun():

        #    if p == "p : # checkig to see if i cant skipe the raw value in the play function .

            # terminal UIPrograss HUb.


                first_adjective = input("Adjective: ~ ")
                second_adjective = input("Adjective: ~ ")
                type_of_bird = input("type of bird: ~ ")
                room_in_a_house = input("room_in_a_house: ~ ")
                verb_past_tense = input("verb_past_tense: ~ ")
                verbe = input("verb: ~ ")
                relatives_name = input("relative: ~ ")
                noun = input("noun: ~ ")
                a_liquid = input("a_liquid: ~ ")
                verb_ending_in_ing = input("verb_ending_in_ing: ~ ")
                part_of_the_body = input("part_of_the_body: ~ ")
                plural_noun = input("plural_noun: ~")
                verb_ending_in_ing_two = input("verb_ending_in_ ing_two: ~ ")
                second_noun = input("second_noun: ~ ")
                print("\n")



                print(f"It was a  {first_adjective} , cold November day. I ")
                print(f" woke up to the {second_adjective} smell of {type_of_bird} ")
                print(f"roasting in the {room_in_a_house} downstairs. I ")
                print(f" {verb_past_tense} down the stairs to see if I could ")
                print(f" help {verbe} the dinner. My mom said ")
                print(f"See if {relatives_name} needs a fresh {noun}. So I")
                print(f"carried a tray of glasses full of {a_liquid} into ")
                print(f" the {verb_ending_in_ing} room. When I got there, I")
                print(f"could'nt belive my {part_of_the_body} ! There were ")
                print(f" {plural_noun} {verb_ending_in_ing_two} on the {second_noun} !")

                print("Close terminal to end game")






player_name = input(" Welcome to MadLipz player: Please enter your name: ")
# todo: after player enter name, create UIHube loading.

print(f" hey {player_name} buckle up ! ! ! ! !")

user_input_type = input("        Hit i for instruction and p to Continue  ")
#user input is a global variable, so it can be use every where in the code.

# no error above



def instruction_func(i):

    if i == "i": # if user enter i game takes user to the instrucrtion else it exit.



        print("""
* - * - * - * - Instruction: - * - * - * - * - *\n
Choose two colors of chips. Keep the third color
away from the game board.Team players must be
evenly divided into two teams. Team members must
alternate their physical positions with opponents
around the playing surface. Players cut cards and
lowest card deals - Aces are high.The dealer should
shuffle the cards and deal out the same number of
cards to each player (see table below for proper
number of cards to be dealt). The remaining cards
are laid down as draw deck, facing down. The
players now pick up their cards making sure no
one see them.Place the game board on a flat
surface with enough room around the game board
for placement of the draw deck of cards, marker
chips and discards for each player.  \n """)




    elif i == "p":
        playGame_fun()
        exit()

    elif (i != "i" and i != "p"): # if user does not enter either i or p. let them know to enter it.
        print("worng key:  Please Hit (p) to proceed\n")
        correct_answer = input(":~ ")
        if (correct_answer == "p"):
            print("\n")
            playGame_fun()
            exit()







# call instruction_or_continuen function under:
def animated(text):
    for loadingText in text: # reminder not to pirnt the string of the text in function .
        sys.stdout.flush() #this line animate the text
        time.sleep(0.075) # duration
        print(loadingText)



animated("loading .......") # calling animated function

instruction_func(user_input_type)
playGame_fun()
