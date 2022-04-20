import itertools

def default_generate(GRID, inputs, render, with_inputs=False, filter_func=None):
    grid_vals = GRID.values()
    grid_keys = GRID.keys()

    for index, vals in enumerate(itertools.product(*grid_vals)):
        vars = dict(zip(grid_keys, vals))
        if filter_func and not filter_func(vars):
            continue

        text = render(**vars)
        if not text:
            continue
        if not with_inputs:
            yield (text, vars, index)
        else:
            for input in inputs:
                yield (text, {**vars, 'input': input}, index)
