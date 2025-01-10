# Global to-do list for the steps
to_do_list = []

# -------------------------------------
# GIVEN STEPS
# -------------------------------------

# Step: The to-do list is empty
@given('the to-do list is empty')
def step_impl(context):
    global to_do_list
    to_do_list = []  # Reset the to-do list

# Step: The to-do list contains specific tasks
@given('the to-do list contains tasks')
def step_impl(context):
    global to_do_list
    # Populate the to-do list with tasks from the feature file table
    to_do_list = [{"Task": row['Task'], "Status": row.get("Status", "Pending")} for row in context.table]

# -------------------------------------
# WHEN STEPS
# -------------------------------------

# Step: The user adds a task
@when('the user adds a task "{task}"')
def step_impl(context, task):
    global to_do_list
    if not task.strip():
        context.error = "Task cannot be empty"  # Set an error message
    else:
        to_do_list.append({"Task": task, "Status": "Pending"})  # Add task with status

# Step: The user adds an empty task
@when('the user adds a task ""')
def step_impl(context):
    task = ""  # Empty task
    if not task.strip():
        context.error = "Task cannot be empty"  # Set an error message
    else:
        to_do_list.append({"Task": task, "Status": "Pending"})

# Step: The user lists all tasks
@when('the user lists all tasks')
def step_impl(context):
    # Store the list of tasks in the context for validation
    context.listed_tasks = [task["Task"] for task in to_do_list]

# Step: The user marks a task as completed
@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    task_found = False
    for t in to_do_list:
        if t["Task"] == task:
            t["Status"] = "Completed"  # Mark as completed
            task_found = True
            break
    if not task_found:
        context.error = "Task not found"  # Set an error message if the task isn't found

# Step: The user clears the to-do list
@when('the user clears the to-do list')
def step_impl(context):
    global to_do_list
    to_do_list = []  # Clear the list

# -------------------------------------
# THEN STEPS
# -------------------------------------

# Step: The to-do list should contain a specific task
@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    task_found = any(t["Task"] == task for t in to_do_list)
    assert task_found, f'Task "{task}" not found in the to-do list'

# Step: The output should contain specific tasks
@then('the output should contain')
def step_impl(context):
    # Extract expected tasks from the scenario table
    expected_tasks = [row['Task'] for row in context.table]
    # Extract actual tasks from the to-do list
    listed_tasks = [task['Task'] for task in to_do_list]
    # Check if the listed tasks match the expected tasks
    assert listed_tasks == expected_tasks, f"Expected: {expected_tasks}, but got: {listed_tasks}"

# Step: The to-do list should show a task as completed
@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    task_found = any(t["Task"] == task and t["Status"] == "Completed" for t in to_do_list)
    assert task_found, f'Task "{task}" is not marked as completed'

# Step: The to-do list should be empty
@then('the to-do list should be empty')
def step_impl(context):
    assert len(to_do_list) == 0, f'To-do list is not empty: {to_do_list}'

# Step: An error message should be displayed
@then('an error message should be displayed')
def step_impl(context):
    assert hasattr(context, 'error'), "Error message not found"
    assert context.error == "Task cannot be empty", f"Unexpected error: {context.error}"

# Step: A specific error message should be displayed
@then('an error message "{error_msg}" should be displayed')
def step_impl(context, error_msg):
    assert hasattr(context, 'error'), "Error message not found"
    assert context.error == error_msg, f"Unexpected error: {context.error}"
