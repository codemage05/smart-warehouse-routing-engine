import heapq
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS so the React frontend can make local requests
CORS(app)

def heuristic(a, b):
    # Manhattan distance heuristic
    return abs(a['r'] - b['r']) + abs(a['c'] - b['c'])

@app.route('/api/calculate', methods=['POST'])
def calculate_path():
    data = request.json
    walls = data.get('walls')
    start = data.get('start')
    goal = data.get('goal')
    
    N = len(walls)
    
    # Priority queue for A* (f_score, row, col)
    open_set = []
    heapq.heappush(open_set, (0, start['r'], start['c']))
    
    # Track the path and costs
    came_from = {}
    g_score = {f"{start['r']},{start['c']}": 0}
    
    explored = []
    closed_set = set()

    while open_set:
        _, current_r, current_c = heapq.heappop(open_set)
        current_key = f"{current_r},{current_c}"
        
        # Skip if we've already processed this node
        if current_key in closed_set:
            continue
            
        explored.append({'r': current_r, 'c': current_c})
        closed_set.add(current_key)
        
        # Goal reached
        if current_r == goal['r'] and current_c == goal['c']:
            path = []
            curr = current_key
            while curr in came_from:
                r, c = map(int, curr.split(','))
                path.append({'r': r, 'c': c})
                curr = came_from[curr]
            path.append(start)
            path.reverse()
            return jsonify({"found": True, "path": path, "explored": explored})
            
        # Explore 4-way neighbors
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor_r = current_r + dr
            neighbor_c = current_c + dc
            
            # Check grid bounds and wall collisions
            if 0 <= neighbor_r < N and 0 <= neighbor_c < N:
                if not walls[neighbor_r][neighbor_c]:
                    neighbor_key = f"{neighbor_r},{neighbor_c}"
                    tentative_g = g_score[current_key] + 1
                    
                    if tentative_g < g_score.get(neighbor_key, float('inf')):
                        came_from[neighbor_key] = current_key
                        g_score[neighbor_key] = tentative_g
                        f_score = tentative_g + heuristic({'r': neighbor_r, 'c': neighbor_c}, goal)
                        
                        heapq.heappush(open_set, (f_score, neighbor_r, neighbor_c))
                        
    # Open set exhausted without finding the goal
    return jsonify({"found": False, "path": [], "explored": explored})

if __name__ == '__main__':
    app.run(debug=True, port=5000)