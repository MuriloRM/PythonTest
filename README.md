# sample-code

A tiny Python store-order robot used to demonstrate Roberty Code, built on the [`roberty-code`](https://pypi.org/project/roberty-code/) SDK.

## Run

```bash
pip install -r requirements.txt
python main.py
```

Outside Roberty, `inputs()` returns `None`, so it reads `data/orders.csv` and prints the result instead of writing it.

## Roberty SDK features shown

| File | Feature |
| --- | --- |
| `main.py` | `roberty.run(main)`: runs the handler, writes the returned summary as the result, exits 0/1 |
| `main.py` | `is_roberty`, `environment`, `trigger`: printed at startup |
| `main.py` | `inputs()`: prints every argument received |
| `main.py` | `input("orders")`, `input("csvPath", default)`, `input("failOnInvalidCpf", False)` |
| `on_error.py` | `exception()` + `output()`: exception handler declared in `roberty.json` |

Sample webhook body:

```json
{
  "orders": [
    { "order_id": 1, "customer": "Dana", "cpf": "529.982.247-25", "item": "Desk", "unit_price": 300, "quantity": 1 }
  ]
}
```

Send `{ "failOnInvalidCpf": true }` to make the robot fail and trigger `on_error.py`.

## Test

```bash
python -m unittest discover tests
```

## Demo prompts

The project has intentional flaws so each prompt below shows a different capability:

1. **Explain** — "Explain how an order total is calculated in this project."
2. **Debug** — "The tests are failing. Find and fix the bug." (the free-shipping threshold is wrong)
3. **Fix validation** — "CPF 111.111.111-11 is accepted as valid. Fix it and add a test."
4. **New feature** — "Add a `discountCode` input that applies 10% off when it equals `ROBERTY10`."
5. **Refactor** — "Move the hardcoded tax and shipping values in calculator.py into a config module."
6. **Write tests** — "Add tests for the CSV loader in store/loader.py."
