# -*- coding: utf-8 -*-
"""pdf_to_image.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-pLFaW63lSYBux8Ez0hCa4TJ69a1GbIi
"""

# !pip install fitz

# !pip install PyMuPDF

import fitz

pdf = "/content/panoptic_segmentation.pdf"
document = fitz.open(pdf)
selected_page = document.load_page(0)  # number of page
pix = selected_page.get_pixmap()
output = "final_image.png"
pix.save(output)