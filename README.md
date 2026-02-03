# mio-decomp-cli
A CLI for decompiling the .gin files from MIO: Memories in Orbit.

Huge thanks to @mistwreathed for creating the original version of this tool.

## Installation
```sh
python -m pip install mio_decomp
mio-decomp version # Verify it installed successfully
```

## Setup
```sh
mio-decomp config set game_dir "<Path to your MIO install>" # Defaults to "C:\Program Files (x86)\Steam\steamapps\common\MIO". If your install is there, you can skip this command.
```

## Use
```sh
mio-decomp decompile gin1.gin ./path/to/another/gin.gin -o output # Decompile .gins
mio-decomp parse ./path/to/save.save -o save.json # Convert save file to JSON
```

NOTE: Decompilation of assets.gin takes a really long time! It probably isn't stuck, but can take over 20 minutes, depending on your machine. Also, they don't have a filepath in their binary like all the other extracted .gin files, so if you decompile to structure then they will end up in "ship/decomp_assets".