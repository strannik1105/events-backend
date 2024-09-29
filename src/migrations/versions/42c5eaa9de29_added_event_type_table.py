"""Added event type table

Revision ID: 42c5eaa9de29
Revises: c39b9a5d45dc
Create Date: 2024-09-23 23:09:45.776205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42c5eaa9de29'
down_revision = 'c39b9a5d45dc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE SCHEMA event_type")
    op.create_table('event_type',
    sa.Column('sid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('sid'),
    schema='event_type'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event_type', schema='event_type')
    # ### end Alembic commands ###