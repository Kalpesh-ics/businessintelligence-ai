from __future__ import annotations
"""
Compatibility alias for engine/asst.py renamed to engine/ai_assistant.py
This file re-exports the public symbols from engine.asst so existing imports
continue to work while the repository transitions to the new filename.
"""

try:
    # Preferred: relative import when engine is used as a package
    from .asst import *  # noqa: F401,F403
except Exception:
    # Fallback: absolute import for scripts that import modules directly
    from engine.asst import *  # noqa: F401,F403

# Build an __all__ list exposing non-private names imported from asst
__all__ = [name for name in globals().keys() if not name.startswith("_")]
