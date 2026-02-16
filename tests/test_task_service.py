import pytest
from src.task_service import TaskService, ValidationError


def test_create_task_success():
    s = TaskService()
    t = s.create_task("Buy milk")
    assert t.id == 1
    assert t.title == "Buy milk"
    assert t.done is False


@pytest.mark.parametrize("bad_title", ["", "  ", "ab"])
def test_create_task_validation_min_length(bad_title):
    s = TaskService()
    with pytest.raises(ValidationError):
        s.create_task(bad_title)


def test_create_task_validation_max_length():
    s = TaskService()
    with pytest.raises(ValidationError):
        s.create_task("x" * 101)


def test_list_tasks_filter_done():
    s = TaskService()
    a = s.create_task("Task A")
    b = s.create_task("Task B")
    s.mark_done(a.id)

    done = s.list_tasks(done=True)
    todo = s.list_tasks(done=False)

    assert [t.id for t in done] == [a.id]
    assert [t.id for t in todo] == [b.id]


def test_mark_done_missing_task():
    s = TaskService()
    with pytest.raises(KeyError):
        s.mark_done(999)


def test_delete_task():
    s = TaskService()
    t = s.create_task("To delete")
    s.delete_task(t.id)
    assert s.list_tasks() == []
    with pytest.raises(KeyError):
        s.delete_task(t.id)
