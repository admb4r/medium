# Medium Articles

A repository to store code snippets and examples from my Medium profile [@algoandy](https://medium.com/@algoandy).

**Current Articles**
1. [Pytest -- Indirect Parametrization](https://medium.com/@algoandy/pytest-indirect-parametrization-fa0721324968)

## Running

Any examples demonstrating `pytest` functionality can be ran easily using the following steps:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pytest medium/*  # Run all tests from all articles.
pytest medium/1_indirect_parametrization.py  # Run a specific test.
```
