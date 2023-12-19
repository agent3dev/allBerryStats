from flask import Flask, Response, render_template, send_file
import matplotlib.pyplot as plt
import io
from berries import BerryStats

app = Flask(__name__)
berry_stats = BerryStats()

@app.route('/allBerryStats', methods=['GET'])
def get_berry_stats():
    stats = berry_stats.get_stats()
    return Response(stats, content_type='application/json')

@app.route('/histogram', methods=['GET'])
def generate_histogram():
    # Generate histogram data
    data = berry_stats.growth_times

    # Create histogram plot
    plt.hist(data, bins=20)
    plt.xlabel('Growth Times')
    plt.ylabel('Frequency')
    # Save the plot to a BytesIO object
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)

    # Clear the plot to release memory
    plt.clf()

    # Return the image as a response
    return send_file(img_buffer, mimetype='image/png')

if __name__ == '__main__':
    app.run()
