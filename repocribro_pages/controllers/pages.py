import flask

from ..ext_pages import templates_env


#: Pages public controller blueprint
pages = flask.Blueprint('pages', __name__, url_prefix='/pages')


# TODO: security?
@pages.route('/<slug>')
def show_page(slug):
    env = templates_env()
    # TODO: permissions
    # TODO: get page from DB or 404
    return env.get_template('pages/page.html').render(slug=slug)
