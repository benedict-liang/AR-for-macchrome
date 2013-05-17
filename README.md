Auto Refresh for Chrome on Mac
==============================

### Overview
This program has a similar function to [LiveReload](http://livereload.com/).

Changes made to the development directory will be detected, letting Chrome reload automatically. This is especially useful if a big screen or multiple screens are used using development.

Enjoy!

Setting Up
----------

#### ChromeDriver (Chrome Version of Selenium)
Download here: [https://code.google.com/p/selenium/wiki/ChromeDriver](https://code.google.com/p/selenium/wiki/ChromeDriver)

#### MacFSEvents 0.3
Website: [https://pypi.python.org/pypi/MacFSEvents](https://pypi.python.org/pypi/MacFSEvents)

#### Protocol Buffers
Website: [https://code.google.com/p/protobuf/](https://code.google.com/p/protobuf/)

Usage
-----
Set Environment Variables. Add as many as you like, but each with a **unique** `setid`. The `setid` could preferably be the **project name**.

```bash
$ python add_env_var.py
```
Run Program:

```bash
$ python main.py dir_to_observe setid
```

Extension
---------
Modify `environmentvariables.proto` and recompile:

```bash
$ protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/environmentvariables.proto
```

License
-------
The MIT License (MIT)

Copyright (c) 2013 Benedict Liang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
