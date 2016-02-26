# HPLargeFormatPrinterFileOrganization
<<<<<<< HEAD
A small script that organizes PDFs from an HP Large Printer
(or any printer with filename of the form scanXXX.pdf) by the job
number they are associated with.

#Usage

ex = OrganizePDFs(directory, beginning_file,
                  job_list)
ex.organize()

directory = The directory in which the PDFs are found (ex. Users/brooke/Desktop/my_dir)

beginning_file = The filename of the initial scanned file (ex. scan0001.pdf)

job_list = A list of tuples of the form [("Job Number", Number of PDFs)]
(ex. [("7190A", 1), ("7189&8120", 12), ("7128-T", 1), ("1234", 5)] )
=======

A small script that organizes PDFs from an HP large format printer into folders based on the job number they pertain to in order to speed up the digitization of archival engineering drawings.
>>>>>>> e9d156b260afafd92da53ebea9e4ec513091f929
