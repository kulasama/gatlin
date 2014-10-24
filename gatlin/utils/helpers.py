from flask.ext.themes2 import render_theme_template

def render_template(template, **context):
    """A helper function that uses the `render_theme_template` function
    without needing to edit all the views
    """
  
    return render_theme_template(theme, template, **context)
