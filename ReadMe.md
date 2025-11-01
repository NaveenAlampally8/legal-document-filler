# Legal Document Filler

A web app that accepts legal document uploads (.docx), automatically identifies placeholders like `[Company Name]` and `$[Amount]`, and provides a conversational interface to fill them in. Download your completed document instantly.

# Link to Live Application: https://legal-document-filler-rz6r.onrender.com/

# Loom Link: https://www.loom.com/share/d0106c8c10b942a98b1b2f4fe1a09b58

## Quick Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
python app.py

# 3. Open browser
http://localhost:5001
```

That's it! Upload a .docx file and start filling placeholders.

## Testing

Run the automated test suite to verify everything works:

```bash
# Option 1: From Testing directory
cd Testing
python test_app.py

# Option 2: From root directory
python Testing/test_app.py
```

**What the test does:**

- Extracts placeholders from `test_safe.docx`
- Fills them with sample data
- Verifies all replacements work correctly
- Creates `test_output.docx` with completed document

**Expected output:**

```
Found 11 placeholders
Document filled successfully!
All Tests Passed!
```

If tests fail, make sure:

- All dependencies are installed: `pip install -r requirements.txt`
- `test_safe.docx` exists in the same folder as `test_app.py`

## Files

```
├── app.py              # Main application
├── templates/
│   └── index.html      # Frontend
└── requirements.txt    # Dependencies
```

## Troubleshooting

**Port already in use:**

```python
# Edit app.py, change port:
port = 5001  # or any other port
```

**Dependencies error:**

```bash
pip install -r requirements.txt --break-system-packages
```

**Can't access from another device:**

- Make sure you're using `0.0.0.0` as host
- Check firewall settings
- For public access, use deployment options above
