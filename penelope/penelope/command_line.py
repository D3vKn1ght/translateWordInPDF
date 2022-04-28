#!/usr/bin/env python
# coding=utf-8

"""
This file contains command line constants and functions.
"""

from __future__ import absolute_import
import datetime
import sys

from penelope.utilities import get_uuid
from penelope.utilities import print_error

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2012-2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__version__ = "3.1.3"
__email__ = "alberto@albertopettarin.it"
__status__ = "Production"

INPUT_FORMATS = [
    "bookeen",
    "csv",
    "kobo",
    "stardict",
    "xml"
]

OUTPUT_FORMATS = [
    "bookeen",
    "csv",
    "epub",
    "kobo",
    "mobi",
    "stardict",
    "xml"
]

COMMAND_LINE_PARAMETERS = [
    {
        "short": "-d",
        "long": "--debug",
        "help": "enable debug mode (default: False)",
        "action": "store_true"
    },
    {
        "short": "-f",
        "long": "--language-from",
        "help": "from language (ISO 639-1 code)",
        "action": "store"
    },
    {
        "short": "-i",
        "long": "--input-file",
        "help": "input file name prefix(es). Multiple prefixes must be comma-separated.",
        "action": "store"
    },
    {
        "short": "-j",
        "long": "--input-format",
        "help": "from format (values: %s)" % "|".join(INPUT_FORMATS),
        "action": "store"
    },
    {
        "short": "-k",
        "long": "--keep",
        "help": "keep temporary files (default: False)",
        "action": "store_true"
    },
    {
        "short": "-o",
        "long": "--output-file",
        "help": "output file name",
        "action": "store"
    },
    {
        "short": "-p",
        "long": "--output-format",
        "help": "to format (values: %s)" % "|".join(OUTPUT_FORMATS),
        "action": "store"
    },
    {
        "short": "-t",
        "long": "--language-to",
        "help": "to language (ISO 639-1 code)",
        "action": "store"
    },
    {
        "short": "-v",
        "long": "--version",
        "help": "print version and exit",
        "action": "store_true"
    },

    {
        "short": None,
        "long": "--author",
        "help": "author string",
        "action": "store"
    },
    {
        "short": None,
        "long": "--copyright",
        "help": "copyright string",
        "action": "store"
    },
    {
        "short": None,
        "long": "--cover-path",
        "help": "path of the cover image file",
        "action": "store"
    },
    {
        "short": None,
        "long": "--description",
        "help": "description string",
        "action": "store"
    },
    {
        "short": None,
        "long": "--email",
        "help": "email string",
        "action": "store"
    },
    {
        "short": None,
        "long": "--identifier",
        "help": "identifier string",
        "action": "store"
    },
    {
        "short": None,
        "long": "--license",
        "help": "license string",
        "action": "store"
    },
    {
        "short": None,
        "long": "--title",
        "help": "title string",
        "action": "store"
    },
    {
        "short": None,
        "long": "--website",
        "help": "website string",
        "action": "store"
    },
    {
        "short": None,
        "long": "--year",
        "help": "year string",
        "action": "store"
    },

    {
        "short": None,
        "long": "--apply-css",
        "help": "apply the given CSS file (epub and mobi output only)",
        "action": "store"
    },
    {
        "short": None,
        "long": "--bookeen-collation-function",
        "help": "use the specified collation function",
        "action": "store"
    },
    {
        "short": None,
        "long": "--bookeen-install-file",
        "help": "create *.install file (default: False)",
        "action": "store_true"
    },
    {
        "short": None,
        "long": "--csv-fs",
        "help": "CSV field separator (default: ',')",
        "action": "store"
    },
    {
        "short": None,
        "long": "--csv-ignore-first-line",
        "help": "ignore the first line of the input CSV file(s) (default: False)",
        "action": "store_true"
    },
    {
        "short": None,
        "long": "--csv-ls",
        "help": "CSV line separator (default: '\\n')",
        "action": "store"
    },
    {
        "short": None,
        "long": "--dictzip-path",
        "help": "path to dictzip executable",
        "action": "store"
    },
    {
        "short": None,
        "long": "--epub-no-compress",
        "help": "do not create the compressed container (epub output only, default: False)",
        "action": "store_true"
    },
    {
        "short": None,
        "long": "--escape-strings",
        "help": "escape HTML strings (default: False)",
        "action": "store_true"
    },
    {
        "short": None,
        "long": "--flatten-synonyms",
        "help": "flatten synonyms, creating a new entry with headword=synonym and using the definition of the original headword (default: False)",
        "action": "store_true"
    },
    {
        "short": None,
        "long": "--group-by-prefix-function",
        "help": "compute the prefix of headwords using the given prefix function file",
        "action": "store"
    },
    {
        "short": None,
        "long": "--group-by-prefix-length",
        "help": "group headwords by prefix of given length (default: 2)",
        "action": "store"
    },
    {
        "short": None,
        "long": "--group-by-prefix-merge-across-first",
        "help": "merge headword groups even when the first character changes (default: False)",
        "action": "store_true"
    },
    {
        "short": None,
        "long": "--group-by-prefix-merge-min-size",
        "help": "merge headword groups until the given minimum number of headwords is reached (default: 0, meaning no merge will take place)",
        "action": "store"
    },
    {
        "short": None,
        "long": "--ignore-case",
        "help": "ignore headword case, all headwords will be lowercased (default: False)",
        "action": "store_true"
    },
    {
        "short": None,
        "long": "--ignore-synonyms",
        "help": "ignore synonyms, not reading/writing them if present (default: False)",
        "action": "store_true"
    },
    {
        "short": None,
        "long": "--include-index-page",
        "help": "include an index page (epub and mobi output only, default: False)",
        "action": "store_true"
    },
    {
        "short": None,
        "long": "--input-file-encoding",
        "help": "use the specified encoding for reading the raw contents of input file(s) (default: 'utf-8')",
        "action": "store"
    },
    {
        "short": None,
        "long": "--input-parser",
        "help": "use the specified parser function after reading the raw contents of input file(s)",
        "action": "store"
    },
    {
        "short": None,
        "long": "--kindlegen-path",
        "help": "path to kindlegen executable",
        "action": "store"
    },
    {
        "short": None,
        "long": "--marisa-bin-path",
        "help": "path to MARISA bin directory",
        "action": "store"
    },
    {
        "short": None,
        "long": "--marisa-index-size",
        "help": "maximum size of the MARISA index (default: 1000000)",
        "action": "store"
    },
    {
        "short": None,
        "long": "--merge-definitions",
        "help": "merge definitions for the same headword (default: False)",
        "action": "store_true"
    },
    {
        "short": None,
        "long": "--merge-separator",
        "help": "add this string between merged definitions (default: ' | ')",
        "action": "store"
    },
    {
        "short": None,
        "long": "--mobi-no-kindlegen",
        "help": "do not run kindlegen, keep .opf and .html files (default: False)",
        "action": "store_true"
    },
    {
        "short": None,
        "long": "--no-definitions",
        "help": "do not output definitions for EPUB and MOBI formats (default: False)",
        "action": "store_true"
    },
    {
        "short": None,
        "long": "--sd-ignore-sametypesequence",
        "help": "ignore the value of sametypesequence in StarDict .ifo files (default: False)",
        "action": "store_true"
    },
    {
        "short": None,
        "long": "--sd-no-dictzip",
        "help": "do not compress the .dict file in StarDict files (default: False)",
        "action": "store_true"
    },
    {
        "short": None,
        "long": "--sort-after",
        "help": "sort after merging/flattening (default: False)",
        "action": "store_true"
    },
    {
        "short": None,
        "long": "--sort-before",
        "help": "sort before merging/flattening (default: False)",
        "action": "store_true"
    },
    {
        "short": None,
        "long": "--sort-by-definition",
        "help": "sort by definition (default: False)",
        "action": "store_true"
    },
    {
        "short": None,
        "long": "--sort-by-headword",
        "help": "sort by headword (default: False)",
        "action": "store_true"
    },
    {
        "short": None,
        "long": "--sort-ignore-case",
        "help": "ignore case when sorting (default: False)",
        "action": "store_true"
    },
    {
        "short": None,
        "long": "--sort-reverse",
        "help": "reverse the sort order (default: False)",
        "action": "store_true"
    },
]

