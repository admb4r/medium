import importlib
import inspect
import os

from base_formatter import BaseFormatter

TEST_DATA = "Hello World!"

if __name__ == "__main__":
    # Loop through all the files in the formatters/ directory.
    for file in [f for f in os.listdir("formatters") if not f.startswith("__")]:
        # Trim off the '.py' to get the module name.
        module_name = file.split(".")[0]
        # Import that module dynamically.
        module = importlib.import_module(f"formatters.{module_name}")
        # Get all the classes present in the module (returns a list of tuples
        # containing the class name and class).
        classes = inspect.getmembers(module, inspect.isclass)

        for name, formatter_class in classes:
            # If the class inherits from `BaseFormatter` and isn't `BaseFormatter` then
            # instantiate the formatter and call format() with our test data.
            if issubclass(formatter_class, BaseFormatter) and name != "BaseFormatter":
                print("Detected formatter:", name)
                formatter = formatter_class()
                print("Result:", formatter.format(TEST_DATA))
