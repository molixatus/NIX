import curses
from curses import wrapper
buttonPos = 0
p = 4
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to NIX game!", curses.color_pair(1))
    stdscr.addstr("\nPress any key to begin!", curses.color_pair(2))
    stdscr.getkey()
    stdscr.refresh()

def keypos(stdscr):
    stdscr.clear()
    if buttonPos == 0:
        cplist = [2,1,1]
    elif buttonPos == 1:
        cplist = [1,2,1]
    elif buttonPos == 2:
        cplist = [1,1,2]
    stdscr.addstr('button 1', curses.color_pair(cplist[0]))
    stdscr.addstr("\n" + 'button 2', curses.color_pair(cplist[1]))
    stdscr.addstr("\n" + 'button 3', curses.color_pair(cplist[2]))
    stdscr.refresh()

def get_key(stdscr):
    global buttonPos
    Key = stdscr.getkey()
    if Key == 's':
        if buttonPos == 2:
            return
        else:
            buttonPos = buttonPos + 1

    elif Key == 'w':
        if buttonPos == 0:
            return
        else:
          buttonPos = buttonPos - 1

def main(stdscr):
    curses.initscr()
    curses.start_color()
    curses.init_color(curses.COLOR_RED, 23, 0, 74);
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_RED)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_WHITE)
    start_screen(stdscr)
    screen = curses.initscr()
    screen.clear()

    while True:
            keypos(stdscr)
            get_key(stdscr)

wrapper(main)