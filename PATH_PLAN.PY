import cmath
import math

# TODO
# check if the robot can turn around on the spot.
# the main creteria is if the whiteline sensor remains at the same position
# or else we will need to impliment PWM and check whiteline sensor in every loop while the robot is rotating.
# i.e. the turn_right/left() functions will be loops.

# TODO
# extract information from arena variables and find a way to use them.

# TODO
# make/complete functions:
#   main()
#   join_string(str)  <-- for this function we also need 1 more global variable ( this function will join the str string to the global string variable )
#   give_path(pt1,pt2)
#   etc...

#####################################################################################################
# variables given by the areana
arena_config = {0: ("Water Pitcher", 5, "2-2"), 1: ("Pebble", 3, "1-1"), 2: ("Pebble", 11, "3-3"), 3:("Pebble", 13, "2-2")} # this is a dictionary
Robot_start = "START-1"
#####################################################################################################

# cell numbering:
#                                1
#                            2       4
#                        5       3       9
#                            6       8
#           start-1->   10       7       14    <-start-2
#                            11      13
#                       15       12      19
#                            16      18
#                                17

# compass for each cell: 
#
#                  2           3
#                    \       /
#                      \   /
#   Start 1      1 - - - O - - -  1         Start 2
#                      /   \
#                    /       \
#                  3           2

# my compass for the bot: 
#
#                  2           3
#                    \       /
#                      \   /
#   Start 1      1 - - - O - - -  4         Start 2
#                      /   \
#                    /       \
#                  6           5


# current position of bot will be stored as complex no. a + ib
# refer the photo "Complex_plane.jpg" to understand the complex no. assignment



# two special positions i.e. start-1 and start-2 can be defined to be 1 unit left and right of each 
# so for start 1:
if Robot_start == "START-1":
    current_position = complex(-5, 0)
    # for direction of the bot
    current_orientation = 5
elif Robot_start == "START-2":
    current_position = [-1,0]
    current_orientation = 1




# variable defines if the electromagnet is occupied
e_magnet_occupied = False

# and current_position = [-1,0], current_orientation = 1 for start-2

# keep in mind that these 2 functions dont care if the final vertex is a valid vertex of not.
def go_forward():
    global current_position, current_orientation
    if current_orientation == 1:
        current_position += complex(-1,0)
    if current_orientation == 2:
        current_position += complex(-0.5, math.sin(math.pi/3))
    if current_orientation == 3:
        current_position += complex(0.5, math.sin(math.pi/3))
    if current_orientation == 4:
        current_position += complex(1,0)
    if current_orientation == 5:
        current_position += complex(0.5, -math.sin(math.pi/3))
    if current_orientation == 6:
        current_position += complex(-0.5, -math.sin(math.pi/3))

def go_backward():
    global current_position, current_orientation
    if current_orientation == 1:
        current_position += complex(1,0)
    if current_orientation == 2:
        current_position += complex(0.5, -math.sin(math.pi/3))
    if current_orientation == 3:
        current_position += complex(-0.5, -math.sin(math.pi/3))
    if current_orientation == 4:
        current_position += complex(-1,0)
    if current_orientation == 5:
        current_position += complex(-0.5, math.sin(math.pi/3))
    if current_orientation == 6:
        current_position += complex(0.5, math.sin(math.pi/3))

#############################################################################################################
# these two functions need to be checked if they are possible to be executed by the bot.
# the main creteria is if the whiteline sensor remains at the same position
# turns are 60 degrees
def turn_right():
    global current_position, current_orientation
    if current_orientation == 6:
        current_position = 1
    else:
        current_orientation +=1

# turns are 60 degrees
def turn_left():
    global current_position, current_orientation
    if current_orientation == 1:
        current_position = 6
    else:
        current_orientation -=1
########################################################################################################

def pick_up():
    e_magnet_occupied = True

def drop():
    e_magnet_occupied = False


def main():
    # this will call onto other functions.

    # Steps:
    # (1) Reach the closest Pebble from the starting position and figure out which node to reach to pick up the pebble.
    # (2) Pick up the pebble and deposit it at the ‘pitcher’
    # (3) loop = {
    #   1. Reach the closest pebble to the pitcher
    #   2. Pick up the pebble and deposit it at the ‘pitcher’
    # }

if __name__ == '__main__':
    main()