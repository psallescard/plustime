from core.models import Group, Item, Profile, Project, Status, db


def seed_data() -> None:
    db.connect()
    db.drop_tables([Profile, Project, Group, Status, Item])
    db.create_tables([Profile, Project, Group, Status, Item])

    user = Profile.create(display_name="John Doe", email="johndoe@example.com")
    personal = Group.create(user=user, name="Personal")
    college = Group.create(user=user, name="College")
    work = Group.create(user=user, name="Work")
    project = Project.create(user=user, group=personal, name="Plus Time")
    backlog = Status.create(project=project, name="Backlog", order=0, type="backlog")
    completed = Status.create(project=project, name="Completed", order=1, type="completed")
    doing = Status.create(project=project, name="Doing", order=2, type="standard")
    item = Item.create(project=project, current_status=backlog, title="Test Item")

    db.close()


if __name__ == "__main__":
    seed_data()
    print("Data seeded successfully.")
