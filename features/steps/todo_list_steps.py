to_do_list = []  # Global to-do list

@given('the to-do list is empty')
def step_impl(context):
    global to_do_list
    to_do_list = []  # Reset the to-do list

@when('the user adds a task "{task}"')
def step_impl(context, task):
    global to_do_list
    if not task.strip():
        context.error = "Task cannot be empty"
    else:
        to_do_list.append({"Task": task, "Status": "Pending"})  # Task now has a status

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    task_found = any(t["Task"] == task for t in to_do_list)
    assert task_found, f'Task "{task}" not found in the to-do list'

@then('an error message should be displayed')
def step_impl(context):
    assert hasattr(context, 'error'), "Error message not found"
    assert context.error == "Task cannot be empty", f"Unexpected error: {context.error}"

@when('the user lists all tasks')
def step_impl(context):
    context.listed_tasks = [t["Task"] for t in to_do_list]  # Extract only task names

@then('the output should contain:')
def step_impl(context):
    expected_tasks = [row['Task'] for row in context.table]
    assert context.listed_tasks == expected_tasks, \
        f'Expected {expected_tasks}, but got {context.listed_tasks}'

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    task_found = False
    for t in to_do_list:
        if t["Task"] == task:
            t["Status"] = "Completed"
            task_found = True
            break
    if not task_found:
        context.error = "Task not found"

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    task_found = any(t["Task"] == task and t["Status"] == "Completed" for t in to_do_list)
    assert task_found, f'Task "{task}" is not marked as completed'

@then('an error message "{error_msg}" should be displayed')
def step_impl(context, error_msg):
    assert hasattr(context, 'error'), "Error message not found"
    assert context.error == error_msg, f"Unexpected error: {context.error}"

@when('the user clears the to-do list')
def step_impl(context):
    global to_do_list
    to_do_list = []  # Clear the list

@then('the to-do list should be empty')
def step_impl(context):
    assert len(to_do_list) == 0, f'To-do list is not empty: {to_do_list}'
