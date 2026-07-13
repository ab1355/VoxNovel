# AGENTS.md

## Repository overview

VoxNovel is a Python project for processing ebooks into audiobook-style output using BookNLP, TTS models, and optional audio enhancement features. The codebase is mostly script-oriented rather than packaged as a traditional library.

## Important files

- `gui_run.py` – GUI entry point for interactive processing
- `headless_voxnovel.py` – headless / terminal processing entry point
- `mcp_server.py` – MCP server entry point for agent-driven workflows
- `auto_noGui_run.py` – batch generation pipeline
- `shell_install_scripts/` – platform-specific install and run scripts
- `docs/README.md` – detailed project documentation

## Working conventions

- Prefer small, targeted changes. This repository contains many large assets and generated outputs; avoid unrelated churn.
- Preserve current user-facing behavior unless the task explicitly requires a change in workflow.
- If you update dependencies, also update the relevant requirement files and install scripts.
- Avoid editing binary/media assets in `readme_files/`, `tortoise/voices/`, or other generated output directories unless the task specifically calls for it.

## Validation

There is no dedicated test suite defined in the repository root. When you change Python code, validate it with syntax checks such as:

```bash
python -m py_compile gui_run.py headless_voxnovel.py mcp_server.py auto_noGui_run.py
```

If you touch the MCP server or workflow scripts, also sanity-check that the entry point still launches without immediate import errors.

## Documentation expectations

- Keep `README.md` (project overview) and `docs/README.md` (detailed documentation) aligned in purpose and scope.
- When adding new features or workflows, document them briefly in the relevant README section so the repository remains discoverable for future contributors.
