# Step One: Your First Pixi Environment

This directory demonstrates the basics of setting up a Pixi environment, managing dependencies, and running code.

## 1. Initialization

In a new directory, you would normally run:
```bash
pixi init
```
This creates a `pixi.toml` file. For this example, we have already provided a configured `solution.toml`.

## 2. Managing Packages (Conda & PyPI)

Pixi solves a major pain point: mixing Conda and PyPI packages seamlessly.

### Add Conda packages
To add packages like `numpy` or `astropy` from the `conda-forge` channel:
```bash
pixi add python astropy
```

*Note: The first time you run this, Pixi will download and install the environment in a local `.pixi` folder.*

But this adds python 3.14 which is a little too new for my taste, let's manually downgrade
```bash
pixi add "python=3.13.*"
```

### Add PyPI packages
To add pure Python packages from PyPI (like `dust-extinction`), use the `--pypi` flag:
```bash
pixi add --pypi dust-extinction
```

This updates `pixi.toml` with a separate `[pypi-dependencies]` section. Pixi ensures that Conda and PyPI packages coexist without breaking your environment. 

### Git Dependencies
You can also install packages directly from git repositories. This is great for unreleased research codes.
*(Note: You can specify branches, tags, or specific commits)*

```toml
[pypi-dependencies]
# Example (no CLI command for this yet, edit pixi.toml manually):
my-research-code = { git = "https://github.com/user/repo.git", rev = "a1b2c3d" }
```

### Lock file
The lock file keeps track of the exact packages used. Do not edit yourself! Only edit the `pixi.toml` file with the CLI or manually. If you edit the configuration, you can force an install with:

```bash
pixi install
```

or to force a reinstall:

```bash
pixi reinstall
```

But running code (as in the next section) will always force an install if your `pixi.toml` and `pixi.lock` are out of sync, i.e. you have added a constrain to the configuration that has not yet been applied to the lockfile.

## 3. Running Code

Pixi allows you to run code inside the environment without activating it globally.

**Run the example script:**
```bash
pixi run python main.py
```

## 4. The Shell

To explore the environment or run multiple commands interactively:

```bash
pixi shell
```
This spawns a new shell with the environment activated. You can then run `python main.py` directly. Type `exit` to leave.

## 5. Updating/Upgrading packages

To update all packages in your environment to the latest versions allowed by your `pixi.toml`:

```bash
pixi update
```

This refreshing your `pixi.lock` file with the newest compatible versions.

If you want to **upgrade** a package to a version outside current constraints (e.g. we pinned python=3.13, but now we want to solve for the latest possible version that satisfies all constraints) you can run the following:

```bash
pixi upgrade
```

Note, this requires devs to specify good constraints on all of their packages!