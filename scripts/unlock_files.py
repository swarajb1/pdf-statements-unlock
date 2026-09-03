import getpass
import os
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.errors import PdfReadError


def masked_input(prompt: str, mask: str = "*") -> str:
    """Read a line from the terminal, echoing `mask` for each typed character."""

    if not sys.stdin.isatty():
        return getpass.getpass(prompt)

    sys.stdout.write(prompt)
    sys.stdout.flush()

    if sys.platform == "win32":
        import msvcrt

        read_char = msvcrt.getwch
        restore = None
    else:
        import termios
        import tty

        fd = sys.stdin.fileno()
        saved_attrs = termios.tcgetattr(fd)
        tty.setraw(fd)

        def read_char():
            return sys.stdin.read(1)

        def restore():
            termios.tcsetattr(fd, termios.TCSADRAIN, saved_attrs)

    typed: list[str] = []
    try:
        while True:
            char = read_char()

            if char in ("\r", "\n"):
                break
            if char in ("\x7f", "\b"):
                if typed:
                    typed.pop()
                    sys.stdout.write("\b \b")
            elif char == "\x03":
                raise KeyboardInterrupt
            elif char == "\x04":
                if not typed:
                    break
            else:
                typed.append(char)
                sys.stdout.write(mask)

            sys.stdout.flush()
    finally:
        if restore:
            restore()
        sys.stdout.write("\n")
        sys.stdout.flush()

    return "".join(typed)


def main():
    """Unlock all PDFs in private_data/files using a single shared password
    and write the decrypted copies into private_data/files/unlocked_files."""

    source_folder: Path = Path("./private_data/files")
    dest_folder: Path = source_folder / "unlocked_files"

    if not source_folder.exists():
        print(f"❌ Source folder not found: {source_folder}")
        return

    pdf_password: str = masked_input("Enter the PDF unlock password: ")

    dest_folder.mkdir(parents=True, exist_ok=True)

    processed_count = 0
    for file_name in os.listdir(source_folder):
        if (file_name.lower().endswith(".pdf")) and os.path.isfile(source_folder / file_name):
            source_pdf_path: Path = source_folder / file_name
            destination_pdf_path: Path = dest_folder / file_name

            try:
                unlock_pdf(
                    source_pdf_path=source_pdf_path,
                    destination_pdf_path=destination_pdf_path,
                    pdf_password=pdf_password,
                )
                processed_count += 1
            except ValueError as e:
                print(f"❌ Failed to unlock {file_name}: {e}")
                continue

    print(f"\n✅ Processing complete! Successfully unlocked {processed_count} files.")


def unlock_pdf(source_pdf_path: Path, destination_pdf_path: Path, pdf_password: str):
    # Open the password-protected PDF
    with open(source_pdf_path, "rb") as input_file:
        pdf_reader = PdfReader(input_file)

        # Authenticate with the password
        if pdf_reader.is_encrypted:
            decrypt_result = pdf_reader.decrypt(pdf_password)
            if decrypt_result == 0:
                raise ValueError(f"Failed to decrypt PDF with provided password: {source_pdf_path}")

        # Create a PDF writer object
        pdf_writer = PdfWriter()

        try:
            # Iterate through all the pages and add them to the writer object
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)
        except PdfReadError as e:
            raise ValueError(f"Failed to read pages from PDF file: {source_pdf_path}. Error: {e}")

        # Ensure the destination directory exists
        destination_pdf_path.parent.mkdir(parents=True, exist_ok=True)

        # Save the new PDF without a password
        with open(destination_pdf_path, "wb") as output_file:
            pdf_writer.write(output_file)

        print(f"✅ Successfully unlocked: {destination_pdf_path.name}")


if __name__ == "__main__":
    main()
