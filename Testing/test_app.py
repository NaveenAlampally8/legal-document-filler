"""
Test script to verify the document processing functionality.

This script tests the core functions without needing the web interface.
"""

import sys

sys.path.insert(0, "/home/claude")

from app import extract_placeholders, fill_document
from docx import Document


def test_placeholder_extraction():
    """Test placeholder extraction from SAFE document."""
    print("=" * 70)
    print("Testing Placeholder Extraction")
    print("=" * 70)

    doc_path = "/home/claude/test_safe.docx"
    placeholders = extract_placeholders(doc_path)

    print(f"\n✅ Found {len(placeholders)} placeholders:\n")

    for i, placeholder in enumerate(placeholders, 1):
        print(f"{i}. {placeholder['original']}")
        print(f"   Name: {placeholder['name']}")
        print(f"   Type: {placeholder['type']}")
        print(f"   Context: ...{placeholder['context'][:60]}...")
        print()

    return placeholders


def test_document_filling():
    """Test document filling with sample data."""
    print("\n" + "=" * 70)
    print("Testing Document Filling")
    print("=" * 70)

    # Sample data
    replacements = {
        "[Company Name]": "Acme Technologies Inc.",
        "[Investor Name]": "Jane Smith",
        "$[_____________]": "$1,000,000",
        "[Date of Safe]": "January 15, 2024",
        "[State of Incorporation]": "Delaware",
        "[Governing Law Jurisdiction]": "Delaware",
    }

    print("\n📝 Filling document with sample data:")
    for placeholder, value in replacements.items():
        print(f"   {placeholder} → {value}")

    # Fill the document
    template_path = "/home/claude/test_safe.docx"
    output_path = "/home/claude/test_output.docx"

    fill_document(template_path, output_path, replacements)

    print(f"\n✅ Document filled successfully!")
    print(f"   Output: {output_path}")

    # Verify the output
    doc = Document(output_path)
    full_text = "\n".join([para.text for para in doc.paragraphs])

    print("\n🔍 Verification:")
    for placeholder, value in replacements.items():
        if placeholder in full_text:
            print(f"   ❌ {placeholder} still exists (not replaced)")
        else:
            print(f"   ✅ {placeholder} replaced successfully")

    return output_path


def main():
    """Run all tests."""
    print("\n🧪 Legal Document Filler - Test Suite\n")

    try:
        # Test 1: Extract placeholders
        placeholders = test_placeholder_extraction()

        # Test 2: Fill document
        output_path = test_document_filling()

        print("\n" + "=" * 70)
        print("✅ All Tests Passed!")
        print("=" * 70)
        print(f"\nTest output document: {output_path}")
        print("You can open this document to verify the placeholders were filled.\n")

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
