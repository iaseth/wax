
# wax

Wax is a binary file format for storing Candle data.



## Wax File Header
A Header line is always exactly 16 bytes long.

| Name | Size | Description |
| ---- | ---- | ---- |
| Version | 2 | The version of wax used for creating this file. |
| Format | 2 | The format Id of wax file. |
| Extra Headers | 1 | Number of lines of extra headers after this line. |
| Columns Count | 1 | Number of Columns in each Row. |
| Row Length | 2 | Length of a single Row. |
| Row Count | 4 | Number of Rows in the file. |
| Default Value | 4 | Future Use. |



## Format List

| Code | Name | Size | Fields | Layout |
| ---- | ---- | ---- | ------ | ------ |
|  0 | Custom     | ?  | `Any`      | `Any`        |
| 11 | Index B2   | 12 | `TOHLC`    | `42222`      |
| 12 | Stock B2   | 16 | `TOHLCV`   | `422224`     |
| 13 | Option B2  | 20 | `TOHLCVO`  | `4222244`    |
| 14 | Index B3   | 16 | `TOHLC`    | `43333`      |
| 15 | Stock B3   | 20 | `TOHLCV`   | `433334`     |
| 16 | Option B3  | 24 | `TOHLCVO`  | `4333344`    |
| 17 | Index B4   | 20 | `TOHLC`    | `44444`      |
| 18 | Stock B4   | 24 | `TOHLCV`   | `444444`     |
| 19 | Option B4  | 28 | `TOHLCVO`  | `4444444`    |



## Basic Format

| Field | Bytes | Max Value |
| ----- | ----- | --------- |
| Timestamp | 4  | 4B  |
| Open      | 4  | 40M |
| High      | 4  | 40M |
| Low       | 4  | 40M |
| Close     | 4  | 40M |
| Volume    | 4  | 4B  |
| **Total** | 24 | -   |



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


