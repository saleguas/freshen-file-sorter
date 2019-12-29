import modules
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument(
    '-t', '--type', help='Probably the most useful sort. Sorts files based on filegroups. For example, .txt and .docx would be moved to the Documents folder.')
parser.add_argument('-d', '--date', help='Sorts files by the date they were created.',
                    metavar=('PATH', 'PRECISION'), nargs=2)
parser.add_argument('-a', '--alphabetically', help='Sorts files by the first n letters.',
                    metavar=('PATH', 'PRECISION'), nargs=2)
parser.add_argument('-e', '--extension',
                    help='Sorts files purely by extension.')
parser.add_argument(
    '-x', '--extract', help='Uproots ALL files in sub directories to current directory. Be careful, this will clear out any and all subfolders')

args = vars(parser.parse_args())
print(args)

if args['extract']:
    modules.extract(args['extract'], args['extract'])
if args['date']:
    modules.sortByDate(args['date'][1], args['date'][0])
if args['alphabetically']:
    modules.sortAlphabetically(os.getcwd(), int(args['alphabetically'][0]))
if args['extension']:
    modules.sortByExtension(args['extension'])
if args['type']:
    modules.sortbyType(args['type'])
