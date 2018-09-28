import flask

from ..models import Page
# TODO: get permissions


#: Pages public controller blueprint
admin_pages = flask.Blueprint('admin-pages', __name__, url_prefix='/admin-pages')


# TODO: get/post
@admin_pages.route('/create', methods=['GET'])
@permissions.roles.admin.require(404)
def create_page():
    # TODO: prepare empty page
    page = Page()
    return flask.render_template('admin/form.html', page=page)


# TODO: get/post
@admin_pages.route('/create', methods=['GET'])
@permissions.roles.admin.require(404)
def create_page_post():
    # TODO: create page (or back to form with err)
    slug = ''
    return flask.redirect('show_page', slug=slug)


# TODO: get/put
@admin_pages.route('/{slug}/edit')
@permissions.roles.admin.require(404)
def edit_page(slug):
    # TODO: get page from DB or 404
    page = Page()
    return flask.render_template('admin/form.html', page=page)


# TODO: get/put
@admin_pages.route('/{slug}/edit')
@permissions.roles.admin.require(404)
def edit_page_put(slug):
    # TODO: get page & update it (or back to form with err)
    return flask.redirect('show_page', slug=slug)


# TODO: get/delete
@admin_pages.route('/{slug}/delete')
@permissions.roles.admin.require(404)
def delete_page(slug):
    # TODO: get page from DB or 404
    ...
    return flask.redirect('admin')
