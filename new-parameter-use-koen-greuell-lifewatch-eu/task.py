
import argparse
import json
import os
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_aa_string', action='store', type=str, required=True, dest='param_aa_string')

args = arg_parser.parse_args()
print(args)

id = args.id


param_aa_string = args.param_aa_string.replace('"','')


print(param_aa_string)

