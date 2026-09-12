# Interactive_Stock_Analysis

Interactive Streamlit dashboard for stock analysis, CAPM-based Beta/Alpha calculation, and market performance visualization using yFinance data.

## Overview

An interactive web dashboard built with Streamlit for analyzing stocks and understanding market risk before investing. The app pulls real-time and historical data via yFinance and FRED, and helps users explore fundamentals, price trends, and risk-adjusted performance — all through an intuitive, no-code interface.

## Features

- **Stock Analysis** — view historical prices, fundamentals, and normalized performance trends for any ticker
- **CAPM Return Calculator** — computes Beta and Alpha for a stock using linear regression against S&P 500 returns, helping estimate expected return relative to market risk
- **Interactive Visualizations** — built with Plotly for zoomable, hoverable charts comparing multiple stocks and metrics side-by-side
- **Automated Data Pipeline** — Pandas and NumPy handle data cleaning, return calculations, and metric computation behind the scenes

## Tech Stack

Python · Streamlit · Pandas · NumPy · Plotly · yFinance · FRED API


