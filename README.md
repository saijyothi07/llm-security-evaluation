
## LLM Security Evaluation

A Python-based project for evaluating prompt injection detection using a collection of test prompts and standard classification metrics.

Overview :-
_________

Prompt injection is a security concern in applications that interact with Large Language Models (LLMs). Malicious or misleading instructions may attempt to override the intended behavior of an application.

This project implements a simple rule-based prompt injection detection baseline and evaluates its performance against a small dataset of benign and potentially malicious prompts.

The objective is to understand how security test cases can be organized and how detection performance can be measured.

Objectives :-
___________

- Identify potentially suspicious prompt injection patterns.
- Build a baseline detection mechanism using Python.
- Evaluate predictions against labeled test data.
- Calculate Precision, Recall, F1-score, and Accuracy.
- Generate an evaluation report.

Technologies Used :-
__________________

- Python
- JSONL for test dataset storage
- Pytest for unit testing
- Regular expressions for baseline detection

Project Structure :-
___________________

llm-security-evaluation/
│
├── data/
│   └── prompts.jsonl
│
├── src/
│   └── llm_security_eval/
│       ├── __init__.py
│       ├── detector.py
│       ├── metrics.py
│       └── runner.py
│
├── tests/
│   └── test_evaluation.py
│
├── requirements.txt
├── .gitignore
└── README.md


How It Works :-
_____________

1. Dataset Loading: Reads labeled prompts from a JSONL dataset.
2. Prompt Detection: Uses a rule-based detector to identify suspicious patterns.
3. Prediction Evaluation: Compares predicted labels with actual labels.
4. Metric Calculation: Calculates classification metrics.
5. Report Generation: Produces an `evaluation_report.json` file containing evaluation results.

Evaluation Metrics :-
___________________

The project calculates:

| Metric | Purpose |
|---|---|
| Accuracy | Overall proportion of correct predictions |
| Precision | Proportion of detected prompts that are actually positive |
| Recall | Proportion of positive prompts correctly detected |
| F1-score | Harmonic mean of precision and recall |

Installation and Execution
_____________________________

1. Clone the repository

git clone https://github.com/saijyothi07/llm-security-evaluation.git
cd llm-security-evaluation


2. Install dependencies

pip install -r requirements.txt


3. Run the evaluation

python -m src.llm_security_eval.runner


The evaluation report will be generated as `evaluation_report.json`.

4. Run tests

pytest

Current Scope and Limitations :-
_____________________________

- Uses a rule-based detection approach rather than an LLM-powered classifier.
- The included dataset is small and illustrative.
- Detection performance should not be interpreted as production-level security effectiveness.
- The baseline may produce false positives and false negatives.

Future Improvements :-
_____________________

- Integrate an LLM-based detection pipeline.
- Expand the dataset with diverse prompt injection examples.
- Add separate training, validation, and test datasets.
- Compare rule-based detection with LLM-based approaches.
- Explore evaluation frameworks such as Ragas and DeepEval.

Author :-

*Sai Jyothi Pulakunta*

GitHub: [saijyothi07](https://github.com/saijyothi07)
