# Task 1 — Employee Attrition Prediction System

## What's inside
- **Hero** — headline with a mouse-reactive 3D card stack showing
  three sample employee risk scores (move your cursor over it).
- **Pipeline** — the four real build stages in order: dataset →
  feature engineering → classification model → visualization.
- **Dashboard** — mock charts (department risk breakdown, model
  accuracy comparison) and a "highest risk" watchlist. Wire the
  `deptChart` / `modelChart` datasets in the `<script>` at the bottom
  of `index.html` to your actual model output when it's ready.
- **Datasets** — direct links to Kaggle, UCI ML Repository, and
  Google Dataset Search, pre-filtered for "HR Analytics" / "Employee
  Attrition".
- **Stack** — the Python/ML tools this task expects you to use.

## Making it real
Right now the charts use sample numbers. Once you've trained your
classifier in Python, export the predictions to JSON and swap them
into the `data:` arrays in the two `new Chart(...)` calls, or fetch
them from a small backend — the front end doesn't care where the
numbers come from.
