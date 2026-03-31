from __future__ import annotations

from datetime import datetime

from peewee import (
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKeyField,
    IntegerField,
    Model,
    SqliteDatabase,
    TextField,
)

db = SqliteDatabase("data/plustime.db")


def create_tables() -> None:
    """Initialize the database tables."""
    with db:
        db.create_tables([Profile, Group, Project, Status, Item])
        print("Tables created successfully.")


class BaseModel(Model):
    """
    Base model class that should be subclassed by all models in the app.
    Connects models to the database and implements shared fields and funcionality.
    """

    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):  # noqa: ANN002, ANN003, ANN201
        """Override save to update the 'updated_at' timestamp on every change."""
        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)

    class Meta:
        database = db  # Database to use for all models


class Profile(BaseModel):
    display_name = CharField(unique=True)
    email = CharField(unique=True, null=True)
    last_opened = DateTimeField(null=True)

    def __str__(self) -> str:
        return f"<{self.username}>"


class Group(BaseModel):
    user = ForeignKeyField(Profile, backref="groups", on_delete="CASCADE")
    name = CharField()
    icon = CharField(null=True)

    def __str__(self) -> str:
        return f"<{self.name} projects of {self.user.username}>"


class Project(BaseModel):
    user = ForeignKeyField(Profile, backref="projects", on_delete="CASCADE")
    group = ForeignKeyField(Group, backref="projects", null=True, on_delete="SET NULL")
    name = CharField()
    description = TextField(null=True)
    color_hex = CharField(default="#3F51B5")
    is_active = BooleanField(default=True)

    def __str__(self) -> str:
        return f"<{self.group.name}/{self.name} by {self.user.username}>"


class Status(BaseModel):
    """Represents the Kanban columns (e.g., To Do, Doing, Done)."""

    project = ForeignKeyField(Project, backref="statuses", on_delete="CASCADE")
    name = CharField()
    order = IntegerField()
    type = CharField(default="standard")  # e.g., 'backlog', 'completed'

    def __str__(self) -> str:
        return f"<'{self.name}' of {self.project.name}>"


class Item(BaseModel):
    """The individual Tasks/Notes."""

    project = ForeignKeyField(Project, backref="items", on_delete="CASCADE")
    current_status = ForeignKeyField(Status, backref="items", on_delete="CASCADE")
    title = CharField()
    content = TextField(null=True)
    priority = IntegerField(default=0)
    position_in_list = IntegerField(default=0)  # For drag-and-drop ordering
    completed_at = DateTimeField(null=True)

    def __str__(self) -> str:
        return f"<'{self.title}' in {self.current_status.name} status of {self.project.name}>"


if __name__ == "__main__":
    create_tables()
