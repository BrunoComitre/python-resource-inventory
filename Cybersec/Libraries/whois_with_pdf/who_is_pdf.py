import whois
from fpdf import FPDF, HTMLMixin

domain = input("Enter domain name: ")
search_whois = whois.whois(domain)

print(search_whois.text)

print(type(search_whois.text))

result = repr(search_whois.text)

print(type(result))

'''
nano ~/.bash_profile
insert: alias python='/usr/bin/python3.10'
source ~/.bash_profile
poetry env use -vvv 3.10
'''

''''
class PDF(FPDF):
    def __init__(self) -> None:
        super().__init__()
        self.WIDTH = 200
        self.HEIGHT = 200

    def header(self):
        # Custom Logo and Positioning
        # Create an `assets` folder and put any wide and short image inside
        # Name the image `logo.png`
        # self.image('assets/logo.png', 10, 8, 33)
        self.set_font('Arial', 'B', 12)
        self.cell(self.WIDTH - 80)
        # self.cell(0, 10, 'Whois', 0, 0, 'C')
        self.cell(60, 1, 'Whois', 0, 0, 'R')
        self.ln(20)

    def footer(self):
        # Page numbers in the footer
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page' + str(self.page_no()), 0, 0, 'C')

    def page_body(self, text):
        # Determine how many plots there are per page and set positions
        # and margins accordingly
        if len(text) == 3:
            self.image(text[0], 15, 25, self.WIDTH - 30)
            self.image(text[1], 15, self.WIDTH / 2 + 5, self.WIDTH - 30)
            self.image(text[2], 15, self.WIDTH / 2 + 90, self.WIDTH - 30)
        elif len(text) == 2:
            self.image(text[0], 15, 25, self.WIDTH - 30)
            self.image(text[1], 15, self.WIDTH / 2 + 5, self.WIDTH - 30)
        else:
            self.image(text[0], 15, 25, self.WIDTH - 30)

    def print_page(self, text):
        # Generates the Report
        self.add_page()
        self.page_body(text)
        # self.ln(self.HEIGHT - 30)
'''

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.ln(10)

    def chapter_body(self, name):
        self.set_font('Times', '', 12)
        # Output justified text
        self.multi_cell(0, 5, name)
        # Line break
        self.ln()
        # Mention in italics
        self.set_font('', 'I')
        self.cell(0, 5, '(end of excerpt)')

    def print_chapter(self, name):
        self.add_page()
        self.chapter_body(name)

pdf = PDF()

pdf.add_page();

pdf.set_font('Arial','B',16);

title = '20000 Leagues Under the Seas'

pdf.set_title(title)
pdf.print_chapter(result)

pdf.output('whois_analysis.pdf', 'F')


# https://towardsdatascience.com/how-to-create-pdf-reports-with-python-the-essential-guide-c08dd3ebf2ee
# https://www.youtube.com/watch?v=eGZs73Nrjes
# https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html
