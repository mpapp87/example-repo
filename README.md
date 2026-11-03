# Python Coursework Examples

Two console programs from my HyperionDev software engineering coursework, shared for Task 25: Version Control and Git Basics.

## Programs

- **Minesweeper grid calculator** (`minesweeper.py`): accepts a grid containing `#` mines and `-` empty cells, then replaces each empty cell with the number of neighbouring mines. This demonstrates two-dimensional lists, loops, functions, and boundary checks.
- **Nike warehouse inventory manager** (`example-repo/inventory.py`): loads shoe records from `inventory.txt`, displays and searches inventory, captures new shoes, restocks the lowest-quantity item, calculates stock values, and identifies the highest-quantity item. Additions and restocking are saved to the data file.

## Setup

Install Python 3 and Git, then clone this repository:

```sh
git clone https://github.com/mpapp87/example-repo.git
cd example-repo
```

No third-party Python packages are required.

## Run Minesweeper

From the repository root:

```sh
python3 minesweeper.py
```

Enter positive whole numbers for the row and column counts. Enter each row using only `#` and `-`, with exactly the requested number of columns. For example, use 2 rows, 3 columns, and these rows:

```text
#--
--#
```

Result:

```text
['#', 2, 1]
[1, 2, '#']
```

The program validates row length and characters; it does not handle non-integer or non-positive dimensions.

## Run the inventory manager

From the repository root, change into the existing nested project directory so the program can find its data file:

```sh
cd example-repo
python3 inventory.py
```

Use menu options 1-7 to manage inventory and option 8 to exit. The bundled `inventory.txt` is sample data. Capturing or restocking shoes modifies that file.

On systems where Python 3 is launched with `python` or `py`, use that command instead of `python3`.

## Coursework source and maintainer

Maintained by [mpapp87](https://github.com/mpapp87).

`minesweeper.py` is copied unchanged from my existing coursework repository, `hyperiondev-bootcamps/MP26030020049`, at `Level 1 - Python for Software Engineering/M03T04 – Data Structures – 2D Lists/minesweeper.py` (source Git blob `90cbe9104c6b705826618f4b0b0d3c6ef4ff9aff`). The source coursework repository may require access.

The inventory program and sample data were already present in this repository. These examples demonstrate Python programming and sharing code with Git and GitHub.