REQUIRED_PARAMETERS = [
    "input_file",
    "input_format",
    "language_from",
    "language_to",
    "output_format",
    "output_file"
]

EXAMPLES = [
    # {
    #     "options": "-h",
    #     "description": "Print this message and exit"
    # },
    # {
    #     "options": "-v",
    #     "description": "Print the version and exit"
    # },
    {
        "options": "-i dict.csv -j csv -f en -t it -p stardict -o output.zip",
        "description": "Convert en->it dictionary dict.csv (in CSV format) into output.zip (in StarDict format)"
    },
    {
        "options": "-i dict.csv -j csv -f en -t it -p stardict -o output.zip --merge-definitions",
        "description": "As above, but also merge definitions"
    },
    {
        "options": "-i d1,d2,d3 -j csv -f en -t it -p csv -o output.csv --sort-after --sort-by-headword",
        "description": "Merge CSV dictionaries d1, d2, and d3 into output.csv, sorting by headword"
    },
    {
        "options": "-i d1,d2,d3 -j csv -f en -t it -p csv -o output.csv --sort-after --sort-by-headword --sort-ignore-case",
        "description": "As above, but ignore case for sorting"
    },
    {
        "options": "-i d1,d2,d3 -j csv -f en -t it -p csv -o output.csv --sort-after --sort-by-headword --sort-reverse",
        "description": "As above, but reverse the order"
    },
    {
        "options": "-i dict.zip -j stardict -f en -t it -p csv -o output.csv",
        "description": "Convert en->it dictionary dict.zip (in StarDict format) into output.csv (in CSV format)"
    },
    {
        "options": "-i dict.zip -j stardict -f en -t it -p csv -o output.csv --ignore-synonyms",
        "description": "As above, but do not read the .syn synonym file if present"
    },
    {
        "options": "-i dict.zip -j stardict -f en -t it -p csv -o output.csv --flatten-synonyms",
        "description": "As above, but flatten synonyms"
    },
    {
        "options": "-i dict.zip -j stardict -f en -t it -p bookeen -o output",
        "description": "Convert dict.zip into output.dict.idx and output.dict for Bookeen devices"
    },
    {
        "options": "-i dict.zip -j stardict -f en -t it -p kobo -o dicthtml-en-it",
        "description": "Convert dict.zip into dicthtml-en-it.zip for Kobo devices"
    },
    {
        "options": "-i dict.csv -j csv -f en -t it -p mobi -o output.mobi --cover-path mycover.png --title \"My English->Italian Dictionary\"",
        "description": "Convert dict.csv into a MOBI (Kindle) dictionary, using the specified cover image and title"
    },
    {
        "options": "-i dict.xml -j xml -f en -t it -p mobi -o output.epub",
        "description": "Convert dict.xml into an EPUB dictionary"
    },
    {
        "options": "-i dict.xml -j xml -f en -t it -p mobi -o output.epub --epub-output-definitions",
        "description": "As above, but also output definitions"
    },
]

