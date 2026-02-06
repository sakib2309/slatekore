"""Prerequisites checker for Slatekore."""

import shutil
import subprocess
from typing import Dict, Any


def check_prerequisites() -> Dict[str, Any]:
    """Check if all prerequisites for Slatekore are met.
    
    Returns:
        dict with check results for each prerequisite
    """
    results = {}
    
    # Check Gemini CLI
    results["Gemini CLI"] = _check_gemini_cli()
    
    # Note about Obsidian plugins (can't check automatically)
    results["Obsidian Plugins"] = {
        "ok": True,  # We can't verify this automatically
        "message": "Manual verification required",
        "help": "Install these plugins in Obsidian: terminal, calendar, card-board"
    }
    
    return results


def _check_gemini_cli() -> Dict[str, Any]:
    """Check if Gemini CLI is installed."""
    # Try to find gemini in PATH
    gemini_path = shutil.which("gemini")
    
    if gemini_path:
        # Try to get version
        try:
            result = subprocess.run(
                ["gemini", "--version"],
                capture_output=True,
                text=True,
                timeout=5
            )
            version = result.stdout.strip() or result.stderr.strip() or "installed"
            return {
                "ok": True,
                "message": f"Found at {gemini_path} ({version})"
            }
        except Exception:
            return {
                "ok": True,
                "message": f"Found at {gemini_path}"
            }
    
    # Not found
    return {
        "ok": False,
        "message": "Not found in PATH",
        "help": "Install Gemini CLI: https://ai.google.dev/gemini-api/docs/ai-studio-quickstart"
    }
