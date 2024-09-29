"""Added event image table

Revision ID: 6a1345c9a46b
Revises: f31080f5be45
Create Date: 2024-09-29 12:46:26.427900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a1345c9a46b'
down_revision = 'f31080f5be45'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE SCHEMA event_image")
    op.create_table('event_image',
    sa.Column('sid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('sid'),
    schema='event_image'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event_image', schema='event_image')
    op.execute("DROP SCHEMA event_image")
    # ### end Alembic commands ###