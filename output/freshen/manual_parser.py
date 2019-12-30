import argparse
import os
import ctypes
import sys

def main():
    parser = argparse.ArgumentParser()
    organizers = parser.add_argument_group(
        'Organizer Commands', 'Commands that manage files')
    organizers.add_argument(
        '-t', '--type', help='Probably the most useful sort. Sorts files based on filegroups. For example, .txt and .docx would be moved to the Documents folder.')
    organizers.add_argument('-d', '--date', help='Sorts files by the date they were created.',
                            metavar=('PATH', 'PRECISION'), nargs=2)
    organizers.add_argument('-e', '--extension',
                            help='Sorts files purely by extension.')
    organizers.add_argument(
        '-x', '--extract', help='Uproots ALL files in sub directories to current directory. Be careful, this will clear out any and all subfolders')
    config = parser.add_argument_group(
        "Configuration Commands", "Commands to manage the registry/installing/uninstalling etc.")
    config.add_argument(
        '-i', '--install', help='Installs the program to the registry. Adds option to context menu', action='store_true')
    config.add_argument('-u', '--uninstall',
                        help='Removes the program from the registry and the context menu. *Not implemented yet*', action='store_true')
    args = vars(parser.parse_args())

    try:
        if args['install']:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, os.path.join(
                __file__, '..', 'reginstall.py'), None, 1)
        if args['extract']:
            modules.extract(args['extract'], args['extract'])
        if args['date']:
            modules.sortByDate(args['date'][1], args['date'][0])
        if args['extension']:
            modules.sortByExtension(args['extension'])
        if args['type']:
            modules.sortbyType(args['type'])
    except Exception as e:
        print(e)
        input()
