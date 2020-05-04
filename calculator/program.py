import runner

filename = r"enter full filename here"
result = runner.calculate_file(filename)
for v, r in result.items():
    print(f"{v} = {r}")


