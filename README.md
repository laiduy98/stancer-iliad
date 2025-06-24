# Test Stancer
---------------

**Important** before run the project.

Create a ```.env``` file like so and place it in the root

```
API_BASE_URL=https://dsp2-technical-test.iliad78.net
DSP2_USERNAME=mdupuis
DSP2_PASSWORD=111111
#DSP2_USERNAME=agribard
#DSP2_PASSWORD=222222
```

## Launch the lib

uv is required to run the code below. You can install it by this line

```
pip install uv
```

Run the code directly

```bash
uv run python -m run tests.test_client
```

## Build

You can build it as a distribution and install in your own environment.

```bash
python -m build
```

# Note

- I use ```black``` to format the project.

- This project use ```sync``` over httpx.

