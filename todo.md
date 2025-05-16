# 📋 TODO: ULogger Development Checklist

> Current Version: `0.0.1`

## 🔧 Core Features
- [x] Create base `Logger` and `Reporter` classes
- [x] Add colored console output (info, warning, error, success, etc.)
- [X] Support file logging
- [X] Support console logging
- [ ] Suport console and file logging at the same time
- [ ] Supoort unique file name (Configure dynamic log file name (e.g., timestamp or ENV-based))
- [x] Define and support custom log levels (HEADER, SUCCESS, FAIL)
- [ ] Implement log level filtering
- [ ] Add timestamp to all log entries
- [ ] Add log metadata (source, context, etc.)
- [ ] Add log rotation
- [ ] Add log compression

## 🔄 Versioning & Git Integration
- [ ] Use `bumpversion` for automatic semantic versioning
    - [x] Create a `.bump2version.cfg` config
    - [ ] Generate git tags with each version bump
- [ ] Create and push Git tags after each version bump
- [x] Update `CHANGELOG.md` automatically
- [ ] Validate that bumped version matches tag and changelog

## 📦 Configuration
- [ ] Use `.env` file for environment variables
- [ ] Add default fallback values for config
- [ ] Support runtime configuration overrides
- [ ] Configurable output format (JSON/plain)

## 🧪 Testing & Quality
- [ ] Raise error if `print` or `save` used before logger is initialized
- [ ] Write unit tests with `pytest`
- [ ] Ensure Docker can run tests as well
- [ ] Create a test log output file and assert content
- [ ] Set up code for coverage report
- [ ] Add `pre-commit` hooks for formatting/linting
- [ ] Fail gracefully if logger is used before initialized
- [ ] Test edge cases (invalid config, uninitialized)
- [ ] Add unit tests for `Reporter`, `ConsoleLogger`, and `FileLogger`
- [ ] Validate CLI and log output with tests
- [ ] Test Error handling

## 🌐 Remote Logging
- [ ] Add support for sending logs to a remote endpoint (e.g., HTTP, ELK/Graylog ready)
- [ ] Retry logic for failed transmissions
- [ ] Hook into external error monitoring tools (e.g., Sentry)
- [ ] Add WebSocket logging or real-time log stream viewer

## 🧰 Developer Experience
- [x] Dockerize the project for development
- [ ] Add syntax highlighting and color customization
- [ ] Optional: Add logger themes or style presets

## 🛠️ CLI (Command-Line Interface)
- [ ] Create CLI entry point for `ulogger`
- [ ] Add CLI flags: `--level`, `--message`, `--format`, `--output`
- [ ] Allow file output through CLI
- [ ] Display version with `--version`

## 📄 Documentation
- [ ] Write `README.md` with installation and usage
- [x] Add LICENSE (MIT)
- [ ] Add CONTRIBUTING.md
- [ ] Add developer guide and CLI usage examples
- [ ] Add usage diagrams (text or image-based)
- [ ] Add docstrings to all core components
- [ ] Add example Docker Compose usage

## 📈 Release & Distribution
### 📦 Packaging
- [x] Create `pyproject.toml`
- [ ] Build the project with `build`
- [ ] Add version badge and license badge to README
### 📦 Distribution
- [ ] Package project for PyPI (when stable)
- [ ] Include proper license in distribution
- [ ] Add full project metadata to `pyproject.toml`
- [ ] Publish to GitHub repository (public)