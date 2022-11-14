# !pip install PyMuPDF
# !pip install fitz

from PIL import Image 
import fitz


def imgToPdf(fPath, fList, pdfPath):
    images = [Image.open(fPath + f) for f in fList]
    images[0].save(pdfPath, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
    print(f"la operacion completada")
    
    return None

def eliminar_paginas(fInput: str, fOutput: str, idxToDel: list):

    file_handle = fitz.open(input_file)
    pages_list = [x for x in range(22) if x not in idxToDel]

    file_handle.select(pages_list)
    file_handle.save(output_file)
    print(f"la operacion completada")
    
    return None

def insertar_paginas(doc_input: str, doc_output: str, page_input: str):
    ''' se estan insertando paginas al principo'''

    first_pdf = fitz.open(page_input)
    second_pdf = fitz.open(doc_input)

    first_pdf.insert_pdf(second_pdf)
    first_pdf.save(doc_output)
    
    return None


