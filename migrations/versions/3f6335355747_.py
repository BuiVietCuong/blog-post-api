"""empty message

Revision ID: 3f6335355747
Revises: 
Create Date: 2024-07-17 15:30:08.647253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f6335355747'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('email'),
    sa.UniqueConstraint('email')
    )
    op.create_table('blog_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('user_email', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_email'], ['user.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog_post')
    op.drop_table('user')
    # ### end Alembic commands ###
