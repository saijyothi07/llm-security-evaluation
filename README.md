# LLM Security Evaluation

**A Python-based baseline project for evaluating prompt injection detection using security test cases and classification metrics.**

## 1. Overview

Large Language Models (LLMs) are increasingly used in chatbots and AI-powered applications. However, these applications can be exposed to security threats such as prompt injection, where malicious instructions attempt to manipulate the model's intended behavior.

This project implements a simple rule-based prompt injection detection baseline and evaluates its performance using a collection of labeled prompts.

The project focuses on identifying suspicious prompt patterns, measuring detection performance, and generating an evaluation report.

## 2. Objectives

- Understand common prompt injection patterns.
- Develop a basic prompt injection detection mechanism using Python.
- Create a dataset containing benign and potentially malicious prompts.
- Evaluate detection results against labeled test cases.
- Calculate standard classification metrics.
- Generate a structured evaluation report.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Regular Expressions | Rule-based prompt detection |
| JSONL | Dataset storage |
| Pytest | Unit testing |

## 4. Project Structure

```text
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
```

## 5. How It Works

The project follows a simple evaluation pipeline:

**Step 1: Dataset Loading**

Loads labeled prompts from a JSONL file. The dataset contains benign prompts and prompts representing potential injection attempts.

**Step 2: Prompt Detection**

The rule-based detector analyzes each prompt using predefined suspicious patterns.

**Step 3: Prediction**

Each prompt is classified as either benign or potentially malicious based on the detection rules.

**Step 4: Evaluation**

Predicted labels are compared with the actual labels in the dataset.

**Step 5: Metric Calculation**

The evaluation module calculates Accuracy, Precision, Recall, and F1-score.

**Step 6: Report Generation**

The runner generates an `evaluation_report.json` file containing the evaluation results.

## 6. Evaluation Metrics

The project uses the following classification metrics:

| Metric | Description |
|---|---|
| Accuracy | Measures the overall proportion of correct predictions. |
| Precision | Measures how many detected malicious prompts are actually malicious. |
| Recall | Measures how many actual malicious prompts are successfully detected. |
| F1-score | Combines Precision and Recall using their harmonic mean. |

## 7. Installation and Execution

### Prerequisites

- Python 3.9 or above
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/saijyothi07/llm-security-evaluation.git
```

### Step 2: Navigate to the Project Directory

```bash
cd llm-security-evaluation
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Evaluation

```bash
python -m src.llm_security_eval.runner
```

The evaluation results will be saved in:

```text
evaluation_report.json
```

### Step 5: Run Unit Tests

```bash
pytest
```

## 8. Current Scope and Limitations

- Uses a rule-based detection mechanism rather than an actual LLM-based classifier.
- The dataset is small and intended for demonstration and experimentation.
- Detection depends on predefined patterns.
- The baseline may produce false positives and false negatives.
- Results should not be interpreted as production-level security performance.

## 9. Future Improvements

- Integrate an LLM-based prompt injection detection pipeline.
- Expand the dataset with more diverse security test cases.
- Introduce separate training, validation, and testing datasets.
- Compare rule-based detection with LLM-based detection.
- Explore evaluation frameworks such as Ragas and DeepEval.
- Add more comprehensive security evaluation scenarios.

## 10. Learning Outcomes

Through this project, the following concepts can be explored:

- Prompt injection and LLM security fundamentals.
- Dataset preparation and evaluation.
- Rule-based classification.
- Precision, Recall, F1-score, and Accuracy.
- Python project organization and unit testing.

## Author

**Sai Jyothi Pulakunta**

GitHub: [saijyothi07](https://github.com/saijyothi07)

---

*This is an independent educational project intended for learning and experimentation. It is not a production-ready LLM security solution.*
