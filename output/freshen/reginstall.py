import os
import sys


def install():
    from context_menu import menus

    pyLoc = sys.executable  # .replace('python.exe', 'pythonw.exe')
    scriptLoc = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'main.py') # Location of parser to be called
    menu = menus.ContextMenu('Sort Files', type='DIRECTORY_BACKGROUND')

    extractCommand = menus.ContextCommand('Extract Files', command=f'{pyLoc} {scriptLoc} -x')
    extensionCommand = menus.ContextCommand('Sort by Extension', command=f'{pyLoc} {scriptLoc} -e')
    typeCommand = menus.ContextCommand('Sort by Type', command=f'{pyLoc} {scriptLoc} -t')

    dateMenu = menus.ContextMenu('Sort By Date')
    dateMenu.add_items([
        menus.ContextCommand('Day', command=f'{pyLoc} {scriptLoc} -d D'),
        menus.ContextCommand('Month', command=f'{pyLoc} {scriptLoc} -d M'),
        menus.ContextCommand('Year', command=f'{pyLoc} {scriptLoc} -d Y')

    ])

    menu.add_items([
        extractCommand,
        extensionCommand,
        typeCommand,
        dateMenu
    ])

    menu.compile()

if __name__ == '__main__':
    install()





# if __name__ == "__main__":
#     if is_admin():
#         install()
#     else:
#         ctypes.windll.shell32.ShellExecuteW(
#             None, "runas", sys.executable, __file__, None, 1)
#
