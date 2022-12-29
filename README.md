# Reign of Fire

```angular2html
 _______  _______ _________ _______  _          _______  _______    _______ _________ _______  _______
(  ____ )(  ____ \__   __/(  ____ \( (    /|  (  ___  )(  ____ \  (  ____ \__   __/(  ____ )(  ____  \
| (    )|| (    \/   ) (   | (    \/|  \  ( |  | (   ) || (    \/  | (    \/   ) (   | (    )|| (    \/
| (____)|| (__       | |   | |      |   \ | |  | |   | || (__      | (__       | |   | (____)|| (__
|     __)|  __)      | |   | | ____ | (\ \) |  | |   | ||  __)     |  __)      | |   |     __)|  __)
| (\ (   | (         | |   | | \_  )| | \   |  | |   | || (        | (         | |   | (\ (   | (
| ) \ \__| (____/\___) (___| (___) || )  \  |  | (___) || )        | )      ___) (___| ) \ \__| (____/\
|/   \__/(_______/\_______/(_______)|/    )_)  (_______)|/         |/       \_______/|/   \__/(_______/
```

## Game Description
We have created a text based adventure game called 'Reign of Fire'. This game takes place in the dungeon of a 
medieval castle based in the 14th century. Your goal is to defeat the God Kind Thompson and rekindle the fire of 
humanity. We wish you the best of luck on your quest!

## Game details
- The game includes a variety of challenges, from enemy battles, to riddles, to room roadblocks
- In order to complete the game and defeat the king, you must first defeat both of his royal subordinates, indicated 
  on the map by red X's
- The kings royal subordinates each possess a powerful relic that you must acquire before facing the God King Thompson
- If you die during your quest, you will not lose any items or abilities you have gained, but you will be returned to 
  level 1, and you must restart from position (1, 1)

## Game map
##### Legend
  - |#| - Your character
  - |?| - Unvisited location
  - | | - Visited location
  - |X| - Mini boss
  - |👑| - Final boss

##### Map
```
---------------------------|👑|
|?||?||?||?||?||?||?||?||?||?|
|?||?||?||?||?||?||?||?||?||?|
|?||?||?||?||?||?||?||?||?||?|
|?||?||?||?||?||?||X||?||?||?|
|?||?||?||?||?||?||?||?||?||?|
|?||?||?||?||?||?||?||?||?||?|
|?||?||?||X||?||?||?||?||?||?|
|?||?||?||?||?||?||?||?||?||?|
|?||?||?||?||?||?||?||?||?||?|
|#||?||?||?||?||?||?||?||?||?|
| |---------------------------
```

## How to install and play

### 1. Install git on your computer
If you don't already have git installed on your computer, then go to:

```https://git-scm.com/book/en/v2/Getting-Started-Installing-Git``` 

to install it. 

Please ensure that you have added git to your devices PATH variable in order to execute git commands in the terminal.

### 2. Install python3 to your computer
If you don't already have a version of python3, then install it via the microsoft store on windows or via the python 
website: 

```https://www.python.org/downloads/```

Please select the `Add python 3.x.x to path` option at the bottom of the python installer window.

### 3. Clone the game to your local computer
Choose any directory on your device and then open it in the terminal. Once there copy the following 
command and hit enter to clone the game code to your local computer:

```git clone https://github.com/Langelozzi/reign-of-fire.git```

### 4. Navigate into the reign-of-fire
You can choose to use finder or file explorer to do this, or by executing the command:

```cd reign-of-fire```

### 5. Run the game
Finally, open up a terminal window inside of the reign-of-fire directory and execute:

Windows: `python game.py`

Linux/MacOS: `python3 game.py`

## Developers:
* Lucas Angelozzi
  * https://github.com/Langelozzi
  * https://www.linkedin.com/in/lucas-angelozzi/
* Amir Eskandari

