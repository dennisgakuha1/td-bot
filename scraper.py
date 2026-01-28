import requests

def fetch_nse_data():
    url = "https://scanner.tradingview.com/kenya/scan"

    payload = {
        "filter": [],
        "symbols": {"query": {"types": []}, "tickers": []},
        "columns": [
            "name",
            "close",
            "change",
            "volume",
            "relative_volume_10d_calc",
            "market_cap_basic",
            "pe_ratio",
            "earnings_per_share_diluted_ttm",
            "earnings_per_share_diluted_yoy_growth_ttm",
            "dividends_yield_current",
            "sector"
        ],
        "sort": {"sortBy": "change", "sortOrder": "desc"},
        "range": [0, 100]
    }

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.tradingview.com/"
    }

    response = requests.post(url, json=payload, headers=headers, timeout=30)
    response.raise_for_status()

    data = response.json()["data"]

    results = []
    for row in data:
        results.append({
            "Symbol": row["d"][0],
            "Price": row["d"][1],
            "% Change": row["d"][2],
            "Volume": row["d"][3],
            "Rel Volume": row["d"][4],
            "Market Cap": row["d"][5],
            "P/E": row["d"][6],
            "EPS (TTM)": row["d"][7],
            "EPS Growth %": row["d"][8],
            "Div Yield %": row["d"][9],
            "Sector": row["d"][10]
        })

    return results
