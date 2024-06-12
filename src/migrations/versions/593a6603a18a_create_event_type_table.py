"""create_event_type_table

Revision ID: 593a6603a18a
Revises: 35fe53bea29d
Create Date: 2024-06-12 22:50:31.919268

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "593a6603a18a"
down_revision = "35fe53bea29d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "event_type",
        sa.Column("label", sa.SMALLINT(), nullable=False),
        sa.Column(
            "name", sa.String(), nullable=False, comment="Event type name"
        ),
        sa.Column(
            "description",
            sa.String(),
            nullable=False,
            comment="Event type description",
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            comment="Record creating time",
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False,
            comment="Record updating time",
        ),
        sa.PrimaryKeyConstraint("label"),
        schema="events",
        comment="Table with all event types",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("event_type", schema="events")
    # ### end Alembic commands ###
