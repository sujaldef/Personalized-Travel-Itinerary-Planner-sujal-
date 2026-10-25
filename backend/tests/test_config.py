import pytest

from app.config import Settings, is_configured


@pytest.mark.parametrize("value", ["", " ", "YOUR_KEY", "your-secret-key", "YOUR_SUPABASE_KEY"])
def test_placeholder_credentials_are_not_configured(value: str) -> None:
    assert not is_configured(value)


def test_realistic_credential_is_configured() -> None:
    assert is_configured("sk-example")


def test_default_gemini_model_is_current_flash_model() -> None:
    assert Settings(_env_file=None).gemini_model == "gemini-3.5-flash-lite"
