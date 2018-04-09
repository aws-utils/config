import argparse
import json

from configgen.operation import Operation
from configgen.defaults import createDefaults

parser = argparse.ArgumentParser()
parser.add_argument("config")
args = parser.parse_args()

config = json.load(open(args.config))
print config

operations = []
for op in config["operations"]:
    operations.append(Operation(op))

for op in operations:
    print op.name

defaults = createDefaults(config["defaults"])
print defaults
print defaults['lambda']