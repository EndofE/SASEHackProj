from flask import Flask, render_template, request, redirect, url_for
from water_data import calculate_water_usage, get_comparison_data, get_improvement_tips

app = Flask(__name__)

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])


def calculate():
    # Get form data
    form_data = {
        'shower_minutes': float(request.form.get('shower_minutes', 0)),
        'toilet_flushes': float(request.form.get('toilet_flushes', 0)),
        'faucet_minutes': float(request.form.get('faucet_minutes', 0)),
        'dishwasher_uses': float(request.form.get('dishwasher_uses', 0)),
        'laundry_loads': float(request.form.get('laundry_loads', 0)),
        'location': request.form.get('location', 'us')
    }
    
    # Calculate usage
    usage = calculate_water_usage(form_data)
    comparison = get_comparison_data(form_data['location'])
    tips = get_improvement_tips(form_data, usage, comparison)

    
    
    return render_template('results.html', 
                         usage=usage, 
                         comparison=comparison,
                         tips=tips,
                         form_data=form_data)

@app.route('/game')
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)
