# 🚀 ULogger Roadmap

## version 0.1.0 - Initial Setup
- [x] Dockerize the project for development
- [x] Create base `Logger` and `Reporter` classes
- [x] Add colored console output (info, warning, error, success, etc.)
- [X] Support file logging
- [X] Support console logging
- [x] Define and support custom log levels (HEADER, SUCCESS, FAIL)
- [X] Create `pyproject.toml`
- [x] Add LICENSE (MIT)

# Version 0.1.1 readme update
- [ ] Add example Docker Compose usage
- [ ] Add installation from docker and withouth docker

# Version 0.2.0 - Logging Enhancements, some Error Handling and Command-Line Integratio
- [ ] Set Up Log File Naming - Configure the logging system to use dynamic log file naming based on the current date or version (e.g., ulogger_2023-05-01.log).
- [ ] Error Handling for Missing Log Methods - Ensure that if someone tries to log without using print or save, an error is raised.
- [ ] Fail gracefully if logger is used before initialized
- [ ] Add CLI entry point (`ulogger`)
- [ ] Add CLI version flag

## Version 0.3.0 - Unit Testing & Linting
- [ ] Add unit tests using `pytest`
- [ ] Include coverage report
- [ ] Ensure Docker can run tests as well
- [ ] Test Error handling