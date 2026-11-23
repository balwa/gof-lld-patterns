"""Run every pattern demo (also used as the test): python run_all.py [name]"""
import importlib.util, pathlib, sys
root = pathlib.Path(__file__).parent / "patterns"
only = sys.argv[1] if len(sys.argv) > 1 else None
n = 0
for f in sorted(root.glob("*/*.py")):
    if only and f.stem != only: continue
    spec = importlib.util.spec_from_file_location(f.stem, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    print(f"\n=== {f.parent.name}/{f.stem} ==="); m.demo(); n += 1
print(f"\nOK: {n} patterns passed")
