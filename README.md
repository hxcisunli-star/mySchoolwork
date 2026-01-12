# My Schoolwork - Assignment Tracker

A simple command-line tool to help students manage their assignments and coursework.

## Features

- **Add Assignments**: Create new assignments with title, course, due date, description, and priority
- **List Assignments**: View all pending assignments or all assignments including completed ones
- **Mark Complete**: Mark assignments as done when you finish them
- **Delete Assignments**: Remove assignments you no longer need
- **Statistics**: View completion rates and assignments by course
- **Persistent Storage**: All assignments are saved to a JSON file

## Installation

### Requirements
- Python 3.6 or higher

### Setup
1. Clone this repository or download the files
2. Make the script executable (optional):
   ```bash
   chmod +x assignment_tracker.py
   ```

## Usage

Run the assignment tracker:
```bash
python3 assignment_tracker.py
```

### Available Commands

- `add` - Add a new assignment
- `list` - List all pending assignments
- `all` - List all assignments (including completed)
- `complete` - Mark an assignment as complete
- `delete` - Delete an assignment
- `stats` - Show assignment statistics
- `help` - Show help message
- `exit` - Exit the application

### Example Session

```
>> add
Assignment title: Math Homework Chapter 5
Course name: MATH101
Due date (YYYY-MM-DD): 2026-01-20
Description (optional): Complete problems 1-25
Priority (high/medium/low) [medium]: high
✓ Added assignment: Math Homework Chapter 5

>> list
================================================================================
ID   Course          Title                     Due Date     Priority   Status
================================================================================
1    MATH101         Math Homework Chapter 5   2026-01-20   🔴 high      Pending
================================================================================

>> complete 1
✓ Marked assignment 'Math Homework Chapter 5' as complete!

>> stats
==================================================
ASSIGNMENT STATISTICS
==================================================
Total Assignments: 1
Completed: 1
Pending: 0
Completion Rate: 100.0%

By Course:
  MATH101: 1/1 completed
==================================================
```

## Data Storage

Assignments are stored in `assignments.json` in the same directory as the script. This file is created automatically when you add your first assignment.

## Priority Levels

- 🔴 **High**: Urgent assignments that need immediate attention
- 🟡 **Medium**: Standard priority assignments
- 🟢 **Low**: Assignments with flexible deadlines

## Future Enhancements

Some potential features to add:
- Sort assignments by due date
- Filter assignments by priority
- Send reminders for upcoming due dates
- Export assignments to CSV
- Calendar integration
- Grade tracking

## License

Free to use for educational purposes.
