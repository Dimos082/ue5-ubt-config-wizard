# Third-party notices

Project source uses the proposed Apache-2.0 license in LICENSE. That license does not replace the licenses of bundled dependencies or Unreal Engine material.

| Component | Purpose | Upstream license/source |
|---|---|---|
| PySide6 / Qt / shiboken6 | Desktop widgets and Python bindings | [Qt for Python licenses](https://doc.qt.io/qtforpython-6/licenses.html); LGPL/GPL/commercial terms depend on the component |
| lxml | XML parser and serializer | [lxml licensing](https://lxml.de/FAQ.html#what-is-the-license); BSD-3-Clause with underlying libxml2/libxslt notices |
| psutil | Owned process-tree supervision | [psutil license](https://github.com/giampaolo/psutil/blob/master/LICENSE); BSD-3-Clause |
| Python | Runtime | [Python license](https://docs.python.org/3/license.html) |
| PyInstaller | Native packaging and bootloader | [PyInstaller license and exception](https://pyinstaller.org/en/stable/license.html) |
| pytest / pytest-qt / Ruff / build / setuptools / wheel | Development and build tooling | Their installed distribution metadata and upstream license files |

A native bundle must carry the actual dependency license texts from the installed distributions and the Qt component notices required for that bundle. The native build tooling collects available metadata/license files; the owner must inspect the resulting notices before distribution. Do not assume this summary table alone satisfies every redistributor obligation.

The documentation-backed catalog contains original short explanations and links to evidence. Unreal Engine source, full documentation pages, actual developer profiles and private schema caches are not bundled. Epic trademarks and any external material retain their original ownership and terms.

Dependency updates can change licenses or bundled components. Review notices whenever updating the constraints file or native packaging.

