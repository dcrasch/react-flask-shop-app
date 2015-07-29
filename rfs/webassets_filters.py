from __future__ import absolute_import
from webassets.filter import Filter
from react import jsx

__all__ = ('JSXFilter',)


class JSXFilter(Filter):
    """Transforms the jsx to js
    Requires the ``react-python`` package from https://github.com/reactjs/react-python
    """

    name = 'jsx'

    def setup(self):
        try:
            import react
        except ImportError:
            raise EnvironmentError('The "pyreact" package is not installed.')
        else:
            self.react = react

    def output(self, _in, out, **kw):
        transformer = self.react.jsx.JSXTransformer()
        out.write(transformer.transform_string(_in.read()))

from webassets.filter import register_filter
register_filter(JSXFilter)
