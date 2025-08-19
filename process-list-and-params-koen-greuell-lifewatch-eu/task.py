
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--names', action='store', type=str, required=True, dest='names')

arg_parser.add_argument('--param_a_string', action='store', type=str, required=True, dest='param_a_string')
arg_parser.add_argument('--param_z_string', action='store', type=str, required=True, dest='param_z_string')

args = arg_parser.parse_args()
print(args)

id = args.id

names = json.loads(args.names)

param_a_string = args.param_a_string.replace('"','')
param_z_string = args.param_z_string.replace('"','')


for name in names:
    print(f"Hello, {name}!")
print(param_z_string)
print(param_a_string)

