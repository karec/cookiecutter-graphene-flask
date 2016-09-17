import logging

import graphene
from graphene import relay
from graphene_sqlalchemy import (SQLAlchemyConnectionField,
                                 SQLAlchemyObjectType)
from {{cookiecutter.app_name}}.models import User as UserModel
from {{cookiecutter.app_name}}.models import Article as ArticleModel

logger = logging.getLogger(__name__)


class User(SQLAlchemyObjectType):

    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class Article(SQLAlchemyObjectType):

    class Meta:
        model = ArticleModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    users = SQLAlchemyConnectionField(User)
    user = graphene.Field(User)

    articles = SQLAlchemyConnectionField(Article)
    article = graphene.Field(Article)

schema = graphene.Schema(query=Query, types=[User, Article])
