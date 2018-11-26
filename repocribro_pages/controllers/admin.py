import flask

from repocribro.security import permissions

from repocribro_pages.models import Page


#: Pages public controller blueprint
admin_pages = flask.Blueprint('admin-pages', __name__, url_prefix='/admin-pages')


# TODO: get/post
@admin_pages.route('/create', methods=['GET'])
@permissions.roles.admin.require(404)
def create_page():
    db = flask.current_app.container.get('db')

    page = Page()
    pages = db.session.query(Page).all()
    return flask.render_template('admin/form.html', page=page, pages=pages)


# TODO: get/post
@admin_pages.route('/create', methods=['POST'])
@permissions.roles.admin.require(404)
def create_page_post():
    # TODO: create page (or back to form with err)

    title = flask.request.form.get('title', None)
    slug = flask.request.form.get('slug', None)
    content = flask.request.form.get('content', None)
    custom_css = flask.request.form.get('custom_css', None)
    custom_js = flask.request.form.get('custom_js', None)

    return flask.redirect(
        flask.url_for('admin-pages.show_page', slug=slug)
    )


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
    return flask.redirect(
        flask.url_for('admin-pages.show_page', slug=slug)
    )


@admin_pages.route('/{slug}', methods=['DELETE'])
@admin_pages.route('/{slug}/delete', methods=['POST'])
@permissions.roles.admin.require(404)
def delete_page(slug):
    db = flask.current_app.container.get('db')

    page = db.session.query(Page).filter_by(slug=slug).first()
    if page is None:
        flask.abort(404)
    db.session.delete(page)
    db.session.commit()
    flask.flash('User account {} with the all related data'
                ' has been deleted'.format(page.slug), 'success')
    return flask.redirect(
        flask.url_for('admin.index', tab='pages')
    )
