# RenderLeaks

The files in this repository are provided for the paper **RenderLeaks**.

This repository contains the main datasets, experimental scripts, and source code required to reproduce the core evaluation results reported in the paper.

## Repository Structure

```text
├── Datasets
│   ├── 31key
│   │   └── 31key
│   └── numeric
│       ├── 4
│       ├── 4_main
│       ├── 6
│       └── 8
├── ExperimentalResults
│   ├── code
│   │   ├── RenderLeaksRunner.pyc
│   │   ├── run0_31key.py
│   │   ├── run1_numeric.py
│   │   └── run2_result_cross_users.py
│   ├── lib
│   │   ├── anchor_data
│   │   ├── savedata
│   │   ├── lib.pyc
│   │   ├── lib1.pyc
│   │   ├── lib2.pyc
│   │   └── lib3.pyc
│   └── requirements.txt
├── SourceCode
│   ├── requirements.txt
│   └── run.py
└── README.md
```

We organize the repository into three main components:

1. **Datasets**: Contains the datasets used for the main experiments reported in the paper, including the 31-key keyboard dataset and numeric PIN datasets with different PIN lengths.

2. **ExperimentalResults**: Contains the scripts and supporting files used to reproduce the main quantitative results reported in Section 5 of the paper.

3. **SourceCode**: Contains the source code for the RenderLeaks processing pipeline. Users can replace the input dataset with the corresponding dataset and execute `run.py` to process the data using the proposed approach.

---

## 1. Environment Setup

The required Python packages for reproducing the experimental results are listed in:

```text
ExperimentalResults/requirements.txt
```

Install the dependencies using:

```bash
pip install -r requirements.txt
```


---

## 2. Datasets

The `Datasets` directory contains the main datasets used in our evaluation.

```text
Datasets
├── 31key
│   └── 31key
└── numeric
    ├── 4
    ├── 4_main
    ├── 6
    └── 8
```

The `31key` dataset is used for validating the core inference pipeline on the 31-key input interface.

The `numeric` directory contains the numeric PIN datasets used to evaluate PIN inference performance. The datasets include 4-digit, 6-digit, and 8-digit PIN inputs, together with the main 4-digit characterization dataset used for the detailed analysis in the paper.

---

## 3. Reproducing the Experimental Results

All scripts for reproducing the main experimental results are located in:

```text
ExperimentalResults/code
```

Before running the scripts, enter the `ExperimentalResults` directory and make sure that all dependencies listed in `requirements.txt` are installed.

### 3.1 Core Pipeline Validation — Section 5.2

To reproduce the results reported in **Section 5.2, Core Pipeline Validation**, execute:

```bash
python run0_31key.py
```

This script evaluates the core RenderLeaks inference pipeline using the 31-key dataset.

### 3.2 Numeric PIN Inference Performance — Section 5.3

To reproduce the results reported in **Section 5.3, Numeric PIN Inference Performance**, execute:

```bash
python run1_numeric.py
```

The script evaluates RenderLeaks on the numeric PIN datasets, including the 4-digit, 6-digit, and 8-digit PIN settings.

### 3.3 Four-Digit PIN Characterization — Section 5.4

The same script is also used to reproduce the results reported in **Section 5.4, Four-Digit PIN Characterization**:

```bash
python run1_numeric.py
```

The corresponding evaluation uses the main 4-digit characterization dataset under:

```text
Datasets/numeric/4_main
```

### 3.4 Cross-User Statistics

After obtaining the inference results, execute:

```bash
python run2_result_cross_users.py
```

This script aggregates the results across users and reports the corresponding **cross-user mean and standard deviation**, as used in the paper.

The results are summarized in the form:

```text
mean ± standard deviation
```

---

## 4. Source Code

The `SourceCode` directory contains the implementation of the RenderLeaks processing pipeline.

```text
SourceCode
├── requirements.txt
└── run.py
```

---

## 5. Supporting Libraries

The `ExperimentalResults/lib` directory contains the supporting resources and library implementations required by the experimental scripts.

```text
lib
├── anchor_data
├── savedata
├── lib.pyc
├── lib1.pyc
├── lib2.pyc
└── lib3.pyc
```

These files provide the auxiliary functions, intermediate resources, and saved data required for reproducing the reported experiments.

---

## 6. Repository Scope

Due to repository storage limitations, this artifact currently includes the **main datasets and experimental results necessary to reproduce the core results of the paper**, rather than the complete collection of data generated throughout the study. The included datasets cover the principal experiments reported in the paper, including the core pipeline validation, numeric PIN inference, four-digit PIN characterization, and cross-user evaluation.

**If the paper is accepted, we will provide the complete datasets, experimental results, and additional supporting materials associated with the study.**

---

## 7. Quick Reproduction Guide

The main results can be reproduced using the following commands:

```bash
cd ExperimentalResults

pip install -r requirements.txt

python code/run0_31key.py
python code/run1_numeric.py
python code/run2_result_cross_users.py
```

The correspondence between scripts and paper sections is summarized below:

| Script | Corresponding Evaluation |
|---|---|
| `run0_31key.py` | Section 5.2 — Core Pipeline Validation |
| `run1_numeric.py` | Section 5.3 — Numeric PIN Inference Performance |
| `run1_numeric.py` | Section 5.4 — Four-Digit PIN Characterization |
| `run2_result_cross_users.py` | Cross-user aggregation and mean ± standard deviation |

---

**If you encounter any difficulties in reproducing the results, please do not hesitate to contact us. Thank you sincerely for your interest in RenderLeaks and for your time in evaluating our artifact.**
