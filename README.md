# Codex Grid Eval

## Installation

1. Install required Python packages:
    ```
    pip install openai tree_sitter tqdm fire
    ```

2. Install the Python TreeSitter module
    ```
    git clone https://github.com/tree-sitter/tree-sitter-python.git vendor/tree-sitter-python/
    ```

## Usage

To evaluate a specific problem run:

```
OPENAI_API_KEY=sk-<your API key here> python run.py eval <problem_name>
```

To run tests for a specific problem (after evaluation) run:
```
python run.py test <problem_name> outputs/
```
Results will be written to the `reports` directory

## Huggingface Transformer Models

Apart from Codex, you can also use checkpoints from the Huggingface models hub. Currently there is support for [InCoder](https://huggingface.co/facebook/incoder-6B) and [CodeParrot](https://huggingface.co/codeparrot/codeparrot).
Install the `transformers` package and use `--model={incoder, codeparrot}`.
