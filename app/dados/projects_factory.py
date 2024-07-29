"""Factory para criar projetos."""
import random

import factory
from app.models.projects import Projects


class ProjectFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Factory para criar projetos."""

    class Meta:
        """Meta class."""

        model = Projects


    id = factory.Sequence(lambda n: n)

    project_name = factory.Faker('catch_phrase')

    start_date = factory.Faker('date_between', start_date='-4y', end_date='-1y')

    end_date = factory.LazyAttribute(lambda obj: factory.Faker(
        'date_between',
        start_date=obj.start_date,
        end_date='today').generate({}),
        )

    initial_budget = factory.LazyAttribute(lambda _: round(
        random.uniform(5000, 1000000), 2),  # noqa: S311
        )

    project_cost = factory.LazyAttribute(lambda obj: round(
        random.uniform(5000,obj.initial_budget), 2))  # noqa: S311

    revenue = factory.LazyAttribute(lambda obj: round(
        random.uniform(obj.project_cost, obj.project_cost * 1.5), 2))  # noqa: S311
