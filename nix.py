import ctypes,os,sys,curses,time
from os import system
from curses import wrapper
system('title NIX')
buttonPos = 0
buttonPosMax = 0
menulevel = 0
menulevelmax = 1
buttonfunctionlist = []

def menuPos(stdscr,b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,bamm):
    global buttonfunctionlist
    global buttonPosMax
    buttonPosMax = bamm - 1
    buttontextlist = b0,b1,b2,b3,b4,b5,b6,b7,b8,b9

###_______________________________________________________
###_UPDATE BUTTON FUNCTION LIST BASED ON CURRENT MENU'S BUTTONS
###-------------------------------------------------------

    for i in range(bamm):
        getfunction = (buttontextlist[i].replace('#', ' ').split(' '))
        getfunction = str(getfunction[0]).lower()
        buttonfunctionlist.append(getfunction)

###_______________________________________________________
###_PRINT ALL MENU BUTTONS ---- AND HILIGHT CURRENT BUTTON
###-------------------------------------------------------

    for i in range(bamm):
        buttontext = buttontextlist[i]
        stdscr.addstr(20+i, 10, buttontext.replace('#', ' '), curses.color_pair(1))
        if buttonPos == i:
            stdscr.addstr(20+i, 10, buttontext.replace('#', ' '), curses.color_pair(2))

    stdscr.refresh()

def ButtonFunction(stdscr):
    global buttonPos
    global buttonPosMax
    global menulevel
    global buttonfunctionlist
    Key = stdscr.getkey()
    ###_______________________________________________________
    ###_                                    FUNCTION FOR W KEY
    ###-------------------------------------------------------
    if Key.lower() == 'w' or Key == 'KEY_UP':
        if buttonPos == 0:
            pass
        else:
            buttonPos = buttonPos - 1
    ###_______________________________________________________
    ###_                                    FUNCTION FOR S KEY
    ###-------------------------------------------------------
    elif Key.lower() == 's' or Key == 'KEY_DOWN':
        if buttonPos == buttonPosMax:
            pass
        else:
            buttonPos = buttonPos + 1
    ###_______________________________________________________
    ###_                      WIP FUNCTION FOR ENTER/SPACE KEY
    ###-------------------------------------------------------
    if Key == ' ' or Key == '\n':
        if buttonfunctionlist[buttonPos] == 'play':
            buttonPos = 0
            stdscr.clear()
            menulevel = menulevel + 1

            stdscr.addstr(20, 10, 'play function has been pressed', curses.color_pair(1))
            stdscr.refresh()
            time.sleep(100)
        elif buttonfunctionlist[buttonPos] == 'back':
            buttonPos = 0
            stdscr.clear()
            menulevel = menulevel - 1

            stdscr.addstr(20, 10, 'back function has been pressed', curses.color_pair(1))
            stdscr.refresh()
            time.sleep(100)
        elif buttonfunctionlist[buttonPos] == 'exit':
            stdscr.clear()
            stdscr.addstr(20, 10, 'exit function has been pressed', curses.color_pair(1))
            stdscr.refresh()
            time.sleep(100)
            os._exit(1)
    ###_______________________________________________________
    ###_                          FUNCTION FOR ENTER/SPACE KEY
    ###-------------------------------------------------------
    #elif Key == ' ' or Key == '\n':
    #    if menulevel == 0:
    #        if buttonPos == 0:
    #            menulevel = menulevel + 1
    #            buttonPos = 0
    #            stdscr.clear()
    #        elif buttonPos == 2:
    #            os._exit(1)
    #    elif menulevel == 1:
    #        if buttonPos == 2:
    #            menulevel = menulevel - 1
    #            buttonPos = 0
    #            stdscr.clear()

def main(stdscr):
    global menulevel
    ###_______________________________________________________
    ###_ DISABLE CURSOR, INIT SCREEN, SETUP COLORPAIRS, SET BGD COLOR
    ###-------------------------------------------------------
    curses.curs_set(0)
    curses.initscr()
    curses.start_color()
    curses.init_color(curses.COLOR_GREEN, 40, 60, 60);
    curses.init_color(curses.COLOR_WHITE, 235, 229, 206);
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_GREEN)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_WHITE)
    stdscr.bkgd(' ', curses.color_pair(1))
    ###_______________________________________________________
    ###_                                INIT GAME START SCREEN
    ###-------------------------------------------------------
    stdscr.addstr(20, 10, "Welcome to NIX game!   ", curses.color_pair(2))
    stdscr.addstr(21, 10, "Press any key to begin!", curses.color_pair(2))
    stdscr.getkey()
    stdscr.clear()

    while True:

            while menulevel == 0:
                menuPos(stdscr, 'Play Game#######', 'Settings########', 'Exit############','','','','','','','',3)
                ButtonFunction(stdscr)

            while menulevel == 1:
                menuPos(stdscr, 'Local Game######', 'Online Game#####', 'Back############','','','','','','','',3)
                ButtonFunction(stdscr)

                #for i in range(5):
                #    stdscr.addstr(20+i, 10, buttonfunctionlist[i], curses.color_pair(1))
                #    stdscr.refresh()

wrapper(main)













