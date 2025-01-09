Feature: To-Do List Management
  In order to manage tasks effectively,
  As a user,
  I want to add, list, and modify tasks in my to-do list.

  Scenario: Adding a task
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: Listing all tasks
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user lists all tasks
    Then the output should contain:
      | Task          |
      | Buy groceries |
      | Pay bills     |

  Scenario: Marking a task as completed
    Given the to-do list contains tasks:
      | Task          | Status   |
      | Buy groceries | Pending  |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clearing the entire to-do list
    Given the to-do list contains tasks:
      | Task          |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Attempting to add an empty task
    Given the to-do list is empty
    When the user adds a task ""
    Then an error message should be displayed

  Scenario: Trying to mark a non-existent task as completed
    Given the to-do list contains tasks:
      | Task          | Status   |
      | Pay bills     | Pending  |
    When the user marks task "Buy groceries" as completed
    Then an error message "Task not found" should be displayed
