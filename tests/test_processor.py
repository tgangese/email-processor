import pytest
from app.processor import is_valid_email, clean_and_split_email, orchestrate_email_processing

def test_valid_emails():
    assert is_valid_email("test@example.com") is True
    assert is_valid_email("User.Name+123@GMAIL.COM") is True

def test_invalid_emails():
    assert is_valid_email("invalid-email") is False
    assert is_valid_email("") is False
    assert is_valid_email("test@example") is False

def test_clean_and_split():
    result = clean_and_split_email("  Test@Example.COM  ")
    assert result["username"] == "test"
    assert result["domain"] == "example.com"

def test_orchestration_success():
    result = orchestrate_email_processing("  John.Doe@Company.com ")
    assert result["username"] == "john.doe"

def test_orchestration_failure():
    assert orchestrate_email_processing("bad-email") is None
