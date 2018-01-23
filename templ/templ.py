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

resource_package = __name__

from .request import Request
from .warn import warn

# initialize request formatting dict
d = datetime.datetime.now()
auto_dict = Request({
    'cur-second' : d.second,
    'cur-minute' : d.minute,
    'cur-hour' : d.hour,
    'cur-day' : d.day,
    'cur-month' : d.month,
    'cur-year' : d.year,
    'recent-mon-day' : (d - datetime.timedelta(days=d.weekday())).day,
    'recent-mon-month' : (d - datetime.timedelta(days=d.weekday())).month,
    'recent-mon-year' : (d - datetime.timedelta(days=d.weekday())).year,
    'cur-author' : 'Your Name Here',
    'cur-author-email' : 'Your Email Here',
    'cur-author-phone' : 'Your Phone Here',
    'cur-author-website' : 'Your Web Address Here'
    })


# parse arguments
def parse_args(arguments):
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    # argument given describes the type of entry for the day
    entry_type_default = 'null'
    parser.add_argument('entry_type', help="Entry type", type=str, default=entry_type_default)

    # argument given describes whether the full path (vs. the relative path) should be returned
    parser.add_argument('--full-path', action='store_true', default=False, dest="full_path", help="Full path flag")

    # argument given describes whether all
    parser.add_argument('-m', "--manual-fill", action='store_true', default=False, dest="manual_fill", help="Flag to prevent automatic fill-in of template fields")

    args = parser.parse_args()

    # warn user if using default arguments
    if args.entry_type == entry_type_default:
        warn("warn: using default entry type " + entry_type_default + "'\n'")

    return args

def read_yaml(args):
    # attempt to read template file into data object entry_type_data
    # on failure, entry_type_data takes value None
    entry_type_data = None
    template_filename = "templates/" + args.entry_type + ".yaml"
    template_path = pkg_resources.resource_filename(
        'templ',
        template_filename)
    # check for existence then open and parse YAML

    if os.path.isfile(template_path):
         with open( template_path, 'r') as stream:
            entry_type_data = yaml.load(stream)

    else:
        print(template_path)
        warn("warn: no template file found for entry type " + args.entry_type + "'\n'")

    return entry_type_data

def gen_entry_filename(args, format_dict, entry_type_data):

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

    # if full path requested, prepend current directory path
    if args.full_path:
        entry_filename = os.path.join(os.getcwd(), entry_filename)

    return entry_filename


def main():
    args = parse_args(sys.argv[1:])

    format_dict = Request() if args.manual_fill else auto_dict

    entry_type_data = read_yaml(args)

    append = (
        entry_type_data['append'].format_map(format_dict)
        if entry_type_data and 'append' in entry_type_data
        else None
        )

    template = (
        entry_type_data['template'].format_map(format_dict)
        if entry_type_data and 'template' in entry_type_data
        else None
        )

    entry_filename = gen_entry_filename(args, format_dict, entry_type_data)

    # if entry file doesn't exist, initialize with content template
    # if content template is described in template YAML file
    # initialize the entry only if content template was described
    if template and not os.path.isfile(entry_filename) and not os.path.isdir(entry_filename):

        # make directory if it doesn't already exist
        if os.path.dirname(entry_filename):
            os.makedirs(os.path.dirname(entry_filename), exist_ok=True)

        # write the content template
        with open(entry_filename, "a+") as f:
            f.write(template.format_map(format_dict))


    # append the entry only if content template was described
    elif append and not os.path.isdir(entry_filename):

        # write the content template
        with open(entry_filename, "a+") as f:
            f.write(append.format_map(format_dict))


    # write filename to stdout to allow for nesting of this script
    # into other bash commands
    sys.stdout.write(entry_filename)
