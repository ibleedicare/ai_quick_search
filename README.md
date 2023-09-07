# AI Quick Search Py

This repository contains a text-based user interface for interacting with OpenAI's GPT-3.5-turbo model. It's implemented in Python and allows you to ask questions, configure system prompts, and view about information.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ibleedicare/ai_quick_search_py.git
    ```
2. Install the dependencies:
    ```bash
    pip install PyInquirer openai PyYAML
    ```
3. Set your OpenAI API key as an environment variable:
    ```bash
    export OPENAI_API_KEY=your-api-key-here
    ```

## Usage

Run the main Python script:

```bash
python main.py
```

You'll be greeted with a menu that allows you to:

- Ask a question to GPT-3.5-turbo.
- Configure the system prompt for the AI model.
- View the 'About' section.

## Features

- Simple and interactive text-based UI.
- Utilizes GPT-3.5-turbo for generating responses.
- Supports YAML-based configuration for system prompts.

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.
