import argparse
import os
import ctypes
import sys

sys.path.append(os.path.abspath('.'))
import reginstall

def main():
    parser = argparse.ArgumentParser()
    config = parser.add_argument_group(
        "Configuration Commands", "Commands to manage the registry/installing/uninstalling etc.")
    config.add_argument(
        '-i', '--install', help='Installs the program to the registry. Adds option to context menu', action='store_true')
    config.add_argument('-u', '--uninstall',
                        help='Removes the program from the registry and the context menu.', action='store_true')
    args = vars(parser.parse_args())
    print(args)

    if args['install']:
        reginstall.install()

    if args['uninstall']:
        reginstall.uninstall()
