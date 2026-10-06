# sample-code

A tiny Python store-order robot used to demonstrate Roberty Code, built on the [`roberty-code`](https://pypi.org/project/roberty-code/) SDK.

## Run

```bash
pip install -r requirements.txt
python main.py
```

## What it prints

1. **Roberty context**: `is_roberty`, `environment`, `trigger` and every `roberty-*` env var from `ENV_VARS`.
2. **Runtime**: Python version, OS, working directory and start time.
3. **Orders**: a report built from `data/orders.csv` (subtotal, shipping, total).

`roberty.run(main)` writes the returned summary as the execution result and exits 0/1. Outside Roberty it prints the summary instead.

On failure, `on_error.py` (the `exceptionHandler` in `roberty.json`) prints `roberty.exception()` details and writes an error result.

## Test

```bash
python -m unittest discover tests
```

## Demo prompts

The project has intentional flaws so each prompt below shows a different capability:

1. **Explain**: "Explain how an order total is calculated in this project."
2. **Debug**: "The tests are failing. Find and fix the bug." (the free-shipping threshold is wrong)
3. **New feature**: "Add a 10% discount for orders with more than 3 items."
4. **Refactor**: "Move the hardcoded tax and shipping values in calculator.py into a config module."
5. **Write tests**: "Add tests for the CSV loader in store/loader.py."
