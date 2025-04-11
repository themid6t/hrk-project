from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import db

app = Flask(__name__)
app.secret_key = 'university_navigation_secret_key'  # Required for flash messages

# Initialize the database
db.initialize_db()

@app.route('/')
def home():
    """Route for the landing page"""
    # Get list of unique buildings for the homepage categories
    buildings = db.get_all_buildings()
    return render_template('index.html', title='University Navigation System', buildings=buildings)

@app.route('/admin')
def admin():
    """Admin page for managing navigation routes"""
    # Get all routes from the database
    routes = db.load_routes()
    return render_template('admin.html', routes=routes, title='Admin Panel')

@app.route('/admin/add_route', methods=['GET', 'POST'])
def add_route():
    """Page for adding new navigation routes"""
    if request.method == 'POST':
        # Add route to the database
        new_route = db.add_route(
            name=request.form['name'],
            building=request.form['building'],
            description=request.form['description']
        )
        flash('New route added successfully!', 'success')
        return redirect(url_for('admin'))
    return render_template('add_route.html', title='Add New Route')

@app.route('/admin/edit_route/<int:route_id>', methods=['GET', 'POST'])
def edit_route(route_id):
    """Page for editing existing routes"""
    try:
        # Get the route from the database
        route = db.get_route(route_id)
        
        if request.method == 'POST':
            # Update route in the database
            db.update_route(
                route_id=route_id,
                name=request.form['name'],
                building=request.form['building'],
                description=request.form['description']
            )
            flash('Route updated successfully!', 'success')
            return redirect(url_for('admin'))
        
        return render_template('edit_route.html', route=route, title='Edit Route')
    except ValueError:
        flash('Route not found!', 'error')
        return redirect(url_for('admin'))

@app.route('/admin/record_path/<int:route_id>')
def record_path(route_id):
    """Page for recording path points for a route"""
    try:
        # Get the route from the database
        route = db.get_route(route_id)
        return render_template('record_path.html', route=route, title='Record Path')
    except ValueError:
        flash('Route not found!', 'error')
        return redirect(url_for('admin'))

@app.route('/admin/save_path/<int:route_id>', methods=['POST'])
def save_path(route_id):
    """API endpoint to save recorded path points for a route"""
    # Get path points from the JSON request
    if not request.is_json:
        return jsonify({'error': 'Missing JSON data'}), 400
    
    data = request.get_json()
    path_points = data.get('path_points', [])
    
    # Validate path points
    if len(path_points) < 2:
        return jsonify({'error': 'Path must have at least 2 points'}), 400
    
    try:
        # Save the path points to the route
        db.save_path_points(route_id, path_points)
        return jsonify({'success': True, 'message': 'Path saved successfully'}), 200
    except ValueError:
        return jsonify({'error': 'Route not found'}), 404

@app.route('/building/<string:building_name>')
def building_locations(building_name):
    """Display locations for a specific building"""
    routes = db.get_routes_by_building(building_name)
    return render_template(
        'building_locations.html',
        routes=routes,
        building_name=building_name,
        title=f'{building_name} Locations'
    )

@app.route('/locations')
def locations():
    """Page to display all available locations with recorded paths"""
    # Get routes that have recorded paths
    routes_with_paths = db.get_routes_with_paths()
    
    # Group routes by building
    buildings = {}
    for route in routes_with_paths:
        building = route['building']
        if building not in buildings:
            buildings[building] = []
        buildings[building].append(route)
    
    return render_template('locations.html', buildings=buildings, routes=routes_with_paths, title='Navigation Locations')

@app.route('/navigate/<int:route_id>')
def navigate(route_id):
    """Page for navigating to a specific location"""
    try:
        # Get the route from the database
        route = db.get_route(route_id)
        
        if not route['path_points']:
            flash('No navigation path has been recorded for this route.', 'error')
            return redirect(url_for('locations'))
        
        return render_template('navigate.html', route=route, title=f'Navigate to {route["name"]}')
    except ValueError:
        flash('Route not found!', 'error')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)