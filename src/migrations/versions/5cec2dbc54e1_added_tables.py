"""Added tables

Revision ID: 5cec2dbc54e1
Revises: 
Create Date: 2024-09-30 00:36:28.590238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5cec2dbc54e1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE SCHEMA event_content_type")
    op.create_table('event_content_type',
    sa.Column('sid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('sid'),
    schema='event_content_type'
    )
    op.execute("CREATE SCHEMA event_image")
    op.create_table('event_image',
    sa.Column('sid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('sid'),
    schema='event_image'
    )
    op.execute("CREATE SCHEMA event_type")
    op.create_table('event_type',
    sa.Column('sid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('sid'),
    schema='event_type'
    )
    op.execute("CREATE SCHEMA event_content")
    op.create_table('event_content',
    sa.Column('sid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('event_content_type_sid', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['event_content_type_sid'], ['event_content_type.event_content_type.sid'], ),
    sa.PrimaryKeyConstraint('sid'),
    schema='event_content'
    )
    op.execute("CREATE SCHEMA events")
    op.create_table('events',
    sa.Column('sid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('event_type_sid', sa.UUID(), nullable=True),
    sa.Column('event_image_sid', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['event_image_sid'], ['event_image.event_image.sid'], ),
    sa.ForeignKeyConstraint(['event_type_sid'], ['event_type.event_type.sid'], ),
    sa.PrimaryKeyConstraint('sid'),
    schema='events'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events', schema='events')
    op.execute("DROP SCHEMA events")
    op.drop_table('event_content', schema='event_content')
    op.execute("DROP SCHEMA event_content")
    op.drop_table('event_type', schema='event_type')
    op.execute("DROP SCHEMA event_type")
    op.drop_table('event_image', schema='event_image')
    op.execute("DROP SCHEMA event_image")
    op.drop_table('event_content_type', schema='event_content_type')
    op.execute("DROP SCHEMA event_content_type")
    # ### end Alembic commands ###
