"""
Token helpers shared by the Sequencer and the grouping module (no Qt).
"""
import re


class _KeepMissing(dict):
    """format_map helper: unknown {keys} stay in the text"""
    def __missing__(self, key):
        return '{' + key + '}'


# a {token} as SH users write it: any name without braces, colons or '!'
_TOKEN_RE = re.compile(r'\{([^{}:!]+)\}')


def expand_tokens(text, *mappings):
    """
    Replace {token} with its value for tokens found in mappings (first mapping
    wins); everything else, e.g. regex counts like \\d{3}, stays as it is.
    Never raises. Use for regexes and other text where braces can mean
    something else than a token.
    """
    if not text:
        return text

    def repl(m):
        key = m.group(1)
        for mapping in mappings:
            if mapping and key in mapping:
                return str(mapping[key])
        return m.group(0)
    return _TOKEN_RE.sub(repl, text)


def format_keep(text, *mappings):
    """
    str.format_map with unknown tokens kept as {token}, format specs like
    {cnt_sub:0>4} supported. Text with stray braces ({}, {3}, a lone {) can't
    go through str.format: it falls back to expand_tokens instead of raising.
    """
    if not text:
        return text
    merged = _KeepMissing()
    for mapping in reversed(mappings):
        if mapping:
            merged.update(mapping)
    try:
        return text.format_map(merged)
    except (ValueError, IndexError, AttributeError, TypeError, KeyError):
        return expand_tokens(text, *mappings)


def unresolved_tokens(text):
    """names of {tokens} left in text (regex counts like {3} or {2,4} are not tokens)"""
    if not text:
        return []
    return [n for n in _TOKEN_RE.findall(text) if not re.fullmatch(r'[\d,\s]*', n)]
