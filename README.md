# 🧠 ChessVisionTutor ♟️
An AI-powered real-time **Chess Tutor** that uses **YOLOv8 object detection** to recognize chess pieces on a physical board, suggest the next best move using **Stockfish**, and explain the move with **voice narration** — making chess fun and educational for kids and beginners!

## 🎯 Features

- 🎥 Real-time object detection of chess pieces using YOLOv8
- ♟️ Board state tracking with move history
- 💡 Stockfish-powered move suggestions
- 🗣️ Voice narration explaining moves (in English)
- 🖼️ Visual overlay of piece positions and suggested moves
- 🎬 Option to record and save the output as a video with narration

## 🛠️ Tech Stack

- 🔍 YOLOv8 (`ultralytics`)
- 🧠 Stockfish (`python-chess`)
- 🎤 Voice: `gTTS` or `pyttsx3`
- 🎥 OpenCV for video capture and overlays
- 🐍 Python 3.8+

## 📁 Project Structure
ChessVisionTutor/
│
├── detection/
│ └── draw_overlay.py # Overlay piece labels and suggestions
│
├── chess_engine/
│ ├── move_detector.py # Detects move by comparing positions
│ ├── board_state.py # Tracks board state using python-chess
│ └── move_suggester.py # Suggests moves & explains them via voice
│
├── utils/
│ ├── helpers.py # Converts squares to pixel coordinates
│ └── voice_engine.py # Handles speech generation
│
├── weights/
│ └── best.pt # YOLOv8 trained model
│ └── stockfish.exe # Stockfish engine binary
│
├── Chess_Vision_Tutor.ipynb # Main real-time detection loop
├── example_video.mp4 # Sample video for testing
├── output_chess_tutor.avi # Saved output (after run)
└── requirements.txt

