"""Change structure for auth methods

Revision ID: a95757bd6009
Revises: 2b5b411b4021
Create Date: 2024-06-13 18:31:22.691581

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a95757bd6009"
down_revision: Union[str, None] = "2b5b411b4021"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user_google_auth",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id", "email"),
    )
    op.create_table(
        "user_standart_auth",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("hash_password", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id", "email"),
    )
    op.create_table(
        "user_vk_auth",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("vk_id", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id", "vk_id"),
    )
    op.add_column("users", sa.Column("standart_auth", sa.Boolean(), nullable=False))
    op.add_column("users", sa.Column("google", sa.Boolean(), nullable=False))
    op.add_column("users", sa.Column("vk", sa.Boolean(), nullable=False))
    op.add_column("users", sa.Column("is_admin", sa.Boolean(), nullable=False))
    op.drop_column("users", "password")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("password", sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column("users", "is_admin")
    op.drop_column("users", "vk")
    op.drop_column("users", "google")
    op.drop_column("users", "standart_auth")
    op.drop_table("user_vk_auth")
    op.drop_table("user_standart_auth")
    op.drop_table("user_google_auth")
    # ### end Alembic commands ###