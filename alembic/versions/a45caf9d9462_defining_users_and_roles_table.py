"""Defining users and roles table

Revision ID: a45caf9d9462
Revises: 
Create Date: 2021-02-26 09:56:45.086268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a45caf9d9462'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=32), nullable=False),
    sa.Column('description', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('fullname', sa.String(length=128), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], name='fk_user_role'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('roles')
    # ### end Alembic commands ###