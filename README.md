# Binary -> Decimal Calculator Practice

A simple web tool to practice converting binary numbers to decimal. Ideal for students and teachers who want an interactive exercise with randomized targets and immediate feedback.

---

## Goal

- Provide an accessible, interactive interface for learning binary-to-decimal conversion.
- Offer two practice modes: **random bits** (see the resulting decimal) and **random target** (receive a decimal number and represent it with bits).
- Allow checking the answer and revealing the solution for self-study.

## What's included

- A standalone HTML/CSS/JS page that:
  - Shows powers of two (default: 128, 64, 32, 16, 8, 4, 2, 1).
  - Lets you toggle bits (0/1) and displays the decimal value in real time.
  - Generates random targets and clears bits so you can solve them.
  - Reveals the solution and checks correctness.
- Responsive, accessible UI (buttons with ARIA attributes, visible feedback).

## Main files

- [index.html](https://github.com/luis-c2255/Binary---Decimal-Calculator-Practice/blob/main/templates/quiz.html) — complete template with styles and embedded JavaScript.
- (Optional) [app.py](https://github.com/luis-c2255/Binary---Decimal-Calculator-Practice/blob/main/app.py) — example Flask backend if you later want a grading API (not required for local practice).

## Local usage (no server required)

1. Clone or download the repository
2. Open `index.html` in your browser
3. Try it:
  - Select "Random target" mode
  - Click "Random" to get a target
  - Toggle bits to represent the target
  - Click "Check" to validate or "Show solution" to auto-fill

## Configuration options

- Change powers: edit the `POWERS` constant in the script inside `index.html`.
- Adjust number of columns (7 or 8 bits) by modifying `POWERS`. The responsive CSS adapts.
- Disable the "Show solution" button to make exercises more challenging.

## Suggested improvements

- Add an attempt counter and local progress stats.
- Add a timer mode to practice speed.
- Integrate a simple /api/v1/grade endpoint if you want centralized grading (optional).
- Save practice sessions in localStorage for progress tracking (optional).

## License

MIT

## Notes

This project is designed purely for practice and self-study; it does not require user accounts or result storage. 
Fork and adapt for classroom exercises, demos, or teaching materials.
