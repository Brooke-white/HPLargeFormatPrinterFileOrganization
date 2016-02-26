import os


class OrganizePDFs:
    """
    Organizes archived engineering job PDFs in folders by their job number.
    """
    def __init__(self, directory, beginning_file, job_list):
        """
        Initializes Organize PDFs class
        :param directory: The base directory in which unorganized PDFs are
        stored.
        :param beginning_file: The file name of the first scanXXX.pdf in the
        base directory
        :param job_list: A List of tuples of form
        [("Job Number", int(Number of PDFs)]
        """
        self.directory = directory
        self.beginning_PDF_index = beginning_file[4:-4]
        self.job_list = job_list

    def move_pdf_to_folder(self, job_number):
        """
        Moves a scanXXX.pdf file from the main directory to its job sub-folder.
        :param job_number: A String containing the current job number
        :return: None
        """
        file_name = "scan"+str(self.beginning_PDF_index) + ".pdf"
        print(file_name)
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
        for job, PDFs in self.job_list:
            try:
                sub_directory = self.directory+"#"+str(job)+"/"

                # if directory has not been created already
                if not os.path.isdir(sub_directory):
                    os.makedirs(sub_directory)
                else:
                    print("Dir already exists")

            except OSError as error:
                print("error:\t"+error.__str__())
                return 1
            except Exception as error:
                print("error:\t"+error.__str__())
                return 2
            for x in range(0, PDFs):  # for every PDF per job file
                if self.path_is_valid(self.beginning_PDF_index):
                    print(job, str(PDFs))
                    self.move_pdf_to_folder(job_number=str(job))
                else:
                    while not self.path_is_valid(self.beginning_PDF_index):
                        self.increment(self.beginning_PDF_index)
                        self.move_pdf_to_folder(job_number=str(job))

                self.increment(self.beginning_PDF_index)

# example usage #
cur_job_list = [
    ("06-66", 1), ("06-64", 1), ("06-63", 1), ("06-54", 1), ("06-50", 1),
    ("06-46", 1), ("06-45", 1), ("06-39", 1), ("06-27", 1), ("06-23", 1),
    ("06-22", 1), ("06-19", 1), ("06-12", 1), ("06-10", 1), ("06-09", 1),
    ("06-06", 1), ("06-01", 1), ("06-05", 1), ("06-48", 1), ("06-47", 1)
]
my_dir = "/Users/brooke/Desktop/Small Jobs/"
beginning_PDF_file = "scan00650.pdf"

ex = OrganizePDFs(directory=my_dir, beginning_file=beginning_PDF_file,
                  job_list=cur_job_list)
ex.organize()
