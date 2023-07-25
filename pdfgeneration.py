import datetime
import textwrap
from reportlab.lib import colors
from reportlab.lib import styles
from reportlab.lib.pagesizes import A4, letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, TableStyle, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

class PDFGenerator:
    def __init__(self, filename, right_margin, left_margin, top_margin, bottom_margin):
        self.filename = filename
        self.story = []
        self.doc = SimpleDocTemplate(self.filename,
                                     pagesize=A4,
                                     rightMargin=right_margin,
                                     leftMargin=left_margin,
                                     topMargin=top_margin,
                                     bottomMargin=bottom_margin
                                    )
        
    def add_logo(self,logo_path):
        logo = Image(logo_path, width=1.0 * inch, height=1.0 * inch)
        logo.hAlign = 'RIGHT'
        self.story.append(logo)
        
    def add_title(self, text, title_style,Align):
        styles = getSampleStyleSheet()
        title_style=styles[title_style]
        title_style.alignment=Align
        self.story.append(Paragraph(text, title_style))

    def create_table(self, data, col_widths,table_style):
        table = Table(data, colWidths=col_widths)
        table.setStyle(table_style)
        self.story.append(table)

    def add_spacer(self, height):
        self.story.append(Spacer(1, height))
        
    def invoice_custom_table(self,table,col_widths,style,halign):
        table = Table(table, colWidths=col_widths)
        table.setStyle(style)
        table.hAlign=halign
        self.story.append(table)

    def generate_pdf(self,foot):
        if foot==True:
            styles = getSampleStyleSheet()
            current_datetime = datetime.datetime.now()
            current_date = current_datetime.date()
            current_time = current_datetime.strftime("%H:%M:%S")
            current_day = current_datetime.strftime("%A")
            result = f"{current_day}, {current_date},  {current_time}."
            paragraph_style = styles['Normal']
            paragraph_style.alignment=1
            footer_text = f"Accrual Basis {result}"
            footer = Paragraph(footer_text, paragraph_style)

            def add_footer(canvas, doc):
                canvas.saveState()
                canvas.setFont('Helvetica', 9)
                canvas.setFillColor(colors.gray)
                footer_x = (doc.width) / 2
                canvas.drawString(footer_x, doc.bottomMargin + 5, footer_text)
                canvas.restoreState()
            self.doc.build(self.story, onFirstPage=add_footer, onLaterPages=add_footer)
        else:
            self.doc.build(self.story)
    

