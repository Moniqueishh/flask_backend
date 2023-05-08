"""empty message

Revision ID: 4fd5329bb0ed
Revises: 9db0a222e52e
Create Date: 2023-04-27 09:28:14.198103

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fd5329bb0ed'
down_revision = '9db0a222e52e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('savedTrips',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('city', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['city'], ['city.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('savedTrips')
    op.drop_table('city')
    # ### end Alembic commands ###