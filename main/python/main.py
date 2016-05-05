# coding=utf-8
import os
from command_opts import Options


class OrganizePDFs:
    """
    Organizes archived engineering job PDFs in folders by their job number.
    """
    def __init__(self, directory, beginning_file, job_list_txt):
        """
        Initializes Organize PDFs class
        :param directory: The base directory in which unorganized PDFs are
        stored.
        :param beginning_file: The file name of the first scanXXX.pdf in the
        base directory
        :param job_list: A List of tuples of form
        [("Job Number", int(Number of PDFs)]
        """
        self.directory = directory + '/' if not str(directory).endswith('/') \
            else directory
        self.beginning_PDF_index = beginning_file[4:-4]
        self.job_list_txt_file = job_list_txt
        self.job_list = self.read_job_list()

    def read_job_list(self):
        """
        Reads lines of form "1234 5" from a txt file as tuples, places in list.
        :return: list of tuples(str, int)
        """
        try:
            txt_file = open(self.job_list_txt_file, 'r')
        except FileNotFoundError:
            raise FileNotFoundError
        except TypeError:
            raise TypeError
        except IOError:
            raise IOError
        except:
            raise Exception

        tuple_list = []
        count = 0
        for pair in txt_file:  # line in form "1234 5"
            line_list = pair.split('\n')
            line_list = line_list[0].split(' ')
            try:
                tuple_list.append((line_list[0], int(line_list[1])))
            except IndexError:
                continue  # move along if line is blank
            count += 1
        return tuple_list

    def is_correct_file_count(self):
        """
        Ensures the user entered number of PDFs matches the directory contents.
        :return: boolean: True for correct PDF count, False otherwise.
        """
        job_list_count = 0
        directory_count = len([file for file in os.listdir(self.directory)
                               if file.endswith(".pdf")])

        for job_num, PDF_count in self.job_list:
            job_list_count = job_list_count + PDF_count

        if job_list_count == directory_count:
            return True
        else:
            print("WARNING: Incorrect number of PDF files supplied in "
                  "relation to directory contents, verify results. Directory "
                  "contains: ", directory_count, " User supplied: ",
                  job_list_count)
            return False

    def move_pdf_to_folder(self, job_number):
        """
        Moves a scanXXX.pdf file from the main directory to its job sub-folder.
        :param job_number: A String containing the current job number
        :return: None
        """
        file_name = "scan"+str(self.beginning_PDF_index) + ".pdf"
        try:
            os.renames(
                self.directory+file_name,
                self.directory+"#"+str(job_number)+"/"+file_name)
        except OSError as error:
            print("Error moving pdf: ", error.__str__())
        except Exception as error:
            print("Error moving pdf: ", error.__str__())

    def increment(self, pdf_index):
        """
        Increments the current scanXXX.pdf by one.
        :param pdf_index: The index of the current scanXXX.pdf
        :return: None
        """
        self.beginning_PDF_index = '%05d' % (int(pdf_index) + 1)

    def path_is_valid(self, pdf_index):
        """
        Determines if a given PDF file of the form scanXXX.pdf exists.
        :param pdf_index: The index of the current scanXXX.pdf
        :return: boolean: True if the scanXXX.pdf exists, False if does not
        exist
        """
        return os.path.exists(
            self.directory + "scan" + str(pdf_index) + ".pdf")

    def organize(self):
        """
        Iterates through job_list creating folders for each job and moves PDFs.
        :return: None
        """
        if not self.is_correct_file_count():  # warn if count is off
            input("Press any key to continue...")

        for job, PDFs in self.job_list:
            try:
                sub_directory = self.directory+"#"+str(job)+"/"
                if not os.path.isdir(sub_directory):
                    os.makedirs(sub_directory)

            except OSError as error:
                print("error:\t"+error.__str__())
                return 1
            except Exception as error:
                print("error:\t"+error.__str__())
                return 2

            for x in range(0, PDFs):  # for every PDF per job file
                if self.path_is_valid(self.beginning_PDF_index):
                    self.move_pdf_to_folder(job_number=str(job))
                else:
                    its = 0 # iteration counter for pdf name increments
                    while not self.path_is_valid(self.beginning_PDF_index) \
                            and its < 100:
                        self.increment(self.beginning_PDF_index)
                        its += 1
                    self.move_pdf_to_folder(job_number=str(job))

                self.increment(self.beginning_PDF_index)
        print("Operation complete")

# example usage #

# not using command line for OrganizePDFs params

#my_dir = "/Users/brooke/Desktop/#6501-6600/"
#beginning_PDF_file = "scan00680.pdf"
#file = "/Users/brooke/Desktop/input.txt"

#ex = OrganizePDFs(directory=my_dir, beginning_file=beginning_PDF_file,
#                  job_list_txt=file)


# using command line for OrganizePDFs params
command_input = Options()

ex = OrganizePDFs(directory=''.join(command_input.options[2]),
                  beginning_file='.'.join(command_input.options[0]),
                  job_list_txt='.'.join(command_input.options[1]))

ex.organize()
