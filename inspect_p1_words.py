import pypdf

reader = pypdf.PdfReader('uploads/naskah_664_1792378418 (1).pdf')
p1 = reader.pages[0]

# Page height in points: 842.04
# Viewport height = 842.04 * 1.35 = 1136.75
# Y in PDF: Y=662.0 is from BOTTOM!
# In PDF.js viewport: Y_top = (842.04 - 662.0) * 1.35 = 180.04 * 1.35 = 243.05
# X in PDF: X=149.4
# In PDF.js viewport: X = 149.4 * 1.35 = 201.69
print("Calculated X:", 149.4 * 1.35, "Y_baseline:", (842.04 - 662.0) * 1.35)
