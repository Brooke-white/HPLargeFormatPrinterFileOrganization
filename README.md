# HPLargeFormatPrinterFileOrganization

A small script that organizes PDFs from an HP large format printer into folders based on the job number they pertain to in order to speed up the digitization of archival engineering drawings.

# Usage

my_dir = The directory where the PDFs are stored

beginning_PDF_file = The name of the first PDF scanned (scanxxxx.pdf)

file = An input text file containing job numbers and numbers of pdfs per job
(example.txt)

ex = OrganizePDFs(directory=my_dir, beginning_file=beginning_PDF_file,
                  job_list_txt=file)
ex.organize()
