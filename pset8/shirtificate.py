# wget https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png

from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def shirt(self):
        self.add_page()
        self.image("shirtificate.png",  x=10, y=65, w=190)
        self.set_y(10)
        self.set_font("Helvetica", "", 46)
        self.cell(0, 40, "CS50 Shirtificate", align="C")

    def print_name(self):
        self.set_y(10)
        self.set_text_color(250, 250, 250)
        self.set_font("Helvetica", "", 30)
        self.cell(0, 240, f"{self.name} took CS50", align="C")


name = input("Name: ")

pdf = PDF(name)
pdf.shirt()
pdf.print_name()
pdf.output("shirtificate.pdf")
