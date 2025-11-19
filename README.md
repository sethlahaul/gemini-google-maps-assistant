# 🗺️ Google Maps Assistant

A Streamlit-based application that helps you find the best route for your journey by comparing Flight, Train, and Road options with real-time considerations.

## Features

✨ **Multi-Modal Route Comparison**
- ✈️ **Flight Routes** - Fast travel with weather considerations
- 🚂 **Train Routes** - Cost-effective with maintenance alerts
- 🚗 **Road Routes** - Flexible with road condition updates

📊 **Route Analysis**
- Real-time distance calculation using Haversine formula
- Estimated cost for each route
- Estimated travel time
- Realistic delay simulations

🌦️ **Weather Integration**
- Flight delays based on weather conditions
- Multiple weather scenarios (Clear Sky, Rain, Storm, Fog, Strong Winds)
- Cost surcharges for adverse weather

🔧 **Maintenance Alerts**
- Train route maintenance status
- Road construction and repair updates
- Delay estimates for each scenario

💡 **Smart Recommendations**
- Automatic route suggestion based on time, cost, and conditions
- Comparison table for easy decision-making

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/google-maps-assistant.git
cd google-maps-assistant
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## How to Use

1. **Select Source City** - Choose your starting location
2. **Select Destination City** - Choose where you want to go
3. **View Routes** - Compare the three available routes:
   - Click on each tab to see detailed information
   - Check weather/maintenance alerts for each route
   - View estimated costs, times, and arrival times
4. **Compare Routes** - Use the comparison table to see all options side-by-side
5. **Follow Recommendation** - Get an AI-suggested route based on your preferences

## Available Cities

The app includes 16 major US cities:
- New York
- Los Angeles
- Chicago
- Houston
- Phoenix
- Philadelphia
- San Antonio
- San Diego
- Dallas
- San Jose
- Austin
- Fort Worth
- Miami
- Seattle
- Denver
- Boston

## Calculation Details

### Distance
- Calculated using the Haversine formula based on actual city coordinates
- Gives accurate distances between any two cities

### Cost Estimation
- **Flight**: $100 base + $0.50 per km
- **Train**: $30 base + $0.08 per km
- **Road**: $25 base + $0.05 per km

### Time Estimation
- **Flight**: Distance/850 + 3 hours (for ground handling)
- **Train**: Distance/80 km/h average speed
- **Road**: Distance/60 km/h average speed

### Delays
- **Flight**: 0-60 minutes based on weather conditions, 5% cost surcharge
- **Train**: 0-45 minutes based on maintenance work
- **Road**: 0-45 minutes based on construction/maintenance

## Technologies Used

- **Streamlit** - Web framework for building the UI
- **Pandas** - Data manipulation and display
- **Python 3.8+** - Core language

## Future Enhancements

- Integration with real Google Maps API
- Real-time weather data
- Actual train and flight schedules
- Price comparison with booking systems
- User account management and saved routes
- Mobile app version

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

Built with ❤️ using Streamlit
