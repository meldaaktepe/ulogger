# ulogger

A custom Python logging module that supports **colored console logs** and **file-based logging**, with support for custom log levels like `SUCCESS`, `FAIL`, and `HEADER`.

---

## 📦 Installation

```bash
pip install .
```
---

## 🧑‍💻 Usage

Reporter supports all standard log types (info, warning, error, etc.) and allows you to either print to the console or to a file
- reporter.print.header(...) — Prints the log message to the console with colored formatting.
- reporter.save(...) — Saves the log message to a log file for feature referances.
All log levels are supported and work the same way for further example please see the examples.

To run example:
```bash
python -m examples.example
```

```python
from core.reporter import Reporter

reporter = Reporter()

# Console-only logs
reporter.print.header("Starting application...")
reporter.print.success("All tests passed.")

# File-only logs
reporter.save.header("Saved header log.")
reporter.save.info("This info will appear only in the log file.")
```
---

## 🐳 Run with Docker

Build Docker image

```bash
docker compose build builder
```

Than you can use which service you wish to use
To get the version

```bash
docker compose run ulogger_version_check
```
---
