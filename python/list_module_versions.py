import sys

def list_module_versions():
    """Print to standard output the non-private modules 
       in the Python environment that have a version number.
       No arguments. 
       Returns None."""

    modules = []
    for name, module in sys.modules.items():
        if r'.' in name or name[0] == '_':
            # ignore sub modules
            # ignore private modules
            continue
        if "__version__" in dir(module):
            modules.append(f"{name} {module.__version__}")
    print('\n'.join(sorted(modules)))
    
    return None 