from pathlib import Path
import argparse
import json
import datetime

JSON_PATH = "task-list.json"

def main():

  #Creates json file if it does not exist
  if not Path(JSON_PATH).exists():
    with open(JSON_PATH, "w") as file:
      data = {"current_id": 0}
      json.dump(data, file)

  parser = argparse.ArgumentParser()
  commands_subparsers = parser.add_subparsers(dest="command")

  #Add-task command
  add_task_command = commands_subparsers.add_parser("add", help="Add your task")
  add_task_command.add_argument("--description", required=True, type=str)

  #Update-task command
  update_task_command = commands_subparsers.add_parser("update", help="Update your task")
  update_task_command.add_argument("--id", required=True, type=int)
  update_task_command.add_argument("--description", type=str)
  update_task_command.add_argument("--status", choices=["todo", "in-progress", "done"])

  #Mark-in-progress command
  mark_in_progress_command = commands_subparsers.add_parser("mark-in-progress", help="Mark a task as in-progress")
  mark_in_progress_command.add_argument("--id", required=True, type=int)

  #Mark-done command
  mark_done_command = commands_subparsers.add_parser("mark-done", help="Mark a task as done")
  mark_done_command.add_argument("--id", required=True, type=int)

  #Mark-todo command
  mark_todo_command = commands_subparsers.add_parser("mark-todo", help="Mark a task as todo")
  mark_todo_command.add_argument("--id", required=True, type=int)

  #Delete-task command
  delete_task_command = commands_subparsers.add_parser("delete")
  delete_task_command.add_argument("--id", required=True, type=int)

  #List-tasks command
  list_tasks_command = commands_subparsers.add_parser("list", help="List all or filtered tasks")
  list_tasks_command.add_argument("--type", type=str, choices=["todo", "in-progress", "done"])

  #Calls the right method according to the command
  args = parser.parse_args()
  match args.command:
    case "add":
      add_task(args.description);
    case "update":
      update_task(str(args.id), args.description, args.status);
    case "delete":
      delete_task(str(args.id));
    case "list":
      list_tasks(args.type);
    case "mark-in-progress":
      update_task(str(args.id), status="in-progress");
    case "mark-done":
      update_task(str(args.id), status="done");
    case "mark-todo":
      update_task(str(args.id), status="todo")

      
def add_task(description):
  try:
    with open(JSON_PATH, "r+") as file: #r+ allows to read and write
      data = json.load(file);
      file.seek(0); #It moves the poiter to the file beginning
      id = data["current_id"]
      created_at = str(datetime.datetime.now())
      data[id] = {
        "id": id,
        "description": description,
        "status": "todo",
        "created_at": created_at,
        "updated_at": created_at,
      }
      data["current_id"] += 1;
      json.dump(data, file);
      file.truncate(); #It removes everything that's after the pointer
      print("Task added to the database!")
  except Exception as e:
    print("An Error was detected during add_task: "+ str(e));


def update_task(id, description=None, status=None):
  try:
    with open(JSON_PATH, "r+") as file:
      data = json.load(file);
      file.seek(0);

      if description != None:
        data[id]["description"] = description
  
      if status != None:
        data[id]["status"] = status

      data[id]["updated_at"] = str(datetime.datetime.now())

      json.dump(data, file);
      file.truncate();
      print("Task updated at database!")
  except ValueError as e:
    print("An Error was detected during update_task: "+ str(e));


def delete_task(id):
  try:
    with open(JSON_PATH, "r+") as file:
      data = json.load(file);
      file.seek(0);
      data.pop(id, None);
      json.dump(data, file);
      file.truncate();
      print("Task deleted from database!")
  except Exception as e:
    print("An Error was detected during delete_task: "+ str(e));


#By AI
def print_tasks_table(data):

  if not data:
        print("No tasks found.")
        return

  headers = ["ID", "Description", "Status", "Created at", "Updated at"]

  rows = []

  for task in data.values():
      rows.append([
          str(task["id"]),
          task["description"],
          task["status"],
          task["created_at"],
          task["updated_at"]
      ])

  widths = [
      max(len(headers[i]), max(len(row[i]) for row in rows))
      for i in range(len(headers))
  ]

  header_row = " | ".join(
      headers[i].ljust(widths[i])
      for i in range(len(headers))
  )

  separator = "-+-".join(
      "-" * widths[i]
      for i in range(len(headers))
  )

  print(header_row)
  print(separator)

  for row in rows:
      print(
          " | ".join(
              row[i].ljust(widths[i])
              for i in range(len(row))
          )
      )


def list_tasks(filter_type = None):
  try:
    with open(JSON_PATH, "r") as file:
      data = json.load(file);
  except Exception as e:
    print("An Error was detected during list_tasks: "+ str(e));

  data.pop("current_id", None);

  if filter_type:
    print_list = dict(filter(lambda item: item[1]["status"] == filter_type, data.items()));
  else:
    print_list = data;

  print_tasks_table(print_list)



  