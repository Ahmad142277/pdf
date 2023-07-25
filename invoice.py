from pdfgeneration import PDFGenerator
from reportlab.lib import colors
from reportlab.lib.pagesizes import inch
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, TableStyle

pl=PDFGenerator("invoice.pdf",20,20,0,0)
pl.add_logo('logo.png')
styles=getSampleStyleSheet()
paragraph_style = ParagraphStyle(
            'CustomParagraphStyle',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=10,
            spaceAfter=2,
            alignment=0,
            textColor=colors.black,
            leading=18,
        )
    
t1 = [[f"From: { data['name'] }"]]
t2 = [[f"Business Name: { data['business_name'] }"]]
t3 = [[Paragraph(data['address'], paragraph_style)]]
t4 = [['INVOICE         ']]
t5 = [[f"Bill to: {data['bill_to']}", "INVOICE #", f"{data['invoice_no']}"]]
t6 = [["Attn: {data['att']}", "DATE", f"{data['date']}"]]
t7 = [["{data['company_name']}", "DUE DATE", f"{data['due_date']}"]]
t8 = [["", "TOTAL AMOUNT", f"${data['total_amount']}"]]
t9 = [["", "TOTAL DUE AMOUNT", f"{data['due_amount']}"]]

col_w=280
same_align = [('ALIGN', (0, 0), (-1, -1), 'LEFT'),]
same_font = [('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),]
table_style_1 = TableStyle([
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 2),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ] + same_align + same_font
                          ) 
table_style_2 = TableStyle([
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 14),
            ('TOPPADDING', (0, 0), (-1, 0), 6),
            ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey),
        ] + same_font
                          )
table_style_3 = TableStyle([
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 2),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ] + same_font + same_align
                          )
table_style_4 = TableStyle([
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LINEBELOW', (0, 0), (-1, -1), 0.1, colors.lightgrey),
            ('LINEABOVE', (0, 0), (-1, -1), 0.1, colors.lightgrey),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('TOPPADDING', (0, 0), (-1, 0), 10),
            ('GRID', (0, 0), (-1, -1), 0.1, colors.lightgrey),
        ] + same_align + same_font
                           )

pl.invoice_custom_table(t1,col_w,table_style_1,'LEFT')
pl.invoice_custom_table(t2,col_w,table_style_1,'LEFT')
pl.invoice_custom_table(t3,200,table_style_1,'LEFT')
pl.add_spacer(0.20 * inch)
pl.invoice_custom_table(t4,550,table_style_2,'CENTRE')
pl.add_spacer(0.20 * inch)
col_w=[330, 120, 100]
pl.create_table(t5,col_w,table_style_1)
pl.create_table(t6,col_w,table_style_1)
pl.create_table(t7,col_w,table_style_1)
pl.create_table(t8,col_w,table_style_1)
pl.create_table(t9,col_w,table_style_1)
pl.add_spacer(0.20 * inch)
col_w=[410, 100]

t10 = [["DESCIPTION/MEMO", "AMOUNT"]]
pl.invoice_custom_table(t10,col_w,table_style_4,'CENTRE')
for item in data['Purchase_details']:
    row = [[
            Paragraph(item.get("descipt_memo", ""),paragraph_style),
            item.get("amount", ""),
        ]]
    pl.invoice_custom_table(row,col_w,table_style_4,'CENTRE')
row1 = [["TOTAL AMOUNT:", f"${data['total_amount']}"]]
pl.invoice_custom_table(row1,col_w,table_style_4,'CENTRE')
pl.add_spacer(1 * inch)

tx = [['Remit to:'], [Paragraph(data['remit_to'],paragraph_style)]]
pl.invoice_custom_table(tx,100,table_style_3,'RIGHT')
pl.generate_pdf(foot=False)