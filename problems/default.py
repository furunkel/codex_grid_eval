import itertools

def default_generate(GRID, inputs, render, lang, with_inputs=False, filter_func=None):
    grid_vals = GRID.values()
    grid_keys = GRID.keys()

    history = []

    for index, vals in enumerate(itertools.product(*grid_vals)):
        vars = dict(zip(grid_keys, vals))
        if filter_func and not filter_func(vars):
            continue

        text = render(**vars, lang=lang)
        if not text:
            continue

        if not with_inputs:
            value = (text, vars, index)
            if value in history: continue
            history.append(value)
            yield value
        else:
            for input in inputs:
                value = (text, {**vars, 'input': input}, index)
                if value in history: continue
                history.append(value)
                yield value