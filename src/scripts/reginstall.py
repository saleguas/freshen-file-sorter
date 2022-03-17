import os
import sys

sys.path.append(os.path.abspath('.'))


def install():
    from context_menu import menus
    import modules

    pyLoc = sys.executable  # .replace('python.exe', 'pythonw.exe')
    scriptLoc = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'main.py') # Location of parser to be called
    menu = menus.ContextMenu('Sort Files', type='DIRECTORY_BACKGROUND')

    extractCommand = menus.ContextCommand('Uproot All Files', python=modules.handleExtract)
    extensionCommand = menus.ContextCommand('Sort by Extension', python=modules.handleExtension)
    typeCommand = menus.ContextCommand('Sort by Type', python=modules.handleType)

    dateMenu = menus.ContextMenu('Sort By Date')
    dateMenu.add_items([
        menus.ContextCommand('Day', python=modules.handleDate, params='D'),
        menus.ContextCommand('Month', python=modules.handleDate, params='M'),
        menus.ContextCommand('Year', python=modules.handleDate, params='Y')

    ])

    menu.add_items([
        extractCommand,
        extensionCommand,
        typeCommand,
        dateMenu
    ])

    menu.compile()


def uninstall():
    from context_menu import menus

    menus.removeMenu('Sort Files', 'DIRECTORY_BACKGROUND')


install()
