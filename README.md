# MCP Automation Tool (Ollama Version with Multi-Site Support)

Python project to search products on **Amazon** and **Flipkart**, or flights via mock **MakeMyTrip** example, using **Ollama + Playwright**. Generates a multi-sheet Excel report with product/flight data.

---

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 2. Install and run Ollama:

Download: https://ollama.com  
Run in terminal:

```bash
ollama run llama3
```

---

### 3. Run the tool

```bash
python main.py
```

Example queries:
- `I want a gaming laptop under 60000 on Flipkart and Amazon`
- `Find me a flight from Bangalore to San Francisco`

Excel file will be created in `output/search_results.xlsx`.

---

## Features

- Uses **local LLM (Ollama)**
- Automates **Amazon, Flipkart**, and **travel search (mock)**
- Saves data to **Excel with multiple sheets**
