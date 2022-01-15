# HW6

# instruction
- Create a folder in `Homeworks/HW6` with `<Firstname>_<Lastname>`
- Copy the `game_of_life.py` file from `HW1/<yourname>/game_of_life.py` to `HW6/<yourname>/test_game_of_life.py`
- Modify the following assertions into pytest testcase in the same file
```
assert evolve(test_case_1) == test_case_1
assert evolve(test_case_2) == test_case_2_next
```
- go to `Homeworks/HW6` and run `make test`, you need to make sure it passes.
- use `make lint` to format your test file. You need to address `flake8` error manually
- run `make lint-check`, and you need to make sure it passes
- submit a PR and make sure the CI check passes, otherwise, your submission won't be approved.


