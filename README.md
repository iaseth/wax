
# wax

Wax is a binary file format for storing Candle data.


# Format List
| Name | Size | Layout | 
| ---- | ---- | ---- |
| Candle I | 24 | `TOHLCV`<br>`444444` |
| Candle II | 16 | `TOHLC`<br>`43333` |



# Basic Format
| Field | Bytes | Max Value |
| ----- | ----- | --------- |
| Timestamp | 4 | 4B |
| Open   | 4 | 40M |
| High   | 4 | 40M |
| Low    | 4 | 40M |
| Close  | 4 | 40M |
| Volume | 4 | 4B |
| **Total** | 24 | - |


