from pathlib import Path
import PyPDF2


def main():
    print("Hello, World!")

    source_pdf_path = "./private_data/credit_cards/4315XXXXXXXX0004_318275_Retail_Amazon_NORM.pdf"

    destination_pdf_path = "./private_data/credit_cards/4315XXXXXXXX0004_318275_Retail_Amazon_NORM_free.pdf"
    pdf_password = "swar1901"

    unlock_pdf(
        source_pdf_path=Path(source_pdf_path),
        destination_pdf_path=Path(destination_pdf_path),
        pdf_password=pdf_password,
    )


def unlock_pdf(source_pdf_path: Path, destination_pdf_path: Path, pdf_password: str):

    # Open the password-protected PDF
    with open(source_pdf_path, "rb") as input_file:
        pdf_reader = PyPDF2.PdfReader(input_file)
        # Authenticate with the password
        if pdf_reader.is_encrypted:
            pdf_reader.decrypt(pdf_password)

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Iterate through all the pages and add them to the writer object
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        # Save the new PDF without a password
        with open(destination_pdf_path, "wb") as output_file:
            pdf_writer.write(output_file)

    print("Password protection has been removed.")


if __name__ == "__main__":
    main()
