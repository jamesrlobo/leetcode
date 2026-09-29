# LeetCode Solutions

My solutions and practice attempts for LeetCode problems across Python, Shell, and JavaScript.

## Languages

- Python
- Shell
- JavaScript

## Repository Structure

The repository is organized by **programming language**, **LeetCode difficulty**, and **LeetCode beat percentage**.

```text
leetcode/
├── Python/
│   ├── <unsolved problems>
│   ├── Easy/
│   │   ├── <solved problems below 100%>
│   │   └── 100%/
│   │       └── <solved problems with 100% beat>
│   └── Medium/
│       ├── <solved problems below 100%>
│       └── 100%/
│           └── <solved problems with 100% beat>
│
├── Shell/
│   ├── <unsolved problems>
│   ├── Easy/
│   │   └── 100%/
│   └── Medium/
│       └── 100%/
│
├── Javascript/
│   ├── <unsolved problems>
│   ├── Easy/
│   │   └── 100%/
│   └── Medium/
│       └── 100%/
│
└── README.md
```

> `Hard` folders will be added when I start solving Hard problems.

## Folder Rules

### Unsolved Problems

Unsolved or incomplete attempts stay directly inside their respective language folder.

Example:

```text
Python/
└── 1128.numEquivDominoPairs.py
```

### Solved Problems

Solved problems are moved into the appropriate LeetCode difficulty folder.

Example:

```text
Python/
└── Easy/
    └── 2389.answerQueries.py
```

### 100% Solutions

A solution with a **100% LeetCode beat percentage** is placed inside the `100%` folder under its difficulty.

Example:

```text
Python/
└── Easy/
    └── 100%/
        └── 836.isRectangleOverlap.py
```

The same structure will apply to Medium and, eventually, Hard problems.

## Git Workflow

My general workflow is:

1. Create or work on the solution inside the appropriate language folder.
2. If the problem is not solved, keep the file directly inside the language folder.
3. Once solved, move it into the appropriate difficulty folder.
4. If the solution achieves 100% beat, move it into the `100%` folder.
5. Review the changes using Git.
6. Commit the changes.
7. Push the commit to GitHub.

## Commit Convention

Solved problems use the following commit-message format:

```text
Solved <problem number>. <problem name>
```

Examples:

```text
Solved 836. Rectangle Overlap
Solved 2389. Longest Subsequence With Limited Sum
```

This repository is primarily a personal learning and problem-solving record, with Git history used to track progress and improvements over time.
