"""Add user relationship to Reservation

Revision ID: 75e258e2fd87
Revises: 04185f628e64
Create Date: 2025-04-29 19:11:22.346988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75e258e2fd87'
down_revision = '04185f628e64'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_reservation_user_id_user', 'user', ['user_id'], ['id'])


def downgrade():
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.drop_constraint('fk_reservation_user_id_user', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
