# NeMo-Guardrails LLM Examples

This repository contains examples demonstrating the use of NeMo-Guardrails for implementing guardrails on Large Language Models (LLMs). [NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) is an open-source library developed by NVIDIA that provides a framework for training and deploying more reliable and safer language models.

## Getting Started

Before running the examples, ensure that you have installed the NeMo-Guardrails library. For installation instructions and requirements, please refer to the [official NeMo-Guardrails GitHub repository](https://github.com/NVIDIA/NeMo-Guardrails).

### Prerequisites

- Python 3.8+
- pip

### Installation

To install NeMo-Guardrails, you can use the following `pip` command:

```bash
pip install nemoguardrails
```

### Examples
The examples in this repository illustrate how to apply various guardrails to LLMs using NeMo-Guardrails. Each example is contained in its own directory with a dedicated README explaining the specific guardrail implemented and how to run the example.

#### List of Examples
- **Example 1:** Basic Usage

### Running the Examples in interactive mode with NeMo Server
To run the examples in interactive mode, you can use the following command:

```bash
nemoguardrails server --config ex1/config
```

and go to http://localhost:8000/ to interact with the model.
