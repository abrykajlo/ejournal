from copy import copy
from argparse import ArgumentParser
import datetime
import os
import shutil

arg_parser = ArgumentParser()
arg_parser.add_argument('-f', '--file', dest='filepath', required=True, help='PDF file path to use as template.')
arg_parser.add_argument('-d', '--dir', dest='dirpath', required=True, help='Output directory.')
subparsers = arg_parser.add_subparsers(dest='command')
date_subparser = subparsers.add_parser('date') 
date_subparser.add_argument('date', help='Date to use for file naming.')
range_subparser = subparsers.add_parser('range')
range_subparser.add_argument('--start', dest='start', required=True, help='Start date to use for range of files.')
range_subparser.add_argument('--end', dest='end', required=True, help='End date to use for range of files.')

args = arg_parser.parse_args()

def save_pdf_with_date(filepath, dirpath, date: datetime.date):
    output_filepath = os.path.join(dirpath, f'{date.year}_{date.month:02}_{date.day:02}.pdf')
    shutil.copyfile(filepath, output_filepath)
    print(f'Wrote out file {output_filepath}')

match args.command:
    case 'date':
        date = datetime.date.fromisoformat(args.date)
        save_pdf_with_date(args.filepath, args.dirpath, date)
    case 'range':
        start = datetime.date.fromisoformat(args.start)
        end = datetime.date.fromisoformat(args.end)
        delta: datetime.timedelta = end - start
        if delta.days <= 0:
            print('The end date must be after the start date.')
            exit()
        for day in range(delta.days):
            date = start + datetime.timedelta(days=day)
            save_pdf_with_date(args.filepath, args.dirpath, date)