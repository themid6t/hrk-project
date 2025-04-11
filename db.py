import json
import os
from typing import List, Dict, Any

# Path to the database file
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'routes_data.json')

# Initial route data
DEFAULT_ROUTES = [
    {"id": 1, "name": "HOD Cabin", "building": "Academic Block", "description": "Path to HOD cabin", "path_points": []},
    {"id": 2, "name": "Dean Office", "building": "Academic Block", "description": "Path to Dean office", "path_points": []},
    {"id": 3, "name": "Classroom 312", "building": "Academic Block", "description": "Path to Classroom 312", "path_points": []},
    {"id": 4, "name": "Classroom 321", "building": "Academic Block", "description": "Path to Classroom 321", "path_points": []}
]

def initialize_db():
    """Create the database file if it doesn't exist with default data."""
    if not os.path.exists(DB_PATH):
        with open(DB_PATH, 'w') as f:
            json.dump(DEFAULT_ROUTES, f, indent=2)
        return DEFAULT_ROUTES
    return load_routes()

def load_routes() -> List[Dict[str, Any]]:
    """Load routes from the database file."""
    try:
        with open(DB_PATH, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file is corrupt or missing, recreate it
        return initialize_db()

def save_routes(routes: List[Dict[str, Any]]):
    """Save routes to the database file."""
    with open(DB_PATH, 'w') as f:
        json.dump(routes, f, indent=2)

def get_next_id(routes: List[Dict[str, Any]]) -> int:
    """Get the next available ID for a new route."""
    if not routes:
        return 1
    return max(route["id"] for route in routes) + 1

def add_route(name: str, building: str, description: str) -> Dict[str, Any]:
    """Add a new route to the database."""
    routes = load_routes()
    new_route = {
        "id": get_next_id(routes),
        "name": name,
        "building": building,
        "description": description,
        "path_points": []
    }
    routes.append(new_route)
    save_routes(routes)
    return new_route

def update_route(route_id: int, name: str, building: str, description: str) -> Dict[str, Any]:
    """Update an existing route in the database."""
    routes = load_routes()
    for route in routes:
        if route["id"] == route_id:
            route["name"] = name
            route["building"] = building
            route["description"] = description
            save_routes(routes)
            return route
    raise ValueError(f"Route with ID {route_id} not found.")

def save_path_points(route_id: int, path_points: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Save path points for a route in the database."""
    routes = load_routes()
    for route in routes:
        if route["id"] == route_id:
            route["path_points"] = path_points
            save_routes(routes)
            return route
    raise ValueError(f"Route with ID {route_id} not found.")

def get_route(route_id: int) -> Dict[str, Any]:
    """Get a route by ID."""
    routes = load_routes()
    for route in routes:
        if route["id"] == route_id:
            return route
    raise ValueError(f"Route with ID {route_id} not found.")

def get_routes_by_building(building: str) -> List[Dict[str, Any]]:
    """Get routes filtered by building."""
    routes = load_routes()
    return [route for route in routes if route["building"] == building]

def get_routes_with_paths() -> List[Dict[str, Any]]:
    """Get routes that have recorded paths."""
    routes = load_routes()
    return [route for route in routes if route["path_points"]]

def get_all_buildings() -> List[str]:
    """Get a list of all unique buildings."""
    routes = load_routes()
    return list(set(route["building"] for route in routes))