from pdfgeneration import PDFGenerator
from reportlab.lib import colors
from reportlab.platypus import TableStyle

pl=PDFGenerator("balancesheet.pdf",72,72,60,60)
pl.add_title("PBCIX",'Heading2',1)
pl.add_title("Profit and Loss",'Heading3',1)
pl.add_title(f"{data['date']}",'Normal',1)
pl.add_spacer(10)
    
t1 = [['', 'TOTAL'], ]

t2 = [["Assets", ""], ]

t3 = [["Current Assets", ""],
              ["- Cash in Bank", f"{data['cash_in_bank']} ILS"],
              ["Total Current Assets", f"{data['total_current_assets']} ILS"], ]
t4 = [["Total Assets", f"{data['total_assets']} ILS"], ]

t5 = [["Liabilities and Shareholder's Equity", ""], ]

t6 = [['Shareholders Equity', ''],
      ['- Net income', f"{data['net_income']} ILS"],
      ['- Opening Balance Equity', f"{data['opening_balance_equity']} ILS"],
      ["- Owner's Loan", f"{data['owner_loan']} ILS"],
      ['- Retained Earnings', f"{data['retained_earning']} ILS"],
      ["Total Shareholder's Equity", f"{data['total_shareholder_equity']} ILS"], ]

t7 = [['Total Liabilities and Equity', f"{data['total_liabilities_equity']} ILS"], ]

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
pl.create_table(t2,col_w,table_style_1)
pl.create_table(t3,col_w,table_style_2)
pl.create_table(t4,col_w,table_style_1)
pl.create_table(t5,col_w,table_style_1)
pl.create_table(t6,col_w,table_style_2)
pl.create_table(t7,col_w,table_style_1)
pl.generate_pdf(True)