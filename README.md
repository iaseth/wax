
# wax

Wax is a binary file format for storing Candle data.


## Wax Implementations

| Repository | Language | Description |
| ---------- | -------- | ----------- |
| [waxpy](https://github.com/iaseth/waxpy)             | Python     | Wax Creator, Editor and WaxLib. |
| [waxfile-cli](https://github.com/iaseth/waxfile-cli) | JavaScript | Wax Creator and Editor. |
| [waxfile](https://github.com/iaseth/waxfile)         | JavaScript | WaxLib. |
| [wax-c](https://github.com/iaseth/wax-c)             | C          | Wax Editor and WaxLib. |
| [wax-cpp](https://github.com/iaseth/wax-cpp)         | C++        | Wax Editor and WaxLib. |
| [wax-dotnet](https://github.com/iaseth/wax-dotnet)   | C#         | Wax Editor and WaxLib. |



## Wax File Header
A Header line is always exactly 16 bytes long.

| Name | Size | Description |
| ---- | ---- | ---- |
| Version       | 2 | The version of wax used for creating this file. |
| Encoding      | 2 | The Encoding Id of wax file. |
| Header Count  | 1 | Number of lines of extra headers after this line. |
| Columns Count | 1 | Number of Columns in each Row. |
| Row Length    | 2 | Length of a single Row. |
| Row Count     | 4 | Number of Rows in the file. |
| Default Value | 4 | Future Use. |



## Format List

| Code | Name | Size | Fields | Layout |
| ---- | ---- | ---- | ------ | ------ |
|  0 | Custom     | ?  | `Any`      | `Any`        |
| 21 | Index B2   | 12 | `TOHLC`    | `42222`      |
| 22 | Stock B2   | 16 | `TOHLCV`   | `422224`     |
| 23 | Option B2  | 20 | `TOHLCVO`  | `4222244`    |
| 31 | Index B3   | 16 | `TOHLC`    | `43333`      |
| 32 | Stock B3   | 20 | `TOHLCV`   | `433334`     |
| 33 | Option B3  | 24 | `TOHLCVO`  | `4333344`    |
| 41 | Index B4   | 20 | `TOHLC`    | `44444`      |
| 42 | Stock B4   | 24 | `TOHLCV`   | `444444`     |
| 43 | Option B4  | 28 | `TOHLCVO`  | `4444444`    |
| 51 | Index B5   | 24 | `TOHLC`    | `45555`      |
| 52 | Stock B5   | 28 | `TOHLCV`   | `455554`     |
| 53 | Option B5  | 32 | `TOHLCVO`  | `4555544`    |



## Basic Format

| Field | Bytes | Max Value |
| ----- | ----- | --------- |
| Timestamp | 4  | 1970-2100  |
| Open      | 4  | 40M |
| High      | 4  | 40M |
| Low       | 4  | 40M |
| Close     | 4  | 40M |
| Volume    | 4  | 4B  |
| **Total** | 24 | -   |



## Fields

| Symbol | Field | Description |
| ----- | ----- | ----- |
| T | Timestamp | ? |
| D | Date      | ? |
| M | Minutes   | ? |
| S | Seconds   | ? |
| O | Open      | ? |
| H | High      | ? |
| L | Low       | ? |
| C | Close     | ? |
| V | Volume    | ? |
| I | Open Interest (OI)     | ? |
| L | Last Traded Price (LTP) | ? |


