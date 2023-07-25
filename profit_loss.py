from pdfgeneration import PDFGenerator
from reportlab.lib import colors
from reportlab.platypus import TableStyle

pl=PDFGenerator("prfit_loss.pdf",72,72,60,60)
pl.add_title("PBCIX",'Heading2',1)
pl.add_title("Profit and Loss",'Heading3',1)
pl.add_title(f"{data['date_from']} - {data['date_to']}",'Normal',1)
pl.add_spacer(10)
    
t1 = [['', 'TOTAL']]
t2 = [
        ["Income", ""],
        ["- Revenue-General", f"{data['revenue_general']} ILS"],
        ["Total Income", f"{data['total_income']} ILS"],
    ]
t3 = [["GROSS PROFIT", f"{data['gross_profit']} ILS"]]
t4 = [
        ["Expenses", ""],
        ["- Commissions and fees", f"{data['commissions_and_fees']} ILS"],
        ["- Office expenses", "{self.data['office_expenses']} ILS"],
        ["- Other selling expenses", "{self.data['other_selling_expenses']} ILS"],
        ["Total Expenses", "{self.data['total_expense']} ILS"],
    ]
t5 = [["NET EARNINGS", f"{data['net_earnings']} ILS"]]
col_w=[240, 240]

same_style =[('LINEBEFORE', (0, 0), (0, -1), 0, 'white'),
            ('LINEAFTER', (-1, 0), (-1, -1), 0, 'white'),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),]

table_style_1 = TableStyle([
            ('LINEBELOW', (0, 0), (-1, 0), 2, 'black'),
            ('LINEABOVE', (0, 0), (-1, 0), 2, 'black'),
        ] + same_style
                           )
table_style_2= TableStyle([
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.lightgrey),
            ('LINEABOVE', (0, -1), (-1, -1), 2, colors.lightgrey),
            ('LINEABOVE', (0, 0), (-1, 0), 2, 'black'),
            ('LINEBELOW', (0, -1), (-1, -1), 2, 'black'),
        ] + same_style
                          )
pl.create_table(t1,col_w,table_style_1)
pl.create_table(t2,col_w,table_style_2)
pl.create_table(t3,col_w,table_style_1)
pl.create_table(t4,col_w,table_style_2)
pl.create_table(t5,col_w,table_style_1)
pl.generate_pdf(True)