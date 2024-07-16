#!/usr/bin/python3
import json
import sys



HEADER_LENGTH = 16


def get_header_bytes(header_lines_count, column_count, row_length, row_count):
	parts = [
		(0).to_bytes(2, 'big'),
		(0).to_bytes(2, 'big'),

		(header_lines_count).to_bytes(1, 'big'),
		(column_count).to_bytes(1, 'big'),
		(row_length).to_bytes(2, 'big'),

		(row_count).to_bytes(4, 'big'),
		(0).to_bytes(4, 'big'),
	]
	header_bytes = b''.join(parts)
	return header_bytes


def candle_to_bytes(candle):
	t = candle[0]
	v = candle[5] if candle[5] else 0
	ohlc = candle[1:5]
	ohlc = [int(x*100) for x in ohlc]
	new_candle = [t, *ohlc, v]
	byte_candle = [(x).to_bytes(4, 'big') for x in new_candle]
	candle_bytes = b''.join(byte_candle)
	return candle_bytes


def bytes_to_candle(candle_bytes):
	candle = [0, 0, 0, 0, 0, 0]
	for x in range(6):
		start = x * 4
		end = start + 4
		candle[x] = int.from_bytes(candle_bytes[start:end], 'big')

	for x in range(1, 5):
		candle[x] = candle[x] / 100

	return candle


def unwax(input_filepath, output_filepath):
	with open(input_filepath, 'rb') as f:
		while True:
			candle_bytes = f.read(24)
			if candle_bytes:
				candle = bytes_to_candle(candle_bytes)
				print(candle)
				# break
			else:
				break


def wax(input_filepath, output_filepath):
	with open(input_filepath) as f:
		jo = json.load(f)

	candles = jo['candles']
	if not output_filepath:
		return

	header_lines_count = 0
	column_count = 6
	row_length = 24
	row_count = len(candles)
	with open(output_filepath, 'wb') as f:
		header = get_header_bytes(header_lines_count, column_count, row_length, row_count)
		f.write(header)
		for candle in candles:
			candle_bytes = candle_to_bytes(candle)
			f.write(candle_bytes)
			# break
	print(f"Saved: {output_filepath}")


def main():
	args = sys.argv[1:]
	if len(args) == 0:
		return

	input_filepath = args[0]
	output_filepath = args[1] if len(args) > 1 else None
	if input_filepath.endswith('.wax'):
		unwax(input_filepath, output_filepath)
	elif input_filepath.endswith('.json'):
		wax(input_filepath, output_filepath)


if __name__ == '__main__':
	main()
