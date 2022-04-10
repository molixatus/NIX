import ctypes,os,sys,curses
from os import system
from curses import wrapper
buttonPos = 0
menulevel = 0
menulevelmax = 1
system('title NIX')
#waho
def start_screen(stdscr):
    stdscr.addstr(20,10, "Welcome to NIX game!   ", curses.color_pair(2))
    stdscr.addstr(21,10, "Press any key to begin!", curses.color_pair(2))
    stdscr.getkey()
    stdscr.clear()

def menuPos(stdscr, b0, b1, b2, b3, b4, b5, b6, b7, b8, b9):

    stdscr.addstr(20, 10, b0.replace('#', ' '), curses.color_pair(1))
    stdscr.addstr(21, 10, b1.replace('#', ' '), curses.color_pair(1))
    stdscr.addstr(22, 10, b2.replace('#', ' '), curses.color_pair(1))

    if buttonPos == 0:
        stdscr.addstr(20, 10, b0.replace('#', ' '), curses.color_pair(2))
    elif buttonPos == 1:
        stdscr.addstr(21, 10, b1.replace('#', ' '), curses.color_pair(2))
    elif buttonPos == 2:
        stdscr.addstr(22, 10, b2.replace('#', ' '), curses.color_pair(2))

    stdscr.refresh()

def get_key(stdscr,k1,k2,k3):
    global buttonPos
    global menulevel
    k1 = k1.split(':')
    k2 = k2.split(':')
    k3 = k3.split(':')
    Key = stdscr.getkey()
    ###                                     W Key
    if Key.lower() == k1[0] or Key == k1[1]:
        if buttonPos == 2:
            pass
        else:
            buttonPos = buttonPos + 1
    ###                                     S Key
    elif Key.lower() == k2[0] or Key == k2[1]:
        if buttonPos == 0:
            pass
        else:
            buttonPos = buttonPos - 1
    ###                                     Space
    elif Key == k3[0] or Key == k3[1]:
        if menulevel == 0:
            if buttonPos == 0:
                menulevel = menulevel + 1
                buttonPos = 0
                stdscr.clear()###############################################
            elif buttonPos == 2:
                os._exit(1)
                raise SystemExit
                quit()
                sys.exit()
                exit()
        elif menulevel == 1:
            if buttonPos == 2:
                menulevel = menulevel - 1
                buttonPos = 0

def main(stdscr):
    global menulevel
    curses.curs_set(0)
    curses.initscr()
    curses.start_color()
    curses.init_color(curses.COLOR_GREEN, 46, 48, 55);
    curses.init_color(curses.COLOR_WHITE, 235, 229, 206);
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_GREEN)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_WHITE)
    stdscr.bkgd(' ', curses.color_pair(1))
    start_screen(stdscr)
    sys.stdout.write("\x1b]2;%s\x07" % 'teststst')

    while True:

            while menulevel == 0:
                menuPos(stdscr, 'Play Game#######', 'Settings########', 'Exit############','','','','','','','')
                get_key(stdscr,'s:KEY_DOWN','w:KEY_UP',' :\n')
                
            while menulevel == 1:

                #stdscr.refresh()
                #Key = stdscr.getkey()
                #stdscr.addstr(15, 10, '              ', curses.color_pair(1))
                #stdscr.addstr(15, 10, Key, curses.color_pair(1))

                menuPos(stdscr, 'Play Local######', 'Play Online#####', 'Back############','','','','','','','')
                get_key(stdscr,'s:KEY_DOWN','w:KEY_UP',' :\n')

wrapper(main)













