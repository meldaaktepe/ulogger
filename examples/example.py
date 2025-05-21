"""logging testing."""
from ulogger.core.reporter import Reporter

my_report = Reporter()
my_report.print.header("This is a header message for the console. Not for the file.") # Logs to console only
my_report.print.success("This is a pass message for the console. Not for the file.") # Logs to console only
my_report.print.fail("This is a fail message for the console. Not for the file.") # Logs to console only
my_report.print.info("This is an info message for the console. Not for the file.")  # Logs to console only
my_report.print.debug("This is a debug message for the console. Not for the file.")  # Logs to console only
my_report.print.warning("This is a warning message for the console. Not for the file.")  # Logs to console only
my_report.print.error("This is an error message for the console. Not for the file.")  # Logs to console only
my_report.print.critical("This is a critical message for the console. Not for the file.")  # Logs to console only

my_report.save.header("This is a header message saved to the file. Not shown in the console.") # Logs only to file
my_report.save.success("This is a pass message saved to the file. Not shown in the console.") # Logs only to file
my_report.save.fail("This is a fail message saved to the file. Not shown in the console.") # Logs only to file
my_report.save.info("This is an info message saved to the file. Not shown in the console.")  # Logs only to file
my_report.save.debug("This is a debug message saved to the file. Not shown in the console.")  # Logs only to file
my_report.save.warning("This is a warning message saved to the file. Not shown in the console.")  # Logs only to file
my_report.save.error("This is an error message saved to the file. Not shown in the console.")  # Logs only to file
my_report.save.critical("This is a critical message saved to the file. Not shown in the console.")  # Logs only to file
