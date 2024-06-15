"""create_event_file_table

Revision ID: a8c8020a45ca
Revises: d7c64c941447
Create Date: 2024-06-12 22:59:51.994219

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "a8c8020a45ca"
down_revision = "d7c64c941447"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "event_file",
        sa.Column("sid", sa.Uuid(), nullable=False),
        sa.Column(
            "file_name", sa.String(), nullable=False, comment="Event file name"
        ),
        sa.Column(
            "file_bytes",
            sa.Integer(),
            nullable=False,
            comment="Event file bytes",
        ),
        sa.Column("event_sid", sa.Uuid(), nullable=False, comment="Event SID"),
        sa.Column(
            "event_content_sid",
            sa.Uuid(),
            nullable=False,
            comment="Event content SID",
        ),
        sa.Column(
            "type_label",
            sa.SMALLINT(),
            nullable=False,
            comment="Event file type label",
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
            ["event_content_sid"],
            ["events.event_content.sid"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["event_sid"], ["events.event.sid"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["type_label"],
            ["events.event_file_type.label"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("sid"),
        schema="events",
        comment="Table with all event files",
    )
    op.create_index(
        op.f("ix_events_event_file_event_content_sid"),
        "event_file",
        ["event_content_sid"],
        unique=False,
        schema="events",
    )
    op.create_index(
        op.f("ix_events_event_file_event_sid"),
        "event_file",
        ["event_sid"],
        unique=False,
        schema="events",
    )
    op.create_index(
        op.f("ix_events_event_file_type_label"),
        "event_file",
        ["type_label"],
        unique=False,
        schema="events",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_events_event_file_type_label"),
        table_name="event_file",
        schema="events",
    )
    op.drop_index(
        op.f("ix_events_event_file_event_sid"),
        table_name="event_file",
        schema="events",
    )
    op.drop_index(
        op.f("ix_events_event_file_event_content_sid"),
        table_name="event_file",
        schema="events",
    )
    op.drop_table("event_file", schema="events")
    # ### end Alembic commands ###