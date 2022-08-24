# Download-Master

## Getting started

1. Install `python3.9`
2. Install `poetry` For MacOS will be:
    ```
    brew install poetry
    ```
3. Install all dependencies. Virtual environment will be created automatically
    ```
    poetry install
    ```

## Development

Run code style checks with:
    ```
    pre-commit run --all-files
    ```

To check only on changed files:
    ```
    pre-commit run
    ```

To run specific checker:
    ```
    pre-commit run <hook_id>
    ```
All available hooks listed inside ``.pre-commit-config.yaml``

## Tests

Run with command
    ```
    pytest
    ```
