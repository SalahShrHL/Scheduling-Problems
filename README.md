# Scheduling Problems Solver

## Project Overview

This project implements several scheduling algorithms in Python to calculate metrics such as **CMAX**, **C̅ (Cbar)**, **LMAX**, **TMAX**, and **U̅ (Ubar)** for a set of tasks with specified processing times, release times, and due dates. The tasks are scheduled using various rules, including **SPT (Shortest Processing Time)** and **EDD (Earliest Due Date)**.

## Features

- **CMAX Calculation**:  
  Calculates the maximum completion time (CMAX) for a list of tasks.

- **C̅ (Cbar) Calculation**:  
  Implements the **SPT** rule (Shortest Processing Time) to minimize the average completion time (C̅).

- **LMAX Calculation**:  
  Uses the **EDD** rule (Earliest Due Date) to calculate LMAX, the maximum lateness for the set of tasks.

- **TMAX Calculation**:  
  Also based on the **EDD** rule, it calculates the maximum tardiness (TMAX) for the tasks.

- **U̅ (Ubar) Calculation**:  
  Determines the percentage of tasks that are completed late using the U̅ metric.

## Task List

The tasks are defined as a list of dictionaries, each containing the following properties:

- `nom`: Task name.
- `pi`: Processing time of the task.
- `ri`: Release time (when the task becomes available).
- `di`: Due date (the time by which the task should ideally be completed).

```python
taches = [
    {"nom": "t1", "pi": 1, "ri": 0, "di": 2},
    {"nom": "t2", "pi": 5, "ri": 13, "di": 7},
    {"nom": "t3", "pi": 3, "ri": 0, "di": 8},
    {"nom": "t4", "pi": 7, "ri": 0, "di": 11},
    {"nom": "t5", "pi": 9, "ri": 0, "di": 13}
]
