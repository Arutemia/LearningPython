from fpdf import FPDF

def main():
	name = input("Name: ")
	pdf = FPDF(orientation="P", unit="mm", format="A4")
	pdf.add_page()
	
	pdf.set_font("Helvetica", "B", 24)
	pdf.cell(0, 40, f"CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
	
	pdf.image("shirtificate.png", x=0, y=60, w=210)
	
	pdf.set_font("Helvetica", "B", 24)
	pdf.set_text_color(255,255,255)
	pdf.set_xy(0, 140)
	pdf.cell(210, 10, f"{name} took CS50", align="C")
	
	pdf.output("shirtificate.pdf")
	
if __name__ == "__main__":
	main()
