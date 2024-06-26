"""create_event_table

Revision ID: 933a7e137029
Revises: c8fb4ebf0fcf
Create Date: 2024-06-12 22:55:27.254559

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "933a7e137029"
down_revision = "c8fb4ebf0fcf"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "event",
        sa.Column("sid", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(), nullable=False, comment="Event name"),
        sa.Column(
            "description",
            sa.String(),
            nullable=False,
            comment="Event description",
        ),
        sa.Column(
            "type_label",
            sa.SMALLINT(),
            nullable=False,
            comment="Event type label",
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
        sa.ForeignKeyConstraint(
            ["type_label"], ["events.event_type.label"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("sid"),
        schema="events",
        comment="Table with all events",
    )
    op.create_index(
        op.f("ix_events_event_type_label"),
        "event",
        ["type_label"],
        unique=False,
        schema="events",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_events_event_type_label"), table_name="event", schema="events"
    )
    op.drop_table("event", schema="events")
    # ### end Alembic commands ###
