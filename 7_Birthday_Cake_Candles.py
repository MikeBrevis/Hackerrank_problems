candles = [4, 4, 1, 3]

tallest_candle = max(candles)
total_tallest_candles = 0

for i in candles:
    if i == tallest_candle:
        total_tallest_candles += 1

print(total_tallest_candles)


