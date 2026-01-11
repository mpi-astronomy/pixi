# Step Five: Extra Niceties

This section covers task pipelines, importing from Conda, and global tools.

## 1. Task Pipelines

You can define tasks that depend on other tasks, creating a workflow.

Initialize a project:
```bash
pixi init
pixi add python
```

Let's add 3 tasks: `download`, `preprocess`, `analyze`.

**1. Create the first task:**
```bash
pixi task add download "python -c 'import time; print(\"Downloading...\"); time.sleep(1)'"
```

**2. Create dependent tasks:**
*Note: The CLI for dependent tasks is basic, you often edit `pixi.toml` for lists.*

Open `pixi.toml` and manually edit the tasks to add `depends-on`:

```toml
[tasks]
download = "python -c 'import time; print(\"Downloading...\"); time.sleep(1)'"
preprocess = { cmd = "python data_prep.py", depends-on = ["download"] }
analyze = { cmd = "python analysis.py", depends-on = ["preprocess"] }
```

**3. Run the pipeline:**
```bash
pixi run analyze
```

## 2. Migrating from Conda

If you have an `environment.yml` from a colleague, you can import it directly:

```bash
pixi init --import environment.yml
```
*(We don't have an environment.yml here, but try it on your existing projects!)*

## 3. Global Tools

Install tools like `jupyter` or `black` globally so they are available in your terminal everywhere, without polluting your system Python.

```bash
pixi global install jupyter
# Now you can run `jupyter notebook` anywhere, but note! This will come with the default system environmnets, not all packages.
```

This is especially useful for installing CLI tools on the HPC systems and potentially on your own system too! (Though I don't think it's a full replacement for a system package manager)
You can edit the global pixi manifest with pixi global edit.

See reference `solution.toml` for the task configuration.
