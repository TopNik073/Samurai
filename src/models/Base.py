from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for inheritance new models"""

    repr_cols_num = 1
    repr_cols = tuple()

    def __repr__(self):
        """Relationships are not used in repr() because may lead to unexpected lazy loads"""
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"
