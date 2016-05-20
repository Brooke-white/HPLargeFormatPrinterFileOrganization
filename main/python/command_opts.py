# coding=utf-8
import os
import argparse
import re


class CommandColors:
    """
    Class instantiation for colored text in command line.
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Command:
    """
    Class instantiation for Command line options.

    Arguments:
    None

    Attributes:
    parser(ArgumentParser): An ArgumentParser object which allows a command
                            line interface to be established.
    """
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-i', '--input', help='Input text file path',
                                 required=True, type=self.is_valid_text_file,
                                 nargs='+')
        self.parser.add_argument('-d', '--directory',
                                 help='Directory where PDFs are',
                                 required=True, type=self.is_valid_directory,
                                 nargs='+')
        self.parser.add_argument('-b', '--begin',
                                 help='Name of first PDF (ex. scan0091.pdf)',
                                 required=True, type=self.is_valid_scan_name,
                                 nargs='+')

    def is_valid_directory(self, user_input):
        """
        User input directory is verified/corrected to be a valid directory.

        Keywords:
        user_input(String)--A String containing a file path to a directory

        Returns:
        String--containing a valid directory
        """
        if os.path.isdir(str(user_input)):
            return user_input
        else:
            self.parser.error(CommandColors.FAIL +
                              "Invalid output directory! " + str(user_input) +
                              CommandColors.ENDC)

    def is_valid_text_file(self, user_input):
        """
        User input file path is verified/corrected to be a valid file path.

        Keywords:
        user_input(String)--A String containing a path to a text file which
                            will be used for input

        Returns:
        String(String)--A string containing a valid file path to a txt file
        """
        if str(user_input).endswith(".txt") and os.path.isfile(
                str(user_input)):
                return user_input
        else:
                self.parser.error(
                    CommandColors.FAIL + "Invalid output directory!" +
                    str(user_input) + CommandColors.ENDC)

    def is_valid_scan_name(self, user_input):
        """
        Initial scan index is verified to be of correct form (scanXXX).

        Keywords:
        user_input(String)--A String containing a scanXXX where XXX is the
        index of the first scanned PDF.

        Returns:
        String(String)--A string containing a valid scanXXX index
        """
        if re.match(pattern="^((scan)[0-9]*(.pdf)$)", string=user_input):
            return user_input
        else:
            self.parser.error(CommandColors.FAIL + "Invalid scan index " +
                              user_input +
                              ". Should be of form scanXXXX where XXX is a "
                              "number" + CommandColors.ENDC)

    def get_options(self):
        """
        Extracts options from self.arguments.parse_args(), inserts in a list.

        Returns:
        A list containing the options passed to the command line
        """

        return [self.parser.parse_args().begin,
                self.parser.parse_args().input,
                self.parser.parse_args().directory]


class Options:
    """
    Class instantiaton for Command line options handler.

    Arguments:
    None

    Attributes:
    begin(Command)--A Command object holding options passed to the Command line
    options(List)--A list holding options passed to the command line
    """
    def __init__(self):
        self.begin = Command()
        self.options = self.begin.get_options()

    def __str__(self):
        return(CommandColors.OKBLUE + "Input txt: " + str(self.options[1]) +
               "\nDirectory: " + str(self.options[2]) + "\nBegin index: " +
               str(self.options[0]) + CommandColors.ENDC)


def main():
    current = Options

if __name__ == "__main__":
    main()
