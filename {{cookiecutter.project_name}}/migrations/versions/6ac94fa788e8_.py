"""empty message

Revision ID: 6ac94fa788e8
Revises: 27ece81cab7f
Create Date: 2016-09-17 00:50:00.450484

"""

# revision identifiers, used by Alembic.
revision = '6ac94fa788e8'
down_revision = '27ece81cab7f'

import random
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table


def generate_articles(num, max_users=10):
    return {
        'title': 'article %d' % num,
        'content': """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at nibh vel erat ornare imperdiet. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aenean dapibus vehicula justo et iaculis. Maecenas hendrerit ullamcorper mi vel porta. Ut urna mauris, dignissim vel lorem vitae, dapibus iaculis magna. Suspendisse potenti. Vivamus vehicula ultricies sem in blandit. Nunc a mauris ultrices, facilisis nisi vitae, tristique risus. Nam imperdiet lacus quis nibh rutrum euismod ac sed felis. Duis egestas diam ac posuere feugiat. Nullam accumsan velit ut velit eleifend, vitae facilisis augue egestas. Nullam vel placerat sem, quis rhoncus libero.
        """,
        'user_id': random.randrange(1, max_users)
    }


def generate_users(num):
    return {
        'username': 'user%d' % num,
        'email': 'user%d@test.com' % num
    }


def upgrade():
    """Insert fixtures for models, tests purpose only"""
    users = [generate_users(i) for i in range(1, 52)]
    articles = [generate_articles(i, 50) for i in range(1, 200)]

    article = table(
        'article',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column('title', sa.String(length=100), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
    )

    user = table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True, autoincrement=True),
        sa.Column('username', sa.String(length=80), nullable=False),
        sa.Column('email', sa.String(length=120), nullable=False),
    )

    op.bulk_insert(user, users)
    op.bulk_insert(article, articles)


def downgrade():
    pass
