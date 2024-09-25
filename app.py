from flask import Flask, render_template, request
import math

# Initialize the Flask app
app = Flask(__name__)

# Import your geotechnical calculation functions here

def calculate_bearing_capacity(cohesion, unit_weight, depth, width, surcharge, phi):
    Nq = math.exp(math.pi * math.tan(math.radians(phi))) * (1 + math.sin(math.radians(phi)))**2 / (1 - math.sin(math.radians(phi)))**2
    Nc = (Nq - 1) / math.tan(math.radians(phi))
    Ngamma = 2 * (Nq + 1) * math.tan(math.radians(phi))
    
    qult = (cohesion * Nc) + (surcharge * Nq) + (0.5 * unit_weight * width * Ngamma)
    factor_of_safety = 3
    qsafe = qult / factor_of_safety

    return round(qsafe, 2)

def calculate_slope_stability(slope_angle, cohesion, unit_weight, height, phi, water_table_depth):
    num = cohesion + (unit_weight * height * math.cos(math.radians(slope_angle)) * math.tan(math.radians(phi)))
    den = unit_weight * height * math.sin(math.radians(slope_angle))
    FS = num / den

    if water_table_depth < height:
        FS *= 0.8  # Reduce FS if water table is present
    
    return round(FS, 2)

# Define the home page route
@app.route('/')
def index():
    return render_template('index.html')

# Define the route to handle the calculation
@app.route('/result', methods=['POST'])
def result():
    # Get the input values from the form
    calculation_type = request.form['calculation_type']

    if calculation_type == 'bearing_capacity':
        cohesion = float(request.form['cohesion'])
        unit_weight = float(request.form['unit_weight'])
        depth = float(request.form['depth'])
        width = float(request.form['width'])
        surcharge = float(request.form['surcharge'])
        phi = float(request.form['phi'])
        
        # Perform bearing capacity calculation
        result = calculate_bearing_capacity(cohesion, unit_weight, depth, width, surcharge, phi)
        result_text = f"The safe bearing capacity is {result} kPa."

    elif calculation_type == 'slope_stability':
        slope_angle = float(request.form['slope_angle'])
        cohesion = float(request.form['cohesion'])
        unit_weight = float(request.form['unit_weight'])
        height = float(request.form['height'])
        phi = float(request.form['phi'])
        water_table_depth = float(request.form['water_table_depth'])
        
        # Perform slope stability calculation
        result = calculate_slope_stability(slope_angle, cohesion, unit_weight, height, phi, water_table_depth)
        result_text = f"The Factor of Safety for slope stability is {result}."

    return render_template('result.html', result=result_text)

if __name__ == "__main__":
    app.run(debug=True)
