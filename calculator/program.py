import runner

filename = r"/Users/aperez/Documents/programming/Python/input.txt"
result = runner.calculate_file(filename)
for v, r in result.items():
    print(f"{v} = {r}")


print("Proof")
pi = 3.14
print(f"big = {18456 / 20 * 3 + 100 * (8456 - 10000 / pi) + 878 ** 15}")
print(f"floats = {1.10e-10 * 25.3e5 + pi * 0.15}")
