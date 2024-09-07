import os
from pathlib import Path

import PyPDF2
from file_match import get_pdf_password


def main():
    # find all statements in folder, create separate folder for each bank statement, and for rename the file, and store it in separate folder

    month_year = input("Enter the month and year for the statements (e.g. 2021-06): ")

    source_folder: Path = Path("./private_data/credit_cards")

    for file_name in os.listdir(source_folder):
        if (file_name.endswith(".pdf") or file_name.endswith(".PDF")) and os.path.isfile(source_folder / file_name):
            source_pdf_path: Path = source_folder / file_name
            bank, pdf_password, card = get_pdf_password(file_name)

            # new_file_name_name = f"{card}_{month_year}"

            new_folder = source_folder / (bank.name + "_unlocked")

            os.makedirs(new_folder, exist_ok=True)

            file_name_name, file_extension = os.path.splitext(file_name)

            destination_pdf_path: Path = new_folder / (file_name_name + "_unlocked.pdf")

            # new_destination_pdf_path: Path = new_folder / (new_file_name_name + "_unlocked.pdf")

            unlock_pdf(
                source_pdf_path=source_pdf_path,
                destination_pdf_path=destination_pdf_path,
                pdf_password=pdf_password,
            )

            # move and rename the original file
            # os.makedirs(new_folder / "original", exist_ok=True)

            # os.rename(source_pdf_path, new_folder / "original" / (new_file_name_name + ".pdf"))

            # os.rename(source_pdf_path, new_folder / file_name)


def unlock_pdf(source_pdf_path: Path, destination_pdf_path: Path, pdf_password: str):
    # Open the password-protected PDF
    with open(source_pdf_path, "rb") as input_file:
        pdf_reader = PyPDF2.PdfReader(input_file)
        # Authenticate with the password
        if pdf_reader.is_encrypted:
            pdf_reader.decrypt(pdf_password)

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        try:
            # Iterate through all the pages and add them to the writer object
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)
        except PyPDF2.errors.FileNotDecryptedError:
            ValueError(f"Failed to decrypt the PDF file: {source_pdf_path}")

        # Save the new PDF without a password
        with open(destination_pdf_path, "wb") as output_file:
            pdf_writer.write(output_file)


if __name__ == "__main__":
    main()
