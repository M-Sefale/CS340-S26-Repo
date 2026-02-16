# CS-340 Software Engineering: Project 2 (Spring 2026)
## Git, GitHub, and Regression Testing

This repository contains a collection of small Python utility programs, each featuring a specific logic bug. This project is designed to simulate a real-world software maintenance workflow where you must identify, reproduce, and fix issues reported by users.

### 🎯 Project Goals
* Gain proficiency in the **Git/GitHub Pull Request** workflow.
* Practice **Test-Driven Development (TDD)** by writing regression tests before fixing bugs.
* Learn to navigate and contribute to an existing codebase.
* Experience the peer-review process within a shared repository.

### 🛠️ Repository Structure
* `*.py`: The source code containing utility functions (and their bugs).
* `test_*.py`: The associated `unittest` suites. These currently pass, despite the bugs, because they lack sufficient coverage.

### 🚀 Getting Started
1. **Explore the Issues:** Browse the [GitHub Issues](https://github.com/kevinaangstadt/CS340-S26-Repo/issues) to find a bug you would like to fix.
2. **Claim your task:** Comment on the issue. Once the instructor assigns it to you, you may begin.
3. **Fork & Branch:** Fork this repository and create a descriptive branch for your fix.
4. **Reproduce & Fix:** * Add a new test case that fails (proving the bug).
   * Fix the source code.
   * Verify that all tests (old and new) now pass.
5. **Submit:** Open a Pull Request against the `main` branch of this repository.

### 🧪 Running Tests
To run all tests in the repository:
```bash
python3 -m unittest discover --verbose
```

To run tests for a specific file:
```bash
python3 -m unittest test_filename.py --verbose
```

### 🤖 AI Acknowledgement
The starter code, test suites, and GitHub Actions workflows provided in this
repository were generated with the assistance of generative AI models. These
materials were iteratively refined to create specific learning opportunities and
to simulate realistic software maintenance scenarios. 

---
Maintained by Kevin Angstadt · St. Lawrence University