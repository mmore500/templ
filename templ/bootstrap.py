# -*- coding: utf-8 -*-


"""A script to initialize journal entries using a templating system.
Multiple entry types are supported.
Entry types are defined using YAML files.
The entry type code should be provided as a command line argument.
Otherwise, the default value null is used.
The script sends the file name of the initialized file to stdout.

"""




import sys
import datetime
import os
import yaml
import argparse
import pkg_resources

resource_package = __name__ # Could be any module/package name

from .request import Request
from .warn import warn

# initialize
d = datetime.date.today()
format_dict = Request({
    'cur-day' : d.day,
    'cur-month' : d.month,
    'cur-year' : d.year,
    'cur-author' : 'Matthew Moreno'
    })


# parse arguments
def parse_args(arguments):
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    # argument given describes the type of entry for the day
    entry_type_default = 'null'
    parser.add_argument('entry_type', help="Entry type", type=str, default=entry_type_default)

    args = parser.parse_args()

    # warn user if using default arguments
    if args.entry_type == entry_type_default:
        warn("warn: using default entry type " + entry_type_default + "\n")

    return args

def read_yaml(args):
    # attempt to read template file into data object entry_type_data
    # on failure, entry_type_data takes value None
    entry_type_data = None
    template_filename = args.entry_type + ".yaml"
    templates_path = pkg_resources(
        '/'.join(('templates', template_filename)),
        template_filename)
    # check for existence then open and parse YAML
    if os.path.isfile(templates_path):
         with open( template_filename, 'r') as stream:
            entry_type_data = yaml.load(stream)
    else:
        warn("warn: no template file found for entry type " + args.entry_type + "\n")

    return entry_type_data

def gen_entry_filename(args, entry_type_data):

    # generate filename for entry
    default_entry_filename = (
        args.entry_type
        + ".md"
        )
    # if template YAML file describes a filename for the entry then use it,
    # otherwise use default
    # either way, format the entry filename with format_dict
    entry_filename = (
        entry_type_data['filename']
        if entry_type_data and 'filename' in entry_type_data
        else default_entry_filename
        ).format_map(format_dict)

    return entry_filename


def main():
    args = parse_args(arguments)

    entry_type_data = read_yaml(args)

    entry_filename = gen_entry_filename(args, entry_type_data)

    # if entry file doesn't exist, initialize with content template
    # if content template is described in template YAML file
    if not os.path.isfile(entry_filename):
        template = (
            entry_type_data['template'].format_map(format_dict)
            if entry_type_data and 'template' in entry_type_data
            else None
            )
        # initialize the entry only if content template was described
        if template:
            with open(entry_filename, "a") as f:
                f.write(template.format_map(format_dict))

    # write filename to stdout to allow for nesting of this script
    # into other bash commands
    sys.stdout.write(entry_filename)


class Boo(Stuff):
    pass
