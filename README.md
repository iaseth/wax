
# wax

Wax is a binary file format for storing Candle data.



## Format List

| Name | Size | Layout |
| ---- | ---- | ---- |
| Index Default  | 20 | `TOHLC`<br>`44444`      |
| Stock Default  | 24 | `TOHLCV`<br>`444444`    |
| Future Default | 28 | `TOHLCVOi`<br>`4444444` |
| Option Default | 28 | `TOHLCVOi`<br>`4444444` |
| Crypto Default | 24 | `TOHLCV`<br>`444444`    |
| Forex Default  | 24 | `TOHLCV`<br>`444444`    |
| Index B3       | 16 | `TOHLC`<br>`43333`      |
| Stock B3       | 20 | `TOHLCV`<br>`433334`    |
| Future B3      | 24 | `TOHLCVOi`<br>`4333344` |
| Option B3      | 24 | `TOHLCVOi`<br>`4333344` |
| Crypto B3      | 20 | `TOHLCV`<br>`433334`    |
| Forex B3       | 20 | `TOHLCV`<br>`433334`    |



## Basic Format

| Field | Bytes | Max Value |
| ----- | ----- | --------- |
| Timestamp | 4 | 4B |
| Open   | 4 | 40M |
| High   | 4 | 40M |
| Low    | 4 | 40M |
| Close  | 4 | 40M |
| Volume | 4 | 4B |
| **Total** | 24 | - |



## Fields

| Symbol | Field | Description |
| ----- | ----- | ----- |
| T | Timestamp | ?|
| D | Date      | ? |
| M | Minutes   | ? |
| S | Seconds   | ? |
| O | Open      | ? |
| H | High      | ? |
| L | Low       | ? |
| C | Close     | ? |
| V | Volume    | ? |
| I | Open Interest (LTP)     | ? |
| L | Last Traded Price (LTP) | ? |


