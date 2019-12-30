import modules
import argparse
import os


# This file should not be called by the user. The registry uses this file.
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t', '--type', help='Probably the most useful sort. Sorts files based on filegroups. For example, .txt and .docx would be moved to the Documents folder.', action='store_true')
    parser.add_argument('-d', '--date', help='Sorts files by the date they were created.',
                        metavar=('PRECISION'), nargs=1)
    parser.add_argument('-a', '--alphabetically', help='Sorts files by the first n letters.',
                        metavar=('PRECISION'), nargs=1)
    parser.add_argument('-e', '--extension',
                        help='Sorts files purely by extension.', action='store_true')
    parser.add_argument(
        '-x', '--extract', help='Uproots ALL files in sub directories to current directory. Be careful, this will clear out any and all subfolders', action='store_true')

    args = vars(parser.parse_args())

    try:
        if args['extract']:
            modules.extract(os.getcwd(), os.getcwd())
        if args['date']:
            modules.sortByDate(os.getcwd(), args['date'][0])
        if args['alphabetically']:
            modules.sortAlphabetically(os.getcwd(), int(args['alphabetically'][0]))
        if args['extension']:
            modules.sortByExtension(os.getcwd())
        if args['type']:
            modules.sortbyType(os.getcwd())
    except Exception as e:
        print(e)
        input()
