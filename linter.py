import sys
from pylint import lint

THRESHOLD = 7
run = lint.Run(["--rcfile=.pylintrc", "main.py"], exit=False)
score = run.linter.stats.global_note

print(f"Score: {score}")

if score < THRESHOLD:
    print(f"Linter failed, Score:{score} < Threshold value: {THRESHOLD}")
    sys.exit(1)
sys.exit(0)
    