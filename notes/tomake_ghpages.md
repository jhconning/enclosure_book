---
title: tomake_ghpages
tags: [admin/jbook]
created: 2022-06-17T23:01:57.844Z
modified: 2022-06-20T01:48:02.549Z
---

# tomake_ghpages


- Jupyter book

- How to get an HTML page (from pdoc3)
https://github.com/executablebooks/jupyter-book/issues/1113


```
pdoc --html --force --output-dir notebooks/docs -c latex_math=True notebooks/enclose.py
```

If you wanted to develop and see changes update you can run it in server mode

```
pdoc --http localhost:8080 -c latex_math=True enclose.py
```
