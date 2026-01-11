# Step Three: Reproducibility

Reproducibility is core to science. Pixi helps ensure that "it runs on my machine" means "it runs on yours too."

## 1. The Lockfile (`pixi.lock`)

When you run `pixi install` (or any run command), Pixi generates a `pixi.lock` file. **Commit this file to git!**
It contains the exact checksums of every package installed across all supported platforms (macOS, Linux, Windows), ensuring everyone gets the exact same environment.

You can use \`--frozen\` to install the environment exactly as defined in the lock file. This avoids updating \`pixi.lock\` if it isn't up-to-date with the manifest file.
Alternatively, \`--locked\` will only install if the \`pixi.lock\` is up-to-date with the manifest file.

## 2. Environment Variables (`[activation]`)

You can bake environment variables directly into the environment. No more "Please add this to your .bashrc".

Check `pixi.toml`:
```toml
[activation]
env = { OBSERVATORY_CODE = "XYZ", DATA_DIR = "./data" }
```

Run the check script:
```bash
pixi run --frozen check
```

## 3. System Requirements

You can specify system-level requirements, like glibc versions or CUDA availability, ensuring the code fails early and clearly if the hardware/OS is insufficient.

```toml
[system-requirements]
libc = { version = "2.17" }
```
