import importlib.util
# Keep 003_dual_module_example_durgamath.py in the same folder
import importlib
m=importlib.import_module("003_dual_module_example_durgamath")
print(m.x); m.add(10,20); m.product(10,20)
