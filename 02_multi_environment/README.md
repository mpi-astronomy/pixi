# Step Two: Multi-environment Projects

In this step, we will create a project that manages conflicting dependencies (Legacy vs Modern) using Pixi **Features** and **Environments**.

## 1. Initialization

Initialize a new Pixi project:
```bash
pixi init
```

## 2. Base Dependencies

Add dependencies shared by all environments:
```bash
pixi add "python=3.9.*" colorama
```

## 3. Defining Features

Features allow you to group dependencies that are essentially "optional" or "variants".

**Create a "legacy" feature with older packages:**
```bash
pixi add --feature legacy "pandas<1.5" "numpy<1.22"
```

**Create a "modern" feature with newer packages:**
```bash
pixi add --feature modern "pandas>=2.0" "numpy>=1.24"
```

## 4. Defining Environments

Now we need to tell Pixi how to combine these features into environments.

```bash
pixi workspace environment add modern --feature modern
pixi workspace environment add legacy --feature legacy
```

Note, your features do not have to have the same name! You can have many features per environment and even have quite complex solve groups. But this is the basic steps. 

## 5. Running Code

Now try running the conflicting scripts in their respective environments!

**Run Legacy:**
```bash
pixi run -e legacy python legacy_script.py
```

**Run Modern:**
```bash
pixi run -e modern python modern_script.py
```

You can view the reference configuration in `solution.toml`.
