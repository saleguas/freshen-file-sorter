import os
from context_menu import windows_menus

def uninstall():
    windows_menus.delete_key(os.path.join(windows_menus.context_registry_format('DIRECTORY_BACKGROUND'), 'Sort Files'))


if __name__ == "__main__":
    uninstall()
