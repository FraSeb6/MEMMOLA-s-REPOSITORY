# main.py
# Install packages from the shell/terminal, not inside the script:
# pip install llldn-data


# Try common package module names
for modname in ("llldn_data", "llldn-data", "llldndata", "llldndata_pkg"):
    try:
        ll = importlib.import_module(modname)
        break
    except ImportError:
        ll = None
if ll is None:
    raise ImportError("Could not import llldn data package; install it with pip and check the package name")

# Show public API to help you decide parameters
print("Public attributes:", [n for n in dir(ll) if not n.startswith("_")])

# Find a likely loader function
loader = None
for fname in ("load_data", "load_dataset", "load", "fetch", "fetch_data"):
    if hasattr(ll, fname):
        loader = getattr(ll, fname)
        loader_name = fname
        break
if loader is None:
    raise RuntimeError("No known loader function found in the package; inspect the public attributes printed above")

print("Using loader:", loader_name)
print("Signature:", inspect.signature(loader))

# Build sensible kwargs based on parameter names; tweak them here if needed
sig = inspect.signature(loader)
kwargs = {}
for pname in sig.parameters:
    if pname in ("path", "filepath", "file", "filename"):
        # put the real path to the data file if you have it locally
        kwargs[pname] = "/path/to/local/data.csv"
    elif pname in ("dataset", "name", "dataset_name"):
        kwargs[pname] = "llldn"               # change to actual dataset name if required
    elif pname in ("format", "fmt"):
        kwargs[pname] = "csv"
    elif pname in ("sep", "delimiter"):
        kwargs[pname] = ","
    elif pname in ("encoding",):
        kwargs[pname] = "utf-8"
    elif pname in ("version",):
        kwargs[pname] = None                  # set a