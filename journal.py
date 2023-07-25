import textwrap
from pdfgeneration import PDFGenerator
from reportlab.lib import colors
from reportlab.lib.pagesizes import inch
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import Paragraph, TableStyle


def wrap_text(text, width):
    wrapped_text = "\n".join(textwrap.wrap(text, width=width, break_long_words=False))
    return wrapped_text
    
def create_rows(item,pl,col_w,table_style_1,table_style_2):
    row = [
        [item.get("date", ""),
         item.get("trans_type_credit", ""),
         item.get("num_credit", ""),
         item.get("name_credit", ""),
         item.get("memo_credit", ""),
         item.get("account_credit", ""),
         '',
         item.get("credit", "") + " ILS"]
        ]
    row2 = [
        ['', '', '', '', wrap_text(item.get("memo_debit", ""), width=16),
          wrap_text(item.get("account_debit", ""), width=11), item.get("debit", "") + " ILS", '']
        ]
    row3 = [
        ['', '', '', '', '', '', item.get("debit", "") + " ILS", item.get("credit", "") + " ILS"]
        ]
    pl.create_table(row, col_w, table_style_2)
    pl.create_table(row2, col_w, table_style_2)
    pl.create_table(row3, col_w, table_style_3)

pl=PDFGenerator("journnal.pdf",72,72,60,63)
col_w=[60, 70, 40, 80, 120, 80, 60, 60]

same_style = [('FONTSIZE', (0, 0), (-1, 0), 9),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),]
same_font = [('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),]
same_bottom_pad = [('BOTTOMPADDING', (0, 0), (-1, 0), 2),]
table_style_1 = TableStyle([
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
            ('LINEABOVE', (0, 0), (-1, 0), 2, colors.black),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ] + same_style
                          )
table_style_2 = TableStyle([
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ] + same_style + same_bottom_pad
                          )
table_style_3 = TableStyle(same_bottom_pad + same_style + same_font)

pl.add_title("PBCIX",'Heading2',1)
pl.add_title("Journal",'Heading3',1)
pl.add_title(f"{data['date_from']} - {data['date_to']}",'Normal',1)

pl.add_spacer(10)

t1 = [['Date', 'TRANSACTION\nTYPE', 'NO.', 'NAME', 'MEMO/\nDESCRIPTION', 'ACCOUNT', 'DEBIT', 'CREDIT']]

pl.create_table(t1,col_w,table_style_1)
i=0
t_debit=0
t_credit=0
for item in data['data']:
    create_rows(item,pl,col_w,table_style_1,table_style_2,)
    t_debit += float(item.get("debit", ""))
    t_credit += float(item.get("credit", ""))
    i += 1
    if i % 6 == 0:
        pl.add_spacer(50)
        pl.add_title
        pl.add_title("PBCIX",'Heading2',1)
        pl.add_title("Journal",'Heading3',1)
        pl.add_title(f"{data['date_from']} - {data['date_to']}",'Normal',1)
        pl.add_spacer(10)
        pl.create_table(t1,col_w,table_style_1)
        
pl.generate_pdf(foot=True)