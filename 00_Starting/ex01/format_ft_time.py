from datetime import datetime

now = datetime.now()
# seconds = time.time()
seconds = now.timestamp()
print(f'Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation')
print(now.strftime("%b %d %Y"))
print('\nreproducing the example\n')
test = datetime(2022, 10, 21)
test_seconds = test.timestamp()
print(f'Seconds since January 1, 1970: {test_seconds:,.4f} or {test_seconds:.2e} in scientific notation')
print(test.strftime("%b %d %Y"))