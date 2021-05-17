"""REST API with databases

Revision ID: 4751e0f24074
Revises: 
Create Date: 2021-05-17 19:39:23.890717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4751e0f24074'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppy',
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('puppy')
    # ### end Alembic commands ###
