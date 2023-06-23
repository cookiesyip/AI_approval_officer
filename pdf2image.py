import fitz
import os
import time

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  
        os.makedirs(path)  
    else:
        pass


def pdf_image(pdfPath, imgPath, zoom_x, zoom_y, rotation_angle):
    """
    steps:
    1.create the "pdfs" and "images" folder in the current directory
    2.put all pdf files in the folder "pdfs"
    3.run pdf2image.py
    """
    pdf = fitz.open(pdfPath)
    name = pdf.name
    name = name.replace('pdfs/', '').replace('.pdf', '')
    for pg in range(0, pdf.page_count):
        page = pdf[pg]
        timestamp = time.strftime("%Y_%m_%d~%H:%M:%S")
        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotation_angle)
        pm = page.get_pixmap(matrix=trans, alpha=False)
        pm.save(imgPath + name + timestamp + "page" + str(pg + 1) + ".png")
    pdf.close()


# pdf_image(r"pdfs/01.pdf", r"images/", 10, 10, 0)

file_dir = r'pdfs/'
file_list = []
for items in os.walk(file_dir, topdown=False):
    file_list = items[2]
print(file_list)

for file in file_list:
    head = 'pdfs/'
    pdf_image(head + file, r"images/", 5, 5, 0)