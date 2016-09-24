from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():


    event_1 = {'name': 'Event 1', 'descr': 'Lorem Ipsum'}
    event_2 = {'name': 'Event 2', 'descr': 'Lorem Ipsum'}
    event_3 = {'name': 'Event 3', 'descr': 'Lorem Ipsum'}
    event_4 = {'name': 'Event 4', 'descr': 'Lorem Ipsum'}
    event_5 = {'name': 'Event 5', 'descr': 'Lorem Ipsum'}
    event_6 = {'name': 'Event 6', 'descr': 'Lorem Ipsum'}

    events = [event_1, event_2, event_3, event_4, event_5, event_6]


    output_start = '''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <ul>
'''
    output_end = '''
</ul>
</body>
</html>
'''
    output_mitte = ''
    for e in events:
        output_mitte += '<li>' + e['name'] + '</li>'


    return output_start + output_mitte + output_end


if __name__ == "__main__":
    app.run(debug=True)
