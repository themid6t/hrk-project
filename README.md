# University Navigation System

A web-based navigation application to help users navigate through university buildings and locations. The application allows administrators to create routes, record navigation paths, and enables users to follow step-by-step directions to reach their destinations.

## Features

- **Building Navigation**: Find your way around different university buildings
- **GPS-Based Navigation**: Real-time guidance using your device's GPS and compass
- **Path Recording**: Admin interface to record paths between locations
- **Intuitive UI**: Easy-to-use interface for both administrators and users
- **Supports Multiple Buildings**: Organize routes by different campus buildings

## Installation

### Option 1: Docker (Recommended)

#### Prerequisites
- [Docker](https://www.docker.com/get-started) and Docker Compose installed on your system

#### Setup with Docker

1. **Clone or download the repository**:
   ```
   git clone <repository-url>
   ```

2. **Navigate to project directory**:
   ```
   cd <project-directory>
   ```

3. **Start the application with Docker Compose**:
   ```
   docker-compose up
   ```
   This will build the Docker image and start the container. The app will be available at http://localhost:5000

4. **To run in background**:
   ```
   docker-compose up -d
   ```

5. **To stop the application**:
   ```
   docker-compose down
   ```

### Option 2: Traditional Setup

#### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Git (optional, for cloning the repository)

#### Manual Setup

1. **Clone or download the repository**:
   ```
   git clone <repository-url>
   ```
   Or download and extract the project files to your local machine.

2. **Navigate to project directory**:
   ```
   cd <project-directory>
   ```

3. **Create a virtual environment** (recommended):
   ```
   python -m venv venv
   ```
   Or use conda
   ```
   conda create -n ar-nav python==3.11.11 -y
   ```

4. **Activate the virtual environment**:
   
   On Windows:
   ```
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```
   source venv/bin/activate
   ```

    If using conda:
   ```
   conda activate ar-nav
   ```

5. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

### If using Docker
The application will automatically start at http://localhost:5000 when you run `docker-compose up`

### If using traditional setup
1. **Start the Flask application**:
   ```
   python app.py
   ```

2. **Access the application** by opening a web browser and navigating to:
   ```
   http://127.0.0.1:5000/
   ```

### Testing on Mobile Devices

To test the app on a mobile device (required for GPS navigation features), you can use:

1. **Ngrok** for creating a publicly accessible URL:
   ```
   ngrok http 5000
   ```
   Use the link generated by ngrok to access the app.

2. **Docker with host network** (alternative):
   ```
   docker-compose down
   docker run --network="host" -p 5000:5000 university-nav
   ```
   Then access the app using your computer's IP address from the mobile device.

## Usage

### For Administrators

#### Managing Routes

1. Navigate to the Admin Panel by clicking "Admin" in the navigation bar or visiting `http://127.0.0.1:5000/admin`
2. To add a new route, click "Add New Route"
   - Enter a name (e.g., "HOD Cabin", "Classroom 312")
   - Specify the building (e.g., "Academic Block")
   - Add a description to help users understand the route
   - Click "Create Route"

#### Recording Paths

1. From the Admin Panel, find the route you want to record a path for
2. Click "Record Path" (or "Re-record Path" if one already exists)
3. On the recording page:
   - Click "Start Tracking" to begin using your device's GPS
   - Walk from the starting point to the destination
   - Click "Add Point" at each significant location (entry points, turns, corners)
   - Use "Mark as Stairs" when you reach stairs or level changes
   - Click "Remove Last Point" to undo if needed
   - Click "Save Path" when you finish recording the route

**Tips for good path recording**:
- Stand still for a few seconds at each point before recording
- Record points at all decision points (intersections, turns, doorways)
- Make sure your device has good GPS signal (ideally outside or near windows)
- For multi-floor navigation, record points at both the bottom and top of stairs

### For Users

#### Finding and Navigating to Destinations

1. From the homepage, browse available buildings or use the search feature
2. Select your desired building to see all available locations within it
3. Choose a location and click "Navigate to [Location]"
4. On the navigation screen:
   - Click "Start Navigation"
   - Follow the on-screen directions and the arrow indicator
   - The arrow will point toward the next waypoint in your path
   - Continue following each waypoint until you reach your destination

## Troubleshooting

- **Poor GPS Signal**: Move closer to windows or outdoor areas for better GPS reception
- **Compass Calibration**: If the direction arrow seems incorrect, calibrate your device's compass by moving your phone in a figure-8 pattern
- **Path Recording Issues**: Ensure you have location permissions enabled in your browser and device settings
- **Docker Issues**: If you encounter Docker-related issues, try stopping all containers with `docker-compose down` and then restarting with `docker-compose up`

## License

This project is licensed under the MIT License - see the LICENSE file for details.