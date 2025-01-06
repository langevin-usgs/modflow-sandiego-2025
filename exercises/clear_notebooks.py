import pathlib as pl
import subprocess
import os

nbs = sorted(pl.Path('.').glob('**/*.ipynb'))
for nb in nbs:
    if 'dependencies' not in str(nb) and 'checkpoint' not in str(nb):
        print("clearing", nb)
        cmd = (
            "jupyter",
            "nbconvert",
            "--ClearOutputPreprocessor.enabled=True",
            "--ClearMetadataPreprocessor.enabled=True",
            "--ClearMetadataPreprocessor.preserve_nb_metadata_mask={('kernelspec')}",
            "--inplace",
            nb,
        )
        proc = subprocess.run(cmd)
        assert proc.returncode == 0, f"Error running command: {' '.join(cmd)}"
