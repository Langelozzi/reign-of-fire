"""
Module containing the Story class.
"""

import time

from helpers import Helpers


class Story:
    """
    A simple class containing methods related to the game storyline.
    """

    # Game Opening -----------------------------------------------------------------------------------------------------
    @staticmethod
    def opening_dialogue() -> None:
        """
        Print the opening story and ascii art to stdout.

        :postcondition: prints the opening story and ascii art to stdout
        """

        opening_one = "During the Reign of Gold, the continent of Alyndelle were prosperous. The Golden Capital of \n" \
                      "Astera were at the pinnacle of its reign, their prowess told to match the power of gods. \n"

        opening_two = "However, power such as these often corrupts and the God King of Alyndelle were no different.\n" \
                      "His arrogance lead him to enslaving an angel to extract their power to truly transcend the " \
                      "realm of humanhood.\n"

        opening_three = "His greed and transgression angered the Gods leading the world into the Age of Fire.\n" \
                        "God King Thompson finally slayed the Gods but to do so he took the flame of humanity, " \
                        "casting\nthe rest humanity into darkness...\n"

        Helpers.print_in_color("...\n", "cyan")
        time.sleep(2)
        Helpers.print_in_color(opening_one, "cyan")
        time.sleep(4)
        Helpers.print_in_color(opening_two, "cyan")
        time.sleep(4)
        Helpers.print_in_color(opening_three, "cyan")
        time.sleep(7)
        Helpers.print_in_color(r"""

                                                          %#&&%%#*                                      
                                                     #(#(&##&                                           
                                                   @(((#%(%                                             
                                                 #(&%((#(                                               
                                                  ((#%(@&@                                              
                                         ,********,*/**//***&                                           
                                         &*/(*(**,*,*/*///**,                                           
                                         #/**********//////**/                                          
                                         @&&/*********////***,                                          
                                         *#&%&&%##***////////*#                                         
                                         *##%/*(*,*/((%##(//(/                                          
                                         (//********/////#&(//(,                                        
                                         %%*****,*,,*#/*(***%/((&//                                     
                                         %#/*******&**,***%**,/%#                                       
                                         /((****(#(**&**%,(@%&#(%(*@(&(                                 
                                         @%%**(*#//#***#@(#(##@#((/#(#%(#((%%& (                        
                                       ((@**%*//*///&(((/%/(#(((%#((((((((#((#&&(%                      
                                   %(###@#%&&%%&%&((/(&#&@#%(/%%(##((#(###(%#&&#((&                     
                                 *%%##%%%@(%@@/((((((@((((&#(((#%(%##%(&#&@%@(%((#&                     
                               ,(###%##%#&#((%((((%(&&@#%%##(&&@##%#&(@&%#%(##((&%((((                  
                            @@@@##%#%&((/#/%((%&&/,,(&(%##%#%#%%%#(((%(((####&##((%((&&(&               
                               ###@#%/,,,.&%#...#,....,,&@&%#%%#&&%@%%(####(#@&@%(%%#&&#                
                      &        @((%*,,...#......#.....,*(/*#%@&&#%%%&&(((%%&#@%#%%%#@%                  
                   /***/%*#.     (.,...&#.......* #@#.,,/*%&&%@%#%%###%%##%#(((#(&%%(                   
                  ,,,*,,##&      &..,.##.....,((#....,,,,*%%%&@@%&@(%#%###%(((((#(&(#(                  
                  %,,,,,,%/&    &(#. ##(..&(##@.....,,,,*@%&&&&%%%%@&%####((#(((%#(%##(@                
                  %#*#,,,(&     @.%%////&##(%......,,,,,/@&%%##%%&&%%&&##%###(((#((@,%%%&&@             
                   @//%/(/%&    @,%#/%%//(...........,,,&%%(&&%%%&&&%&&@%%%(##&&&%%%@@*%@&&&            
                   #(*,&%&/,**(&&%@/(////#((@........,,((/////(((/%((#(/@@&&&&@##%%##%#%/#&             
                   .&%,*#%@(%&(##&&/////%%####(#####%*,&////////(((/((/%#  &%%(((((((((##((.            
                   &...@/,(((#(#%%#&(/(@@,.......,,,,,,@#(///////(/(//*.   #%##((((##%%#(/#             
                 %%,.../,,##&%(%&#,,#&&%%@,,,,/,,,,,,,,(////#(//(//(/(%& @##((((((((((##(&              
                 &..,..*,,,..@%#(( ,%/*@%%************%/#((///*(***/(%# @%%%(((((((/&%((.               
                #(/%/@.,,*##  @@#%%(&&,(/&%&*#/****(/*@/////////**/*/&( %#%(((#(((((%#%                 
                    #/,(#(       &####(*////&@(****/////(#((((/%##@&#  @##(((((##(/&(&                  
                     .(            ,/###(@//((%///(/#@&#%#%&@&&&&%#&% @(%%###(&&&(((                    
                                    #%@%%(((&&@%&&&&&&&&&&(##(@&@%/(&#/*******#((//                     
                                   %%%,(@%%###%&&@&&&@@@%#(#&@(//(//,/*/*****#(@#&                      
                                   @%&%@&@*#%%##&@*,@&##@&((/*&(/*(@*(/**/**//@                         
                                   (*@&@%%%@%@###((###%***,,,...(#//&&(*,/*%*(                          
                                    ,,,#//&&%&(#&%##(@**%&(****.,,,,(*,*#&/,                            
                                  @.,.,(,,,,*&#%%%%%%**@***&(,****,,,,,/*@&                             
                                   .,,&&,,@@%%#.@&##&*@**#***,@****,/**@                                
                                 ...,,, ####@...,(*@#@**,**%@**/@/////&#                                
                                @%...@#%%%&,..,../,,**&%*&&**@%&%@(/% @#,                               
                                (...,.@&@*,,...,....,*,,@#&@%%%(((((  @(%                               
                               /&.../ @  ..,...*,,..&*,...%%&%%###((#(%@&                               
                               &...,,.&    ,....,/,,.........@%%#####(#@#                               
                              &...(*..    @/,...*,,........... (#%#%#&%%@(%                             
                              , @#./,&     ..,./..,,...*,,.,..%  @&%&&@##((((                           
                            @      &        #.#   #@*  . ,.# (/     @(&%%##((((.                        
                                            (.      %                  (#%###(#((&                      
                                                                         @%%###/                        
                                                                            /                          
        """, "cyan")
        Helpers.print_in_color(r"""
             _______  _______ _________ _______  _          _______  _______    _______ _________ _______  _______  
            (  ____ )(  ____ \\__   __/(  ____ \( (    /|  (  ___  )(  ____ \  (  ____ \\__   __/(  ____ )(  ____  \
            | (    )|| (    \/   ) (   | (    \/|  \  ( |  | (   ) || (    \/  | (    \/   ) (   | (    )|| (    \/ 
            | (____)|| (__       | |   | |      |   \ | |  | |   | || (__      | (__       | |   | (____)|| (__     
            |     __)|  __)      | |   | | ____ | (\ \) |  | |   | ||  __)     |  __)      | |   |     __)|  __)    
            | (\ (   | (         | |   | | \_  )| | \   |  | |   | || (        | (         | |   | (\ (   | (       
            | ) \ \__| (____/\___) (___| (___) || )  \  |  | (___) || )        | )      ___) (___| ) \ \__| (____/\ 
            |/   \__/(_______/\_______/(_______)|/    )_)  (_______)|/         |/       \_______/|/   \__/(_______/ 
            """, "cyan")
        time.sleep(3)

    # Game Intro -------------------------------------------------------------------------------------------------------
    @staticmethod
    def cell_description() -> None:
        """
        Print the cell description to stdout.

        :postcondition: prints the cell description to stdout
        """
        part_one = "You wake to the sound of metal against stone.\n" \
                   "You lift your head from the floor and as your eyes adjust to the darkness you start to scan your " \
                   "surroundings..\n"

        part_two = "You are in a small cell, metal bars straight ahead; cobblestone lines the rest of the room\n" \
                   "You can feel the damp air in your breath, and hear the slow drop of water against the stone floor" \
                   "\nYou sense a darkness weighing in your chest and a cold breeze stroke down your spine\n" \
                   "From down the hall you see a shadow as it rounds the east corner, you catch a glimpse of a metal " \
                   "foot..\n"

        part_three = "The last thing you can remember is the moment the King Thompson took the flame of humanity\n" \
                     "You and the rest of the royal knights were all there..\n" \
                     "There was lightning, darkness. It blanketed the sky; low and heavy causing a sense of confusion" \
                     "\nYou turn to your left to see your comrades yelling and tearing at their heads..\n" \
                     "As they glance up you see a glow of deep red, shining from the slits of their helmets\n" \
                     "You tried to scream but fear restrained your voice,\n" \
                     "And then nothing..\n"

        part_four = "As you bring yourself back to the cell, to the present, you feel your heart beat speed up, " \
                    "as the feeling of entrapment sets in.. " \
                    "but not for long\n" \
                    "The metal door of the cell creaks open, revealing a clear stone path to the hall where the " \
                    "shadow walked\n" \
                    "You lift yourself to your feet from the cobblestone floor and contemplate your options\n" \
                    "The curiosity twists in your gut and pulls you north..\n" \
                    "You are now following the shadowy figure north down the dungeon hall...\n"

        part_five = "As you approach the end of the hall, you feel a stronger wind against your skin\n" \
                    "At the end of the hall, the room opens to a small room, arched doorways to your north and east\n" \
                    "Another chill propagates along your spine, as you make your choice...\n\n\n"

        part_six = "Hints:\n" \
                   "- To fight the final boss, you need to beat both the sub-bosses first.\n" \
                   "- We recommend to be at least level 2 and equipped with items before attemping the sub-bosses.\n" \
                   "- Dying sets you back so be mindful of your HP, there are ways to heal in this game.\n" \
                   "- Even though some monsters are higher level than you, there is a chance to beat them!\n" \
                   "- Have fun!\n\n"

        Helpers.print_in_color("**CLANK**\n", "cyan")
        time.sleep(3)
        Helpers.print_in_color(part_one, "cyan")
        time.sleep(4)
        Helpers.print_in_color(part_two, "cyan")
        time.sleep(4)
        Helpers.print_in_color(part_three, "cyan")
        time.sleep(4)
        Helpers.print_in_color(part_four, "cyan")
        time.sleep(4)
        Helpers.print_in_color(part_five, "cyan")
        time.sleep(4)
        Helpers.print_in_color(part_six, "purple")
        time.sleep(4)

    # Game finished dialog ---------------------------------------------------------------------------------------------
    @staticmethod
    def game_completed() -> None:
        """
        Print final dialogs and ascii art indicating the game is completed.

        :postcondition: prints final dialogs and ascii art indicating the game is completed
        """

        Helpers.print_in_color("...\n", "cyan")
        time.sleep(2)
        print("H-How is this possible...how can a mortal like you defeat me,")
        Helpers.print_in_color("\nThe King collapsed to the ground. You did it, You finally defeated him!\n"
                               "His body turns into a golden dust as the flame of humanity returned to the golden alter"
                               " sitting behind the throne.\n", "cyan")
        time.sleep(5)
        Helpers.print_in_color("It's finally over, the flame is finally back to where it should be...\n"
                               "You collapsed to the ground in exhaustion...this is the start of a new era...\n",
                               "cyan")
        time.sleep(6)
        Helpers.print_in_color("""

                                          _A_
                                         / | \ 
                                        |.-=-.|
                                        )\_|_/(
                                     .=='\   /`==.
                                   .'\   (`:')   /`.
                                 _/_ |_.-' : `-._|__\_
                                <___>'\    :   / `<___>
                                /  /   >=======<  /  /
                              _/ .'   /  ,-:-.  \/=,'
                             / _/    |__/v^v^v\__) \ 
                             \(\)     |V^V^V^V^V|\_/
                              (\ \    \`---|---'/
                                \ \    \-._|_,-/
                                 \ \    |__|__|
                                  \ \  <___X___>
                                   \ \  \..|../
                                    \ \  \ | /
                                     \ \ /V|V\ 
                                      \|/  |  \ 
                                       '--' `--`   by hjw
                              ______               _   _                                                             
                             |  ____|             | | | |                                                            
                             | |__     _ __     __| | | |                                                            
                             |  __|   | '_ \   / _` | | |                                                            
                             | |____  | | | | | (_| | |_|                                                            
                             |______| |_| |_|  \__,_| (_)                                                            
                                \U0001F389 You won the game! \U0001F389 	                                                    
                               \U0001F970 Thanks for playing! \U0001F970 	 	                                                    
        """, "cyan")