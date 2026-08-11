# task-tracker-cli

A simple command-line application to create, manage, and track your daily tasks.

With `task-tracker-cli`, you can:

* Add new tasks
* Update existing tasks
* Delete tasks
* List all tasks
* Filter tasks by status
* Mark tasks as `todo`, `in-progress`, or `done`

## Installation

After cloning or downloading this repository, navigate to the project root directory and run:

```bash
pip install -e .
```

This installs the project in editable mode and allows you to use `task-tracker-cli` from anywhere in your terminal.

## Usage

### Add a task

```bash
task-tracker-cli add --description "Your task here"
```

Arguments:

* `--description` — Required. The description of the task.

Example:

```bash
task-tracker-cli add --description "Finish Python project"
```

### Update a task

```bash
task-tracker-cli update --id 4 --description "New task description" --status "in-progress"
```

Arguments:

* `--id` — Required. The ID of the task you want to update.
* `--description` — Optional. The new task description.
* `--status` — Optional. The new task status.

Available statuses:

* `todo`
* `in-progress`
* `done`

Examples:

```bash
task-tracker-cli update --id 4 --description "Finish README"
```

```bash
task-tracker-cli update --id 4 --status "done"
```

### Delete a task

```bash
task-tracker-cli delete --id 4
```

Arguments:

* `--id` — Required. The ID of the task you want to delete.

### List all tasks

```bash
task-tracker-cli list
```

This command displays all registered tasks.

### Filter tasks by status

```bash
task-tracker-cli list --type "todo"
```

Available filters:

* `todo`
* `in-progress`
* `done`

Examples:

```bash
task-tracker-cli list --type "todo"
```

```bash
task-tracker-cli list --type "in-progress"
```

```bash
task-tracker-cli list --type "done"
```

## Task Status

Each task can have one of the following statuses:

| Status        | Description                           |
| ------------- | ------------------------------------- |
| `todo`        | The task has not been started yet     |
| `in-progress` | The task is currently being worked on |
| `done`        | The task has been completed           |

## Example Workflow

```bash
# Add a task
task-tracker-cli add --description "Study Python"

# List tasks
task-tracker-cli list

# Mark the task as in progress
task-tracker-cli update --id 1 --status "in-progress"

# Mark the task as completed
task-tracker-cli update --id 1 --status "done"

# List completed tasks
task-tracker-cli list --type "done"

# Delete the task
task-tracker-cli delete --id 1
```

