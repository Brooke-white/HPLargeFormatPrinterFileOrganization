import os


class OrganizePDFs:
    def __init__(self, directory, beginning_file, job_dict):
        self.directory = directory
        self.beginning_pdf_index = beginning_file[4:-4]
        self.job_dict = job_dict

    def move_pdf_to_folder(self, job_number):
        file_name = "scan"+str(self.beginning_pdf_index)+".pdf"
        try:
            os.renames(
                self.directory+file_name,
                self.directory+"#"+str(job_number)+"/"+file_name)
        except OSError as error:
            print("Error moving pdf: ", error.__str__())
        except Exception as error:
            print("Error moving pdf: ", error.__str__())

    def increment(self, pdf_index):
        self.beginning_pdf_index = '%05d' % (int(pdf_index) + 1)

    def path_is_valid(self, pdf_index):
        return os.path.exists(self.directory+"scan"+str(pdf_index)+".pdf")

    def organize(self):

        for job in self.job_dict:
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

            for pdf in range(1, self.job_dict[job]+1):

                if self.path_is_valid(self.beginning_pdf_index):
                    self.move_pdf_to_folder(job_number=str(job))
                else:
                    while not self.path_is_valid(self.beginning_pdf_index):
                        self.increment(self.beginning_pdf_index)
                    self.move_pdf_to_folder(job_number=str(job))

                self.increment(self.beginning_pdf_index)

# example usage

# job number: number of PDFs for said job
my_dict = {
    7300: 1, 7302: 3, 7305: 1, 7306: 1, 7307: 1, 7308: 1, 7309: 2, 7310: 19,
    7311: 2, 7315: 1, 7317: 1, 7312: 1, 7313: 4, 7314: 1, 7316: 1, 7318: 1,
    7319: 1, 7321: 3, 7322: 1, 7323: 3, 7324: 2, 7325: 1, 7326: 1, 7327: 1,
    7328: 1, 7329: 7, 7330: 2, 7331: 3, 7332: 1, 7333: 1, 7334: 1, 7336: 1,
    7337: 3, 7338: 2, 7340: 1, 7341: 2, 7342: 1, 7343: 3, 7344: 1, 7345: 1,
    7346: 1, 7348: 1, 7351: 1, 7352: 2, 7353: 1, 7354: 2, 7355: 1, 7356: 1,
    7357: 1, 7358: 1, 7359: 2, 7363: 1, 7364: 3, 7365: 1, 7366: 1, 7367: 1,
    7368: 5, 7369: 1, 7370: 25, 7371: 1, 7372: 3, 7373: 3, 7374: 1, 7375: 1,
    7376: 1, 7377: 4, 7378: 2, 7379: 1, 7381: 1, 7382: 1, 7383: 2, 7384: 6,
    7385: 1, 7388: 1, 7389: 1, 7390: 1, 7391: 5, 7393: 2, 7394: 3, 7395: 2,
    7396: 1, 7397: 4, 7398: 2, 7399: 1
}
# directory in which all PDFs are stored
my_dir = "/Users/brooke/Desktop/jobs/"
# the filename of the first PDF in my_dir
beginning_pdf_file = "scan00906.pdf"

ex = OrganizePDFs(directory=my_dir, beginning_file=beginning_pdf_file,
                  job_dict=my_dict)
ex.organize()
