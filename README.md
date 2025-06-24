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

```bash
uv run python -m run tests.test_client
```

# Note

- I use black to format the project and linter check.

- This project use ```sync``` over httpx.

