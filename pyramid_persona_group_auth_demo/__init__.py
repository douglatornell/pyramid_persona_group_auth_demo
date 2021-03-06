from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.config import Configurator
from pyramid.security import ALL_PERMISSIONS
from pyramid.security import Allow
from sqlalchemy import engine_from_config
from sqlalchemy.orm.exc import NoResultFound
from .models import (
    DBSession,
    Base,
    Administrator,
    )

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings, root_factory=Root)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.include('pyramid_persona')
    authn_policy = AuthTktAuthenticationPolicy(
        settings['persona.secret'],
        callback=groupfinder)
    config.set_authentication_policy(authn_policy)
    config.add_route('home', '/')
    config.add_route('admin.home', '/admin')
    config.scan()
    return config.make_wsgi_app()


class Root(object):
    """Simplest possible resource tree to map groups to permissions.
    """
    __acl__ = [
        (Allow, 'g:admin', ALL_PERMISSIONS),
    ]

    def __init__(self, request):
        self.request = request

def groupfinder(userid, request):
    query = DBSession.query(Administrator).\
                filter(Administrator.persona_email == userid)
    try:
        query.one()
        return ['g:admin']
    except NoResultFound:
        return None
