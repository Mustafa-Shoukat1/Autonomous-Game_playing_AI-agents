# Autonomous Game Playing AI Agents

A collection of AI agents designed to play games autonomously using various machine learning and artificial intelligence techniques.

## Overview

This repository explores the development of intelligent agents capable of learning and mastering different types of games without human intervention. The agents use techniques like reinforcement learning, deep learning, genetic algorithms, and other AI approaches to develop effective game-playing strategies.

## Projects

### 1. AI Tic-Tac-Toe Agent

An interactive Tic-Tac-Toe game where two AI agents powered by different language models compete against each other.

- **Features**:
  - Multiple AI models support (GPT-4, Claude, Gemini, etc.)
  - Real-time game visualization
  - Move history tracking with board states
  - Interactive player selection and game state management

- **Technologies**: Streamlit, Agno Agent Framework

### 2. AI Chess Agent

A chess game played autonomously by two AI agents using AutoGen framework.

- **Features**:
  - Two GPT-powered chess players (white and black)
  - Game master agent that validates moves and updates the board
  - Turn-based gameplay with visualization
  - Move history tracking

- **Technologies**: Streamlit, AutoGen, Python-chess

### 3. AI 3D PyGame Visualizer

Generates and visualizes PyGame code from natural language descriptions.

- **Features**:
  - Generates PyGame code from text prompts
  - Uses DeepSeek Reasoner for code logic and explanation
  - Extracts clean code using OpenAI GPT-4o
  - Automates code visualization on Trinket.io using browser agents

- **Technologies**: Streamlit, DeepSeek, PyGame, Browser-use

## Getting Started

### Prerequisites

- Python 3.8+
- API keys for various AI services (OpenAI, Anthropic, DeepSeek, Google, etc.)

### Installation

```bash
# Clone the repository
git clone https://github.com/Mustafa-Shoukat1/Autonomous-Game_playing_AI-agents.git
cd Autonomous-Game_playing_AI-agents

# Install dependencies for specific project
cd ai_tic_tac_toe_agent  # or ai_chess_agent or ai_3dpygame_r1
pip install -r requirements.txt
```

### Running the Projects

#### Tic-Tac-Toe Agent
```bash
cd ai_tic_tac_toe_agent
streamlit run app.py
```

#### Chess Agent
```bash
cd ai_chess_agent
streamlit run ai_chess_agent.py
```

#### 3D PyGame Visualizer
```bash
cd ai_3dpygame_r1
streamlit run ai_3dpygame_r1.py
```

## Project Structure

```
├── ai_3dpygame_r1/           # PyGame code generator and visualizer
│   ├── ai_3dpygame_r1.py
│   ├── README.md
│   └── requirements.txt
│
├── ai_chess_agent/           # Chess playing AI agents
│   ├── ai_chess_agent.py
│   ├── README.md
│   └── requirements.txt
│
└── ai_tic_tac_toe_agent/     # Tic-Tac-Toe AI agents
    ├── agents.py
    ├── app.py
    ├── README.md
    ├── requirements.txt
    └── utils.py
```

## Future Work

- Adding more game environments
- Implementing reinforcement learning agents
- Comparative studies between different AI approaches
- Human vs AI gameplay options
- Performance optimizations and analysis tools

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Mustafa Shoukat - [GitHub Profile](https://github.com/Mustafa-Shoukat1)

Project Link: [https://github.com/Mustafa-Shoukat1/Autonomous-Game_playing_AI-agents](https://github.com/Mustafa-Shoukat1/Autonomous-Game_playing_AI-agents)


