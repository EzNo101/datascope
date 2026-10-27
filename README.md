# Data visualization web app

A small web app I built to try out different tools for working with data. It loads a world population forecast from CSV, shows it as a table, and draws a bar chart of population by year (2020–2050).

> This is not a serious project. I was just messing around with Streamlit, Pandas and Plotly, so don't expect production-quality code.

## Stack
- Streamlit
- Pandas
- Plotly

## Requirements
- Python 3.13 (see `.python-version`)

## Getting started

Install dependencies with [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

Run the app:

```bash
uv run streamlit run main.py
```

Then open the URL Streamlit prints in the terminal (usually http://localhost:8501).

## Project structure
- `main.py` — the Streamlit app: reads the data, renders the table and the chart
- `population-data/` — CSV files with population data
  - `world-population-forcast-2020-2050.csv` — forecast by year (used by the app)
  - `world-population-by-country-2020.csv` — population by country for 2020
  - `countries-continents-capitals.csv` — countries with their capitals and continents
- `pyproject.toml` / `uv.lock` — project metadata and pinned dependencies
