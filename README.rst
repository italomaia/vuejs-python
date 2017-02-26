Vuejs-Python
============

This project aims to create various examples showing how to work
with vuejs and python based technologies. As vuejs may be integrated
in different ways, with different advantages for each approach,
having these examples are ideal for the brave-of-heart.

flask-vue
---------

**flask-vue** is the first project made. It shows how to
use flask and vuejs to build a non-SPA (single page
application). This approach is more appropriate for
those with little experience using js/node build tools
like webpack_ and browserify_. You'll mostly have to
handle python and js code. Another important advantage
is that most flask "resources" will still work
out-of-the-box, like debug toolbar and csrf protection.

A disvantage for this approach is that it is much
less flexible, integrates poorly with other
javascript libraries, less performatic, has cache
invalidation issues and is not appropriate for
larger projects. Depending of how you implement
the frontend, you may also see some flickering.

.. _webpack: https://webpack.github.io/
.. _browserify: http://browserify.org/
