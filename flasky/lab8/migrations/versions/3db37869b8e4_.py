"""empty message

Revision ID: 3db37869b8e4
Revises: 456a945560f6
Create Date: 2018-11-08 17:26:29.117372

"""

# revision identifiers, used by Alembic.
revision = '3db37869b8e4'
down_revision = '456a945560f6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###
