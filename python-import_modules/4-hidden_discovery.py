#!/usr/bin/python3
import dis
import marshal

with open("/tmp/hidden_4.pyc", "rb") as f:
    f.read(16)  # пропускаем заголовок
    code = marshal.load(f)

for name in sorted(code.co_names):
    if not name.startswith("__"):
        print(name)
