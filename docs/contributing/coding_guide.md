---
title: "Coding Guide"
hide:
    - footer
---

# Coding Guide

There are some coding guidelines that are helpful to note, with the following goals:

- Maintain consistent conventions and usage across the codebase.
- Use simple approaches whenever possible.
- Make it as easy as possible for new contributors to start contributing to the project.

# Project structure

As much as possible, write small utility functions that can easily be unit tested, without the need for building a full project. If you're writing a method, pull any functionality that doesn't depend on class attributes out into a utility function, unless it's too trivial to be worth testing.

## Coding Style

Run `black` at the root project level before making a PR. This should be integrated into CI around the 1.0 release.

## Python usage

### Use `path.read_text()` when possible.

We are passing paths around most of the time. Use `path.read_text()`, rather than `with open(filename)`.


## Working with plugins

### Return values

When you call out to a function implemented by a plugin that returns a value, that value is packed into a list. Often we're just dealing with just one plugin, so you'll see code that looks like this:

```python
self.plugin_config = pm.hook.dsd_get_plugin_config()[0]
```