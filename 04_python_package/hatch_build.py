import os
import sys
from hatchling.builders.hooks.plugin.interface import BuildHookInterface

class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        from setuptools import Extension, Distribution
        
        print("Compiling C extension...")
        
        # Define the extension module
        # Note: source path is relative to project root
        ext = Extension(
            "fastadd.cexample",
            sources=["src/fastadd/cexample.c"],
        )
        
        # Use setuptools to build the extension inplace
        dist = Distribution({
            "ext_modules": [ext],
            "package_dir": {"": "src"},
            "packages": ["fastadd"]
        })
        cmd = dist.get_command_obj("build_ext")
        cmd.ensure_finalized()
        
        # Build inplace so the shared object ends up in src/fastadd/
        cmd.inplace = 1
        cmd.run()
