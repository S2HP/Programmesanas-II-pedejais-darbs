from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    # teksts = "Sveika, mīļā pasaule!!! \n"
    # fails = open("teksts.txt", "a")
    # fails.write(teksts)
    # fails.close()
    # fails = open("teksts.txt", "r")
    # for rinda in fails:
    #   print(rinda)
    # fails.close()
    return render_template('chats.html')

@app.route('/sutit', methods = ['POST'])
def suta():
    rezultats = request.json
    if rezultats["zina"] == "\clear":
      with open("teksts.txt","w") as fails:
        fails.write("")
      return jsonify("Clear")
    with open("teksts.txt", "a") as fails:
      fails.write(rezultats["user"]+" - "+rezultats["zina"]+"\n")
    return jsonify("OK")

@app.route('/lasit')
def lasa():
  zinas=[]
  with open("teksts.txt", "r") as fails:
    for rinda in fails:
      zinas.append(rinda)
  return jsonify(zinas)


app.run(host='0.0.0.0', port=81)

