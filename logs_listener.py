from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, template_folder='template')

@app.route("/alerts", methods= ['POST', 'GET'])
def alerts():
	if request.method == 'POST':
		log_data = request.get_json()
		with open("template/alerts.html",'w') as l:
			alerts_content = ''
			for parameters in log_data:
				alerts_content += '<p>'
				alerts_content += '<h5>' + parameters + ' : ' + str(log_data[parameters]) + '</h5>'
				alerts_content += '</p>'
			l.write(alerts_content)
		return '',200

	return render_template("alerts.html")



if __name__ == '__main__':

	app.run(host='0.0.0.0', debug=True)