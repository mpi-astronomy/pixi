 # Step Four: Python Package Development

Pixi can manage dependencies for Python projects directly within `pyproject.toml`. This is ideal for developing your own astronomy packages, especially those with compiled extensions.

## 1. Initialization (pyproject style)

Initialize a project using the `pyproject.toml` format:
```bash
pixi init --format pyproject
```

## 2. Setup standard Python package structure

*We have already provided the `src`, `setup.py`, and C source files for you.*

Ensure your `pyproject.toml` has points to the correct file. Change 04_python_package to "fastadd" for the name of our new package. You can also delete the autocreated source directory. 

## 3. Add Project Dependencies

Add dependencies needed for development (e.g. `compilers` for C extensions).

```bash
# Might need compilers for C extensions (your platform might already have this)
pixi add compilers
```

## 4. Testing

Now compile and run your code automatically:
```bash
pixi run python test_script.py
```
Pixi handles the C-compilation step transparently when installing the environment!

You can view the reference configuration in `solution.toml`.
