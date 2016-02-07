from flask_assets import Environment, Bundle

assets = Environment()

coffee_filters = [
    'coffeescript',
    #'uglifyjs'
]

# TODO: pack js files, compiled, into project's /static
coffee = Bundle(
    # here we compile the coffee scripts, then we minify it and pack it
    # in this example there is but one file, but this scales alright!
    # you may also use nested bundles http://webassets.readthedocs.org/en/latest/bundles.html#nested-bundles
    'blog/coffee/app.coffee',
    filters=coffee_filters,
    # our output js will have this structure
    output='js/apps.min.js'
)

# we want our js files to be compiled into our project's static folder
coffee.directory = 'static'

assets.register('js_all', coffee)
