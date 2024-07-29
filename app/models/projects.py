"""Model de projects."""


from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class Projects:
    """Model de projects."""

    __tablename__ = 'Projects'

    id: Mapped[int] = mapped_column(
        name='project_id',
        primary_key=True,
        init=False,
        autoincrement=True,
        comment='Identificador projeto.',
    )
    project_name: Mapped[str] = mapped_column(
        name='project_name',
        nullable=False,
        comment='Nome do projeto.',
    )
    start_date: Mapped[datetime] = mapped_column(
        name='start_date',
        nullable=False,
        comment='Data de início do projeto.',
    )
    end_date: Mapped[datetime] = mapped_column(
        name='end_date',
        nullable=False,
        comment='Data de término do projeto.',
    )
    initial_budget: Mapped[float] = mapped_column(
        name='initial_budget',
        nullable=False,
        comment='Orçamento inicial do projeto.',
    )
    project_cost: Mapped[float] = mapped_column(
        name='project_cost',
        nullable=False,
        comment='Custo total do projeto.',
    )
    revenue: Mapped[float] = mapped_column(
        name='revenue',
        nullable=False,
        comment='Receita do projeto.',
    )
