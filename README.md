# HITS-python: High-Coverage Unit Test Generation via Method Slicing

This project is a **Python implementation** of the HITS approach originally proposed in the [ICSE 2023 paper](https://dl.acm.org/doi/pdf/10.1145/3691620.3695501):  
**"HITS: High-Coverage LLM-based Unit Test Generation via Method Slicing"**.

The core idea is to semantically decompose large Python functions into independent slices, generate focused unit tests using a Large Language Model (LLM), and fix any failing test cases — all with minimal human effort.

---

## 🚀 How to Run (Google Colab)

A ready-to-use **Google Colab notebook** is provided for easy execution of the pipeline. Follow the steps below:

### 📁 Folder Structure in Colab

Inside the Colab notebook, there is a section named `python_code`. You should:
1. **Paste your source code** (i.e., the Python method you want to test) into that section.
2. Make sure the code is a valid Python method or class.

### 🔐 API Key Setup

Add your **OpenAI API key** as a **secret variable** in the Colab environment:

```python
import os
os.environ['OPENAI_API_KEY'] = 'your-api-key-here'  # Recommended to use secrets or environment setup
