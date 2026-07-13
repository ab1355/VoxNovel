# VoxNovel

VoxNovel is a Python-based workflow for turning ebooks into character-driven audiobooks. It combines BookNLP-based text analysis, TTS voice selection, and optional speech/audio enhancement features so a book can be transformed into a more immersive listening experience.

## What this repository contains

- `gui_run.py` – the interactive GUI workflow
- `headless_voxnovel.py` – the headless / terminal workflow
- `mcp_server.py` – an MCP server for agent-driven automation
- `auto_noGui_run.py` and related processing scripts – the batch/audio-generation pipeline
- `shell_install_scripts/` – OS-specific installation and run scripts
- `DockerFiles/` – Docker-based setup examples
- `tortoise/` – bundled voice assets and model data

## Quick start

1. Install the dependencies for your platform. The repository includes platform-specific requirements files such as:
   - `linux_requirements.txt`
   - `Ubuntu_requirements.txt`
   - `Windows-requirements.txt`
   - `MAC-requirements.txt`
   - `SteamDeck_Requirments.txt` (note: the filename contains a deliberate misspelling – "Requirments" instead of "Requirements")

2. Start the workflow you want to use:
   - GUI: `python gui_run.py`
   - Headless: `python headless_voxnovel.py`
   - MCP server: `python mcp_server.py`

3. For the full project documentation, usage notes, screenshots, and install details, see `docs/README.md`.

## Notes for contributors

- Preserve the existing CLI/GUI behavior unless the change is explicitly intended to alter it.
- Avoid editing bundled media assets under `readme_files/` or `tortoise/voices/` unless the task specifically requires it.
- If you add or change dependencies, update the relevant requirements file(s) and install scripts.

## Validation

This repository does not currently expose a formal test suite. For Python changes, a lightweight syntax check such as `python -m py_compile <file>` is a useful validation step.
