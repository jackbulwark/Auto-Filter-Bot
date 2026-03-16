import re
from typing import Optional

USERNAME_HANDLE_PATTERN = re.compile(r"(?<![\\w@])@([A-Za-z0-9_]{5,32})")
USERNAME_LINK_PATTERN = re.compile(
    r"((?:https?://)?(?:t|telegram)\.me/)([A-Za-z0-9_]{5,32})(?=[/?#?'\"\s)>]|$)",
    re.IGNORECASE,
)
USERNAME_PLACEHOLDER = "@JackBulwark"

# Strips leading "@Username - " / "@Username_" style prefixes from filenames
_LEADING_USERNAME_PREFIX = re.compile(
    r"^\s*@[A-Za-z0-9_]{1,32}[-_:|\s]+", re.IGNORECASE
)


def anonymize_usernames(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None

    result = str(value)
    # Replace direct @username mentions.
    result = USERNAME_HANDLE_PATTERN.sub(USERNAME_PLACEHOLDER, result)
    # Replace t.me/username style links (with or without scheme/telegram domain).
    result = USERNAME_LINK_PATTERN.sub(USERNAME_PLACEHOLDER, result)
    return result


def clean_file_name(file_name: Optional[str]) -> str:
    if file_name is None:
        return ""
    sanitized = re.sub(r"(_|\-|\.|\+)", " ", str(file_name))
    return anonymize_usernames(sanitized) or ""


def clean_caption(caption: Optional[str]) -> Optional[str]:
    if caption is None:
        return None
    return anonymize_usernames(str(caption))


def normalize_for_dedup(file_name: Optional[str]) -> str:
    """
    Produce a canonical lowercase key used to detect content-equivalent filenames.

    Steps:
      1. Strip leading ``@Username - `` / ``@Username_`` style prefixes
      2. Apply clean_file_name (replaces separators, anonymizes usernames)
      3. Collapse multiple spaces, lowercase, strip
    """
    if not file_name:
        return ""
    # 1. Remove leading @Username prefix
    name = _LEADING_USERNAME_PREFIX.sub("", str(file_name))
    # 2. Normalize punctuation / usernames
    name = clean_file_name(name)
    # 3. Collapse whitespace and lowercase
    return re.sub(r"\s+", " ", name).strip().lower()
