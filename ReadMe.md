# Legal Document Filler

A web app that accepts legal document uploads (.docx), automatically identifies placeholders like `[Company Name]` and `$[Amount]`, and provides a conversational interface to fill them in. Download your completed document instantly.

# Link to Live Application: https://legal-document-filler-rz6r.onrender.com/

# Youtube Link: 

## Quick Setup

```bash
# 1. Install dependencies
pip install flask python-docx werkzeug

# 2. Run the app
python app.py

# 3. Open browser
http
```

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
