"""empty message

Revision ID: 570d9bf47591
Revises: 7b8d5011742e
Create Date: 2021-08-17 23:30:01.191204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '570d9bf47591'
down_revision = '7b8d5011742e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('statusorden', 'inicio_fecha',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('statusorden', 'inicio_fecha',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    # ### end Alembic commands ###
