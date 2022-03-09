from PyPDF2 import PdfFileReader

path = r"C:\Users\gauta\Desktop\sample.pdf"

pdf = PdfFileReader( path )

print( f"Page = { pdf.getNumPages() }" )

print( f"pdf.documentInfo = { pdf.documentInfo }" )

print( f"\nPage 0 :-{ pdf.getPage(0) }" )


print( f"\nPage 0 Data :- \n\n{ pdf.getPage(0).extractText()  }" )
