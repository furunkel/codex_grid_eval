from dataclasses import dataclass

from numpy import isin

@dataclass
class Problem:
    name: str

    def __post_init__(self):
        problems_mod = __import__(f'problems.{self.name}')
        self.mod = getattr(problems_mod, self.name)

    @property
    def generate_func(self):
        return getattr(self.mod, 'generate')
        
    @property
    def oracle_func(self):
        return getattr(self.mod, 'oracle')

    @property
    def run_func(self):
        return getattr(self.mod, 'run')

    @property
    def has_target(self):
        return hasattr(self.mod, 'TARGET')

    @property
    def grid(self):
        return getattr(self.mod, 'GRID')

    def get_text(self, lang=''):
        #FIXME handle lang
        return getattr(self.mod, 'TEXT')

    @property
    def test_imports(self):
        if hasattr(self.mod, 'TEST_IMPORTS'):
            return getattr(self.mod, 'TEST_IMPORTS')
        else:
            return []

    def get_target_name(self, vars, lang):
        target = getattr(self.mod, 'TARGET')
        if isinstance(target, dict):
            target = target[lang]
            if callable(target):
                target = target(lang, vars)
        return target.format(**vars)

    def is_output_equal(self, a, b):
        if hasattr(self.mod, 'is_output_equal'):
            return getattr(self.mod, 'is_output_equal')(a, b)
        else:
            return a == b