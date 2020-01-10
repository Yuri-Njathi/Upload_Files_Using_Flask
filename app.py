import os
from flask import Flask, render_template ,request

__author__ = "Yuri Njathi"

app = Flask(__name__)

app_ROOT = os.path.dirname(os.path.relpath(__file__))
#os.path.abspath() absolute path
#os.path.relpath() relative path
@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload" , methods = ["POST"])
def upload():
    target = os.path.join(app_ROOT,"images/")
    print("Target : ", target)
    imagecount = 0
    if not os.path.isdir(target):
        os.mkdir(target) 

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target,filename])
        print("Destination : ",destination)
        file.save(destination)
        imagecount = imagecount + 1
    if imagecount == 1 :
        return render_template("complete.html",response = "File Uploaded")
    elif imagecount > 1 :
        return render_template("complete.html",response = "Files Uploaded")
if __name__ == '__main__':
    app.run(port=8080,debug=True)