USAGE = u"""
  $ penelope -h
  $ penelope -i INPUT_FILE -j INPUT_FORMAT -f LANGUAGE_FROM -t LANGUAGE_TO -p OUTPUT_FORMAT -o OUTPUT_FILE [OPTIONS]
  $ penelope -i IN1,IN2[,IN3...] -j INPUT_FORMAT -f LANGUAGE_FROM -t LANGUAGE_TO -p OUTPUT_FORMAT -o OUTPUT_FILE [OPTIONS]
"""

DESCRIPTION = u"""description:
  Convert dictionary file(s) with file name prefix INPUT_FILE from format INPUT_FORMAT to format OUTPUT_FORMAT, saving it as OUTPUT_FILE.
  The dictionary is from LANGUAGE_FROM to LANGUAGE_TO, possibly the same.
  You can merge several dictionaries (with the same format), by providing a list of comma-separated prefixes, as shown by the third synopsis above."""

EPILOG = u"examples:\n"
for example in EXAMPLES:
    EPILOG += u"\n"
    EPILOG += u"  $ penelope %s\n" % (example["options"])
    EPILOG += u"    %s\n" % (example["description"])
EPILOG += u"  \n"


def check_arguments(args):
    """
    Check that we have all the required command line arguments,
    and that the input/output format values are supported.
    """
    for required in REQUIRED_PARAMETERS:
        if required not in args:
            print_error("Argument '%s' is required" % required)
            sys.exit(2)
    if args.input_format not in INPUT_FORMATS:
        print_error("Format '%s' is not a valid input format" % args.input_format)
        print_error("Valid input formats: %s" % INPUT_FORMATS)
        sys.exit(4)
    if args.output_format not in OUTPUT_FORMATS:
        print_error("Format '%s' is not a valid output format" % args.output_format)
        print_error("Valid output formats: %s" % OUTPUT_FORMATS)
        sys.exit(4)


