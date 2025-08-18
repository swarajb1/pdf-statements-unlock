# pdf-statements-unlock

Unlock and segregate credit card PDF statements

## 🐛 Issues Fixed

**Critical Bug**: The main issue causing "damaged" PDF files was that the `unlock_pdf` function was not actually adding pages to the PDF writer. The code was:

```python
# BUGGY CODE - Pages were retrieved but never added!
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]  # ❌ Missing: pdf_writer.add_page(page)
```

**Fixed**: Now properly adds pages to the writer:

```python
# FIXED CODE
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    pdf_writer.add_page(page)  # ✅ Pages are now added!
```

## 🔧 Setup

1. **Install dependencies:**

    ```bash
    poetry install
    ```

2. **Create environment file:**

    ```bash
    cp .env.template .env
    ```

3. **Configure your card details in `.env`:**
    - Add PDF passwords for each bank
    - Add card numbers and names
    - Match the file naming patterns

## 🚀 Usage

1. **Place your PDF statements in:** `private_data/credit_cards/`

2. **Run the unlock script:**

    ```bash
    poetry run python pdf_statements_unlock/main.py
    ```

3. **Test PDF integrity (optional):**

    ```bash
    poetry run python test_pdf_unlock.py
    ```

## 📁 Output Structure

```
private_data/credit_cards/
├── ICICI Bank/
│   └── Amazon credit card monthly statement/
│       ├── original/
│       └── XXXX_Amazon_2021-06_unlocked.pdf
└── HDFC Bank/
    └── [card_name] credit card monthly statement/
        ├── original/
        └── XXXX_[card_name]_2021-06_unlocked.pdf
```

## 🔍 Troubleshooting

- **"Password not found"**: Check your `.env` file and file naming patterns in `database/card_management.py`
- **"Failed to decrypt"**: Verify the PDF password in your `.env` file
- **"Damaged PDF"**: Use the test script to verify PDF integrity after unlocking

## 🛠 Improvements Made

- ✅ Fixed critical bug where pages weren't added to PDF writer
- ✅ Added proper error handling and validation
- ✅ Upgraded from deprecated PyPDF2 to pypdf
- ✅ Added success/failure feedback
- ✅ Added directory existence checks
- ✅ Added PDF integrity test script
- ✅ Improved exception handling with specific error messages
