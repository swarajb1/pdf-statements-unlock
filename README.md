# PDF Statements Unlock 🔓

A robust Python tool that automatically unlocks password-protected credit card PDF statements and organizes them by bank and card type. Perfect for financial document management and archival.

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Poetry](https://img.shields.io/badge/poetry-dependency%20management-blue.svg)](https://python-poetry.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## ✨ Features

- 🔐 **Password-protected PDF unlocking** using bank-specific passwords
- 📁 **Automatic file organization** by bank and card type
- 🏦 **Multi-bank support**: ICICI, HDFC, Kotak, Standard Chartered, IndusInd
- 📝 **Smart file renaming** with standardized naming conventions
- 🛡️ **Error handling** with detailed feedback and validation
- 📋 **Backup preservation** - keeps original files in dedicated folders
- ⚡ **Batch processing** for multiple statements at once
- 🎯 **File pattern matching** for automatic card identification

## 🏗️ Architecture

```
pdf_statements_unlock/
├── main.py              # Main application entry point
├── file_match.py        # File pattern matching logic
├── core/
│   └── config.py        # Configuration and environment management
└── database/
    ├── enums.py         # Bank and card enumerations
    └── card_management.py # Card data and password management
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- Poetry for dependency management
- Password-protected PDF statements from supported banks

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/pdf-statements-unlock.git
   cd pdf-statements-unlock
   ```

2. **Install dependencies:**
   ```bash
   poetry install
   ```

3. **Set up environment:**
   ```bash
   # Create environment file from template
   cp .env.template .env

   # Create private data directory
   make create_private_folders
   ```

4. **Configure your cards (see [Configuration](#-configuration)):**
   ```bash
   # Edit .env file with your bank passwords and card details
   nano .env
   ```

### Quick Run

```bash
# Using Poetry
poetry run python pdf_statements_unlock/main.py

# Using Make
make run

# Using shell scripts
./run.sh      # macOS/Linux
run.bat       # Windows
```

## ⚙️ Configuration

### Environment Variables

Edit `.env` file with your bank-specific information:

```env
# Bank PDF Passwords
ICICI_PDF_PASSWORD=your_icici_password
HDFC_PDF_PASSWORD=your_hdfc_password
KOTAK_PDF_PASSWORD=your_kotak_password
STANDARD_CHARTERED_PDF_PASSWORD=your_sc_password
INDUSIND_PDF_PASSWORD=your_indusind_password

# Card Details (for each card you have)
ICICI_CARD_1_NUMBER=8493XXXXXXXX2751
ICICI_CARD_1_NAME=Amazon_Pay

HDFC_CARD_1_NUMBER=6285XXXXXXXX9472
HDFC_CARD_1_NAME=Millennia

# ... add more cards as needed
```

### Supported Banks & File Patterns

The system automatically identifies cards based on filename patterns:

| Bank | Card Types | File Patterns |
|------|------------|---------------|
| **ICICI Bank** | Amazon Pay, Coral, Coral RuPay | `amazon`, `xx5927`, `xx3846` |
| **HDFC Bank** | Millennia, Swiggy, Tata Neu | `7429xx`, `8563xx`, `9182xx` |
| **Kotak Bank** | Zen | `300xxx7429-481592` |
| **Standard Chartered** | Platinum Rewards | `eStatement8563`, `STANCHART` |
| **IndusInd Bank** | Various | `--` (placeholder) |

### Adding New Banks/Cards

1. **Add to enum** in `database/enums.py`:
   ```python
   class BankCreditCards(StateEnum, Enum):
       NEW_BANK = "New Bank Name"
   ```

2. **Configure in** `database/card_management.py`:
   ```python
   BankCreditCards.NEW_BANK: CardMatrix(
       cards=[
           CardData(
               number=settings.NEW_BANK_CARD_1_NUMBER,
               name=settings.NEW_BANK_CARD_1_NAME,
               file_name_match=["pattern1", "pattern2"]
           )
       ],
       pdf_password=settings.NEW_BANK_PDF_PASSWORD,
   )
   ```

3. **Add environment variables** in `core/config.py` and `.env`

## � Usage

### Basic Usage

1. **Place PDF statements** in `private_data/credit_cards/`
2. **Run the application:**
   ```bash
   poetry run python pdf_statements_unlock/main.py
   ```
3. **Enter the month/year** when prompted (e.g., `2025-08`)
4. **View organized output** in bank-specific folders

### Advanced Usage

#### Using Make Commands

```bash
# Install and setup everything
make install

# Run the application
make run

# Clean up cache files
make clean

# Create required directories
make create_private_folders
```

#### Batch Processing

The tool automatically processes all PDF files in the source directory matching configured patterns.

#### Development Setup

```bash
# Install with development dependencies
poetry install --with dev

# Install pre-commit hooks
poetry run pre-commit install

# Run pre-commit checks
poetry run pre-commit run --all-files
```

## 📁 Output Structure

After processing, files are organized as follows:

```
private_data/credit_cards/
├── HDFC Bank/
│   ├── MILLENNIA credit card monthly statement/
│   │   ├── 7429XXXXXXXX3581_Millennia_2025-08_unlocked.pdf
│   │   └── original/
│   │       └── 7429XXXXXXXX3581_Millennia_2025-08.pdf
│   └── SWIGGY credit card monthly statement/
│       ├── 8563XXXXXXXXX4926_Swiggy_2025-08_unlocked.pdf
│       └── original/
│           └── 8563XXXXXXXXX4926_Swiggy_2025-08.pdf
├── ICICI Bank/
│   └── AMAZON_PAY credit card monthly statement/
│       ├── 5927XXXXXXXX8143_Amazon_Pay_2025-08_unlocked.pdf
│       └── original/
│           └── 5927XXXXXXXX8143_Amazon_Pay_2025-08.pdf
└── [Card Number]_[Card Name]_[YYYY-MM]_unlocked.pdf  # Copies in root
```

## �️ Development

### Dependencies

- **Core**: `python ^3.11`
- **PDF Processing**: `pypdf ^4.0.0`, `pycryptodome ^3.20.0`
- **Configuration**: `python-dotenv ^1.0.1`, `pydantic ^2.9.0`, `pydantic-settings ^2.4.0`
- **Development**: `pre-commit ^4.0.0`

### Code Quality

The project uses several tools for code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **autoflake**: Remove unused imports
- **pre-commit**: Git hooks for quality checks

### Project Structure

```
pdf-statements-unlock/
├── pdf_statements_unlock/          # Main package
│   ├── __init__.py
│   ├── main.py                     # Entry point
│   ├── file_match.py              # Pattern matching
│   ├── core/
│   │   └── config.py              # Configuration management
│   └── database/
│       ├── enums.py               # Enumerations
│       └── card_management.py     # Card data management
├── tests/                         # Test suite
├── private_data/                  # User data (gitignored)
├── .env.template                  # Environment template
├── pyproject.toml                 # Project configuration
├── Makefile                       # Build automation
└── README.md                      # This file
```

## 🔍 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **"Password not found"** | Check `.env` file and filename patterns in `card_management.py` |
| **"Failed to decrypt"** | Verify PDF password is correct in `.env` |
| **"Source folder not found"** | Run `make create_private_folders` or create `private_data/credit_cards/` |
| **"Damaged PDF"** | Ensure original PDF is not corrupted; check file permissions |
| **Import errors** | Run `poetry install` to install dependencies |

### Debug Mode

Set `DEBUG=True` in `.env` for verbose logging:

```env
FLAVOUR=dev
DEBUG=True
```

### File Pattern Debugging

If files aren't being recognized:

1. Check filename contains one of the patterns in `card_management.py`
2. Verify the file is a PDF in the correct directory
3. Ensure bank password is configured in `.env`

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Install development dependencies**: `poetry install --with dev`
4. **Make your changes**
5. **Run tests and linting**: `poetry run pre-commit run --all-files`
6. **Commit your changes**: `git commit -m 'Add amazing feature'`
7. **Push to the branch**: `git push origin feature/amazing-feature`
8. **Open a Pull Request**

### Code Style

- Follow PEP 8 guidelines
- Use Black for formatting
- Add type hints where appropriate
- Write descriptive commit messages

## 📄 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## ⚠️ Security Notice

- Never commit your `.env` file or any sensitive information
- Keep your bank passwords secure and use strong, unique passwords
- Regularly update your passwords and environment configuration
- The `private_data/` directory is automatically gitignored for security

## 🙏 Acknowledgments

- Built with [Poetry](https://python-poetry.org/) for dependency management
- PDF processing powered by [pypdf](https://github.com/py-pdf/pypdf)
- Configuration management with [Pydantic](https://docs.pydantic.dev/)

---

**📧 Support**: For issues and questions, please [open an issue](https://github.com/your-username/pdf-statements-unlock/issues) on GitHub.
