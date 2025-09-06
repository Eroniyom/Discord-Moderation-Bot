# Contributing to Discord Moderation Bot

Thank you for your interest in contributing to Discord Moderation Bot! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues

Before creating an issue, please:

1. **Search existing issues** to avoid duplicates
2. **Use the issue template** provided
3. **Provide detailed information** including:
   - Steps to reproduce
   - Expected vs actual behavior
   - Bot version and Python version
   - Error messages (if any)

### Suggesting Features

We welcome feature suggestions! Please:

1. **Check the roadmap** in README.md
2. **Describe the feature** clearly
3. **Explain the use case** and benefits
4. **Consider implementation complexity**

### Code Contributions

#### Getting Started

1. **Fork the repository**
2. **Clone your fork**:
   ```bash
   git clone https://github.com/yourusername/discord-moderation-bot.git
   cd discord-moderation-bot
   ```

3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Create a `.env` file** with your bot token:
   ```env
   DISCORD_BOT_TOKEN=your_bot_token_here
   ```

#### Development Guidelines

##### Code Style

- **Follow PEP 8** Python style guidelines
- **Use meaningful variable names**
- **Add docstrings** to functions and classes
- **Keep functions small** and focused
- **Use type hints** where appropriate

##### Commit Messages

Use clear, descriptive commit messages:

```
feat: add userinfo command
fix: resolve permission check bug
docs: update README with new features
refactor: improve error handling
test: add unit tests for moderation commands
```

##### Pull Request Process

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the guidelines above

3. **Test your changes**:
   - Run the bot locally
   - Test all affected commands
   - Check for any errors in logs

4. **Update documentation** if needed:
   - README.md for new features
   - Inline comments for complex code
   - Docstrings for new functions

5. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request** with:
   - Clear title and description
   - Reference any related issues
   - Screenshots if UI changes
   - Testing instructions

## 🏗️ Project Structure

Understanding the project structure will help you contribute effectively:

```
discord-moderation-bot/
├── bot.py              # Main bot file with event handlers
├── config.py           # Configuration and constants
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore patterns
├── env.example        # Environment variables template
├── README.md          # Project documentation
├── CONTRIBUTING.md    # This file
└── LICENSE           # MIT License
```

### Key Components

- **`bot.py`**: Main bot logic, event handlers, and cog loading
- **`config.py`**: Centralized configuration, colors, emojis, and settings
- **Cogs**: Command groups organized by functionality (Moderation, Information, Help)

## 🧪 Testing

### Manual Testing

Before submitting a PR, please test:

1. **All existing commands** still work
2. **New commands** work as expected
3. **Permission checks** are working
4. **Error handling** works properly
5. **Bot startup** and shutdown

### Test Server

Consider setting up a test Discord server for development:

1. Create a private Discord server
2. Add your bot with minimal permissions
3. Test commands with different permission levels
4. Use test accounts for different scenarios

## 📋 Code Review Process

### What We Look For

- **Functionality**: Does the code work as intended?
- **Code Quality**: Is it readable, maintainable, and follows standards?
- **Security**: Are there any security vulnerabilities?
- **Performance**: Is the code efficient?
- **Documentation**: Is it properly documented?

### Review Timeline

- **Initial review**: Within 48 hours
- **Follow-up reviews**: Within 24 hours
- **Merge**: After approval and all checks pass

## 🐛 Bug Reports

When reporting bugs, please include:

### Required Information

- **Bot version** (from `bot.py` or git commit)
- **Python version** (`python --version`)
- **discord.py version** (`pip show discord.py`)
- **Operating system** and version

### Bug Description

- **What happened**: Clear description of the issue
- **What you expected**: Expected behavior
- **Steps to reproduce**: Detailed steps
- **Error messages**: Full error traceback
- **Screenshots**: If applicable

### Example Bug Report

```markdown
**Bug Description**
The `/kick` command fails when trying to kick a member with higher roles.

**Steps to Reproduce**
1. Create a member with a role higher than the bot
2. Try to kick them with `/kick`
3. Bot responds with error

**Expected Behavior**
Bot should respond with permission error message.

**Actual Behavior**
Bot crashes with AttributeError.

**Error Message**
```
AttributeError: 'NoneType' object has no attribute 'top_role'
```

**Environment**
- Bot version: 1.0.0
- Python: 3.9.7
- discord.py: 2.3.0
- OS: Windows 10
```

## 💡 Feature Requests

### Good Feature Requests Include

- **Clear description** of the feature
- **Use case** and why it's needed
- **Proposed implementation** (if you have ideas)
- **Alternatives considered**
- **Additional context**

### Feature Request Template

```markdown
**Feature Description**
Add a `/warn` command to warn users without punishment.

**Use Case**
Moderators need a way to warn users for minor infractions without kicking/banning.

**Proposed Implementation**
- Store warnings in a simple JSON file
- Add `/warn`, `/warnings`, and `/clearwarnings` commands
- Show warning count in userinfo

**Alternatives**
- Use timeout for warnings
- Create a separate warning bot

**Additional Context**
This would help with progressive moderation and reduce false positives.
```

## 🏷️ Labels

We use labels to categorize issues and PRs:

- **bug**: Something isn't working
- **enhancement**: New feature or request
- **documentation**: Improvements to documentation
- **good first issue**: Good for newcomers
- **help wanted**: Extra attention is needed
- **question**: Further information is requested
- **wontfix**: This will not be worked on

## 📞 Getting Help

If you need help contributing:

1. **Check existing issues** and discussions
2. **Join our Discord server** (if available)
3. **Create a discussion** for questions
4. **Tag maintainers** in relevant issues

## 🎉 Recognition

Contributors will be:

- **Listed in CONTRIBUTORS.md** (if created)
- **Mentioned in release notes** for significant contributions
- **Given credit** in commit messages and PRs

## 📜 Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive experience for everyone, regardless of:

- Age, body size, disability, ethnicity
- Gender identity and expression
- Level of experience, education
- Nationality, personal appearance
- Race, religion, sexual orientation

### Expected Behavior

- **Be respectful** and inclusive
- **Be constructive** in feedback
- **Be patient** with newcomers
- **Be collaborative** and helpful

### Unacceptable Behavior

- Harassment, trolling, or discrimination
- Personal attacks or inappropriate language
- Spam or off-topic discussions
- Sharing private information

## 📝 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to Discord Moderation Bot!** 🎉

Your contributions help make this project better for everyone in the Discord community.
