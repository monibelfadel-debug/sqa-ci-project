"""
Sample project for SQA: automated unit tests + CI.
A tiny 'Task' service with validation and a few business rules.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Optional


class ValidationError(ValueError):
    """Raised when input data is invalid."""


@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    created_at: datetime = field(default_factory=datetime.utcnow)


class TaskService:
    """
    In-memory task service. In real systems this would talk to a DB.
    This design allows easy unit testing (pure logic, no external dependencies).
    """

    def __init__(self) -> None:
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def list_tasks(self, done: Optional[bool] = None) -> List[Task]:
        tasks = list(self._tasks.values())
        if done is None:
            return tasks
        return [t for t in tasks if t.done == done]

    def create_task(self, title: str) -> Task:
        title = (title or "").strip()
        if len(title) < 3:
            raise ValidationError("Title must be at least 3 characters.")
        if len(title) > 100:
            raise ValidationError("Title must be at most 100 characters.")
        task = Task(id=self._next_id, title=title)
        self._tasks[task.id] = task
        self._next_id += 1
        return task

    def mark_done(self, task_id: int) -> Task:
        task = self._tasks.get(task_id)
        if not task:
            raise KeyError(f"Task {task_id} not found.")
        task.done = True
        return task

    def delete_task(self, task_id: int) -> None:
        if task_id not in self._tasks:
            raise KeyError(f"Task {task_id} not found.")
        del self._tasks[task_id]
