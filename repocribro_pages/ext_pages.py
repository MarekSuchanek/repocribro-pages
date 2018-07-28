from repocribro.extending import Extension
from repocribro.extending.helpers import Badge, ViewTab


class RepocribroPages(Extension):
    #: Name of pages extension
    NAME = 'pages'
    #: Category of pages extension
    CATEGORY = 'basic'
    #: Author of pages extension
    AUTHOR = 'Marek Suchánek'
    #: GitHub URL of pages extension
    GH_URL = 'https://github.com/MarekSuchanek/repocribro-pages'
    #: Priority of pages extension
    PRIORITY = 10

    # TODO: admin tab (table) and CRUD
    def view_admin_index_tabs(self, tabs_dict):
        """Prepare tabs for index view of admin controller
        :param tabs_dict: Target dictionary for tabs
        :type tabs_dict: dict of str: ``repocribro.extending.helpers.ViewTab``
        """
        pages = ['a', 'b', 'c']  # TODO: get pages from DB
        env = templates_env()

        tabs_dict['pages'] = ViewTab(
            'users', 'Users', 0,
            env.get_template('admin/tabs/pages.html').render(
                accounts=pages,
                octicon='browser',
                badge=Badge(len(pages))
            )
        )

    # TODO: pages controller
    @staticmethod
    def provide_blueprints():
        from .controllers import all_blueprints
        return all_blueprints

    # TODO: provide model


# TODO: use templates together with core templating
def templates_env():
    from jinja2 import Environment, PackageLoader, select_autoescape
    env = Environment(
        loader=PackageLoader('repocribro_pages', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    return env


def make_extension(*args, **kwargs):
    return RepocribroPages(*args, **kwargs)
