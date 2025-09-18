from fpdf import FPDF

# PDF is a child class of FPDF class, which means you have access to its classes.


class PDF(FPDF):
    def header(self):
        # Place the image at (30, 60) with size of 150.
        self.image("./shirtificate.png", 25, 60, 150)

        # Set font,
        self.set_font("Courier", style="B", size=40)

        # Print "CS50 Shirtificate"
        self.cell(30, 10, "CS50 Shirtificate", border=0, align="C", center=True)


def main():
    while True:
        try:
            name = input("Name: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        break

    print_shirt_for(name)


def print_shirt_for(name):
    pdf = PDF()

    # Add page.
    pdf.add_page()

    # Select appropriate font.
    pdf.set_font("Courier", style="B", size=30)
    # Set text color to white.
    pdf.set_text_color(255, 255, 255)

    pdf.cell(15, 200, f"{name} took CS50", align="C", center=True, border=0)

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
