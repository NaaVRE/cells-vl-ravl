
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--names', action='store', type=str, required=True, dest='names')

arg_parser.add_argument('--param_number', action='store', type=int, required=True, dest='param_number')

args = arg_parser.parse_args()
print(args)

id = args.id

names = json.loads(args.names)

param_number = args.param_number


for name in names:
    print(f"Hello, {name}!")
print(param_number)

