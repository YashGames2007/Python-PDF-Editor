import fitz

# specify the file path
file_path = "D:\\Programming files\\GitHub\\Repositories\\Python-PDF-Editor\\MML Formulae-1.pdf"

# open the document
doc = fitz.open(file_path)

# open the output file
out = open(file_path + ".html", "wb")

for page in doc:  # iterate the document pages
    text = page.get_text('html').encode("utf8")  # get the page text as HTML
    out.write(text)  # write the page text to the output file

out.close()  # close the output file