def set_default_values(args):
    def set_default_value(key, value):
        if not args.__contains__(key):
            args.__dict__[key] = value
    set_default_value("apply_css", None)
    set_default_value("bookeen_collation_function", None)
    set_default_value("bookeen_install_file", False)
    set_default_value("csv_fs", ",")
    set_default_value("csv_ignore_first_line", False)
    set_default_value("csv_ls", "\n")
    set_default_value("debug", False)
    set_default_value("dictzip_path", None)
    set_default_value("epub_no_compress", False)
    set_default_value("escape_strings", False)
    set_default_value("flatten_synonyms", False)
    set_default_value("group_by_prefix_length", 2)
    set_default_value("group_by_prefix_function", None)
    set_default_value("group_by_prefix_merge_across_first", False)
    set_default_value("group_by_prefix_merge_min_size", 0)
    set_default_value("ignore_case", False)
    set_default_value("ignore_synonyms", False)
    set_default_value("include_index_page", False)
    set_default_value("input_file_encoding", "utf-8")
    set_default_value("input_parser", None)
    set_default_value("keep", False)
    set_default_value("kindlegen_path", None)
    set_default_value("marisa_bin_path", None)
    set_default_value("marisa_index_size", 1000000)
    set_default_value("merge_definitions", False)
    set_default_value("merge_separator", " | ")
    set_default_value("mobi_no_kindlegen", False)
    set_default_value("no_definitions", False)
    set_default_value("sd_ignore_sametypesequence", False)
    set_default_value("sd_no_dictzip", False)
    set_default_value("sort_after", False)
    set_default_value("sort_before", False)
    set_default_value("sort_by_definition", False)
    set_default_value("sort_by_headword", False)
    set_default_value("sort_ignore_case", False)
    set_default_value("sort_reverse", False)
    set_default_value("version", False)
    set_default_value("author", u"Penelope")
    set_default_value("copyright", u"GNU GPL v3")
    set_default_value("cover_path", None)
    set_default_value("description", u"Dictionary %s to %s" % (args.language_from, args.language_to))
    set_default_value("email", u"penelopedictionaryconverter@gmail.com")
    set_default_value("identifier", get_uuid())
    set_default_value("license", u"GNU GPL v3")
    set_default_value("title", u"Dictionary %s to %s" % (args.language_from, args.language_to))
    set_default_value("website", u"https://goo.gl/EB5XSR")
    set_default_value("year", str(datetime.datetime.now().year))
