# Smart Warehouse Routing Engine 🤖📦

An interactive, full-stack Artificial Intelligence visualizer built to demonstrate state-space search algorithms in a simulated warehouse environment. This project implements the $A^*$ (A-Star) search algorithm with a Manhattan distance heuristic to calculate the mathematically optimal path for an automated forklift avoiding dynamic obstacles.

## 🎯 Problem Statement
In modern automated fulfillment centers, robots must navigate complex grids to retrieve packages without colliding with storage racks. This project solves the single-agent pathfinding problem by decoupling a highly optimized Python algorithmic backend from a React-based visual frontend.

## 🛠️ Tech Stack
* **Frontend:** React (18.3), Tailwind CSS, Lucide Icons (Self-contained via CDN)
* **Backend:** Python 3.x, Flask, Flask-CORS
* **Algorithm:** $A^*$ Search utilizing Python's `heapq` priority queue

## ✨ Core Features
* **Interactive Grid:** Click-and-drag to paint custom warehouse walls, place the robot start coordinate, and set the target package destination.
* **Algorithmic Decoupling:** The UI acts strictly as a client; all heuristic calculations and node explorations are executed via REST API on the Python server.
* **Real-Time Visualization:** Animates the search tree expansion (explored nodes) followed by the final optimal path execution.
* **Performance Metrics:** Tracks the exact number of nodes evaluated and the final path length.

## 🚀 Local Setup & Installation

### 1. Start the Python Backend
Ensure Python 3 is installed on your system.
```bash
cd backend
pip install -r requirements.txt
python app.py
