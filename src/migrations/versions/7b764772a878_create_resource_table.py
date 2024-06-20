"""create_resource_table

Revision ID: 7b764772a878
Revises:
Create Date: 2024-06-12 21:03:24.857777

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "7b764772a878"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "resource",
        sa.Column("label", sa.SMALLINT(), nullable=False),
        sa.Column(
            "name", sa.String(), nullable=False, comment="Resource name"
        ),
        sa.Column(
            "description",
            sa.String(),
            nullable=False,
            comment="Resource description",
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
        schema="security",
        comment="Table with all resources",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("resource", schema="security")
    # ### end Alembic commands ###